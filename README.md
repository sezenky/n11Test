-------------------------------------------------------
## Table of contents
* [Project info](#project-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Test Scenarios](#test-scenarios)
* [Examples of use](#examples-of-use)

## Project info
Actualize load testing regarding a specific search for predefined keyword within all the date stored in the web page.
	
## Technologies
Project is created with:
* Python version: 3.7.3
* Pip version: 19.1.1 
* Locust version: 0.9.0
* Webbrowser Library version: 20.1.
	
## Setup
To run this project, needed to install Python, Pip and Locust locally.

```
$ python get-pip.py
$ python3 -m pip install locustio
```

## Test scenarios
1) First scenario is setting 5000 users as Number of users to simulate and keep the Hatch rate minimum, like 20.
So It will be take wide time to complete all of the 5000 users, because there will be only 20 user will send requests by second. 

2) Second scenario is setting 50000 users as Number of users to simulate and keep the Hatch rate a bit higher, like 500.
This case will be more intensive when comparing the first scenario because of the number of users who sending requests will be much more for per second. 
Failures may be expected due to load.

## Examples of use
To run Locust with the test scenarios Locust file, following steps needed to be done.
You can use these lines both on cmd or python idle with selecting run as administrator mode. 
First navigate to proper directory that your file is placed.

After that run the file
```
$ locust --host=https://www.n11.com --locustfile search.py
```

You should receive 
```
...../locust.main: Starting web monitor at *:8089
```

Then navigate to browser and go for http://localhost:8089.
Try to run test scenario number 1. Insert;
Number of users to simulate =5000
Hatch rate (users spawned/second)=20
Then click Start swarming button.

on cmd prompt you will see .../locust.runners: Hatching and swarming 5000 clients at the rate 20 clients/s.
Then you can check the Statistics , Charts or Failures during the run or complete.

Then every step should be done for test scenario number 2.

-----------------------------------------------------------


