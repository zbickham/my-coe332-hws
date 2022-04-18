# Creating a Flask Application
This folder contains a containerization script (`Dockerfile`), a script to run the image (`Makefile`), a Python script (`app.py`), and a text file (`requirements.txt`)

## Project Objective
The purpose of this project was to learn how to read data to and from a Redis server. The task is to launch a Redis container, then build a small Flask app to load data into and retrieve data from the database.

## Description of Files
### app.py
This Python script contains different routes and functions that run the application.
### Makefile
This file contains commands to build, run, and push the containerized Docker image.
### Dockerfile
This file contains commands that containerize the `app.py` script.

## Instructions to Run Code
- To pull and use the default redis image, use the following command in the terminal:
```bash
$ docker pull redis:6
$ docker run -d -p 6403:6379 -v $(pwd)/data:/data --name=hw5-redis redis:6 --save 1 1
```

- The inclusion of the `Dockerfile` will allow you to pull and run an image of the container by using the following command in the terminal:
```bash
$ docker build -t zbickham/ml_data_analysis:hw04 .
```

- To run the containerized code against the sample data inside the container, use the following command in the terminal. The first command allows you to enter the container while the second command runs the code and data file within the containter:
```bash
$ docker pull zbickham/hw5:latest
$ docker run --name "hw5" -d -p 5003:5000 zbickham/hw5:latest
```

- You can use the included `Makefile` to build, launch, and push the containerized Flask application using the following command in the terminal:
```bash
make
```

## Interacting with the Flask Application
- You can perform a POST request to download the data to the Redis server by using the following command:
```bash
$ curl -X POST localhost:5003/data
```

- To access all of the loaded data in the app, you can use the following GET command:
```bash
$ curl localhost:5003/data
```

## Data Description
The meteorite data contains information on each line about a specific meteorite (such as who discovered it, the mass, the class, and the location).
