# Modules
import os
import csv
import statistics

# Specify the file to read from
csvpath = os.path.join("Resources", "budget_data.csv")

# Specify the file to write to
output_path = os.path.join("Analysis", "financial_analysis.txt")

# Open the file to read from
with open(csvpath) as csvfile:

    # Initialize csv.reader
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip header row
    next(csvreader)

    # Create empty list for profit/loss values and months
    profitLoss = []
    months = []

    # Loop through and add profit/loss values and months to lists
    for row in csvreader:
        profitLoss.append(int(row[1]))
        months.append(row[0])

    # Calculate net total
    netTotal = sum(profitLoss)

    # Find total number of months
    totalMonths = len(profitLoss)

    # Create variable for net change, incrementing variable for loop (starting at 2nd row of data, or first change), and empty list for changes    
    netChange = 0
    change = []
    i = 1

    # Loop through length of profit/loss list and add to net change variable, append changes to change list
    while i < len(profitLoss):
        netChange += (int(profitLoss[i])) -int(profitLoss[i - 1])
        change.append((int(profitLoss[i])) -int(profitLoss[i - 1]))
        i += 1

    # Calculate average change
    averageChange = round(netChange / (totalMonths - 1), 2)

    # Find max/min and respective months based on index position (accounting for fact that change list is one item shorter)
    maxIncrease = max(change)
    maxMonth = months[change.index(max(change)) + 1]
    maxDecrease = min(change)
    minMonth = months[change.index(min(change)) + 1]

# Print financial analysis results to terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {totalMonths}")
print(f"Total: ${netTotal}")
print(f"Average Change: ${averageChange}")
print(f"Greatest Increase in Profits: {maxMonth} (${maxIncrease})")
print(f"Greatest Decrease in Profits: {minMonth} (${maxDecrease})")

# Open the file to write to
with open(output_path, 'w') as txtFile:

    # Write financial analysis results to output text file
    txtFile.write("Financial Analysis \n")
    txtFile.write("---------------------------- \n")
    txtFile.write(f"Total Months: {totalMonths} \n")
    txtFile.write(f"Total: ${netTotal} \n")
    txtFile.write(f"Average Change: ${averageChange} \n")
    txtFile.write(f"Greatest Increase in Profits: {maxMonth} (${maxIncrease}) \n")
    txtFile.write(f"Greatest Decrease in Profits: {minMonth} (${maxDecrease}) \n")

