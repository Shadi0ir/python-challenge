
# Create file paths across operating systems and reading CSV file
import os
import csv
csv_path = os.path.join('..','Resources','election_data.csv')
csv_path_out = os.path.join('..','PyPoll-challenge','election_data.txt')

#Creates a dictionary to be used for candidate name and vote count
poll_inf={}
total_votes=0

with open(csv_path,"r", newline='',encoding="UTF-8") as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=',')

    # Read the header row first 
    csv_header = next(csv_reader)

    #Create a dictionary based on column 3 as keys and count vote for each candidates.

    for row in csv_reader:
        total_votes +=1
        if row[2] in poll_inf.keys():
            poll_inf[row[2]] = poll_inf[row[2]] + 1
        else:
            poll_inf[row[2]] = 1

       
    #Create lists for candidates and the number of vote from our dictionary.
    candidates=[]
    vote_count=[]

    for row in poll_inf.items():
       candidates.append(row[0])
       vote_count.append(row[1])
    
   
    #calculate the vote % for each candidate and adjust the format
    vote_percentage=[]

    for i in vote_count:
        vote_percentage.append(format(i/total_votes*100,'.3f'))
       
    
    # find the winner 
    winner=max(zip(vote_count,candidates))
    
    # zips candidates, num_votes, vote_percent into tuples (Rika: I kept this code to ask you a question otherwise eliminating this code won't impact the results)

    zip_data = list(zip(candidates, vote_percentage,vote_count, ))
    
    #export a text file with the results
    
with open(csv_path_out, 'w', newline= '',encoding="UTF-8")as txt_file:
    txt_file.write('Election Results\n')
    txt_file.write('----------------------------\n')
    txt_file.write('Total Votes: '+str(total_votes) + '\n')
    txt_file.write('----------------------------\n')
    
    for j in range(len(candidates)):
        txt_file.write(candidates[j] + ": " + str(vote_percentage[j]) +'%  (' + str(vote_count[j]) + ')\n')

    txt_file.write('----------------------------\n')
    txt_file.write('Winner:'+ winner[1] + '\n')
    txt_file.write('----------------------------\n')

with open(csv_path_out, newline= '') as f:
    for line in f:
        print(line, end = '')
