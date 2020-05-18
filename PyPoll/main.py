# Modules
import os
import csv
import statistics
import numpy as np 
  
# Specify the file to read from
csvpath = os.path.join("Resources", "election_data.csv")

# Specify the file to write to
output_path = os.path.join("Analysis", "election_analysis.txt")

# Open the file to read from
with open(csvpath) as csvfile:

    # Initialize csv.reader
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip header row
    next(csvreader)

    # Create empty list for votes
    candidateVotes = []

    # Loop through and add candidate votes to list
    for row in csvreader:
        candidateVotes.append(row[2])

    # Find total number of votes
    totalVotes = len(candidateVotes)

# Find all candidates in election using numpy module
# Convert candidateVotes list to numpy array, then add unique values to new list
totalCandidates = np.unique(np.array(candidateVotes))

#Create variables for election winner and vote count tracking
winner = ""
mostVotes = 0

# Open the file to write to
with open(output_path, 'w') as txtFile:

    # Print financial analysis results to terminal
    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {totalVotes}")
    print("----------------------------")

    # Write financial analysis results to output text file
    txtFile.write("Election Results \n")
    txtFile.write("---------------------------- \n")
    txtFile.write(f"Total Votes: {totalVotes} \n")
    txtFile.write("---------------------------- \n")

    # Loop through candidates and calculate their specific vote details from all votes
    for i in totalCandidates:
        percentVotes = round((candidateVotes.count(i) / totalVotes) * 100, 2)
        votes = candidateVotes.count(i)
        # Print and write candidate specific vote results    
        print(f"{i}: {percentVotes}% ({votes})")
        txtFile.write(f"{i}: {percentVotes}% ({votes}) \n")
        # Compare and update election winner based on number of votes
        if votes > mostVotes:
            mostVotes = votes
            winner = i

    # Finish printing and writing results        
    print("----------------------------")
    txtFile.write("---------------------------- \n")
    print(f"Winner: {winner}")
    txtFile.write(f"Winner: {winner} \n")
