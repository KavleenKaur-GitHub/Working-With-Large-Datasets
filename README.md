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


# SECOND QUESTION:

In order to find the field name, we just have to use the above concept.In this, instead of printing the first line, we have to print the heeder line which is indexed at 0. In order to print in a proper column format, we can use looping to print every column in the row. Apart from this, for proper presentation, we can add count too in the loop.

```python
count=1
with open('trip_data_6.csv') as f:
    reader=csv.reader(f)
    line=f.read().splitlines()
    fieldnames=line[0]
    names=fieldnames.split(",")
    print("NUMBER| FIELD NAME")
    for fields in names:
        print(" " " " " " " " " " "{}|{}".format(count,fields))
        count=count+1
 ```
 ### The result are as follows:
 
 |  COLUMN NUMBER   |    FIELD NAME  | 
|-----------------|-----------------| 
|     1             |  medallion    |
|     2             | hack_license   |
|     3             | vendor_id      |
|     4             | rate_code      |
|     5             | store_and_fwd_flag|
|     6             | pickup_datetime |
|     7             | dropoff_datetime |
|     8             | passenger_count |
|     9             | trip_time_in_secs |
|     10            | trip_distance   |
 |    11            | pickup_longitude |
|     12            | pickup_latitude |
|     13            | dropoff_longitude |
|     14            | dropoff_latitude | 


# python output

     1|medallion
     2| hack_license
     3| vendor_id
     4| rate_code
     5| store_and_fwd_flag
     6| pickup_datetime
     7| dropoff_datetime
     8| passenger_count
     9| trip_time_in_secs
     10| trip_distance
     11| pickup_longitude
     12| pickup_latitude
     13| dropoff_longitude
     14| dropoff_latitude
     
# DESCRIPTION:
- ***medallion:*** It refers to the tranferrable permit of the taxi driver driving that particular vehicle.
- ***hack_license:*** It refers to the licence of the driver of the cab that allows the person to drive a car for hire.
- ***vendor_id:*** It refers to the vendor id.e.g.,Verifone Tranfortation System(VTS) or Mobile Knowledge System Inc(CMS)
- ***rate_code:*** It refers to the taximeter rate
- ***store_and_fwd_flag:*** It refers to whether a cab has a flag in its front or not(Y/N).
- ***pickup_datetime:*** It refers to date and time when the cab picked up the passenger.
- ***dropoff_datetime:*** It refers to date and time when the cab dropped off the passenger.
- ***passenger_count:*** It refers to the amount of passengers onboard the vehicle.
- ***trip_time_in_secs:*** It refers to the amount of time calculated in seconds by the cab to pickup a passenger and then drop off the passenger. 
- ***trip_distance:***  It refers to the distance calculated to pickup a passenger and then drop off the passenger.
- ***pickup_longitude:*** It refers to the longitude of the place where the cab picked up the passenger
- ***pickup_latitude:*** It refers to the lattitude of the place where the cab picked up the passenger
- ***dropoff_longitude:*** It refers to the longitude of the place where the cab dropped off the passenger
- ***dropoff_latitude:*** It refers to the lattitude of the place where the cab dropped off the passenger


# THIRD QUESTION

In order to find some sample data, we just have to print few lines. For this purpose, we will use ***range*** function that will help us print first few rows.


```python
  for i in range(10):
        line=f.readline()
        print(line)
```

### FEW OUTPUTS OF THE CODE ARE GIVEN BELOW :

medallion, hack_license, vendor_id, rate_code, store_and_fwd_flag, pickup_datetime, dropoff_datetime, passenger_count, trip_time_in_secs, trip_distance, pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude
D1C79CF706C80D3A1DC7FBCA6CD56E43,DAC7742E8F00034774098DBC6B4FF2B7,CMT,1,N,2013-06-03 00:02:12,2013-06-03 00:10:07,1,474,1.30,-73.981583,40.773529,-73.981827,40.782124
3567E8B49FEBFCBB587F1864D723D5C8,430B8022563CDE1D51D44786DFD8D6CB,CMT,1,N,2013-06-03 00:03:03,2013-06-03 00:19:27,1,982,4.90,-73.999565,40.728367,-73.952927,40.729546
4220E1995D36A40DF34664AD33ED13F6,48A1C9C9300AFC7BDBB718CE308EE45A,CMT,2,N,2013-06-03 00:01:30,2013-06-03 00:28:11,1,1745,17.70,-73.788445,40.641151,-73.985451,40.744194
440900089FF528A873424DED689C77A3,E6A63B40E565A8A03AF32E0B138F5EB1,CMT,1,N,2013-06-03 00:04:14,2013-06-03 00:27:50,1,1415,12.10,-73.862816,40.768875,-74.008797,40.738842
16129167D9E7B0846DBA3D04B78E1B8D,227A03FC03CF429DFC9EAFF0AE8BA579,CMT,1,N,2013-06-03 00:04:53,2013-06-03 00:10:46,1,353,1.10,-73.964905,40.806881,-73.962349,40.794987


  
### IN THIS, THE FIELDS NAMES AND THEIR VALUES IN EACH ROW ARE ARE SEPERATED BY COMMA'S. SO, IT IS FAIRLY EASY TO MAP THE FILED NAMES WITH THER VALUES.


| medallion| hack_license| vendor_id| rate_code |store_and_fwd_flag |pickup_datetime | dropoff_datetime|passenger_count| trip_time_in_secs|trip_distance| pickup_longitude|pickup_latitude |dropoff_longitude|dropoff_latitude|  
| ---------| --------|--------|------- |--------- |-------- | ---------|-------| ---------|--------| --------|------- |---------|-----------| 
| D1C79CF706C80D3A1DC7FBCA6CD56E43|DAC7742E8F00034774098DBC6B4FF2B7|CMT|1|N|2013-06-03 00:02:12|2013-06-03 00:10:07|1|474|1.30|-73.981583|40.773529|-73.981827|40.782124|
|3567E8B49FEBFCBB587F1864D723D5C8|430B8022563CDE1D51D44786DFD8D6CB|CMT|1|N|2013-06-03 00:03:03|2013-06-03 00:19:27|1|982|4.90|-73.999565|40.728367|-73.952927|40.729546|
|4220E1995D36A40DF34664AD33ED13F6|48A1C9C9300AFC7BDBB718CE308EE45A|CMT|2|N|2013-06-03 00:01:30|2013-06-03 00:28:11|1|1745|17.70|-73.788445|40.641151|-73.985451|40.744194 |


# FOURTH QUESTION:

| FIELD NAME| DATATYPE|SIZE|REASONS |
|-----------|---------|-------|-------|
| medallion| VARCHAR| 50| VARCHAR BECAUSE IT IS A COMBINATION OF BOTH NUMBER AND CHARACTER AND THE SIZE IS 50 BECAUSE IT IS APPRX 50 LETTERS LONG |
|hack_license|VARCHAR|50| VARCHAR BECAUSE IT IS A COMBINATION OF BOTH NUMBER AND CHARACTER AND THE SIZE IS 50 BECAUSE IT IS APPRX 50 LETTERS LONG |
|vendor_id|VARCHAR |4|VARCHAR BECAUSE IT IS CHAR AND THE SIZE IS 4 BECAUSE IT IS APPRX 3 CHARACTER LONG BUT JUST TO BE SAFE, IT SHOULD BE 4| 
|rate_code |INT |2| INT BECAUSE IT IS ONLY NUMBER AND THE SIZE IS 2 BECAUSE IT IS APPRX 1 NUMBER LONG BUT JUST TO BE SAFE, IT SHOULD BE 2|
|store_and_fwd_flag |VARCHAR |2|VARCHAR BECAUSE IT IS CHAR AND THE SIZE IS 2 BECAUSE IT IS APPRX 1 CHARACTER LONG BUT JUST TO BE SAFE, IT SHOULD BE 2|
|pickup_datetime | DATETIME| 25| DATTIME BECAUSE IT IS A DATETIME
|dropoff_datetime|DATETIME| 25| DATTIME BECAUSE IT IS A DATETIME
|passenger_count|INT |2| INT BECAUSE IT IS ONLY NUMBER AND THE SIZE IS 2 BECAUSE IT IS APPRX 1 NUMBER LONG BUT JUST TO BE SAFE, IT SHOULD BE 2|
|trip_time_in_secs| INT |10| INT BECAUSE IT IS ONLY NUMBER AND THE SIZE IS 10 BECAUSE IT IS CALCULATED IN SECONDS|
|trip_distance| DECIMAL| (4,7)| DECIMAL BECAUSE IT CONTAINS DECIMAL VALUES AND IS MAXIMUM 4 NUMBERS LONG FOLLOWED BY 7 DECIMAL POINTS|
|pickup_longitude|DECIMAL| (4,7)| DECIMAL BECAUSE IT CONTAINS DECIMAL VALUES AND IS MAXIMUM 4 NUMBERS LONG FOLLOWED BY 7 DECIMAL POINTS|
|pickup_latitude |DECIMAL| (4,7)| DECIMAL BECAUSE IT CONTAINS DECIMAL VALUES AND IS MAXIMUM 4 NUMBERS LONG FOLLOWED BY 7 DECIMAL POINTS|
|dropoff_longitude|DECIMAL| (4,7)| DECIMAL BECAUSE IT CONTAINS DECIMAL VALUES AND IS MAXIMUM 4 NUMBERS LONG FOLLOWED BY 7 DECIMAL POINTS|
|dropoff_latitude| DECIMAL| (4,7)| DECIMAL BECAUSE IT CONTAINS DECIMAL VALUES AND IS MAXIMUM 4 NUMBERS LONG FOLLOWED BY 7 DECIMAL POINTS| 

### IN THIS QUESTION, THE MOST IMPORTANT POINT TO NOTE WOULD BE THAT WHEN WE PUT THESE VALUES INTO A SQL DATABASE, ONE PROBLEM THAT COULD OCCUR IS THAT THE DATETIME WOULD NOT BE IN TAKEN IN DESIRED FORMAT. SO, WE WOULD LIKE TO IMPORT DATETIME IN ORDER TO CONVERT INTO THE DESIRED FORMAT.  


# FIFTH QUESTION
     
