# Polling data analysis
# Modules
import os
import csv

# A complete list of candidates and votes received
candidates = {}

# Total votes in file
total_votes = 0

# Polling data path
data_path = './Resources/election_data.csv'
output_path = './Analysis/election_results.txt'

# If having difficulty with the path uncomment the following line to determine 
# the path you are running the file from. Adjust the data_path to correspond 
# with the current working directory.
# print(os.getcwd())


# Open the data file
with open(data_path) as data_file:
    data_reader = csv.reader(data_file, delimiter=",")

    # Save the header
    header = next(data_reader)

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
