# Polling data analysis
# Modules
import os
import csv

# The total number of votes cast
vote_count = 0

# A complete list of candidates who received votes
# Dict of candidates
candidates = {}
total_votes = 0

# The percentage of votes each candidate won


# The total number of votes each candidate won


#The winner of the election based on popular vote.


# Polling data path
data_path = './Resources/election_data.csv'
output_path = './Analysis/election_results.txt'
# print(os.getcwd())


# Open the data file
with open(data_path) as data_file:
    data_reader = csv.reader(data_file, delimiter=",")

    # Skip the header
    next(data_reader)

    # Loop through data and add candidates and votes for each candidate.
    # Voter ID, County, and Candidate
    for row in data_reader:
        total_votes += 1
        candidates.update({row[2] : candidates.get(row[2], 0) + 1})

# initialize who the winner will be
winner_name = ""
winner_votes = 0

# Create a string to hold the output
output = "Election Results\n"
output += "-------------------------\n"
output += "Total Votes: " + str(total_votes) + "\n"
output += "-------------------------\n"
for candidate in candidates:
    output += candidate + ": " + str(round(candidates[candidate]/total_votes*100,2)) + "% (" + str(candidates[candidate]) + ")\n"
    # Determine winner
    if candidates[candidate] > winner_votes:
        winner_name = candidate
        winner_votes = candidates[candidate]
output += "-------------------------\n"
output += "Winner: " + winner_name + "\n"
output += "-------------------------\n"

# Output to file
with open(output_path, "w") as text_file:
    text_file.write(output)

# Output to terminal
print(output)
