# Investigating Five Meteorite Landing Sites

## Project Objective
This folder contains two Python scripts: calculate_trip.py and generate_sites.py

The purpose of this project was to learn more abot JSON through a scenario where I am operating a robotic vehicle on Mars. The task is to investigate five meteorite landing sites in Syrtis Major. The scripts work together to randomly generate meteorite sites and calculate the distance it would take a robot to travel between those sites.

## Description of Python Scripts
### generate_sites.py
This Python script randomly generates a latitude, longitude, and composition for five different meteorite landing sites. The script creates a JSON file called "sites.json" that stores this information.
### calculate_trip.py
This Python script reads in the meteorite site JSON file ("sites.json") and calculates the time required to visit and take samples from the five sites in order. The script outputs the travel time and sample time for each individual site as well as the total time for all sites combined.

The function calc_gcd below was given in Slack. It is the great-circle distance algorithm and it calculates the distance between points.

    def calc_gcd(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float) -> float:
        lat1, lon1, lat2, lon2 = map( math.radians, [latitude_1, longitude_1, latitude_2, longitude_2] )
        d_sigma = math.acos( math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(abs(lon1-lon2)))
        return ( mars_radius * d_sigma )

## Instructions to Run Code
First, enter the command "python3 generate_sites.py". This will generate a file called "sites.json" containing randomized data for all five meteorite sites. Next, enter the command "python3 calculate_trip.py". This script will output the time it takes to travel to each site and take a sample. It will also show the total time that it took to complete all legs of the journey.
