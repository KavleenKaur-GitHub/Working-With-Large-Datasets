# Assignment-4
### In this assignment, we were provided with the task of analyzing a ***large dataset*** which contained the information about ***taxi rides in NYC city***. In order to achieve the given task, there certainly were some challenges which are explained here along with every single task description. 


# TABLE OF CONTENT
- FIRST QUESTION:
  - What datetime range does your data cover?
  - How many rows are there total?
- SECOND QUESTION:
  - What are the field names?  Give descriptions for each field.
- THIRD QUESTION:
  - Give some sample data for each field.
- FOURTH QUESTION:
  - What MySQL data types / len would you need to store each of the fields?
- FIFTH QUESTION:
  - What is the geographic range of your data (min/max - X/Y)?
   - Plot this (approximately on a map)
- SIXTH QUESTION
  - What are the distinct values for each field?
- SEVENTH QUESTION
  - For other numeric types besides lat and lon, what are the min and max values?
- EIGHTH QUESTION
  - Create a chart which shows the average number of passengers each hour of the day.
- NINTH QUESTION
  - Create a new CSV file which has only one out of every thousand rows.
- TENTH QUESTION
  - Repeat step 8 with the reduced dataset and compare the two charts.


### SOMETHING THAT HOLDS TRUE FOR ALL THE ABOVE QUESTION IS THE STRATERGY USED TO READ SUCH A LARGE DATASET. 

THERE CERTAINLY ARE MANY WAYS WHICH CAN BE USED TO READ A FILE:
- LOADING THE WHOLE DATASET INTO MEMORY.
  
  
  ```python
   with open("name_of_csv.csv") as f:
          data=[{k:str(v) for k,v in row.items()}
          for row in csv.DictReader(f,skipinitialspace=True}]
   ```
   
### But being a file more than 2.5 GB,it is more than unlikely that this method is best. The amount of time taken by this script could be huge for a file this large


- USING PANDAS:


```python
  import pandas as pd 
  df=pd.read('name_of_the file.csv')
   ```
 ### But being a file more than 2.5 GB,it is more than unlikely that this method is best. Pandas is though very efficient library but even it fails to work on large datasets.
   
- PROCESSING THROUGH THE DISC ITSELF.

### The only method efficient enough is this method right here. This method is the method that we will be using to answer the above questions. It allows us to read and work on the data line by line which is very beneficial as it loads only one line into the memory at a time. 

```python
 import csv
 with open('trip_data_6.csv') as f:
   reader=csv.reader(f)
   ```
# FIRST QUESTION:
 
The first question had two parts, the first part allows us find the datatime range of our data. In order to find that, we could just get access to the first and the last line of our dataset. As our dataset is in chronological order of dates and time, it would save us from finding the minimum and maximum.
 
In order to achieve the above said task, we would have to split the csv file into rows and then we could access any particular row by indexing the variable containing all the rows that are splitted. The challenge still remains at large as now we have full row as a lineow  but now want a particular column. It is simple as we have to repeat the process for a particular row. We again split the row ang index the column needed. 

We repeat this process for one and last line.

```python
    line=f.read().splitlines() # splitted the whole csv into rows
    lastline=line[-1] # accessed last row
    ending_range=lastline.split(",") # splitted the last row to use indexing to get particular columns
    firstline=line[1] # accessed first line
    starting_range=firstline.split(",") # splitted the first row to use indexing to get particular columns
    print("|  COLUMN NUMBER   ||    FIELD NAME     | STARTING RANGE     |  ENDING RANGE      |")
    print("|-----------------:||:-----------------:|: -----------------:| :----------------: |")
    print("|    1             || PICK-UP DATETIME  |{} |{} |".format(starting_range[5],ending_range[5])) # accessed the pickup datetime column
    print("|    2             || DROP-OFF DATETIME |{} |{} |".format(starting_range[6],ending_range[6])) # accessed the drop-off datetime column
```
### THE RESULTS ARE AS FOLLOWS:

|  COLUMN NUMBER   |    FIELD NAME     | STARTING RANGE     |  ENDING RANGE      |
|-----------------|-----------------| -----------------| ---------------- |
|    1             | PICK-UP DATETIME  |2013-06-03 00:02:12 |2013-06-01 00:30:00 |
|    2             | DROP-OFF DATETIME |2013-06-03 00:10:07 |2013-06-01 00:35:00 |

### THE SOND PART OF FIRST QUESTION:

In the second part, we had to find to total number of rows.


This particular task is fairly easy as we just had to place a counter***inside the loop*** and ***print the value of the counter outside the loop*** to avoid printing while it is counting.
```python
    for i,line in enumerate(reader):
        count=count+1
    print(f" Total number of rows in this particular dataset are {count}")
```
### The result are as follows:

### Total number of rows in this particular dataset are 14385457
