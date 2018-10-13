#import modules
import os
import csv

#designate data path
csvpath = os.path.join('.','budget_data.csv')

#use the file
with open(csvpath, 'r') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	
	#initialize variables
	rowcount = 0
	Previous_Month = 0
	Total = 0
	Total_change = 0
	GIIP = ["Month/year",0]
	GDIP = ["Month/year",0]
	
	#begin row-by-row analysis
	print(f"Running Analysis on {csvpath}")
	for row in csvreader:
		#print(f"{rowcount} {row[0]}, {row[1]}, {Total}")
		#not first rodeo
		if rowcount >0:
			#not second rodeo
			if rowcount>1:
				Total_change += int(row[1])-Previous_Month
			Total += int(row[1])
			if int(row[1])>GIIP[1]:
				GIIP[0]=row[0]
				GIIP[1]=int(row[1])-Previous_Month
			if int(row[1])<GDIP[1]:
				GDIP[0]=row[0]
				GDIP[1]=int(row[1])-Previous_Month
			Previous_Month = int(row[1])
		rowcount +=1

#correct overcount
rowcount -=1

#Format output without having to do it on each line
def money_format(raw_number):
	Currency = '{:,.2f}'.format(raw_number)
	return Currency

#Print results to console
print(f"\nFinancial Analysis")
print(f"------------------")
print(f"Total Months Analyzed: {rowcount}")
print(f"Total: ${money_format(Total)}")
print(f"Average monthly change:  ${money_format(Total_change/(rowcount-1))}")
print(f"Greatest Increase in Profits: ${money_format(int(GIIP[1]))} on {GIIP[0]}")
print(f"Greatest Decrease in Profits: ${money_format(int(GDIP[1]))}on {GIIP[0]}")

#Print results to file
output_path = os.path.join(".", "Financial_Analysis.txt")
with open(output_path, 'w') as textfile:
	textfile.write(f"Financial Analysis")
	textfile.write(f"\n------------------")
	textfile.write(f"\nTotal Months Analyzed: {rowcount}")
	textfile.write(f"\nTotal: ${money_format(Total)}")
	textfile.write(f"\nAverage monthly change:  ${money_format(Total_change/(rowcount-1))}")
	textfile.write(f"\nGreatest Increase in Profits: ${money_format(int(GIIP[1]))} on {GIIP[0]}")
	textfile.write(f"\nGreatest Decrease in Profits: ${money_format(int(GDIP[1]))} on {GIIP[0]}")
	print(f"\n\nAnalysis output to {output_path}")
