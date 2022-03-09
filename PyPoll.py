# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote

# Add dependencies
import csv
import os

# Create a filename variable to load a file from direct path
election_file = 'Resources/election_results.csv'
# Create a filename variable to output results to a direct path
election_notes = 'analysis/election_analysis.txt'
# Open election results and read file:
with open(election_file) as election_data:
    # Reference the file object in memory
    file_reader = csv.reader(election_data)
    # Create headers & print
    headers = next(file_reader)
    print(headers)
    # Print each row in the csv file
    for row in file_reader:
        print(row)