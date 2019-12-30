# Create file paths across operating systems and reading CSV file
import os
import csv
csv_path = os.path.join("..", "Resources", "budget_data.csv")

month=[]
amount=[]

with open(csv_path,"r", newline='',encoding="UTF-8") as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=',')

    # Read the header row first 
    csv_header = next(csv_reader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header and add iteams to two lists of month and revenue.
    for row in csv_reader:
       month.append(row[0])
       amount.append(int(row[1]))
       
    #total number of months
    total_month=len(month)
    print(f"Total months:{total_month}")
    
    #net total amount of "Profit/Losses"
    total=0

    for i in range(len(amount)):
        total=int(amount[i])+total

    print(f"Total:{total}")

    #The average of the changes in "Profit/Losses"
    average_change=round((amount[i]-amount[0])/(len(amount)-1),2)
    
    print(f"Average Change:{average_change}")
    #total_revenue=
    #print(total_month)   

    
        