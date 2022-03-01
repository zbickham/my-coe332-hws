# Containerizing Code Using Docker
This folder contains a containerization script (`Dockerfile`), two Python scripts (`ml_data_analysis.py` and `test_ml_data_analysis.py`), and JSON data (`Meteorite_Landings.json`)

## Project Objective
The purpose of this project was to learn about containerization with Docker by expanding upon the meteorite data used in previous projects. The task is to update the `ml_data_analysis.py` script and then write a `Dockerfile` to containerize that script (as well as the test script and a copy of the example data set) so that anyone can pull the files.

## Description of Files
### ml_data_analysis.py
This Python script has been updated so that it can run without needing the python3 command. The structure of the output has also been modified so that it is more clear and easier to interpret. It provides information about the meteorites such as the average mass, location, and class. 
### test_ml_data_analysis.py
This Python script runs six different unit tests. These tests check the validity of the functions defined in the `ml_data_analysis.py script`.
### Meteorite_Landings.json
This is JSON data that contains information about the meteorites. The data is used in the `ml_data_analysis.py` script.
### Dockerfile
This file contains commands that containerize the `ml_data_analysis.py` script, the test script (for pytest), and a copy of the example data set.

## Instructions to Run Code
- To pull and use the existing image from my Docker Hub repository, use the following command in the terminal:
```bash
$ docker pull zbickham/ml_data_analysis:hw04
```
> Beginning of expected output:
```
hw04: Pulling from zbickham/ml_data_analysis
```

- The inclusion of the `Dockerfile` will allow you to build an image of the container by using the following command in the terminal:
```bash
$ docker build -t zbickham/ml_data_analysis:hw04 .
```
> Beginning of expected output:
```
Sending build context to Docker daemon   16.9kB
Step 1/10 : FROM centos:7.9.2009
 ---> eeb6ee3f44bd
Step 2/10 : RUN yum update -y
```

- To run the containerized code against the sample data inside the container, use the following command in the terminal. The first command allows you to enter the container while the second command runs the code and data file within the containter:
```bash
$ docker run --rm -it -v $PWD:/data zbickham/ml_data_analysis:hw04 /bin/bash
$ ml_data_analysis.py /code/Meteorite_Landings.json
```
> Expected output:
```
Summary data following meteorite analysis:

Average mass of 30 meteor(s):
83857.3 grams

Hemisphere summary data:
There were  21  meteors found in the Northern & Eastern quadrant
There were  6  meteors found in the Northern & Western quadrant
There were  0  meteors found in the Southern & Eastern quadrant
There were  3  meteors found in the Southern & Western quadrant

Class summary data:
The  L5  class was found  1  times
The  H6  class was found  1  times
The  EH4  class was found  2  times
The  Acapulcoite  class was found  1  times
The  L6  class was found  6  times
The  LL3-6  class was found  1  times
The  H5  class was found  3  times
The  L  class was found  2  times
The  Diogenite-pm  class was found  1  times
The  Stone-uncl  class was found  1  times
The  H4  class was found  2  times
The  H  class was found  1  times
The  Iron-IVA  class was found  1  times
The  CR2-an  class was found  1  times
The  LL5  class was found  2  times
The  CI1  class was found  1  times
The  L/LL4  class was found  1  times
The  Eucrite-mmict  class was found  1  times
The  CV3  class was found  1  times
```
Make sure to use the command `exit` to leave the container once you are finished.

- If you have your own data that you would like to use, you can run the following command.

NOTE: The exact commands shown below use additional Meteorite Landing data. You can use the exact commands to download this data and run the containerized scripts against this data. However, if you would like to use other data, simply replace the link after the `wget` command with the link to your data and navigate to your data once in the container (not `ML_Data_Sample.json`).
```bash
$ wget https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json
$ docker run --rm -v $PWD:/data zbickham/ml_data_analysis:hw04 ml_data_analysis.py /data/ML_Data_Sample.json
```
> Expected output using additional Meteorite Landing data provided:
```
Summary data following meteorite analysis:

Average mass of 300 meteor(s):
5081.37 grams

Hemisphere summary data:
There were  71  meteors found in the Northern & Eastern quadrant
There were  86  meteors found in the Northern & Western quadrant
There were  74  meteors found in the Southern & Eastern quadrant
There were  69  meteors found in the Southern & Western quadrant

Class summary data:
The  H4  class was found  22  times
The  L6  class was found  18  times
The  CI1  class was found  29  times
The  L5  class was found  36  times
The  LL3-6  class was found  27  times
The  LL5  class was found  39  times
The  CV3  class was found  24  times
The  CR2-an  class was found  26  times
The  H6  class was found  31  times
The  EH4  class was found  22  times
The  H5  class was found  26  times
```

- To run the containerized test suite with pytest, you can use the following commands. The first two navigate inside the container while the third runs the unit tests:
```bash
$ docker run --rm -it -v $PWD:/data zbickham/ml_data_analysis:hw04 /bin/bash
$ cd code/
$ pytest
```
> Expected output:
```
================================================= test session starts ==================================================
platform linux -- Python 3.6.8, pytest-7.0.0, pluggy-1.0.0
rootdir: /code
collected 6 items

test_ml_data_analysis.py ......                                                                                  [100%]

================================================== 6 passed in 0.04s ===================================================
```
Make sure to use the command `exit` to leave the container once you are finished.

## Expected Input Data
Input data should look similar in structure to the data below that is from `Meteorite_Landings.json`. The script uses the key words shown below in certain functions, so they must match for the script to run properly. The data should be formatted as a dictionary whose values are a list of dictionaries.
```bash
{
  "meteorite_landings": [
    {
      "name": "Gerald",
      "id": "10001",
      "recclass": "H4",
      "mass (g)": "5754",
      "reclat": "-75.6691",
      "reclong": "60.6936",
      "GeoLocation": "(-75.6691, 60.6936)"
    },
```
