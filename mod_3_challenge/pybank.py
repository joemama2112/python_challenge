#import libraries
import os
import csv
from datetime import datetime

# navigate to and access csv
filepath = "Instructions/PyBank/Resources/budget_data.csv"
with open(filepath) as file:

    # create reader
    reader = csv.reader(file)

    # skip header
    next(reader)

    # initialize variables
    num_months = 0
    gross_profit = 0
    prev_month_profit = 0
    monthly_profit = 0
    highest_profit = float('-inf')
    highest_profit_date = None
    lowest_profit = float('inf')
    lowest_profit_date = None

    # loop through each row
    for row in reader:
        # reformat dates in first column
        date = datetime.strptime(row[0], '%b-%d')
        # calculate profit from next column
        profit = int(row[1])
        # add to months counter
        num_months += 1
        # add to gross profit/loss
        gross_profit += profit
        # calculate change from month to month and update previous month value
        if num_months > 1:
            monthly_profit += profit - prev_month_profit
        prev_month_profit = profit
        # update high/low values and dates
        if profit > highest_profit:
            highest_profit = profit
            highest_profit_date = date
        if profit < lowest_profit:
            lowest_profit = profit
            lowest_profit_date = date

# calculate monthly average
if num_months > 1:
    monthly_profit /= num_months - 1

#output results to text file
with open("bank_results.txt", "w") as output_file:
    print(f"""Financial Analysis

    -------------------------

    Number of months: {num_months}

    Gross profit/loss: {gross_profit}

    Average monthly profit/loss: {monthly_profit}

    Highest profit: {highest_profit_date:%b-%d} {highest_profit}

    Lowest profit: {lowest_profit_date:%b-%d} {lowest_profit}""", file=output_file)

#output results to terminal
print(f"""Financial Analysis

    -------------------------

    Number of months: {num_months}

    Gross profit/loss: {gross_profit}

    Average monthly profit/loss: {monthly_profit}

    Highest profit: {highest_profit_date:%b-%d} {highest_profit}

    Lowest profit: {lowest_profit_date:%b-%d} {lowest_profit}

    -------------------------

    Results may also be found in bank_results.txt
    """)