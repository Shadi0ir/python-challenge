# Create file paths across operating systems and reading CSV file
import os
import csv
csv_path = os.path.join("C:/Users/17144/Course Work/python-challenge/PyBank/Resources/budget_data.csv")
csv_path_out = os.path.join("C:/Users/17144/Course Work/python-challenge/Homework-challenge/PyBank-challenge/budget_data.txt")
month=[]
amount=[]

with open(csv_path,"r", newline='',encoding="UTF-8") as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=',')

    # Read the header row first 
    csv_header = next(csv_reader)

    # Read each row of data after the header and add iteams to two lists of month and revenue.
    for row in csv_reader:
       month.append(row[0])
       amount.append(int(row[1]))
       
    #total number of months
    total_month=len(month)
    #Test print(f"Total months:{total_month}")
    
    #net total amount of "Profit/Losses"
    total=0

    for i in range(len(amount)):
        total=int(amount[i])+total

    #Test print(f"Total:${total}")

    #The average of the changes in "Profit/Losses"
    average_change=round((amount[i]-amount[0])/(len(amount)-1),2)
    
    #Test print(f"Average Change:${average_change}")
   
   #The greatest increase and decrease in profits

    greatest_increase= amount[1]-amount[0]
    greatest_decrease= amount[1]-amount[0]
    
    for j in range(1, len(amount)):
        if amount[j]-amount[j-1]>greatest_increase:
            greatest_increase=amount[j]-amount[j-1]
            great_inc_month=month[j]
        
        elif amount[j]-amount[j-1]<=greatest_decrease:
            greatest_decrease=amount[j]-amount[j-1]
            great_dec_month=month[j]
    

    #Test print(f"Greatest Increase in Profits: {great_inc_month} (${greatest_increase})")
    #Test print(f"Greatest Decrease in Profits: {great_dec_month} (${greatest_decrease})")
    
    #export a text file with the results
with open(csv_path_out, 'w', newline= '',encoding="UTF-8")as txt_file:
    txt_file.write('Financial Analysis\n')
    txt_file.write('----------------------------\n')
    txt_file.write('Total Months: '+str(total_month) + '\n')
    txt_file.write('Total: $'+str(total) + '\n')
    txt_file.write("Average Change: $"+str(average_change) + '\n')
    txt_file.write('Greatest Increase in Profits: '+str(great_inc_month)+' ($'+str(greatest_increase) + ')\n')
    txt_file.write('Greatest Decrease in Profits:'+great_dec_month+' ($'+str(greatest_decrease) + ')\n')


with open(csv_path_out, newline= '') as f:
    for line in f:
        print(line, end = '')


       