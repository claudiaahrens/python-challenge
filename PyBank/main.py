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
path = os.path.join(".","02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")

# open the file using "write" mode. Specify the variable to hold the contents
with open(path, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skipping over column headers
    next(csvreader)

    previous_row = []
    profit_loss_change_mom_list = []

    for row in csvreader:
        # Updated total months
        total_months += 1

        # Updated total earnings
        total_earnings += int(row[1])

        if len(previous_row) > 0:
            profit_loss_change_mom = int(row[1]) - int(previous_row[1])

            # add to total p/l mom list
            profit_loss_change_mom_list.append(profit_loss_change_mom)

            if profit_loss_change_mom > greatest_increase_profit:
                greatest_increase_date = row[0]
                greatest_increase_profit = profit_loss_change_mom
            
            if profit_loss_change_mom < greatest_decrease_profit:
                greatest_decrease_date = row[0]
                greatest_decrease_profit = profit_loss_change_mom
        else:
            greatest_increase_date = row[0]
            greatest_increase_profit = int(row[1])

            greatest_decrease_date = row[0]
            greatest_decrease_profit = int(row[1])

        # Assign variable for next loop to compare against
        previous_row = row

average_change = sum(profit_loss_change_mom_list) / len(profit_loss_change_mom_list)

# found on https://stackoverflow.com/questions/2389846/python-decimals-format
average_change_display = '{:0.2f}'.format(average_change)

print("Financial Analysis")
print("----------------------------")
print('Total Months: ' +str(total_months))
print('Total: $' +str(total_earnings))
print('Average Change: $'+average_change_display)
print('Greatest Increase in Profits: '+ greatest_increase_date + ' ($' + str(greatest_increase_profit) + ")")
print('Greatest Decrease in Profits: '+ greatest_decrease_date + ' ($' + str(greatest_decrease_profit) + ")")

# write to file
# https://www.w3schools.com/python/python_file_write.asp
file = open('financial-analysis.txt', 'a')
file.write('Financial Analysis')
file.write('\n')
file.write('----------------------------')
file.write('\n')
file.write('Total Months: ' + str(total_months))
file.write('\n')
file.write('Average Change: $' + average_change_display)
file.write('\n')
file.write('Greatest Increase in Profits: ' + greatest_increase_date + " ($" + str(greatest_increase_profit) +")")
file.write('\n')
file.write('Greatest Decrease in Profits: ' + greatest_decrease_date + " ($" + str(greatest_decrease_profit) +")")
file.close()