📊 Campus Energy Use Dashboard

Capstone Project – Lab Assignment 5


---

🔍 Project Overview

This project analyzes and visualizes energy consumption across campus buildings using real meter data.
It merges multiple CSV files, performs aggregations, and builds an easy-to-understand dashboard of energy usage trends.


---

✨ Features

Feature	Description

Data Loading	Reads multiple CSV building data files automatically
Data Cleaning	Fixes timestamps and removes invalid rows
Aggregation	Calculates daily & weekly energy consumption
OOP Modeling	Object-oriented representation of buildings & meter readings
Visual Dashboard	Line, bar, and scatter plots for insights
Data Exports	Saves cleaned data, summary tables, and reports



---

📁 Folder Structure

CAMPUS ENERGY DASHBOARD/
│
├── data/
│   ├── adminblock.csv
│   ├── hostel.csv
│   ├── library.csv
│
├── output/
│   ├── cleaned_energy_data.csv
│   ├── building_summary.csv
│   ├── summary.txt
│   ├── dashboard.png
│
├── main.py
├── README.md


---

🧠 Object-Oriented Concepts Used

Class	Responsibility

MeterReading	Stores timestamp + kWh values
Building	Stores readings for a single building
BuildingManager	Manages all buildings + creates reports



---

📈 Dashboard Visuals

The dashboard includes:

⿡ Daily Consumption Line Chart
⿢ Weekly Average Bar Chart
⿣ Peak Load Scatter Plot

Output saved as:

output/dashboard.png


---

🛠 Requirements

Install dependencies:

pip install pandas matplotlib


---

▶ How to Run

⿡ Place your building CSV files inside /data
⿢ Run the script:

python main.py

⿣ Check results in the /output folder ✔


---

📊 Results Files

File	Description

cleaned_energy_data.csv	Combined cleaned dataset
building_summary.csv	Total & average energy use per building
summary.txt	Text report: highest consuming building
dashboard.png	Visualization dashboard



---

📝 Conclusions

This dashboard provides actionable insights into:

✔ Which building consumes the most energy
✔ When energy load peaks
✔ Usage patterns across weeks & days

These insights support better energy planning and sustainability on campus 🌱


---

✍ Author
AANYA MANGAL
