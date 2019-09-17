# PyBank main for U of M assignment
import os
import csv

total_months = 0
total_earnings = 0
average_change = 0
greatest_increase_date = ""
greatest_increase_profit = 0
greatest_decrease_date = ""
greatest_decrease_profit = 0

# parse csv file
path =os.path.join(".","02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")
print(path)

# open the file using "write" mode. Specify the variable to hold the contents
with open(path, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # skipping over column headers
    next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:
        print(row)


print("Financial Analysis")
print("----------------------------")
print('Total Months: ' +str(total_months))
print('Total: $' +str(total_earnings))
print('Average Change: $'+str(average_change))
print('Greatest Increase in Profits: '+ greatest_increase_date + ' ($' + str(greatest_increase_profit) + ")")
print('Greatest Decrease in Profits: '+ greatest_decrease_date + ' ($' + str(greatest_decrease_profit) + ")")