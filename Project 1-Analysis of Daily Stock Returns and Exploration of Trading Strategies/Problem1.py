"""
Weiqi Zhang
Class: CS677 - Online 2 Spring  2023
Date: 03/22/2023
Homework 1
Description of problem:
1. for each of the 5 years, compute the mean and standard deviation for the sets R, R− and R+ of daily returns for your stock for each day of the week
2. summarize your results in the table as shown below (5 tables total).
3. the days with negative and non-negative returns
"""
import pandas as pd
import csv

ZG = pd.read_csv('ZG.csv')
SPY = pd.read_csv('SPY.csv')
def add_column(file_name):
    True_label = []
    for row in file_name['Return']:
        if row < 0:
            True_label.append('-')
        else:
            True_label.append('+')
    file_name['True_label'] = True_label
    print(file_name)

print("********************     The ZG_table after add True_label   ******************* ")
add_column(ZG)
print("********************     The SPY_table after add True_label   ******************* ")
add_column(SPY)

# Define a dictionary to store the daily returns for each day of the week
data = {"Monday": {"R": [], "R-": [], "R+": []},
        "Tuesday": {"R": [], "R-": [], "R+": []},
        "Wednesday": {"R": [], "R-": [], "R+": []},
        "Thursday": {"R": [], "R-": [], "R+": []},
        "Friday": {"R": [], "R-": [], "R+": []}}


###### For 1 and 2 summarize results in the table as shown below (5 tables total).
print("\n ********************     Question 1.1 and 1.2   ******************* ")

# Define the headers for the tables
headers = ["Day", "µ(R)", "σ(R)", "|R−|", "µ(R−)", "σ(R−)", "|R+|", "µ(R+)", "σ(R+)"]

# Loop through the five years from 2016 to 2020
for year in range(2016, 2021):
    print(f"Results for {year}")
    # Initialize the data for each day of the week
    data = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}
    # Read the data from the CSV file
    with open(f"ZG.csv") as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row
        for row in reader:
            if int(row[1]) == year:  # Check if the row is for the current year
                day = row[4]
                return_val = float(row[13])
                if day in data:
                    if return_val < 0:
                        data[day].append(("R-", return_val))
                    else:
                        data[day].append(("R+", return_val))

    # Calculate the statistics for each day of the week
    table_data = []
    for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
        r_vals = [x[1] for x in data[day]]
        r_neg = [x[1] for x in data[day] if x[0] == "R-"]
        r_pos = [x[1] for x in data[day] if x[0] == "R+"]
        if r_vals:
            table_data.append([
                day,
                round(sum(r_vals) / len(r_vals), 4),
                round((sum([(x - sum(r_vals) / len(r_vals)) ** 2 for x in r_vals]) / len(r_vals)) ** 0.5, 4),
                len(r_neg),
                round(sum(r_neg) / len(r_neg), 4) if len(r_neg) > 0 else "-",
                round((sum([(x - sum(r_neg) / len(r_neg)) ** 2 for x in r_neg]) / len(r_neg)) ** 0.5, 4) if len(
                    r_neg) > 0 else "-",
                len(r_pos),
                round(sum(r_pos) / len(r_pos), 4),
                round((sum([(x - sum(r_pos) / len(r_pos)) ** 2 for x in r_pos]) / len(r_pos)) ** 0.5, 4)
            ])
        else:
            table_data.append([day] + ["-" for i in range(8)])
    # Print the table
    print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format(*headers))
    for row in table_data:
        print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format(*row))
    print("\n")  # Add a blank line between tables

print("\n ********************     Question 1.3  ******************* ")
negative_days = 0
non_negative_days = 0

# Loop through the five years from 2016 to 2020
for year in range(2016, 2021):
    # Initialize the data for each day of the week
    data = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}

    # Read the data from the CSV file
    with open(f"ZG.csv") as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row
        for row in reader:
            if int(row[1]) == year:  # Check if the row is for the current year
                return_val = float(row[13])
                if return_val < 0:
                    negative_days += 1
                else:
                    non_negative_days += 1

print(f"Number of days with negative returns: {negative_days}")
print(f"Number of days with non-negative returns: {non_negative_days}")

print("\n ********************     Question 1.4  ******************* ")
positive_returns = []
negative_returns = []

# Loop through the five years from 2016 to 2020
for year in range(2016, 2021):
    # Read the data from the CSV file
    with open(f"ZG.csv") as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row
        for row in reader:
            if int(row[1]) == year:  # Check if the row is for the current year
                return_val = float(row[13])
                if return_val < 0:
                    negative_returns.append(return_val)
                else:
                    positive_returns.append(return_val)

# Calculate the average return on "up" days and "down" days separately
avg_positive_return = sum(positive_returns) / len(positive_returns)
avg_negative_return = sum(negative_returns) / len(negative_returns)
print("avg_positive_return",avg_positive_return)
print("avg_negative_return",avg_negative_return)
# Compare the absolute values of the two averages
if abs(avg_negative_return) > abs(avg_positive_return):
    print("The stock loses more on a 'down' days than it gains on 'up' days.")
else:
    print("The stock gains more on a 'up' days than it loses on 'down' days.")

print("\n ********************     Question 1.5  ******************* ")

# Read the data from the CSV file
with open("ZG.csv") as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row
    data = [(float(row[13]), row[4]) for row in reader]

# Calculate the overall average return
overall_avg_return = sum([d[0] for d in data]) / len(data)
print("Overall average return:", overall_avg_return)

# Calculate the average return for each day of the week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
day_avg_returns = {}
for day in days:
    day_data = [d[0] for d in data if d[1] == day]
    day_avg_returns[day] = sum(day_data) / len(day_data) if day_data else None

print("Average returns by day of the week:")
for day in days:
    print(day, day_avg_returns[day])
    if day_avg_returns[day]>0:print(f"For {day},the stock gains more on 'up' days than it loses on 'down' days.")
    else:print("For {day},the stock loses more on 'down' days than it gains on 'up' days.")

