# PYTHON-API Server

API server with user can login, add players and reserve Game request.  The server response with JSON reponse and validate tokens for user authentication. This app is buiit in Python 3 with Postgres DB for data persistance.  

## Features

- User can Login (JWT Access token)
- User can Logout
- User can stay logged in (JWT Refresh token)
- User can add players to the game
- User can search for course to play
- User can schedule a game
- User can add scores and stats of the game.
- User can see his or her performace according the it's category.

## Used Techology
- JWT
- python 3.65
- SQLAlchemy
- yelpapi
- Postgres 

## Demo

[![Watch the video](https://imgur.com/IHtE2mq.png)](https://www.youtube.com/watch?v=tUyJOc41jPs)


## Installation

1. Install
````
cd server
pip install -r requirement.txt
````

2. Configure DB
  - Download and install Postgres.
  - Create a default or desired schema.
  - Create a golf-score-tracker DB using command
  ````
  CREATE DATABASE "golf-score-tracker"
  ````
  
## Starting the App

1. Client

```
 cd client
 npm run dev
```

2. Server

Windows
````
cd server
python app.py
````

Mac
````
cd server
python3 app.py
````
