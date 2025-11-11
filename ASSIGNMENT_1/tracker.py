#Aanya Mangal
#Date: 11-Nov-2025
#Project Title: Daily Calorie Tracker CLI

import datetime

#Welcome Message
print("\n")
print("Welcome to the Daily Calorie Tracker! ")

#Taking input of calorie
meals = []
calorie = []
n = int(input("Enter total no. of meals: "))

for i in range(n):
    m = input(f"Enter your meal {i+1}: ")
    meals.append(m)
    
    c = float(input(f"Enter calories for your {m}: "))
    calorie.append(c)

#Calculating calorie
total = sum(calorie)
avg = total / len(calorie)

#Input daily calorie intake
limit = float(input("Enter your daily calorie intake: "))

#Printing Table 
print("\n" + "-"*35)
print(f"| {'MEALS':<12} | {'Calories (kcal)':>15} |")
print("-"*35)
for m, c in zip(meals, calorie):
    print(f"| {m:<12} | {c:>15.2f} |")

print("-"*35)
print(f"| {'TOTAL ':<12} | {total:>15.2f} |")
print(f"| {'Average ':<12} | {avg:>15.2f} |")
print("-"*35)
print("\n")

#Check calorie range
if total > limit:
    print("⚠ Warning: Your calorie intake exceeds the recommended daily intake!")
else:
    print("✅ Success: Your calorie intake is within a healthy range!")

#Ending Message
print("\n")
print(" Thank you for using the Calorie Tracker! ")
print(" Stay healthy and eat balanced! ")
print("\n")
#Bonus Task: Save Session Log to File
save = input("Would you like to save this session? (yes/no): ").strip().lower()

if save == "yes":
    timestamp = datetime.datetime.now().strftime("%d-%b-%Y %I:%M %p")
    with open("calorie_log.txt", "w", encoding="utf-8") as file:
        file.write("\n")
        file.write("Daily Calorie Tracker - Session Log ")
        file.write("\n")
        file.write(f"📅 Session Date & Time: {timestamp}\n\n")

        file.write("Meal Details:\n")
        file.write("-"*35 + "\n")
        file.write(f"| {'MEALS':<12} | {'Calories (kcal)':>15} |\n")
        file.write("-"*35 + "\n")
        for m, c in zip(meals, calorie):
            file.write(f"| {m:<12} | {c:>15.2f} |\n")

        file.write("-"*35 + "\n")
        file.write(f"| {'TOTAL ':<12} | {total:>15.2f} |\n")
        file.write(f"| {'Average ':<12} | {avg:>15.2f} |\n")
        file.write("-"*35 + "\n\n")

        file.write(f"Daily Calorie Limit: {limit:.2f}\n")
        if total > limit:
            file.write("⚠ Warning: Calorie intake exceeds the recommended daily intake!\n")
        else:
            file.write("✅ Success: Calorie intake is within a healthy range!\n")

        file.write("\n")
        file.write("Thank you for using the Calorie Tracker! \n")
        file.write(" Stay healthy and eat balanced! \n")
        file.write("\n")

    print("\n📁 Session has been saved successfully as 'calorie_log.txt'!")
else:
    print("\nSession not saved.")


