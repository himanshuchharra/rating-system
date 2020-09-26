# a) Assumption made
Rating can be provided for many general products. Product may be anything which provide service. Ex. Mobile phone, 
Driver etc.

There can be different endpoints for getting rating for different product. But according to requirement of project I
 chose a general approach. 
 
# b) Approach to solution
Tech stack used: Language - Python, Framework - Flask, Database - MongoDB
 
Two endpoints are used for this project.
* To save the rating (user or driver)
* To get the average rating (user or driver)

To provide rating, parameters - rating_to_id, rating_by_id, rating_value and ride_id are used.

To get average rating, parameter - product_id is used

Rating is provided for each ride to both (user and driver). Each ride should have a unique id. For each ride, user and 
driver can be rated only once individually.

For database, two collections are used - "user_rating" and "driver_rating". 

Average rating is calculated every time when it is called. 

 
# Step to run application

Create and activate a virtual environment inside your project directory:

```
python -m venv venv
venv/Scripts/activate
```

Install the requirements:

```
pip install -r requirements.txt
```

Run the app:

```
python app/app.py
```

Request - To provide rating:

Import cURL request:

```
curl --location --request POST 'localhost:5000/rating/user' \
--form 'rating_to_id=user_1' \
--form 'rating_by_id=driver_1' \
--form 'rating_value=4' \
--form 'ride_id=ride_111'
```
OR
```
curl --location --request POST 'localhost:5000/rating/driver' \
--form 'rating_to_id=driver_1' \
--form 'rating_by_id=user_1' \
--form 'rating_value=5' \
--form 'ride_id=ride_111'
```

Response - To provide rating:

```json
{
  "code": 200,
  "data": "Thanks for rating.",
  "status": "success"
}
```

```json
{
  "code": 400,
  "data": "URL not supported.",
  "status": "failed"
}
```

```json
{
  "code": 400,
  "data": {
    "error": "field required",
    "parameter": "rating_to_id, rating_by_id, rating_value, ride_id"
  },
  "status": "failed"
}

```

```json
{
  "code": 400,
  "data": "Rating already provided.",
  "status": "failed"
}
```

Request - To get average rating:

Import cURL request:

```
curl --location --request GET 'localhost:5000/rating/user?product_id=user_1'
```
OR
```
curl --location --request GET 'localhost:5000/rating/driver?product_id=driver_1'
```

Response - to get average rating
```json
{
  "code": 200,
  "data": {
    "average_rating": 4.0
  },
  "status": "success"
}
```

```json
{
  "code": 400,
  "data": "URL not supported.",
  "status": "failed"
}
```

```json
{
  "code": 400,
  "data": "Provide product id.",
  "status": "failed"
}
```
