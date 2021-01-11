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

#Provides an output path for the csv file path
output_path = os.path.join('Resources/budget_data.csv')

#Opens the csv file as a new variable
with open(output_path,mode='r') as csvfile:
	csv_read_in = csv.reader(csvfile, delimiter=',')
	next(csv_read_in)
	budget_list = list(zip(*csv_read_in))
	#Total number of months
	month_count = len(budget_list[0])
	
#Net total amount of "Profit/Losses" over the entire period
net_total = 0
    
for row in budget_list[1]:
    net_total = net_total + int(row)
        
change = []
for x in range(month_count-1):
    differ = int(budget_list[1][x+1]) - int(budget_list[1][x])
    change.append(differ)

avg_change = sum(change)/(month_count-1)
    
great_prof = 0
great_loss = 0
month_prof = ''
month_loss = ''

for x in range(len(change)):
    if int(change[x]) > great_prof:
        great_prof = change[x]
        month_prof = budget_list[0][x+1] 
        
        
    elif int(change[x]) < great_loss:
        great_loss = change[x]
        month_loss = budget_list[0][x+1]     
            
n = 2
print('Financial Analysis')
print('___________________')
print('')    
print(f'Total Months: {month_count}')
print(f'Total: ${net_total}')
print(f'Average Change: ${avg_change:.{n}f}')
print(f'Greatest Increase In Profits: {month_prof} (${great_prof})')
print(f'Greatest Decrease In Profits: {month_loss} (${great_loss})')
    
import sys
sys.stdout = open('main_Pybank.txt','w')

print('Financial Analysis')
print('___________________')
print('')
print(f'Total Months: {month_count}')
print(f'Total: ${net_total}')
print(f'Average Change: ${avg_change:.{n}f}')
print(f'Greatest Increase In Profits: {month_prof} (${great_prof})')
print(f'Greatest Decrease In Profits: {month_loss} (${great_loss})')

sys.stdout.close()