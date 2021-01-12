#Pybank
#Name:Pramod Philip
#Creates a Python script that analyzes the records to calculate each of the following:
#Outputs the total amount of "Profit/Losses" over the entire period
#Outputs the net total amount of "Profit/Losses" over the entire period
#Calculates the change in "Profit/Losses" over the entire period, then find the average of those changes
#Outputs the greatest increase in profits (date and amount) over the entire period
#Determines the greatest decrease in losses (date and amount) over the entire period

#Imports the os and csv modules
import os, csv

#Provides an output path name for the csv file path
output_path = os.path.join('Resources/budget_data.csv')

#Opens the csv file as a new variable
with open(output_path,mode='r') as csvfile:
	csv_read_in = csv.reader(csvfile, delimiter=',')
    #Skips header
	next(csv_read_in)
    #Converts the csv_read_in object to a list
	budget_list = list(zip(*csv_read_in))
	#Total number of months
	month_count = len(budget_list[0])
	
#Net total amount of "Profit/Losses" over the entire period
net_total = 0

#Loops through the end of the Profit/Losses column in budget_list
for row in budget_list[1]:
    #Adds the current Profit/Loss to the net total amount
    net_total = net_total + int(row)

#Initializes the Profit/Losses change list
change = []
#Loops through to the second to last value in the Profit/Losses column
for x in range(month_count-1):
    #Calculates the different between the current and next Profit/Loss in the loop
    differ = int(budget_list[1][x+1]) - int(budget_list[1][x])
    #Appends the calculated difference to the change list
    change.append(differ)

#Determines the average change in Profits/Losses
avg_change = sum(change)/(month_count-1)

#Initializes the greatest increase in change list
great_prof = 0
#Initiailizes the greatest decrease in change list
great_loss = 0
#Initializes the respective month to the greatest increase in change
month_prof = ''
#Initializes the respective month to the greatest decrease in change
month_loss = ''

#Loops through the entire change list
for x in range(len(change)):
    #Checks if the current change value is
    #greater than the current great_prof value
    if int(change[x]) > great_prof:
        #Establishes the current change value as
        #the new great_prof
        great_prof = change[x]
        #Establishes the respective month to the current change value
        month_prof = budget_list[0][x+1] 
        
    #Checks if the current change value is
    #less than the current great_loss
    elif int(change[x]) < great_loss:
        #Establishes the current change value as
        #the new great_loss
        great_loss = change[x]
        #Establishes the respective month to the current change value
        month_loss = budget_list[0][x+1]     

#Initializes the precision variable for average change
n = 2

#Prints the financial analysis
print('Financial Analysis')
print('___________________')
print('')    
print(f'Total Months: {month_count}')
print(f'Total: ${net_total}')
print(f'Average Change: ${avg_change:.{n}f}')
print(f'Greatest Increase In Profits: {month_prof} (${great_prof})')
print(f'Greatest Decrease In Profits: {month_loss} (${great_loss})')

#Imports the sys module
import sys
#Opens a new .txt file named "main_Pybank.txt"
sys.stdout = open('main_Pybank.txt','w')

#Prints the financial analysis to the .txt file
print('Financial Analysis')
print('___________________')
print('')
print(f'Total Months: {month_count}')
print(f'Total: ${net_total}')
print(f'Average Change: ${avg_change:.{n}f}')
print(f'Greatest Increase In Profits: {month_prof} (${great_prof})')
print(f'Greatest Decrease In Profits: {month_loss} (${great_loss})')

#Closes the .txt file
sys.stdout.close()