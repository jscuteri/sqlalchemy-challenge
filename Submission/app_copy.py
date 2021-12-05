# Import Dependencies
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import pandas as pd
import datetime as dt

from flask import Flask, jsonify

# Create an engine for the chinook.sqlite database
engine = create_engine("sqlite:///../Homework/Instructions/Resources/hawaii.sqlite")

# Reflect Database and reflect tables
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to each table

Measurement = Base.classes.measurement
Station = Base.classes.station

# create the connection to Flask
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

# Homepage and routes
@app.route("/")
def home():
    return (
        f"Welcome to the Climate Analysis and Exploration homepage!<br/>"
        f"<br/>" 
        f"Available Routes:<br/>"
        f"<br/>" 
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    f"Dates must be entered in YYYY-MM-DD format"
    )

# Precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    year_ago = dt.date(2017, 8, 23) - dt.timedelta(days = 365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= year_ago).\
    all()
    df = pd.DataFrame(precipitation, columns = ['Date', "Precipitation"])
    precipitation_dictionary =df.set_index('Date').T.to_dict('list')
    session.close()
    return jsonify(
    precipitation_dictionary
    )

# Stations route
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    stations_list = session.query(Measurement.station, func.count(Measurement.station)).\
    group_by(Measurement.station).\
    order_by(func.count(Measurement.station).desc()).\
    all()
    df = pd.DataFrame(stations_list, columns = ['Station ID', "Number of Records"])
    stations_list_dict =df.set_index('Station ID').T.to_dict('list')
    session.close()
    return jsonify(
    stations_list_dict
    )


# tobs route
@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    low = session.query(func.min(Measurement.tobs)).\
    filter(Measurement.station == 'USC00519281').all()
    high = session.query(func.max(Measurement.tobs)).\
    filter(Measurement.station == 'USC00519281').all()
    average = session.query(func.avg(Measurement.tobs)).\
    filter(Measurement.station == 'USC00519281').all()
    low_df = pd.DataFrame(low, columns = ["Low Temperature"])
    low_df = low_df.to_json()
    high_df = pd.DataFrame(high, columns = ["High Temperature"])
    high_df = high_df.to_json()
    avg_df = pd.DataFrame(average, columns = ["Average Temperature"])
    avg_df = avg_df.to_json()
    session.close()
    return jsonify(
    low_df,
    high_df,
    avg_df
    )
    
# Start and Stop route
# URLs Not being found 
@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def start_and_stop(start, stop = None):
    session = Session(engine)
    canonicalized = start
    sel = [(func.min(Measurement.tobs)),(func.max(Measurement.tobs)),(func.avg(Measurement.tobs))]
    if not stop:
        start_without_stop = session.query(*sel).filter(func.strftime('%m-%d', Measurement.date) == canonicalized).all()
        return jsonify (start_without_stop)
    start_with_stop = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= stop).all()
    session.close()
    return jsonify (start_with_stop)

if __name__ == "__main__":
    app.run(debug=True)
