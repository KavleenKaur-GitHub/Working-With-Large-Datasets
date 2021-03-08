# Assignment-4
### In this assignment, we were provided with the task of analyzing a ***large dataset*** which contained the information about ***taxi rides in NYC***. In order to achieve the given task, there certainly were some challenges which are explained here along with every single task description. 


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
     
### IN ORDER TO FIND MAXIMUM AND MINIMUN RANGE OF LATTITUDES, WE DO NEED SOME FACTS. SO, ACCORDING TO THE WEBSITE GIVEN BELOW, THE RANGE OF LATTITUDE AND LONGITUDE OF NYC ARE AS FOLLOWS:


### GPS COORDINATE:
-***LATTITUDE***42.165726	
-***LONGITUDE***-74.948051
### DATA SOURCE:
[WEBSITE FOR INFORMATION][https://inkplant.com/code/state-latitudes-longitudes]
### SO, THE RANGE OF MINIMUM AND MAXIMUM MUST LIE WITHIN IT.


IN ORDER TO SOLVE THIS QUESTION WE FIRST HAVE TO MAKE A LIST OF COLUMNS CONTAINING THE LATTITUDES AND THE LONGITUDES.

```python
 for i,line in enumerate(reader):
        picklat.append(line[11])
        picklong.append(line[10]) 
        droplat.append(line[13])
        droplong.append(line[12])
```

### Now, we must remember that to perform any operation, it must be converted to either ***int type*** or ***float type*** depending on the values.

``` python
    picklat = [float(i) for i in picklat[1:]]
    picklong = [float(i) for i in picklong[1:]]
    droplat = [float(i) for i in droplat[1:]]
    droplong = [float(i) for i in droplong[1:]]
```
This particular codew converts entire list of lattitudes and longitudes into float type.

### An interesting point to note here is that the headers rows are removed because we cannot convert string into float. (picklat[1:])


After this particular step, we have to initialise min and max at the first value of each coulumn so that we can check and then later chnge the values. By doing this, we can get id (index number) of the line. From the line, we can get the corresponding lattitude or longitude and then use a website to see which place has the minimum lattitude or the minimum longitude. But we have to bear in mind that we have to do this for four columns-pickup_lattitude,pickup_longitude,dropoff_lattitude and drop_off longitude.
```python
    minpicklat=picklat[0]
    maxpicklat=picklat[0]
    for x in picklat[1:]:
        if(minpicklat > picklat[count]):
            minpicklat=picklat[count]
            id1=count
        if(maxpicklat < picklat[count]):
            maxpicklat=picklat[count]
            id2=count
        count=count+1
    print(id1)
    print(id2)
```
### The same can be done for the rest three

### For getting ***corresponding lattitudes and longitude***:

```python
    max_pickup_lattitude=line[4752898].split(",")[12]
    max_pickup_longitude=line[4752898].split(",")[13]
    print(max_pickup_lattitude) #max lattitude
    print(max_pickup_longitude)
    min_pickup_lattitude=line[14310378].split(",")[12]
    min_pickup_longitude=line[14310378].split(",")[13]
    print(min_pickup_lattitude) #min lattitude
    print(min_pickup_longitude)
    min_pickup=[min_pickup_lattitude,min_pickup_longitude]
    max_pickup=[max_pickup_lattitude,max_pickup_longitude]
 ```



![image](https://user-images.githubusercontent.com/38343820/110364097-60452e00-8069-11eb-867d-bebea3415b12.png)

### Website used to know the location:
[Website to know the location][https://www.gps-coordinates.net/]

![image](https://user-images.githubusercontent.com/38343820/110365687-51f81180-806b-11eb-9756-c42c4d730e7d.png)
![image](https://user-images.githubusercontent.com/38343820/110371542-211bda80-8073-11eb-8fd0-48af109f8420.png)

### The same goes for dropoff longitudes and lattitude.

    min_dropoff=[40.908452,-74.405731]
    max_dropoff=[40.649765,-73.460228]
    
![image](https://user-images.githubusercontent.com/38343820/110368477-16f7dd00-806f-11eb-85b7-ad359baaf5b4.png)
![image](https://user-images.githubusercontent.com/38343820/110368581-3e4eaa00-806f-11eb-9125-20efaa594c4a.png)

### In order to plot, we need to iport the pyplot from matpolib. 
```python
import matplotlib.pyplot as plt
```
Now, we use pyplot to plot a graph. the color attribute soecifies the color of the line and marker shows the type of plot points used.Pytitle helps us to give title of pour graph. Plt.xlabel and plt.ylabel help us to label x and y axis.

```python
    min_pickup=[min_pickup_lattitude,min_pickup_longitude]
    max_pickup=[max_pickup_lattitude,max_pickup_longitude]
    plt.plot(min_pickup,max_pickup,color='red', marker='o')
    plt.title('GEOGRAPHICAL RANGE OF PICK_UP LATTITUDE', fontsize=12)
    plt.xlabel('MIN', fontsize=14)
    plt.ylabel('MAX', fontsize=14)
    plt.grid(True)
    plt.show()
```
# The rest are plotted the same.
# The graphs are as follows.
![geographical range of pick_up lattitude](https://user-images.githubusercontent.com/38343820/110370110-4a3b6b80-8071-11eb-8d0e-00d655dbdec3.png)
![GEOGRAPHICAL RANGE OF PICK_UP LONGITUDE](https://user-images.githubusercontent.com/38343820/110370119-4dcef280-8071-11eb-920a-95ea0d620ade.png)
![GEOGRAPHICAL RANGE OF DROP_OFF Lattitude](https://user-images.githubusercontent.com/38343820/110370151-57f0f100-8071-11eb-9117-4e9915a91582.png)
![GEOGRAPHICAL RANGE OF DROPOFF LONGITUDE](https://user-images.githubusercontent.com/38343820/110370167-5b847800-8071-11eb-9bd2-c96ca3c37c96.png)

# SIXTH QUESTION:

In this particular question, we have to find out the unique values in each field.

###  STEP-1:
INITIATE AN EMPTY LIST OF ALL THE COLUMNS AND THEN APPEND ALL THE VALUES IN THE LIST.

```python
 medallion.append(line[0])
        hack_license.append(line[1])
        vendor_id.append(line[2])
        rate_code.apppend(line[3])
        store_and_fwd_flag.apppend(line[4])
        pickup_datetime.apppend(line[5])
        dropoff_datetime.apppend(line[6])
        passenger_count.apppend(line[7])
        trip_time_in_sec.apppend(line[8])
        trip_distance.apppend(line[9])
        pick_up_longitude.apppend(line[10])
        pick_up_lattitude.apppend(line[11])
        dropoff_longitude.apppend(line[12])
        dropoff_lattitude.apppend(line[13])
```
# ***STEP -2***
ACCORDING TO THE WEBSITE, WE KNOW THAT TO GET UNIQUE VALUES, WE HAVE TO USE SET FUNCTION AND FUNCTION IS VERY QUICK AND WAS VERY HELPFUL IN SOLVING THIS QUERY.


[WEBSITE FOR INFORMATION][https://www.geeksforgeeks.org/python-get-unique-values-list/]


### SO, WE CAN USE SET FUNCTION TO FIND UNIQUE VALUES
```python
unique_word_rate_code=set(rate_code[1:])
    print(unique_word_rate_code)
    unique_words_medallion = set(medallion[1:])
    print(unique_words_medallion)
    unique_words_hack_license = set(hack_license[1:])
    print(unique_words_hack_license)
    unique_word_vendor_id=set(vendor_id[1:])
    print(unique_word_vendor_id)
    unique_word_store_and_fwd_flag=set(store_and_fwd_flag[1:])
    print(unique_word_store_and_fwd_flag)
    unique_word_ pickup_datetime=set(pickup_datetime[1:])
    print(unique_word_pickup_datetime)
    unique_word_dropoff_datetime=set(dropoff_datetime[1:])
    print(unique_word_dropoff_datetime)
    unique_word_passenger_count=set(passenger_count[1:])
    print(unique_word_passenger_count)
    unique_word_trip_time_in_sec=set(trip_time_in_sec[1:])
    print(unique_word_trip_time_in_sec)
    unique_word_trip_distance=set(trip_distance[1:])
    print(unique_word_trip_distance)
    unique_word_pick_up_longitude=set(pick_up_longitude[1:])
    print(unique_word_pick_up_longitude)
    unique_word_pick_up_lattitude=set(pick_up_lattitude[1:])
    print(unique_word_pick_up_lattitude)
    unique_word_ dropoff_lattitude=set( dropoff_lattitude[1:])
    print(unique_word_dropoff_lattitude)
    unique_word_dropoff_longitude=set(dropoff_longitude[1:])
    print(unique_word_dropoff_longitude)
```
### IN THIS CODE, WE HAVE EXEMPTED THE FIRST COLUMN AS THE FIRST COLUMN FOR ALL ARE THE HEADERS AND WE DID NOT WANTED IT COLLABERATED IN OUR LIST OF UNIQUE VALUES.

###  OUTPUT
### SOME OUTPUTS ARE TOO LONG TO PUT IN HERE SO AVOIDING THOSE, I AM PRINTING THE REST:
|FIELD_NAME | UNIQUE_ VALUES |
|-----------|----------------|
|VENDOR_ID  | {'VTS', 'CMT'} |
|RATE_CODE  | {'1', '3', '4', '0', '210', '9', '5', '6', '8', '2', '77'} |
| store_and_fwd_flag|{'N', '', 'Y'}|
| passenger_count |{'1', '4', '3', '0', '5', '6', '8', '208', '2'} |

# SEVENTH QUESTION:

IN ORDER TO SOLVE THIS QUESTION WE FIRST HAVE TO MAKE A LIST OF COLUMNS CONTAINING EVERY OTHER FIELD EXCEPT FOR THE LATTITUDES AND THE LONGITUDES.


```python
 for i,line in enumerate(reader):
        rate_code.append(line[3])
        passenger_count.append(line[7])
        trip_distance.append(line[9])
        trip_in_sec.append(line[8]
```


### REST OF THE FIELDS ARE STRING VARIABLE SO FINDING MINIMUM AND MAXIMUM OF THESE VARIABLES IS NOT POSSIBLE. Except their length can be compared. 


### Now, we must remember that to perform any operation, it must be converted to either ***int type*** or ***float type*** depending on the values.

``` python
    rate_code =[int(i) for i in rate_code[1:]]
    passenger_count=[int(i) for i in passenger_count[1:]]
    trip_in_sec=[int(i) for i in trip_in_sec[1:]]
    trip_distance=[float(i) for i in trip_distance[1:]]
```

### This particular code converts entire list of trip_distance into float type as it should be a float type. Rest all contain int values

### An interesting point to note here is that the headers rows are removed because we cannot convert string into float. (rate_code[1:])


After this particular step, we have to initialise min and max at the first value of each coulumn so that we can check and then later change the values by going through in a loop. By doing this, we can get minimum and maximum values of all fields. 

```python
    minrate=rate_code[0]
    maxrate=rate_code[0]
    for x in rate_code[1:]:
        if(minrate > rate_code[count]& minrate!=0):
            minrate=rate_code[count]
            id1=count
        if(maxrate < rate_code[count]):
            maxrate=rate_code[count]
            id2=count
        count=count+1
    print(minrate)
    print(maxrate)
```
### OUTPUT (FOR ONLY RATE_CODE)

1
120

### the same could be done for rest three variables.

### ALTERNATIVE METHOD:

COULD HAVE FOUND THE UNIQUE VALUES AND THEN SEARCHED FOR MIN AND MAXIMUM VALUES.

```python
for i,line in enumerate(reader):
        rate_code.append(line[3])
    unique_words_rate_code=set(rate_code[1:])
    print(unique_words_rate_code)
    for value in range(0,len(unique_words_rate_code)):
         print(unique_words_rate_code[value], end='')
```

# EIGHTH QUESTION

IN THIS QUESTION, WE HAVE TO FIND THE AVERAGE NUMBER OF PASSENGERS EACH HOUR OF THE DAY.

SO, AFTER APPENDING THE ROWS NEEDED AND CHANGING IT INTO INTEGER FORMAT( TRIP_TIME _IN_SEC, PASSENGER_COUNT), WE HAVE TO KEEP IN MIND TO CHANGE EVERY TRIP TIME IN SECOND TO HOURS.
```python
    for i,line in enumerate(reader):
        passenger_count.append(line[3])
        trip_in_sec.append(line[8])
    passenger_count =[int(i) for i in passenger_count[1:]]
    trip_in_sec =[int(i) for i in trip_in_sec[1:]]
```
### CHANGING TIME FROM SEC TO HOURS.
WE SHOULD DIVIDE EVERY VALUE BY 3600.
```python
  for x in trip_in_sec[1:]:
        value=trip_in_sec[count]/sec
        trip_in_hour.append(value)
        count=count+1
```
WE HAVE CREATED ***TRIP_IN_HOUR*** THAT CONTAINS TIME IN HOURS

NOW, FINDING AVERAGE NUMBER OF PASSENGER EVERY HOUR BY DIVING NUMBER OF PASSENGER BY NUMBER OF HOURS.

```python
  for x in range(1,len(passenger_count[1:])):
        try:
            value=passenger_count[count2]/trip_in_hour[count2]
        except:ZeroDivisionError
        sum=sum+value
        count2=count2+1
    print(sum) 
```
### BECAUSE IN HERE SOME VALUES ARE 0 DUE TO INCORRECT DATA, WE HAD TO DO EXCEPTION HANDLING FOR ZERO ERRROR.

NOW, WE FIND AVERAGE NUMBER OF PASSENGER FOR EVERY HOUR BY INITIALISING AN HOUR LIST AND FINDING THE AVERAGE FOR ALL.

```python 
for i in hour:
        average.append((sum/len(passenger_count[1:]))*i)
    print(average)
```
NOW, TO PLOT WE USE PYPLOT LIBRARY AS DISCUSSED ABOVE.

```python
    plt.plot(hour,average,color='red', marker='o')
    plt.title('average number of passenger per hour', fontsize=12)
    plt.xlabel('hour', fontsize=14)
    plt.ylabel('number of passenger', fontsize=14)
    plt.grid(True)
    plt.show()
```
![image](https://user-images.githubusercontent.com/38343820/110379648-1bc38d80-807d-11eb-8c22-87b58fb2fc44.png)

# NINTH QUESTION
IN THIS WE HAVE TO WORK ON EVERY 1 IN A 1000 ROW. SO, A SIMPLER WAY TO DO THAT COULD BE UDING ***PANDAS*** WITH CHUNKSIZE ATTRIBUTE BUT HERE, WE HAVE USE COUNT AS OUR COUNTER AND CHECH THE LINE INDEX, IF IT IS FULLY DIVISIBLE BY THOUSAND ( i%1000==0) THEN, THAT ROW SHOULD BE USED FOR ANY OPERATION. SINCE THE FIRST INDEX IS ZERO, IT WOULD HAVE COUNTERED ZERO EXCEPTION ERROR, I DID ADDED ADDED AN IF STATEMENT THAT PREVENTED 0 TH ROW TO BE EXECUTED.

```python
import csv
import matplotlib.pyplot as plt
passenger_count=[]
count=0
with open('trip_data_6.csv',) as f:
    reader=csv.reader(f)
    for i,line in enumerate(reader):
        if(count>=1):
            if(count%1000==0):
                passenger_count.append(line[3])
        count=count+1
    print(len(passenger_count)) 
```
![image](https://user-images.githubusercontent.com/38343820/110381730-e1a7bb00-807f-11eb-8210-4d4e0abab5d8.png)


### AS WE CAN SEE THAT THE NUMBER OF ROWS HAVE REDUCED SUBSTANCIALLY.


# TENTH QUESTION

AS WE CAN SEE THAT AFTER REDUCING THE ROWS IN ABOVE QUESTION, WE CAN REPEAT THE SAME PROCESS IN EIGHTH QUESTION AS ABOVE. THE NEW PLOT IS GIVEN BELOW.

![average number of passengers(question 10)](https://user-images.githubusercontent.com/38343820/110382318-be314000-8080-11eb-8228-9d9c26adb82a.png)

### THE GRAPH DOES NOT SEEM DIFFERENT BUT THE AVERAGE VALUES CALCULATED DO SHOW A VERY SMALL DIFFERENCE.

### Second dataset(REDUCED DATASET)
### 129876.71765961662
[9.029876775333145, 18.05975355066629, 27.089630325999437, 36.11950710133258, 45.14938387666572, 54.179260651998874, 63.20913742733202, 72.23901420266516, 81.26889097799831, 90.29876775333145, 99.3286445286646, 108.35852130399775, 117.38839807933088, 126.41827485466403, 135.44815162999717, 144.47802840533032, 153.50790518066347, 162.53778195599662, 171.56765873132974, 180.5975355066629, 189.62741228199604, 198.6572890573292, 207.68716583266234, 216.7170426079955]
### question 8 (NOT REDUCED DATASET)
### 134581214.30726555
[9.35536723080817, 18.71073446161634, 28.06610169242451, 37.42146892323268, 46.77683615404085, 56.13220338484902, 65.48757061565719, 74.84293784646536, 84.19830507727353, 93.5536723080817, 102.90903953888987, 112.26440676969804, 121.61977400050621, 130.97514123131438, 140.33050846212257, 149.68587569293072, 159.04124292373888, 168.39661015454706, 177.75197738535525, 187.1073446161634, 196.46271184697156, 205.81807907777974, 215.17344630858793, 224.52881353939608]
