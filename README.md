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
   
### But being a file more than 2.5 GB,it is more than unlikely that this method is best. The amount od time taken by this script coud be huge for a file this large


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



