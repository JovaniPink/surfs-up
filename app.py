"""
Main module of the server app
"""

__version__ = "0.1.0"

import os
from datetime import date, datetime
import connexion
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Test Data to serve with our API
TEST = {
    "Station_One": {
        "id": "234233",
        "station": "sdfdsfdsfsdf",
        "prcp": "sdfsdfsdfsdfsdf",
        "tobs": "sdfsdhfnsldvlsin",
    },
    "Station_Two": {
        "id": "234234",
        "station": "sdfdsfdsfsdf",
        "prcp": "sdfsdfsdfsdfsdf",
        "tobs": "sdfsdhfnsldvlsin",
    },
    "Station_Three": {
        "id": "234235",
        "station": "sdfdsfdsfsdf",
        "prcp": "sdfsdfsdfsdfsdf",
        "tobs": "sdfsdhfnsldvlsin",
    },
}

# @connex_app.route("/api/v1.0/precipitation")
def precipitation():
    return [TEST[key] for key in sorted(TEST.keys())]


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
    def __init__(self, **kwargs):
        super().__init__(strict=True, **kwargs)

    class Meta:
        model = Measurement
        sqla_session = db.session


class StationSchema(ma.SQLAlchemySchema):
    def __init__(self, **kwargs):
        super().__init__(strict=True, **kwargs)

    class Meta:
        model = Station
        sqla_session = db.session


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
