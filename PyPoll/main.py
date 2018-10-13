#import modules
import os
import csv

#designate data path
csvpath = os.path.join('.','election_data.csv') #test_data.csv

#use the file
with open(csvpath, 'r') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	
	#initialize variables
	votecount = 0
	tracker = {'name':0} #this will require a for loop to check if a name already exists
	
	#begin row-by-row analysis
	print(f"\nRunning Analysis on {csvpath}\n")
	for row in csvreader:
		#print(f"{votecount}, {row[2]}")
		if votecount >0:
			#find the first contestant
			if votecount == 1:
				tracker[row[2]]=0
				tracker.pop('name') #get rid of placeholder
			check = 0
			while check == 0:
				for i in tracker.keys():
					#print(f"{i}, {tracker[i]}")
					if i == row[2]:
						tracker[i] = int(tracker[i])+1
						check = 1
					if check == 0:
						check = 2
			if check == 2:
				tracker[row[2]] = 1
			#print(tracker)
		if votecount % 100000 == 0:
			print(f"{votecount // 100000}00k votes counted")
		votecount +=1

#correct overcount
votecount -=1

#print results to console
print(f"\nElection Results")
print(f"----------------")
print(f"Total Votes: {votecount}")
print(f"----------------")

#prep format for vote percentages
def per(raw_number):
	percentage = '{:,.3f}'.format(100*raw_number)
	return percentage

#print tracker to console
winner = "No Winner"
winvotes = 0
for i in tracker.keys():
	print(f"{i} had {per(tracker[i]/votecount)}% with {tracker[i]} votes")
	if tracker[i]>winvotes:
		winner = i
		winvotes = tracker[i]
print(f"----------------")
print(f"The winner is {winner}")

#Print results to file
output_path = os.path.join(".", "Election_results.txt")
with open(output_path, 'w') as textfile:
	textfile.write(f"Election Results")
	textfile.write(f"\n----------------")
	textfile.write(f"\nTotal Votes: {votecount}")
	textfile.write(f"\n----------------")
	for i in tracker.keys():
		textfile.write(f"\n{i} had {per(tracker[i]/votecount)}% with {tracker[i]} votes")
	textfile.write(f"\n----------------")
	textfile.write(f"\nThe winner is {winner}")
	print(f"\n\nAnalysis output to {output_path}")




	
