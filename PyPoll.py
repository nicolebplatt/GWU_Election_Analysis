# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote

# Add dependencies
import csv
import os
from telnetlib import theNULL

# Create a filename variable to load a file from direct path
election_file = 'Resources/election_results.csv'
# Create a filename variable to output results to a direct path
election_notes = 'analysis/election_analysis.txt'

# Initialize a total vote counter
total_votes = 0
# Initialize list of candidates
candidate_options = []
# Initialize candidate votes
candidate_votes = {}
# Winning tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open election results and read file:
with open(election_file) as election_data:
    # Reference the file object in memory
    file_reader = csv.reader(election_data)
    # Create headers & read header row
    headers = next(file_reader)
    # Print each row in the csv file
    for row in file_reader:
        # Add row to the total vote count
        total_votes += 1
        # Capture candidate name from each row
        candidate_name = row[2]
        # Add candidate name to candidate list if not already included
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            # Start counting candidates' votes
            candidate_votes[candidate_name] = 0
        # Add 1 vote to candidate's count if name appears in row
        candidate_votes[candidate_name] +=1
# Print 
#print(total_votes)
#print(candidate_options)
#print(candidate_votes)

# Calculate percentage of votes
# Iterate through the 'list' of candidates to calculate vote counts--this looping through our dictionary
for candidate_name in candidate_votes:
    # Declare votes for a candidate-- breaking out the value in the KVP
    votes = candidate_votes[candidate_name]
    # Calculate vote percentage--module wanted to pass through float but unnecessary, see below
    vote_percentage = votes / total_votes *100
    # print(type(vote_percentage))
    # print(f'{candidate_name} received {vote_percentage:.1f}% of the vote.')
    print(f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')
    # Determine the winner
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_candidate = candidate_name
        winning_count = votes
        winning_percentage = vote_percentage
winning_candidate_summary = (
    f"------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Vote Percentage: {winning_percentage:.1f}%\n"
    f"--------------------------\n")
print(winning_candidate_summary)

