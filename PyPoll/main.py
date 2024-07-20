import os
import csv

#Link to pyBank dataset in the resource folder
PyPoll_Path = os.path.join('Resources', 'election_data.csv')

#Read the Budget Data csv file
with open(PyPoll_Path) as PyPoll_CSV:

    #Identifying the delimiter and the first row as the header
    csvreader = csv.reader(PyPoll_CSV, delimiter=',')
    cvsHeader = next(csvreader)

    #Setting initial values to variables
    Total_Votes = 0
    Candidate_Vote_Count = {}
    Vote_Percentage = {}
    Winner_Count = 0
    Winner = ""


    #Loop through the csv file starting from the second row(After the header)
    for row in csvreader:
        #Gets the candidate's name in each row and stores in Variable Candidate
        Candidate = row[2]
        
        #Count the total number of votes cast
        Total_Votes += 1

        #If Candidate is missing, add their name and count a vote towards their name
        if Candidate not in Candidate_Vote_Count:
            #Candidates_list.append(Candidate)
            Candidate_Vote_Count[Candidate] = 1

        #Else add to count to the candidate name each time it shows up  
        else:
            Candidate_Vote_Count[Candidate] += 1
            

   #Percentage of votes for Candidates
        for Candidates, Vote_Count in Candidate_Vote_Count.items():
            #Vote_Count = Candidate_Vote_Count.get(Candidate)
            Vote_Percentage[Candidates] = '{0:.3%}'.format(Vote_Count/Total_Votes)


        #Winning Candidate; if number of votes is the larger than winning count, we 
            if Vote_Count > Winner_Count:
                Winner_Count = Vote_Count
                Winner = Candidates


#Print results to the terminal
Election_Results = print(
f"Election Results\n"
f"--------------------------\n"
f"Total Votes: {Total_Votes}\n"
"--------------------------\n")
for Candidates, Vote_Count in Candidate_Vote_Count.items():
    print(f"{Candidates}: {Vote_Percentage[Candidates]} ({Vote_Count})\n")
print(f"--------------------------\n"
f"Winner: {Winner}\n"
f"--------------------------")

#Print results to  text file
Txt_file = open('./analysis/Election_Results', 'w')

Txt_file.write(f"Election Results\n")
Txt_file.write(f"--------------------------\n")
Txt_file.write(f"Total Votes: {Total_Votes}\n")
Txt_file.write(f"--------------------------\n")
for Candidates, Vote_Count in Candidate_Vote_Count.items():
    Txt_file.write(f"{Candidates}: {Vote_Percentage[Candidates]} ({Vote_Count})\n")
Txt_file.write(f"--------------------------\n")
Txt_file.write(f"Winner: {Winner}\n")
Txt_file.write(f"--------------------------\n")

Txt_file.close()