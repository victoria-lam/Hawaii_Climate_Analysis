#Climate App

#dependencies and modules
import pandas as pd
import numpy as np

#Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine, inspect, func

#import flask
from flask import Flask, jsonify

#########################################################################
#create engine connection to sqlite database 
engine = create_engine("sqlite:///hawaii.sqlite", echo=False)

#reflect database into ORM class
Base = automap_base()
Base.prepare(engine, reflect=True)

#save references to table
Measurements = Base.classes.measurements
Stations = Base.classes.stations

#create a session - link from Python to database
session = Session(engine)
#########################################################################

#########################################################################
# Flask Setup

#create an app
app = Flask(__name__)

#########################################################################
# Flask Routes
#########################################################################

@app.route("/")
def welcome():
    #available navigation routes
    return (
        f"<strong>Available Routes:</strong><br/>"
        f"Observed temperature in the last year (2016): /api/v1.0/precipitation<br/>"
        f"List of stations in Hawaii: /api/v1.0/stations<br/>"
        f"List of temperature observations in the last year (2016): /api/v1.0/tobs<br/>"
        f"Min., Avg. and Max. Temperature of data starting on May 22, 2017: /api/v1.0/2017-05-22<br/>"
        f"Min., Avg. and Max. Temperature of start-end range of vacation (05/22/17-05/31/17): /api/v1.0/2017-05-22/2017-05-31"

##dates and temperature observed in the last year
@app.route("/api/v1.0/precipitation")
def dates_prcp():
    #query dates and prcp from last year
    prcp_by_dates = session.query(Measurements.date, func.avg(Measurements.prcp))\
                    .filter(Measurements.date.between("2016-01-01", "2016-12-31"))\
                    .group_by(Measurements.date)\
                    .order_by(Measurements.date).all()
    #set "date" as key, "prcp" as value
    prcp_dict = dict(prcp_by_dates)
    
    return jsonify(prcp_dict)

##list of stations in Hawaii
@app.route("/api/v1.0/stations")
def stations():
    #query stations from dataset
    results = session.query(Stations.station)\
              .group_by(Stations.station).all()
    #convert to list
    stations_list = list(np.ravel(results))
    
    return jsonify(stations_list)

##list of tobs for the previous year
@app.route("/api/v1.0/tobs")
def tobs():
    results = session.query(Measurements.tobs)\
              .filter(Measurements.date.between("2016-01-01", "2016-12-31"))\
              .group_by(Measurements.date).all()

    #convert to list
    tobs_list = list(np.ravel(results))
    
    return jsonify(tobs_list)

##list of min, avg, and max temperature for given start date: 5/22/17
@app.route("/api/v1.0/2017-05-22")
def start_date():
    results = session.query(func.min(Measurements.tobs), func.avg(Measurements.tobs), func.max(Measurements.tobs))\
              .filter(Measurements.date >= "2017-05-22").all()
    #convert to list
    temp_results = list(np.ravel(results))
    
    return jsonify(temp_results)
    
##list of min, avg, and max temperature for range: 5/22/17 - 5/31/17
@app.route("/api/v1.0/2017-05-22/2017-05-31")
def date_range():
    results = session.query(func.min(Measurements.tobs), func.avg(Measurements.tobs), func.max(Measurements.tobs))\
           .filter(Measurements.date.between("2017-05-22", "2017-05-31")).all()
    #convert to list
    range_results = list(np.ravel(results))
    
    return jsonify(range_results)

if __name__ == "__main__":
    app.run(debug=False)

