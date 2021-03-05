import csv
from datetime import datetime
count=0
with open('trip_data_6.csv') as f:
    reader=csv.reader(f)
    line=f.read().splitlines()
    lastline=line[-1]
    ending_range=lastline.split(",")
    firstline=line[1]
    starting_range=firstline.split(",")
    print("|  COLUMN NUMBER   ||    FIELD NAME     | STARTING RANGE     |  ENDING RANGE      |")
    print("|-----------------:||:-----------------:|: -----------------:| :----------------: |")
    print("|    1             || PICK-UP DATETIME  |{} |{} |".format(starting_range[5],ending_range[5]))
    print("|    2             || DROP-OFF DATETIME |{} |{} |".format(starting_range[6],ending_range[6]))
