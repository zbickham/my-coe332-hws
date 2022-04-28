# Creating a Software Diagram for my ISS Tracker
This folder contains an image file (`image.png`).

## Project Objective
The purpose of this project was to introduce diagrams for software design. The task is to create a software diagram that shows off some interesting aspect of my [ISS Position and Sighting Tracker](https://github.com/zbickham/iss-tracker.git). You can click the previous link to access the referenced project.

## Description of Files
### image.png
This PNG file contains a flowchart that represents a software diagram for my ISS Tracker.

## Software Diagram
![Flowchart](https://github.com/zbickham/my-coe332-hws/blob/ce7f88a3033e95d87a001f8af02cf91767065ca2/homework07/image.png)
<p align="center">
A flowchart showing navigation of the ISS Tracker API.
</p>

## Description of the Design Diagram
The diagram shows the function of the ISS Position and Sighting Tracker. It depicts ways that the user can interact with the application as well as what output would result from each action.

At the start of the application, the user can either perform a `GET` operation or a `POST` operation (commands for both can be found in the linked project repository). Ideally, the user would first perform a `POST` operation to load the XML data files to memory. Once the data has been loaded, the user can use perform `GET` operations to navigate through the routes.

Each `GET` pathway requires the user to enter a unique route in the curl command (each of which can be found in the linked project repository). If the user does not specify a route, the application will list all possible routes that the user can take.

First, there are routes to query positional and velocity data from the ISS. This data is called epoch data. The user can route to list all epochs or they can specify an epoch to return more specific data about that individual epoch.

Next, there are routes to query ISS sighting data. This data has information about countries, regions, and cities that the ISS has sighted. If the user is not requesting epoch data, then they can request sighting data. The user can first route to list all countries that have sighting data or they can specify a country to return more specific data about that individual country. The user can also route to list all regions that have sighting data or they can specify a region to return more specific data about that individual region. Lastly, the user can route to list all cities that have sighting data or they can specify a city to return more specific data about that individual city.

After the user has received output, the application ends. However, the user can start again by using the `curl` commands to start at the top of the flowchart and retrieve more data from the application.

## Link to Referenced Project
Instructions to specifically navigate the API can be found in my [ISS Position and Sighting Tracker](https://github.com/zbickham/iss-tracker.git) repository.
