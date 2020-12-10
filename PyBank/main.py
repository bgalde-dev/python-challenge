# Budget data analysis
# Modules
import sys
import csv

# Budget data path
data_path = './Resources/budget_data.csv'
output_path = './Analysis/budget_results.txt'

# Variables
total_months = 0
total_amount = 0
prior_month = sys.float_info.min
chg = 0
chg_sum = 0
greatest_inc = ["", sys.float_info.min]
greatest_dec = ["", sys.float_info.max]

# Open the data file
with open(data_path) as data_file:
    data_reader = csv.reader(data_file, delimiter=",")

    # Save the header
    header = next(data_reader)
    
    # Loop through data 
    # Date and Profit/Losses
    for row in data_reader:
        total_months += 1
        total_amount += int(row[1])
        # Find chg
        if prior_month == sys.float_info.min:
            prior_month = 0
        else:
            chg = int(row[1]) - prior_month
            chg_sum += chg

        # Determine the greatest increase and decrease changes   
        if chg > greatest_inc[1]:
            greatest_inc[0] = row[0]
            greatest_inc[1] = chg
        elif chg <= greatest_dec[1]:
            greatest_dec[0] = row[0]
            greatest_dec[1] = chg

        # Set the prior month amount
        prior_month = int(row[1])

# Create a string to hold the output
output = "Financial Analysis\n"
output += "-------------------------\n"
output += "Total Months: " + str(total_months) + "\n"
output += "Total Amount: $" + str(total_amount) + "\n"
output += "Average  Change: " + str(round(chg_sum/(total_months-1),2)) + "\n"
output += "Greatest Increase in Profits: " + greatest_inc[0] + " ($" + str(greatest_inc[1]) + ")\n"
output += "Greatest Decrease in Profits: " + greatest_dec[0] + " ($" + str(greatest_dec[1]) + ")\n"
output += "-------------------------\n"

# Output to file
with open(output_path, "w") as text_file:
    text_file.write(output)

# Output to terminal
print(output)
