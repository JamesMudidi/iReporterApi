## Badges
[![Coverage Status](https://coveralls.io/repos/github/JamesMudidi/iReporterApi/badge.svg?branch=develop-v1)](https://coveralls.io/github/JamesMudidi/iReporterApi?branch=develop-v1)
[![Build Status](https://travis-ci.org/JamesMudidi/iReporterApi.svg?branch=develop-v1)](https://travis-ci.org/JamesMudidi/iReporterApi)
[![Maintainability](https://api.codeclimate.com/v1/badges/11b0282d0f924649df79/maintainability)](https://codeclimate.com/github/JamesMudidi/iReporterApi/maintainability)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/f67f3e96d96f43849796c31782176141)](https://www.codacy.com/app/JamesMudidi/iReporterApi?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=JamesMudidi/iReporterApi&amp;utm_campaign=Badge_Grade)
[![Requirements Status](https://requires.io/github/JamesMudidi/iReporterApi/requirements.svg?branch=develop-v1)](https://requires.io/github/JamesMudidi/iReporterApi/requirements/?branch=develop-v1)

# iRepoter
iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that need government intervention around the community

## Features
1. Users can create an account and log in.
2. Users can create a ​ redflag ​ record (An incident linked to corruption)
3. Users can create ​ intervention​​ record​ ​ (a call for a government agency to intervene e.g repair bad road sections, collapsed bridges, flooding e.t.c).
4. Users can edit their ​ redflag ​ or ​ intervention ​ records.
5. Users can delete their ​ redflag ​ or ​ intervention ​ records.
6. Users can add geolocation (Lat Long Coordinates) to their ​ redflag ​ or ​ intervention records​ .
7. Users can change the geolocation (Lat Long Coordinates) attached to their ​ redflag ​ or intervention ​ records​ .
8. Admin can change the ​ status​​ of a record to either ​ under investigation, rejected ​ (in the event of a false claim)​ ​ or​ resolved ( ​ in the event that the claim has been investigated and resolved)​


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

Open the directory you are going to work from and clone this project using this [link](https://github.com/JamesMudidi/iReporterDB.git)

Open your terminal or console and navigate to your working directory then enter the following commands to create a virtual environment, install all the requirements, create a database, activate the database path and run the API respectively

```
$ mkvirtualenv venv
$ pip install -r requirements.txt
$ python run.py
$ sudo -u postgres psql
$ source .env
$ CREATE DATABASE ireporter;
```

## Deployment

The API is hosted on [Heroku](https://ireporterapi_v2.herokuapp.com/)

## Running Tests
* Install Pytest `$ pip install pytest`
* Navigate to project root
* Use `pytest` to run the tests
* To have a more detailed look at the tests use `pytest -v`

### API endpoints

Prefix `api/v2/` to all api endpoints below

| METHOD | URL | ACTION |
|---|---|---|
| GET |  `/redflag` | Get a list of all redflags |
| GET |  `/redflag/<int:redflagId>` | Get Redflags by `redflagId` field |
| GET |  `/intervention` | Get a list of all interventions |
| GET |  `/intervention/<int:interventionId>` | Get Interventions by `interventionId` field |
| GET |  `/users` | Get all users |
| GET |  `/users` | fetch all users |
| GET |  `/users/<int:userId>` | fetch one user by `userId` |
| POST |  `/auth/signup` | Register a user to the system |
| POST |  `/auth/login` | Login to the system |
| POST |  `/redflag` | Post a Redflag |
| POST |  `/intervention` | Post an Intervention |
| PATCH |  `/redflag/<int:redflagId>/location` | Edit redflag location by `incidentId` field |
| PATCH |  `/redflag/<int:redflagId>/comment` | Edit redflag comment by `incidentId` field |
| PATCH |  `/redflags/<int:redflagId>/status` | Edit redflag record status by `redflagId` field |
| PATCH |  `/intervention/<int:interventionId>/location` | Edit intervention location by `interventionId` field |
| PATCH |  `/intervention/<int:interventionId>/comment` | Edit redflag intervention comment by `interventionId` field |
| PATCH |  `/intervention/<int:interventionId>/status` | Edit redflag intervention status by `interventionId` field |
| DELETE |  `/redflag/<int:redflagId>` | Delete redflag record with given `redflagId` |
| DELETE |  `/redflag/<int:redflagId>` | delete redflag record by `redflagId` |
| DELETE |  `/intervention/<int:interventionId>` | delete intervention record by `interventionId` |
| DELETE |  `/users/<int:userId>` | delete one user by `userId` |

## Built with
* Python 3.6
* Flask (Python microframework)
* PostgreSQL

## Tools
* Sublime Text
* VS Code
* Virtual environment
* Pylint
* Pytest
* PostgreSQL

## Versioning
This is version 1 of the API

## Authors
[James Mudidi](https://github.com/JamesMudidi)

## Acknowledgements
* Special Thanks to God Almighty
* Special Thanks to Andela
* Special Thanks to Andela KLA Bootcamp 15 members
