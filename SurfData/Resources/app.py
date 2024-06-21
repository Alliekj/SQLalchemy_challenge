# Import the dependencies.
from flask import Flask, jsonify
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#################################################
# Database Setup
#################################################
# Create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Find the most recent date in the data set
    most_recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    
    # Calculate the date one year from the last date in data set
    one_year_ago = dt.datetime.strptime(most_recent_date, "%Y-%m-%d") - dt.timedelta(days=365)
    
    # Query the last 12 months of precipitation data
    precipitation_data = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= one_year_ago).all()
    
    # Convert the query results to a dictionary using date as the key and prcp as the value
    precipitation_dict = {date: prcp for date, prcp in precipitation_data}
    
    return jsonify(precipitation_dict)

@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    all_stations = list(np.ravel(results))
    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    # Find the most recent date in the data set
    most_recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    
    # Calculate the date one year from the last date in data set
    one_year_ago = dt.datetime.strptime(most_recent_date, "%Y-%m-%d") - dt.timedelta(days=365)
    
    # Query the dates and temperature observations of the most-active station for the previous year of data
    most_active_station = session.query(Measurement.station).group_by(Measurement.station)\
        .order_by(func.count(Measurement.station).desc()).first()[0]
    
    temperature_data = session.query(Measurement.date, Measurement.tobs)\
        .filter(Measurement.station == most_active_station)\
        .filter(Measurement.date >= one_year_ago).all()
    
    temperature_list = list(np.ravel(temperature_data))
    return jsonify(temperature_list)

@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def temperature_stats(start=None, end=None):
    # Select statement
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    
    if not end:
        # calculate TMIN, TAVG, TMAX for all dates greater than start
        results = session.query(*sel).filter(Measurement.date >= start).all()
    else:
        # calculate TMIN, TAVG, TMAX for dates between start and end inclusive
        results = session.query(*sel).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    
    temperature_stats_list = list(np.ravel(results))
    return jsonify(temperature_stats_list)

if __name__ == '__main__':
    app.run(debug=True)

# Close session
session.close()

