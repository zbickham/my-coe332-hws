# Deploying in Kubernetes
This folder contains a containerization script (`Dockerfile`), a Python script (`app.py`), and five YAML files to deploy the Flask app and Redis server from `app.py` in Kubernetes

## Project Objective
The purpose of this project was to learn how to utilize Kubernetes. The task is to deploy the Flask app and Redis server from Homework 05 in Kubernetes.

## Description of Files
### app.py
This Python script contains different routes and functions that run the application.
### Dockerfile
This file contains commands that containerize the `app.py` script.
### zekeb-test-redis-pvc.yml
This is a persistent volume claim file for my Redis data.
### zekeb-test-redis-deployment.yml
This is a deployment file for my Redis database.
### zekeb-test-redis-service.yml
This is a file to create a service for my Redis database.
### zekeb-test-flask-deployment.yml
This is a file to create a deployment for my flask API.
### zekeb-test-flask-service.yml
This is a file that creates a service for my flask API.

## Instructions to Run Code
- First, you will need to ssh into a k8 cluster and then pull this git repo into the shell and enter the /homework06 directory:
```bash
$ ssh <username>@coe332-k8s.tacc.utexas.edu
```

- Use the following command with each individual YAML file name to start all the pods:
```bash
$ kubectl apply -f <filename>.yml
```

- Use the following command to get the IP addresses for both the Redis and Flask services:
```bash
$ kubectl get services
```

- To find the name of the debug deployment pod use the following command:
```bash
$ kubectl get pods
```

- Then, enter the name of the pod with the following command so that you can make curl requests to the server:
```bash
$ kubectl exec -it <pod_name> -- /bin/bash
```

## Interacting with the Flask Application
- You can perform a POST request to download the data to the Redis server by using the following command:
```bash
$ curl -X POST <FlaskIP>:5000/data
```

- To access all of the loaded data in the app, you can use the following GET command:
```bash
$ curl <FlaskIP>:5000/data
```

## Data Description
The meteorite data contains information on each line about a specific meteorite (such as who discovered it, the mass, the class, and the location).
