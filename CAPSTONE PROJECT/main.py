# FINAL CAPSTONE DASHBOARD - FULLY FIXED

import pandas as pd
import matplotlib.pyplot as plt
from dataclasses import dataclass
from pathlib import Path

# Make sure output directory exists
Path("output").mkdir(exist_ok=True)

# TASK 1: DATA LOADING
def load_and_merge_data():
    data_path = Path("data")
    if not data_path.exists():
        print("❌ Missing data folder!")
        return pd.DataFrame(), ["No /data folder"]

    data_frames = []
    errors = []

    for file in data_path.glob("*.csv"):
        try:
            df = pd.read_csv(file)
            if "timestamp" not in df.columns or "kwh" not in df.columns:
                errors.append(f"Missing columns in {file.name}")
                continue

            df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
            df = df.dropna(subset=["timestamp"])
            df["building"] = file.stem
            data_frames.append(df)

        except Exception as e:
            errors.append(f"{file.name}: {e}")

    if not data_frames:
        return pd.DataFrame(), errors

    final_df = pd.concat(data_frames, ignore_index=True)
    final_df = final_df.sort_values("timestamp")
    final_df = final_df.set_index("timestamp")

    return final_df, errors


df, errors = load_and_merge_data()
print("Rows Loaded:", len(df))
print("Errors:", errors)

if df.empty:
    print("❌ No data to process. Add files to /data")
    exit()


# TASK 2: CALCULATIONS
daily = df.groupby("building").resample("D")["kwh"].sum().reset_index()
weekly = df.groupby("building").resample("W")["kwh"].sum().reset_index()

summary = df.groupby("building")["kwh"].agg(
    total_kwh="sum",
    mean_kwh="mean",
    min_kwh="min",
    max_kwh="max"
).reset_index()

print("\n📌 Summary Table:")
print(summary)


# TASK 3: OOP MODEL
from dataclasses import dataclass

@dataclass
class MeterReading:
    timestamp: pd.Timestamp
    kwh: float


class Building:
    def _init_(self, name):
        self.name = name
        self.readings = []

    def add_reading(self, time, kwh):
        self.readings.append(MeterReading(time, kwh))

    def calculate_total_consumption(self):
        return sum(r.kwh for r in self.readings)

    def generate_report(self):
        return {
            "building": self.name,
            "total_kwh": self.calculate_total_consumption(),
            "num_readings": len(self.readings)
        }


class BuildingManager:
    def _init_(self):
        self.buildings = {}  # <--- THIS MUST BE INDENTED INSIDE _init_

    def get_building(self, name):
        if name not in self.buildings:
            self.buildings[name] = Building(name)
        return self.buildings[name]

    def load_df(self, df):
        df_reset = df.reset_index()
        for _, row in df_reset.iterrows():
            b = self.get_building(row["building"])
            b.add_reading(row["timestamp"], row["kwh"])

    def generate_reports(self):
        return [b.generate_report() for b in self.buildings.values()]

# TASK 4: VISUAL DASHBOARD
pivot = daily.pivot(index="timestamp", columns="building", values="kwh")
weekly_avg = weekly.groupby("building")["kwh"].mean()
top_peaks = df.reset_index().nlargest(20, "kwh")

plt.figure(figsize=(10,12))

plt.subplot(3,1,1)
plt.plot(pivot.index, pivot)
plt.title("Daily Energy (kWh)")
plt.ylabel("kWh")
plt.legend(pivot.columns)

plt.subplot(3,1,2)
plt.bar(weekly_avg.index, weekly_avg.values)
plt.title("Weekly Average Energy Usage")
plt.ylabel("kWh")

plt.subplot(3,1,3)
plt.scatter(top_peaks["timestamp"], top_peaks["kwh"])
plt.title("Top Load Peaks")
plt.xlabel("Time")
plt.ylabel("kWh")

plt.tight_layout()
plt.savefig("output/dashboard.png")
plt.close()


# TASK 5: FILE EXPORTING
df.to_csv("output/cleaned_energy.csv")
summary.to_csv("output/building_summary.csv", index=False)

with open("output/summary.txt", "w") as f:
    f.write("CAMPUS ENERGY SUMMARY\n")
    f.write("-----------------------\n")
    f.write(f"Total kWh: {df['kwh'].sum():.2f}\n")
    f.write(f"Top Building: {summary.iloc[0]['building']} = {summary.iloc[0]['total_kwh']:.2f} kWh\n")

print("\n🎯 Completed Successfully!")
print("✔ cleaned_energy.csv")
print("✔ building_summary.csv")
print("✔ summary.txt")
print("✔ dashboard.png")