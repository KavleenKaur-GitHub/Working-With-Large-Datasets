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
        unique_words_medallion = set(medallion[1:])
        hack_license.append(line[1])
        unique_words_hack_license = set(hack_license[1:])
        vendor_id.append(line[2])
        unique_word_vendor_id=set(vendor_id[1:])
        rate_code.apppend(line[3])
        unique_word_rate_code=set(rate_code[1:])
        store_and_fwd_flag.apppend(line[4])
        unique_word_store_and_fwd_flag=set(store_and_fwd_flag[1:])
        pickup_datetime.apppend(line[5])
        unique_word_ pickup_datetime=set(pickup_datetime[1:])
        dropoff_datetime.apppend(line[6])
        unique_word_dropoff_datetime=set(dropoff_datetime[1:])
        passenger_count.apppend(line[7])
        unique_word_passenger_count=set(passenger_count[1:])
        trip_time_in_sec.apppend(line[8])
        unique_word_trip_time_in_sec=set(trip_time_in_sec[1:])
        trip_distance.apppend(line[9])
        unique_word_trip_distance=set(trip_distance[1:])
        pick_up_longitude.apppend(line[10])
        unique_word_pick_up_longitude=set(pick_up_longitudee[1:])
        pick_up_lattitude.apppend(line[11])
        unique_word_pick_up_lattitude=set(pick_up_lattitude[1:])
        dropoff_longitude.apppend(line[12])
        unique_word_dropoff_longitude=set(dropoff_longitude[1:])
        dropoff_lattitude.apppend(line[13])
        unique_word_ dropoff_lattitude=set( dropoff_lattitude[1:])
    print(unique_word_rate_code)
    print(unique_words_medallion)
    print(unique_words_hack_license)
    print(unique_word_vendor_id)
    print(unique_word_store_and_fwd_flag)
    print(unique_word_pickup_datetime)
    print(unique_word_dropoff_datetime)
    print(unique_word_passenger_count)
    print(unique_word_trip_time_in_sec)
    print(unique_word_trip_distance)
    print(unique_word_pick_up_lattitude)
    print(unique_word_pick_up_longitude)
    print(unique_word_dropoff_lattitude)
    print(unique_word_dropoff_longitude)
        
