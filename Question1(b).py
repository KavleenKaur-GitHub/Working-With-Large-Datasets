import csv
from datetime import datetime
count=0
with open('trip_data_6.csv') as f:
    reader=csv.reader(f)
    for i,line in enumerate(reader):
        count=count+1
    print(f" Total number of rows in this particular dataset are {count}")
