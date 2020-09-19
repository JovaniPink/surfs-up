"""
Main module of the weather server app
"""

__version__ = "0.1.0"

import os
from datetime import date, datetime, timedelta
import connexion
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# @connex_app.route("/api/v1.0/precipitation")
def precipitation():
    db.create_all()
    precipitation = Measurement.query.all()
    print(type(precipitation))
    precipitation_schema = MeasurementSchema(many=True)
    print(type(precipitation_schema))
    prep_sch_json = precipitation_schema.dump(precipitation)
    print(type(prep_sch_json))
    return prep_sch_json

# @connex_app.route("/api/v1.0/stations")
def stations():
    return

# @connex_app.route("/api/v1.0/tobs")
def temp_monthly():
    return

# @connex_app.route("/api/v1.0/temp/<start>")
# @connex_app.route("/api/v1.0/temp/<start>/<end>")
def stats():
    return


# Create the connexion application instance
connex_app = connexion.FlaskApp(__name__)
# Read the openapi.yaml file to configure the endpoints
connex_app.add_api("openapi.yaml")
# Get the underlying Flask app instance
app = connex_app.app

# basedir = os.path.abspath(os.path.dirname(__file__))
# # Build the Sqlite ULR for SQLAlchemy
# sqlite_url = "sqlite:////" + os.path.join(basedir, "hawaii.db")

# Configure the SQLAlchemy part of the app instance
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///hawaii.db"
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Flask-SQLAlchemy makes using the database outside of a Flask context difficult.
# I ran into this issue when I wanted to still use my SQLAlchemy scripts in FastAPI.
# Create the SQLAlchemy db instance
db = SQLAlchemy(app)


class Measurement(db.Model):
    __tablename__ = "measurement"
    id = db.Column(db.Integer, primary_key=True)
    station = db.Column(db.String)
    date = db.Column(db.String)
    prcp = db.Column(db.Float)
    tobs = db.Column(db.Float)


class Station(db.Model):
    __tablename__ = "station"
    id = db.Column(db.Integer, primary_key=True)
    station = db.Column(db.String)
    name = db.Column(db.String)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    elevation = db.Column(db.Float)


# Initialize Marshmallow
ma = Marshmallow(app)


class MeasurementSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Measurement
        sqla_session = db.session

    id = ma.auto_field()
    station = ma.auto_field()
    date = ma.auto_field()
    prcp = ma.auto_field()
    tobs = ma.auto_field()


class StationSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Station
        sqla_session = db.session

    id = ma.auto_field()
    station = ma.auto_field()
    name = ma.auto_field()
    latitude = ma.auto_field()
    longitude = ma.auto_field()
    elevation = ma.auto_field()


db.init_app(app)

# Create a URL route in our application for "/"
@connex_app.route("/")
def index():
    """
    This function just responds to the browser URL
    localhost:5000/
    :return:        the rendered template "index.html"
    """
    return render_template("index.html")

if __name__ == "__main__":
    connex_app.run(debug=True)
