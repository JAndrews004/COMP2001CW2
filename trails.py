# trails.py

import requests
from flask import abort, make_response
from config import db
from models import Trail, trail_schema, trails_schema,Feature,FeatureLink,link_schema



def read_all():
    trails = Trail.query.all()
    return trails_schema.dump(trails)

def read_one(trailId):
    trail = Trail.query.filter(Trail.TrailID == trailId).one_or_none()
    
    if trail is not None:
        return trail_schema.dump(trail)
    else:
        abort(
            404, f"Trail with id {trailId} not found"
        )

def create_trail(body):
        TrailId= body.get("TrailId")
        existing_trail = Trail.query.filter(Trail.TrailID == TrailId).one_or_none()

        if existing_trail is None:
             new_trail = trail_schema.load(body,session=db.session)
             db.session.add(new_trail)
             db.session.commit()
             return trail_schema.dump(new_trail) , 201
             
        else:
             abort(
                  406,
                  f"Trail with id {TrailId} already exists",
             )

def update(id, trail):
    existing_trail = Trail.query.filter(Trail.TrailID == id).one_or_none()

    if existing_trail:
        update_person = trail_schema.load(trail, session=db.session)
        existing_trail.fname = update_person.fname
        db.session.merge(existing_trail)
        db.session.commit()
        return trail_schema.dump(existing_trail), 201
    else:
        abort(404, f"Person with last name {id} not found")

def delete(id):
    existing_trail = Trail.query.filter(Trail.TrailID == id).one_or_none()
    if existing_trail:
        db.session.delete(existing_trail)
        db.session.commit()
        return make_response(f"{id} successfully deleted", 200)
    else:
        abort(404, f"Person with last name {id} not found")

def LinkFeature(body):
    trailid = body.get("TrailId")
    featureid = body.get("FeatureId")

    new_link =  FeatureLink(TrailId=trailid,FeatureId=featureid)
    db.session.add(new_link)
    db.session.commit()
    return link_schema.dump(new_link) , 201



def Authenticate(body):
    email = body.get("email")
    password = body.het("password")

    response = requests.post('https://web.socem.plymouth.ac.uk/COMP2001/auth/api/users',json=body)
    if response.status_code == 200:
        try:
            json_response = response.json()
            print("Authenticated successfully:",
            json_response)

        except requests.JSONDecodeError:
            print("Response is not valid JSON. Raw response content:")

            print(response.text)
    else:
        print(f"Authentication failed with status code {response.status_code}")

        print("Response content:", response.text)
