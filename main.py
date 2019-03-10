#Import necessary modules
import os
import csv

profit = 0
sum_delta = 0
max_increase = 0
min_increase = 0
data = []

#Open file
with open("/Users/etrigan/Documents/GitHub/python-challenge/PyBank/budget_data.csv", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Loads all the data into an array
    for row in csvreader:
        data += csvreader

for i in range(len(data)):
    
    #Sum the net profit
    profit += float(data[i][1])
    
    if i >= 1 :
        #Extended the array to include a column with the delta in profit between actual month and previous one
        data[i].extend([int(data[i][1]) - int(data[i-1][1])])
        
        #Therefore data[i][2] is profit delta between actual month and previous one
        sum_delta += data[i][2]
    
        #print(delta)
        if data[i][2] > max_increase:
            max_month = data[i][0]
            max_increase = data[i][2]
        
        if data[i][2] < min_increase:
            min_month = data[i][0]
            min_increase = data[i][2]
 
#PRINTING RESULTS

#Total number of months is the length of the array
print("Total months: " + str(len(data)))

#Total profit is a cumulative variable
print("Total: " + str(profit))

#The mean of deltas is the sum of deltas divided by the count of deltas
print("Average change: $" + str(sum_delta/(len(data)-1)))

#Just printing Max and Min of profits
print("Greatest Increase in Profits: " + str(max_month) + " ($" + str(max_increase) + ")")
print("Greatest Decrease in Profits: " + str(min_month) + " ($" + str(min_increase) + ")")



text_file = open("Homework3_output.txt","a")
text_file.write("Financial Analysis\n"
                "Total months: " + str(len(data)) + "\n"
                "Total: " + str(profit) + "\n"
                "Average change: $" + str(sum_delta/(len(data)-1)) + "\n"
                "Greatest Increase in Profits: " + str(max_month) + " ($" + str(max_increase) + ")" + "\n"
                "Greatest Decrease in Profits: " + str(min_month) + " ($" + str(min_increase) + ")" + "\n")
text_file.close()