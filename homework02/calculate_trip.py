import json
import math

mars_radius = 3389.5    # km

def calc_gcd(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float) -> float:
    lat1, lon1, lat2, lon2 = map( math.radians, [latitude_1, longitude_1, latitude_2, longitude_2] )
    d_sigma = math.acos( math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(abs(lon1-lon2)))
    return ( mars_radius * d_sigma )

def calc_trip_time(lat_1: float, long_1: float, lat_2: float, long_2: float) -> float:
    distance = calc_gcd(lat_1, long_1, lat_2, long_2)
    return (distance / 10)

def main():

    with open('sites.json', 'r') as f:
        data_sites = json.load(f)
    
    total_time = 0
    lat_1 = 16.0
    long_1 = 82.0
    leg = 0
    count = 0

    for i in data_sites['sites']:
        latitude = data_sites['sites'][count]['latitude']
        longitude = data_sites['sites'][count]['longitude']
        composition = data_sites['sites'][count]['composition']
        count += 1

        lat_2 = latitude
        long_2 = longitude

        sample_time = 0

        if composition == "stony":
            sample_time = 1
        elif composition == "iron":
            sample_time = 2
        else:
            sample_time = 3

        travel_time = calc_trip_time(lat_1, long_1, lat_2, long_2)

        total_time += (travel_time + sample_time)

        lat_1 = lat_2
        long_1 = long_2
        leg += 1        

        print("leg = ", str(leg), ", time to travel = ", str(round(travel_time, 2)), " hr, time to sample = ", str(sample_time), " hr")


    print("===============================================================")
    print("number of legs = 5, total time elapsed = ", str(round(total_time, 2)), " hr")

if __name__ == '__main__':
    main()
