# Create file paths across operating systems and reading CSV file
import os
import csv
csv_path = os.path.join("C:/Users/17144/Course Work/python-challenge/PyPoll/Resources/election_data.csv")

candidate=[]
vote_list=[]
vote_percent=[]

with open(csv_path,"r", newline='',encoding="UTF-8") as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=',')

    # Read the header row first 
    csv_header = next(csv_reader)
  

     #Read each row of data after the header and add iteams to two lists of candidate and the number of vote.
    for row in csv_reader:
        candidate.append(row[2])
        vote_list.append(row[0])

    #The total number of votes cast
    total_votes=len(vote_list)
    print(f"Total Votes:{total_votes}")
   
    #complete list of candidates who received votes
    def find_percentage(value,total):
        

    # calculate vote percent list
    
   # for vote in vote_list:
    
    #    vote_percent.append(round(vote/total_votes*100, 1))
    #print(vote_percent)