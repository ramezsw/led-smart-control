import csv

data = [1,2,3,4,5,6]

with open("welp.csv", "wb") as myfile:
	spamwriter = csv.writer(myfile)
	spamwriter.writerow([data])


