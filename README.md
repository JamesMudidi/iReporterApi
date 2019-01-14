## Badges
[![Build Status](https://travis-ci.org/JamesMudidi/iReporterApi.svg?branch=develop-v1)](https://travis-ci.org/JamesMudidi/iReporterApi)
[![Maintainability](https://api.codeclimate.com/v1/badges/11b0282d0f924649df79/maintainability)](https://codeclimate.com/github/JamesMudidi/iReporterApi/maintainability)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/f67f3e96d96f43849796c31782176141)](https://www.codacy.com/app/JamesMudidi/iReporterApi?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=JamesMudidi/iReporterApi&amp;utm_campaign=Badge_Grade)
[![Requirements Status](https://requires.io/github/JamesMudidi/iReporterApi/requirements.svg?branch=develop-v1)](https://requires.io/github/JamesMudidi/iReporterApi/requirements/?branch=develop-v1)

# iRepoter
iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that need government intervention around the community

## Features
1. Users can create an account and log in.
2. Users can create a ​ red-flag ​ record (An incident linked to corruption)
3. Users can create ​ intervention​​ record​ ​ (a call for a government agency to intervene e.g repair bad road sections, collapsed bridges, flooding e.t.c).
4. Users can edit their ​ red-flag ​ or ​ intervention ​ records.
5. Users can delete their ​ red-flag ​ or ​ intervention ​ records.
6. Users can add geolocation (Lat Long Coordinates) to their ​ red-flag ​ or ​ intervention records​ .
7. Users can change the geolocation (Lat Long Coordinates) attached to their ​ red-flag ​ or intervention ​ records​ .
8. Admin can change the ​ status​​ of a record to either ​ under investigation, rejected ​ (in the event of a false claim)​ ​ or​ resolved ( ​ in the event that the claim has been investigated and resolved)​

## Demo

Project API demo is hosted at [Heroku](https://)

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
* A working computer with Windows OS, Linux OS, Mac OS.
* A text editor
* Postman to consume the API endpoints
* Git for Version control
* Python 3.6
* Pytest for testing the api

## Installing

Open the directory you are going to work from and clone this project using this [link](https://github.com/JamesMudidi/iReporterApi.git)

Open your terminal or console and navigate to your working directory then enter the following commands to select the branch to work with, create a virtual environment, install all the requirements and run the API respectively

```
$ git checkout devlop-v1
$ virtualenv venv
$ pip install -r requirements.txt
$ python run.py
```

## Deployment

The API is hosted on [Heroku](https://ireporterapi.herokuapp.com/)

## Running Tests
* Install Pytest `$ pip install pytest`
* Navigate to project root
* Use `pytest` to run the tests

### API endpoints

Prefix `api/v1/` to all api endpoints below

| **METHOD**   | **URL**  | **ACTION** |
|---|---|---|
|  **POST** |  `/redflag` | post a red-flag |
|  **GET** |  `/redflag` | get list of all redflags |
|  **GET** |  `/redflag/<int:redflagId>` | fetch red-flag records by `redflagId` field |
|  **PATCH** |  `/redflag/<int:redflagId>/location` | edit redflag location `incidentId` field |
|  **PATCH** |  `/redflag/<int:redflagId>/comment` | edit redflag comment `incidentId` field |
| **DELETE**  |  `/redflag/<int:redflagId>` | delete redflag record with given `redflagId` |
|  **POST** |  `/incidents` | post an incident |
|  **GET** |  `/incidents` | get list of all incidents |
|  **GET** |  `/incidents/<int:incidentId>` | fetch incident records by `incidentId` field |
|  **POST** |  `/users` | create a new user |
|  **DELETE, GET, PUT** |  `/users/<int:userId>` | get, delete and update user with given `userId`|
|  **GET** |  `/users` | fetch all users |

## Built with
* Python 3.6
* Flask (Python microframework)

## Versioning
This is version 1 of the API

## Authors
[James Mudidi](https://github.com/JamesMudidi)

## Acknowledgements
* Special Thanks to God Almighty
* Special Thanks to Andela
* Special Thanks to Andela KLA Bootcamp 15 members
