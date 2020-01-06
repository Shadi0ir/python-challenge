# Create file paths across operating systems and reading CSV file
import os
import csv
csv_path = os.path.join("C:/Users/17144/Course Work/python-challenge/Homework-challenge/Resources/election_data.csv")

candidates=[]
vote_count=[]
total_votes=0

#Creates dictionary to be used for candidate name and vote count
poll_inf={}

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

    print(poll_inf)
    print(total_votes)
    #Create lists for candidates and the number of vote from our dictionary.
    
    for row in poll_inf.items():
       candidates.append(row[0])
       vote_count.append(row[1])
    
    print(candidates)
    print(vote_count)
    
    #calculate the vote % for each candidate
    vote_percentage=[]

    for i in vote_count:
        vote_percentage.append(round(i/total_votes*100,1))
    print(vote_percentage)    
    
    # find the winner 
    print(max(zip(candidates,vote_count,vote_percentage)))
        

    