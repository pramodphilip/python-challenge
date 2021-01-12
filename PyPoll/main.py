#PyPoll
#Name: Pramod Philip
#Creates a Python Script that analyzes the votes of a small, rural town
#Calculates:
#1. The total number of votes cast
#2. Complete list of all candidates who received votes
#3. The percentage of votes each candidate received
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.

#Imports the os and csv modules
import os, csv

#Provides output path name for csv file
output_path = os.path.join('Resources/election_data.csv')
#Opens the csv file in read mode
with open(output_path,mode='r') as csvfile:
    #Creates object based on csv file
    csv_read_in = csv.reader(csvfile,delimiter=',')
    #Skips header
    next(csv_read_in)
    #Converts object csv_read_in to a list
    elec_list = list(zip(*csv_read_in))
    #Equates the total number of votes to the length of the first column
    #in elec_list
    vote_total = int(len(elec_list[0]))
    
    #Creates a list to store candidate names, initializes with first name in the Candidate Name column
    candidate = [elec_list[2][0]]

    #Loops through candidate column up until second to last row
    for x in range(vote_total-1):
        #Checks to see if the names in current and next column are different
        if elec_list[2][x] != elec_list[2][x+1]:
            #If different, it then determines whether or not the candidate is inside
            #the candidate list
            if elec_list[2][x+1] not in candidate:
                #If the candidate is not in the candidate list,
                #the candidate's name is appened to the candidate list
                candidate.append(elec_list[2][x+1])

    #Creates a new list for counting the number of votes
    #that each candidate received
    cand_vote = []

    #Loops through each row in candidate
    for row in candidate:
        #Appends a 0 to each row to initialize the cand_vote list
        cand_vote.append(0)

    #Loops through length of candidate column until the last row
    for x in range(vote_total):
        #Separate loop looping until last column in candidate list
        for y in range(len(candidate)):
            #Checks if the current candidate name matches that in the candidate list
            if elec_list[2][x] == candidate[ y]:
                #If yes, adds one vote the respective candidate in cand_vote
                cand_vote[y] = cand_vote[y] + 1
                
    #Creates list for calculating the percentage of votes each
    #candidate received
    per_vote = []

    #Loops through the length of of the cand_vote list
    for x in range(len(cand_vote)):
        #Each candidate's percentage of votes is
        #appended to the per_vote list
        per_vote.append((cand_vote[x]/vote_total)*100)
        
    #Initializes the winning vote percentage variable
    win_vote = 0

    #Loops through the range of the per_vote list
    for z in range(len(per_vote)):
        #Checks if the current percentage vote value
        #is larger than the current winning vote percentage
        #variable
        if per_vote[z] > win_vote:
            #If yes, the new winning vote percentage is
            #the current vote percentage
            win_vote = per_vote[z]
            #The corresponding candidate name of the 
            #new winning percentage is stored in winner
            winner = candidate[z]

    #The percentage vote is converted to a string that
    #provides the correct amount of accuracy for each vote
    per_vote = ['%.3f' % elem for elem in per_vote]
    
#Prints out the election results
print('Election Results')
print('___________________')
print('')
print(f'Total Votes: {vote_total}')
print('___________________')
print('')
#Loops through length of the candidate list
for x in range(len(candidate)):
    #Prints the candidate name, vote percentage
    #and the number of votes that candidate received
    print(f'{candidate[x]}: {per_vote[x]}% ({cand_vote[x]})')
print('___________________')
print('')
print(f'Winner: {winner}')
print('___________________')

#Exports the election results to a .txt file
import sys
#Opens a new .txt file name "main_PyPoll.txt"
sys.stdout = open('main_PyPoll.txt','w')

#Prints election results to the .txt file
print('Election Results')
print('___________________')
print('')
print(f'Total Votes: {vote_total}')
print('___________________')
print('')
for x in range(len(candidate)):
    print(f'{candidate[x]}: {per_vote[x]}% ({cand_vote[x]})')
print('___________________')
print('')
print(f'Winner: {winner}')
print('___________________')

#Closes the .txt file
sys.stdout.close()