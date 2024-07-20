import os
import csv

#Link to pyBank dataset in the resource folder
PyBank_Path = os.path.join('Resources', 'Budget_data.csv')

#Read the Budget Data csv file
with open(PyBank_Path) as PyBank_CSV:

    #Identifying the delimiter and the first row as the header
    csvreader = csv.reader(PyBank_CSV, delimiter=',')
    cvsHeader = next(csvreader)

    #Setting initial values to variables
    Total_Months = 0
    Total = 0
    Prev_Revenue = 0
    Month_Change = []
    Rev_Change = []
    Total_Change = 0
    

    #Loop through the csv file starting from the second row(After the header)
    for row in csvreader:
    
        #Labeling the Revenue column
        Revenue = int(row[1])

        #Count the total number of months and total revenue 
        Total_Months += 1
        Total += Revenue 

        #Calculate the total profit/loss starting from month 1
        Profit_Loss = Revenue - Prev_Revenue 

        # Add the profit/loss to a list along with its corresponding month
        Rev_Change.append(Profit_Loss)
        Month_Change.append(row[0])
        
        Prev_Revenue = int(row[1])

        #Calculate the total revenue change and then the average
        Total_Change += Profit_Loss
        Average_Change = round(Total_Change/Total_Months, 2)

    
        #Find the greatest increase in profit/change and its corresponding month
        Great_Increase = max(Rev_Change)
        Increase_month = Month_Change[Rev_Change.index(Great_Increase)]
    
        #Find the greatest decrease in profit/change and its corresponding month
        Great_Decrease = min(Rev_Change)
        Decrease_month = Month_Change[Rev_Change.index(Great_Decrease)]

     # print the result to the terminal
    Financial_Analysis = (f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {Total_Months}\n"
    f"Total: ${Total}\n"
    f"Average Change: ${Average_Change}\n"
    f"Greatest Increase in Profits: {Increase_month}(${Great_Increase})\n"
    f"Greatest Decrease in Profits: {Decrease_month}(${Great_Decrease})")

    print(Financial_Analysis)


    Txt_file = open('./analysis/Financial_analysis.txt', 'w')

    Txt_file.write(Financial_Analysis)

    Txt_file.close()