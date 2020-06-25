import csv
from filehandler.csvimport import importHumans as ih

# list of humans
data = ih('../data')



with open('export.csv','w',newline='') as file:
    writer = csv.writer(file)

    for human in data.values():
        for row in human.toList():
            writer.writerow(row)

