# COMP2001CW2
Source code files for the trails microservice linked to my database.

Api endpoints:

### 1. Authenticate user
- **URL**: `/Authenticate`
- **Method**: `POST`
- **Description**: Authenticates user using email and password
- **Response**:
  - **200 OK**: Authentication successful


### 2. Get All trails
- **URL**: `/AdminAll`
- **Method**: `GET`
- **Description**: Retrieve a list of all trails
- **Response**:
  - **200 OK**: Returns a JSON array of trail objects.
  - **Sample Response**:
    ```json
    [
      {
        "TrailID": 5,
        "Trailname":"Plymouth Circuit",
    "Summary":"Short walk around plymouth",
    "Description":"Sceanic route for all types of walkers",
    "Difficulty":"Easy",
    "Location":"Plymouth",
    "Length":2,
    "Elevationgain":85,
    "RouteType":"Loop",
    "OwnerID":4,
    "Pt1_Lat":47,
    "Pt1_Long":12,
    "Pt1_Desc":"Start",
    "Pt2_Lat":48,
    "Pt2_Long":12,
    "Pt2_Desc":"Hill",
    "Pt3_Lat":49,
    "Pt3_Long":12,
    "Pt3_Desc":"Middle",
    "Pt4_Lat":48,
    "Pt4_Long":12,
    "Pt4_Desc":"Hill",
    "Pt5_Lat":47,
    "Pt5_Long":12,
    "Pt5_Desc":"End"
    
      },
      ...
    ]
    ```

### 3. Get All trails
- **URL**: `/Admin/{TrailID}`
- **Method**: `GET`
- **Description**: Retrieve a trail with the specified id
- **Response**:
  - **200 OK**: Returns a JSON trail objects.
  - **Sample Response**:
    ```json
    
      {
        "TrailID": 5,
        "Trailname":"Plymouth Circuit",
        "Summary":"Short walk around plymouth",
        "Description":"Sceanic route for all types of walkers",
        "Difficulty":"Easy",
        "Location":"Plymouth",
        "Length":2,
        "Elevationgain":85,
        "RouteType":"Loop",
        "OwnerID":4,
        "Pt1_Lat":47,
        "Pt1_Long":12,
        "Pt1_Desc":"Start",
        "Pt2_Lat":48,
        "Pt2_Long":12,
        "Pt2_Desc":"Hill",
        "Pt3_Lat":49,
        "Pt3_Long":12,
        "Pt3_Desc":"Middle",
        "Pt4_Lat":48,
        "Pt4_Long":12,
        "Pt4_Desc":"Hill",
        "Pt5_Lat":47,
        "Pt5_Long":12,
        "Pt5_Desc":"End"
    
      }
    
    ```
    ### 4. Create new trail
- **URL**: `/createTrail`
- **Method**: `POST`
- **Description**: creates a new trail
  -**Request Body**:
    -"TrailID": Int. Required,
    -"Trailname": String,
    -"Summary":String,
    -"Description":String,
    -"Difficulty":String,
    -"Location":String,
    -"Length": Int,
    -"Elevationgain":Int,
    -"RouteType":String,
    -"OwnerID":Int,
    -"Pt1_Lat":Int,
    -"Pt1_Long":Int,
    -"Pt1_Desc":String,
    -"Pt2_Lat":Int,
    -"Pt2_Long":Int,
    -"Pt2_Desc":String,
    -"Pt3_Lat":Int,
    -"Pt3_Long":Int,
    -"Pt3_Desc":String,
    -"Pt4_Lat":Int,
    -"Pt4_Long":Int,
    -"Pt4_Desc":String,
    -"Pt5_Lat":Int,
    -"Pt5_Long":Int,
    -"Pt5_Desc":String,
    
- **Response**:
  - **201 OK**: Returns a successful message

### 5. Create new link for trail and feature
- **URL**: `/addfeatures`
- **Method**: `POST`
- **Description**: creates a new trail
  -**Request Body**:
    -"TrailID": Int. Required,
    -"FeatureID Int. Required,
    
- **Response**:
  - **201 OK**: Returns a successful message

### 6. Updates a trail
- **URL**: `/updatetrail/{trailId}`
- **Method**: `PUT`
- **Description**: Updates a trail
  -**Request Body**:
    -"TrailID": Int. Required,
    -"Trailname": String,
    -"Summary":String,
    -"Description":String,
    -"Difficulty":String,
    -"Location":String,
    -"Length": Int,
    -"Elevationgain":Int,
    -"RouteType":String,
    -"OwnerID":Int,
    -"Pt1_Lat":Int,
    -"Pt1_Long":Int,
    -"Pt1_Desc":String,
    -"Pt2_Lat":Int,
    -"Pt2_Long":Int,
    -"Pt2_Desc":String,
    -"Pt3_Lat":Int,
    -"Pt3_Long":Int,
    -"Pt3_Desc":String,
    -"Pt4_Lat":Int,
    -"Pt4_Long":Int,
    -"Pt4_Desc":String,
    -"Pt5_Lat":Int,
    -"Pt5_Long":Int,
    -"Pt5_Desc":String,
    
- **Response**:
  - **200 OK**: Returns a successful message

### 7. Deletes a trail
- **URL**: `/deletetrail/{trailId}`
- **Method**: `DELETE`
- **Description**: deletes a trail
  -**Parameters**:
    -"TrailID": Int. The id of the trail to be deleted
   
    
- **Response**:
  - **200 OK**: Returns a successful message
  - **404 Not Found**: Returns an error that trail with TrailId was not found
