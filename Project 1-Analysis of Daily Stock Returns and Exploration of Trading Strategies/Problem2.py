"""
Weiqi Zhang
Class: CS677 - Online 2 Spring  2023
Date: 03/22/2023
Homework 1
Description of problem:
1. Examine your 5 tables
2. any patterns across days of the week,any patterns across different years for the same day of the week
3. the best and worst days of the week to be invested for each year.
"""


import pandas as pd
import csv

ZG = pd.read_csv('ZG.csv')
SPY = pd.read_csv('SPY.csv')
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

# Read the data from the CSV file

print("\n ********************     Question 2.1  ******************* ")

with open(f"ZG.csv") as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row
    # Initialize the data for each day of the week
    data = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}
    for row in reader:
        day = row[4]
        return_val = float(row[13])
        if day in data:
            data[day].append(return_val)

# Calculate the average return for each day of the week
avg_returns = {}
for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    avg_returns[day] = round(sum(data[day]) / len(data[day]), 4)

# Print the results
print("Average returns by day of the week:")
for day in avg_returns:
    print(f"{day}: {avg_returns[day]}")

print("1.The average return values for Thursday are mostly negative, while the average return values for Monday and Friday are mostly positive. ")
print("2.The standard deviation of returns for Wednesday is generally higher than for the other days of the week. ")
print("So,these patterns suggest that there might be some systematic factors affecting stock returns on different days of the week.")

print("\n ********************     Question 2.2  ******************* ")

# Read the data from the CSV file
with open(f"ZG.csv") as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row
    # Initialize the data for each year and day of the week
    data = {}
    for year in range(2016, 2021):
        data[year] = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}
    for row in reader:
        year = int(row[1])
        day = row[4]
        return_val = float(row[13])
        if year in data and day in data[year]:
            data[year][day].append(return_val)

# Calculate the average return for each year and day of the week
avg_returns = {}
for year in range(2016, 2021):
    avg_returns[year] = {}
    for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
        avg_returns[year][day] = round(sum(data[year][day]) / len(data[year][day]), 4)

# Print the results
print("Average returns by year and day of the week:")
for year in avg_returns:
    print(f"Results for {year}")
    for day in avg_returns[year]:
        print(f"{day}: {avg_returns[year][day]}")

print("the average returns value in 2016 from Monday to Friday is 0.0012,0.004,0.0032,-0.0011, 0.0021 always higher than the  average returns value in 2017 from Monday to Friday is 0.005,0.0013,-0.0033,-0.0031,0.0038")
print("the average returns value in 2017 from Monday to Friday is 0.005,0.0013,-0.0033,-0.0031,0.0038 always lower than the  average returns value in 2018 from Monday to Friday  is 0.0008,0.0003,0.0022,0.0001,-0.0056")
print("the average returns value in 2018 from Monday to Friday is 0.0008,0.0003,0.0022,0.0001,-0.0056 always lower than the  average returns value in 2017 from Monday to Friday  is 0.0007,-0.0015,-0.0004，-0.0013,0.0122")
print("the average returns value in 2019 from Monday to Friday is 0.0007,-0.0015,-0.0004，-0.0013,0.0122 always higer than the  average returns value in 2020 from Monday to Friday  is 0.0019,0.0037,0.0059，0.0042,0.0119")
print("Means,for the same day of the week,different years have the same tend.")

print("\n ********************     Question 2.3  ******************* ")
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

    # Sort the table_data based on the mean return value
    sorted_table_data = sorted(table_data, key=lambda x: x[1], reverse=True)

    # Print the best and worst days of the week
    print(f"Best day: {sorted_table_data[0][0]} (mean return: {sorted_table_data[0][1]})")
    print(f"Worst day: {sorted_table_data[-1][0]} (mean return: {sorted_table_data[-1][1]})")
    print("\n")

print("In 2016,the average return values is best in Tuesday of 0.004,and worst in Thursday of -0.0011 ")
print("In 2017,the average return values is best in Monday of 0.005,and worst in Wednesday of -0.0033 ")
print("In 2018,the average return values is best in Wednesday of 0.0022,and worst in Friday of -0.0056 ")
print("In 2019,the average return values is best in Friday of 0.0122,and worst in Tuesday of -0.0015 ")
print("In 2020,the average return values is best in Friday of 0.0119,and worst in Monday of 0.0019 ")

print("\n ********************     Question 2.4  ******************* ")
# Calculate the average return for each day of the week across all years
all_years_data = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}
for year in range(2016, 2021):
    with open(f"ZG.csv") as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row
        for row in reader:
            if int(row[1]) == year:  # Check if the row is for the current year
                day = row[4]
                return_val = float(row[13])
                if day in all_years_data:
                    all_years_data[day].append(return_val)

# Calculate the average return for each day of the week
avg_returns = {}
for day, data in all_years_data.items():
    if data:
        avg_returns[day] = sum(data) / len(data)

# Find the best and worst days across all years
best_day_all_years = max(avg_returns, key=avg_returns.get)
worst_day_all_years = min(avg_returns, key=avg_returns.get)

print(f"The best day to invest across all years is {best_day_all_years}")
print(f"The worst day to invest across all years is {worst_day_all_years}")
