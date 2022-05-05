# Analyzing Water Quality Data

## Project Objective
This folder contains two Python scripts: analyze_water.py and test_analyze_water.py

The purpose of this project was to work more with JSON and unit testing by continuing a scenario where I am operating a robotic vehicle on Mars. The task is to check the latest water quality data to assess whether it is safe to analyze samples, or if the Mars lab should go on a boil water notice. The scripts work together to read in the water quality data set and perform unit testing for the functions in the script.

## Downloading the Data Set
To download the data set from the original source, use the following command in the command line while in the homework03 directory:
```
wget https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json
```

## Description of Python Scripts
### analyze_water.py
This Python script calculates the turbidity of the water from the water quality data set. If the water turbidity is below a certain threshold, a warning is sent to the use. If the water turbidity is above that threshold, the program calculates the minimum time required for turbidity to fall below the safe threshold.
### test_analyze_water.py
This Python script runs five different unit tests. These tests check the validity of the functions defined in the analyze_water.py script.

## Instructions to Run Code
After downloading the JSON file using the directions above, enter the command "python3 analyze_water.py". This will tell the user if the water is safe to use based on the water turbidity. Example output is shown here:

```
Average turbidity based on most recent five measurements = 1.166279 NTU
WARNING: Turbidity is above threshold for safe use
Minimum time required to return below a safe threshold = 7.61374881476668 hours
```

Next, enter the command "python3 test_analyze_water.py". This script will run unit tests on the functions created in "analyze_water.py" to ensure that everything is valid.
