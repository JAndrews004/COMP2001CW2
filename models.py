# models.py


from marshmallow_sqlalchemy import fields
from config import db, ma


class Trail(db.Model):
    __tablename__ = "Trail"
    __table_args__ = dict(schema="CW2")
    TrailID = db.Column(db.Integer, primary_key=True)
    Trailname= db.Column(db.String(30))
    Summary= db.Column(db.String(1000))
    Description= db.Column(db.String(1000))
    Difficulty= db.Column(db.String(6))
    Location= db.Column(db.String(25))
    Length= db.Column(db.Integer)
    Elevationgain= db.Column(db.Integer)
    Routetype= db.Column(db.String(15))
    ownerId= db.Column(db.Integer)
    Pt1_Lat= db.Column(db.Integer)
    Pt1_Long= db.Column(db.Integer)
    Pt1_Desc= db.Column(db.String(50))
    Pt2_Lat= db.Column(db.Integer)
    Pt2_Long= db.Column(db.Integer)
    Pt2_Desc= db.Column(db.String(50))
    Pt3_Lat= db.Column(db.Integer)
    Pt3_Long= db.Column(db.Integer)
    Pt3_Desc= db.Column(db.String(50))
    Pt4_Lat= db.Column(db.Integer)
    Pt4_Long= db.Column(db.Integer)
    Pt4_Desc= db.Column(db.String(50))
    Pt5_Lat= db.Column(db.Integer)
    Pt5_Long= db.Column(db.Integer)
    Pt5_Desc= db.Column(db.String(50))

    features=db.relationship(
        "Feature",
        secondary="CW2.TrailFeatureLink",
        back_populates="trails"
    )

class FeatureLink(db.Model):
    __tablename__ ="TrailFeatureLink"
    __table_args__ =  dict(schema="CW2")
    
    TrailID = db.Column(db.Integer, db.ForeignKey("CW2.Trail.TrailID"),primary_key=True)
    TrailFeatureID = db.Column(db.Integer, db.ForeignKey("CW2.Feature.TrailFeatureID"),primary_key=True)
    

class Feature(db.Model):
    __tablename__ ="Feature"
    __table_args__ = dict(schema="CW2")
    TrailFeatureID = db.Column(db.Integer,primary_key=True)
    TrailFeature = db.Column(db.String(50))
    trails = db.relationship("Trail",secondary ="CW2.TrailFeatureLink",back_populates="features")


class FeatureSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Feature
        load_instance =True
        include_relationships=True
        sqla_session = db.session
        include_fk = True

class TrailSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Trail
        load_instance =True
        include_relationships=True
        sqla_session = db.session
    features = fields.Nested(FeatureSchema, many=True)

class LinkSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = FeatureLink
        load_instance =True
        include_relationships=True
        sqla_session = db.session

trail_schema = TrailSchema()
trails_schema = TrailSchema(many=True)
feature_schema = FeatureSchema()
features_schema = FeatureSchema(many=True)
link_schema = LinkSchema()
