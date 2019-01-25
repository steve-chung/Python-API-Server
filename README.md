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
3. Create View table 
  - Run the following query at the SQL console
  ````
  CREATE OR REPLACE VIEW public.stat_by_date AS
 SELECT sc.id AS score_id,
    sc.user_id,
    sc.game_id,
    sc.hole_id,
    ga.date,
    st.first_club,
    st.first_distance,
    st.second_club,
    st.second_distance,
    st.stroks_green,
    ho.par,
    st.total_shot,
    ga.total_score
   FROM scores sc
     JOIN games ga ON sc.game_id = ga.id
     JOIN stat st ON sc.stat_id = st.id
     JOIN holes ho ON sc.hole_id = ho.id
  GROUP BY sc.user_id, sc.id, ga.date, st.first_club, st.first_distance, st.second_club, st.second_distance, st.stroks_green, ga.total_score, ho.par, st.total_shot
  ORDER BY ga.date DESC;

ALTER TABLE public.stat_by_date
    OWNER TO postgres;
````
  
## Starting the App

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
## API
#### 1. Getting info of golf courses with geo location

##### Path: localhost:3000/api/courses?lat=34.0522&lng=-118.2437
##### Method: GET
##### RESPONSE

```json
{
    "businesses": [
        {
            "alias": "kiliki-golf-los-angeles",
            "categories": [
                {
                    "alias": "golf",
                    "title": "Golf"
                }
            ],
            "coordinates": {
                "latitude": null,
                "longitude": null
            },
            "display_phone": "(818) 588-8744",
            "distance": 4.049322216540503,
            "id": "R0K5p1YQ-bRneWe076Fg7Q",
            "image_url": "https://s3-media3.fl.yelpcdn.com/bphoto/wRHBdK_Lf3eAORkTYz0z4w/o.jpg",
            "is_closed": false,
            "location": {
                "address1": "",
                "address2": "",
                "address3": "",
                "city": "Los Angeles",
                "country": "US",
                "display_address": [
                    "Los Angeles, CA"
                ],
                "state": "CA",
                "zip_code": ""
            },
            "name": "Kiliki Golf",
            "phone": "+18185888744",
            "rating": 5,
            "review_count": 2,
            "transactions": [],
            "url": "https://www.yelp.com/biz/kiliki-golf-los-angeles?adjust_creative=9N8YwJ3mxL93_qWMvl-W5w&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=9N8YwJ3mxL93_qWMvl-W5w"
        },
        {
            "alias": "bravo-golf-academy-los-angeles",
            "categories": [
                {
                    "alias": "golf",
                    "title": "Golf"
                }
            ],
            "coordinates": {
                "latitude": 34.06344,
                "longitude": -118.29831
            },
            "display_phone": "(213) 382-9800",
            "distance": 5202.467932358186,
            "id": "GRvXqc5AbSDdn7s0FjO6lw",
            "image_url": "",
            "is_closed": false,
            "location": {
                "address1": "3500 W 6th St",
                "address2": "Ste 308",
                "address3": "",
                "city": "Los Angeles",
                "country": "US",
                "display_address": [
                    "3500 W 6th St",
                    "Ste 308",
                    "Los Angeles, CA 90020"
                ],
                "state": "CA",
                "zip_code": "90020"
            },
            "name": "Bravo Golf Academy",
            "phone": "+12133829800",
            "rating": 4,
            "review_count": 1,
            "transactions": [],
            "url": "https://www.yelp.com/biz/bravo-golf-academy-los-angeles?adjust_creative=9N8YwJ3mxL93_qWMvl-W5w&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=9N8YwJ3mxL93_qWMvl-W5w"
        }]
       }
 ````
#### 2. User Register 

##### Path: localhost:3000/api/auth/register
##### Method: POST
##### REQUEST
```json
{
	"name": "young",
	"email": "young@email.com",
	"password": "1234",
	"phone": "123-123-1234"
}
````
##### RESPONSE
```json
{
    "message": "User young was created",
    "username": "young",
    "id": 14,
    "accessToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NDg0NDU4ODAsIm5iZiI6MTU0ODQ0NTg4MCwianRpIjoiOWVkYmY3NDAtNzM5Ny00MjBhLTljNWYtMTk4M2RlNDEyMjE5IiwiZXhwIjoxNTQ4NDU2NjgwLCJpZGVudGl0eSI6InlvdW5nQGVtYWlsLmNvbSIsImZyZXNoIjp0cnVlLCJ0eXBlIjoiYWNjZXNzIn0.qU84ei64Y1ohwN4D9wbTZc7E2Oiyjj5MOjO-C_cvR8A",
    "refreshToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NDg0NDU4ODAsIm5iZiI6MTU0ODQ0NTg4MCwianRpIjoiZmU0YWZmMjUtMzQxZi00YjYyLTg4N2MtYzAwYjE2MDYyM2JiIiwiZXhwIjoxNTUxMDM3ODgwLCJpZGVudGl0eSI6InlvdW5nQGVtYWlsLmNvbSIsInR5cGUiOiJyZWZyZXNoIn0.mnu_sRktztPylRKrVGaMLgnqHOHLTS2_L_rgxJakM5k"
}
````
#### 3. User Log In 

##### Path: localhost:3000/api/auth/login
##### Method: POST
##### REQUEST
```json
{ 
	"email": "test@test.com",
	"password": "1234"
}
````
##### RESPONSE
```json
{
    "message": "Logged in as test",
    "username": "test",
    "id": 1,
    "accessToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NDg0NDUxMDIsIm5iZiI6MTU0ODQ0NTEwMiwianRpIjoiODFjZDJhYTEtYTYzOC00NTIzLThmMTMtODE5MDYwNjI4YzZjIiwiZXhwIjoxNTQ4NDU1OTAyLCJpZGVudGl0eSI6InRlc3RAdGVzdC5jb20iLCJmcmVzaCI6dHJ1ZSwidHlwZSI6ImFjY2VzcyJ9.wZ3r15e8wgQ3FUniI5ir2i61iocuVbg0bh6VW4jK4pQ",
    "refreshToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NDg0NDUxMDIsIm5iZiI6MTU0ODQ0NTEwMiwianRpIjoiY2JlOTIyMWQtZDg4NS00NmFkLWFiOTUtMjAxZGU0OTFjNDQwIiwiZXhwIjoxNTUxMDM3MTAyLCJpZGVudGl0eSI6InRlc3RAdGVzdC5jb20iLCJ0eXBlIjoicmVmcmVzaCJ9.nAmpq1koGmZe6WH__209gkDyl5lp2eusQh3YwUKLdGc"
}
````
#### 4. User Log out 

##### Path: localhost:3000/api/auth/logout
##### Method: POST
##### Header: {Authorization: 'Bearer {access_token}'}
##### RESPONSE
```json
{
    "message": "Successfully Logged Out"
}
````

#### 5. User Reserves a Course

##### Path: localhost:3000/api/reserve
##### Method: POST
##### Header: {Authorization: 'Bearer {access_token}'}
##### REQUEST
```json
{
	"date":"11/05/2018",
	"course": "test Course",
	"players": [
		{"name": "steve",
		 "aveScore": 100,
		 "email": "steve@data.com"
		 }
		  ],
	"totalScores": 200
}
````
##### RESPONSE
```json
{
    "message": "Course test Course was scheduled for 11/05/2018",
    "id": 16
}
````

#### 6. User Saves Holes Info

##### Path: localhost:3000/api/holes
##### Method: POST
##### Header: {Authorization: 'Bearer {access_token}'}
##### REQUEST
```json
{
	"game_id":14,
	"holes":[{"1":4}, {"2":3}, {"3":5}, {"4":6}, {"5":6}, {"6":5}, {"7":5}, {"8":6}, {"9":4}, {"10":5}, {"11":6}, {"12":5}, {"13":4}, {"14":3}, {"15":4},{"16":5}, {"17":3},{"18":5}]
}
	
````
##### RESPONSE
```json
[
    {
        "holeId": 757,
        "holeNumber": 1,
        "par": 4
    },
    {
        "holeId": 758,
        "holeNumber": 2,
        "par": 3
    },
    {
        "holeId": 759,
        "holeNumber": 3,
        "par": 5
    },
    {
        "holeId": 760,
        "holeNumber": 4,
        "par": 6
    },
    {
        "holeId": 761,
        "holeNumber": 5,
        "par": 6
    },
    {
        "holeId": 762,
        "holeNumber": 6,
        "par": 5
    },
    {
        "holeId": 763,
        "holeNumber": 7,
        "par": 5
    },
    {
        "holeId": 764,
        "holeNumber": 8,
        "par": 6
    },
    {
        "holeId": 765,
        "holeNumber": 9,
        "par": 4
    },
    {
        "holeId": 766,
        "holeNumber": 10,
        "par": 5
    },
    {
        "holeId": 767,
        "holeNumber": 11,
        "par": 6
    },
    {
        "holeId": 768,
        "holeNumber": 12,
        "par": 5
    },
    {
        "holeId": 769,
        "holeNumber": 13,
        "par": 4
    },
    {
        "holeId": 770,
        "holeNumber": 14,
        "par": 3
    },
    {
        "holeId": 771,
        "holeNumber": 15,
        "par": 4
    },
    {
        "holeId": 772,
        "holeNumber": 16,
        "par": 5
    },
    {
        "holeId": 773,
        "holeNumber": 17,
        "par": 3
    },
    {
        "holeId": 774,
        "holeNumber": 18,
        "par": 5
    }
]
````
#### 7. User Add Score

##### Path: localhost:3000/api/stat
##### Method: POST
##### Header: {Authorization: 'Bearer {access_token}'}
##### REQUEST
```json
{
{
	"game_id":14,
	"hole_id":757,
	"firstClub": "Driver",
	"firstDistance": 250,
	"secondClub": "6-iron",
	"secondDistance": 150,
	"stroksGreen": 3,
	"totalShots": 8,
	"totalScore": 8
}
````
##### RESPONSE
```json
{
    "message": "successfully add hole 757",
    "stat_id": 20,
    "firstClub": "Driver",
    "firstDistance": 250,
    "secondClub": "6-iron",
    "secondDistance": 150,
    "stroksGreen": 3,
    "totalShots": 8,
    "totalScore": 8
}
````
#### 8. User Add Score

##### Path: localhost:3000/api/stat
##### Method: POST
##### Header: {Authorization: 'Bearer {access_token}'}
##### REQUEST
```json
{
{
	"game_id":14,
	"hole_id":757,
	"firstClub": "Driver",
	"firstDistance": 250,
	"secondClub": "6-iron",
	"secondDistance": 150,
	"stroksGreen": 3,
	"totalShots": 8,
	"totalScore": 8
}
````
##### RESPONSE
```json
{
    "message": "successfully add hole 757",
    "stat_id": 20,
    "firstClub": "Driver",
    "firstDistance": 250,
    "secondClub": "6-iron",
    "secondDistance": 150,
    "stroksGreen": 3,
    "totalShots": 8,
    "totalScore": 8
}
````

#### 9. User Can Update Score

##### Path: localhost:3000/api/stat/{stat_id}
##### Method: PUT
##### Header: {Authorization: 'Bearer {access_token}'}
##### REQUEST
```json
{
{
	"game_id":14,
	"hole_id":757,
	"firstClub": "Driver",
	"firstDistance": 250,
	"secondClub": "6-iron",
	"secondDistance": 150,
	"stroksGreen": 3,
	"totalShots": 8,
	"totalScore": 8
}
````
##### RESPONSE
```json
{
    "message": "successfully update a stat 20",
    "stat_id": 20
}
````


#### 10. User Can Get Score

##### Path: localhost:3000/api/stat/{stat_id}
##### Method: GET
##### Header: {Authorization: 'Bearer {access_token}'}
##### RESPONSE
```json
{
    "firstClub": "Driver",
    "firstDistance": 250,
    "secondClub": "6-iron",
    "secondDistance": 150,
    "stroksGreen": 3,
    "totalShot": 8
}
````
#### 11. User Can View Game Stats

##### Path: localhost:3000/api/stat/view
##### Method: GET
##### Header: {Authorization: 'Bearer {access_token}'}
##### RESPONSE
```json
[
    {
        "date": "Jan 05, 2019",
        "stats": [
            {
                "first_club": "Driver",
                "first_distance": 250,
                "game_id": 14,
                "hole_id": 757,
                "par": 4,
                "score_id": 1529,
                "second_club": "6-iron",
                "second_distance": 150,
                "stroks_green": 3,
                "total_score": 8,
                "total_shot": 8
            }
        ]
    }
]
````
