# Paragraph analysis
# Modules
import sys
import re

# Budget data path
data_path = [['./Resources/paragraph_1.txt','./Analysis/paragraph_1.analysis.txt'], 
            ['./Resources/paragraph_2.txt', './Analysis/paragraph_2.analysis.txt']]

# If having difficulty with the path uncomment the following line to determine 
# the path you are running the file from. Adjust the data_path to correspond 
# with the current working directory.
# print(os.getcwd())

# Open the data file
for path in data_path:
    with open(path[0]) as data_file:
        paragraph = data_file.read()
        # Split at punctuation marks (sentences)
        # Should take care of suffixes, quoted line ends, initials. Ther
        sentences = len(re.split("(?<=[\.|\?|\!][\"])|(?<=[\.|\?|\!])(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<![A-Z]\.)\s+", paragraph))

        # non-alphanumeric characters
        letters = 0
        words = 0
        for s in re.split("\W+", paragraph):
            # If it is a zero length word don't count it
            if len(s) > 0:
                words += 1
            letters += len(s)

        # Create a string to hold the output
        output = "Paragraph Analysis of " + path[0] + "\n"
        output += "-------------------------\n"
        output += "Approximate Word Count: " + str(words) + "\n"
        output += "Approximate Sentence Count: " + str((sentences)) + "\n"
        output += "Average Letter Count (per word): " + str(round((letters/words),2)) + "\n"
        output += "Average Sentence Length (in words): " + str(round((words/sentences),2)) + "\n"
        output += "-------------------------\n"

        # Output to file
        with open(path[1], "w") as text_file:
           text_file.write(output)

        # Output to terminal
        print(output)
