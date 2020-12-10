# Modules
import state_util as su
import csv

# Empolyee data path
data_path = './Resources/employee_data.csv'
output_path = './Output/employee_data_new.txt'

# Emp ID,First Name,Last Name,DOB,SSN,State
emp_id = []
first_name = []
last_name = []
dob = []
ssn = []
state = []

# Open the data file
with open(data_path) as data_file:
    data_reader = csv.reader(data_file, delimiter=",")

    # Skip the header
    next(data_reader)

    # Loop through data and add candidates and votes for each candidate.
    # Emp ID,Name,DOB,SSN,State
    for row in data_reader:
        emp_id.append(row[0])
        first_name.append(row[1].split(" ")[0])
        last_name.append(row[1].split(" ")[1])
        dob.append(row[2])
        ssn.append("***-**-" + row[3].split("-")[2])
        state.append(su.get_state_abbrev(row[4]))

# Zip lists together
cleaned_csv = zip(emp_id, first_name, last_name, dob, ssn, state)

#  Open the output file
with open(output_path, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Emp ID", "First Name", "last Name", "DOB", "SSN", "State"])

    # Write in zipped rows
    writer.writerows(cleaned_csv)