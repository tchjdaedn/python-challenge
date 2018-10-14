#import modules
import os
import csv

#designate data path
csvpath = os.path.join('.','employee_data.csv')

#use the file
with open(csvpath, 'r') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	
	#initialize variables
	EmpID = 0
	Name=["First Name","Last Name"]
	DOB = ["Year","Month","Day"]
	SSN = ["123","12","1234"]
	State = "State"
	us_state_abbrev = {'State':'State','Alabama': 'AL','Alaska': 'AK','Arizona': 'AZ','Arkansas': 'AR','California': 'CA','Colorado': 'CO','Connecticut': 'CT','Delaware': 'DE','Florida': 'FL','Georgia': 'GA','Hawaii': 'HI','Idaho': 'ID','Illinois': 'IL','Indiana': 'IN','Iowa': 'IA','Kansas':'KS','Kentucky': 'KY','Louisiana': 'LA','Maine': 'ME','Maryland': 'MD','Massachusetts': 'MA','Michigan': 'MI','Minnesota': 'MN','Mississippi': 'MS','Missouri': 'MO','Montana': 'MT','Nebraska': 'NE','Nevada': 'NV','New Hampshire': 'NH','New Jersey': 'NJ','New Mexico': 'NM','New York': 'NY','North Carolina': 'NC','North Dakota': 'ND','Ohio': 'OH','Oklahoma': 'OK','Oregon': 'OR','Pennsylvania': 'PA','Rhode Island': 'RI','South Carolina': 'SC','South Dakota': 'SD','Tennessee': 'TN','Texas': 'TX','Utah': 'UT','Vermont': 'VT','Virginia': 'VA','Washington': 'WA','West Virginia': 'WV','Wisconsin': 'WI','Wyoming': 'WY',}
	#rowcount = 0
	
	#begin row-by-row conversion
	print(f"\nRunning Conversion on {csvpath}\n")
	output_path = os.path.join(".", "Converted_records.txt")
	with open(output_path, 'w') as textfile:
		for row in csvreader:
			#rowcount+=1
			#print(rowcount)
				if EmpID == 0:
					EmpID = "Emp ID"
					#print(f"{EmpID}\t{Name[0]}\t{Name[1]}\tDOB\tSSN\tState")
					textfile.write(f"{EmpID},{Name[0]},{Name[1]},DOB,SSN,State")
				else:
					#Employee ID
					EmpID = row[0]
					#Name
					Name = row[1].split()
					#DOB
					DOB = row[2].split("-")
					#SSN
					SSN = row[3].split("-")
					#State
					State = us_state_abbrev[row[4]]
					textfile.write(f"\n{EmpID},{Name[0]},{Name[1]},{DOB[1]}/{DOB[2]}/{DOB[0]},***-**-{SSN[2]},{State}")
					#print(f"{EmpID}\t{Name[0]}\t{Name[1]}\t{DOB[1]}/{DOB[2]}/{DOB[0]}\t***-**-{SSN[2]}\t{State}")
	print(f"\n\nConversion output to {output_path}")


		
		
		