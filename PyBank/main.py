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
profit_loss_change_mom =[]


# parse csv file
path = os.path.join(".","02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")
print(path)

# open the file using "write" mode. Specify the variable to hold the contents
with open(path, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skipping over column headers
    next(csvreader)

# calculation for profit/loss change month over month
#profit_loss_change_mom.append int(row[1])-int(previous_row[-1])

  #rev_change.append(revenue[i] - revenue[i-1])  
    # If data is present in a row, add 1 to total
    #profit_lost_change = []
    previous_row = []
    for row in csvreader:
        # Updated total months
        total_months += 1

        # Updated total earnings
        total_earnings += int(row[1])

        if len(previous_row) > 0:
            profit_loss_change_mom = int(row[1]) - int(previous_row[1])
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

        #average_change =sum profit_loss_change_mom/total_months
        #greatest_increase_profit =max(profit_loss_change_mom)
        #greatest_decrease_profit =min(profit_loss_change_mom)

        # Assign variable for next loop to compare against
        previous_row = row
        #greatest_increase_date =str ? [profit_loss_change_mom.index(max(profit_loss_change_mom))]
        

    # Calculate total earnings (Profit - Losses)


print("Financial Analysis")
print("----------------------------")
print('Total Months: ' +str(total_months))
print('Total: $' +str(total_earnings))
print('Average Change: $'+str(average_change))
print('Greatest Increase in Profits: '+ greatest_increase_date + ' ($' + str(greatest_increase_profit) + ")")
print('Greatest Decrease in Profits: '+ greatest_decrease_date + ' ($' + str(greatest_decrease_profit) + ")")