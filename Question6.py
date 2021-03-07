import csv
with open('trip_data_6.csv') as f:
    reader=csv.reader(f)
    vendor_id=[]
    pickup_datetime=[]
    dropoff_datetime=[]
    passenger_count=[]
    trip_time_in_sec=[]
    trip_distance=[]
    pick_up_lattitude=[]
    pick_up_longitude=[]
    dropoff_lattitude=[]
    dropoff_longitude=[]
    store_and_fwd_flag=[]
    rade_code=[]
    hack_license=[]
    medallion=[]
    for i,line in enumerate(reader):
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
        
