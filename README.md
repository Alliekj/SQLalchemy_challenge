# Climate Analysis and Flask API Project

## Overview
This project involves data exploration of a climate database using Python, SQLAlchemy ORM queries, Pandas, and Matplotlib. Additionally, a Flask API was created to serve the analysis results. The tasks are divided into two main parts: data analysis and designing a climate app.


## Part 1: Data Analysis

### Precipitation Analysis
- **Task**: Retrieve and analyze the precipitation data for the last 12 months.
- **Steps**:
  - Query the most recent date in the dataset.
  - Retrieve the last 12 months of precipitation data.
  - Load the results into a Pandas DataFrame.
  - Sort the data by date and plot it using Matplotlib.
  - Calculate and print summary statistics for the precipitation data.

### Station Analysis
- **Task**: Analyze station data and find the most active weather station.
- **Steps**:
  - Query the total number of weather stations in the dataset.
  - Identify the most active stations by counting the number of observations.
  - For the most active station, calculate the minimum, maximum, and average temperatures.
  - Retrieve the last 12 months of temperature data for the most active station and plot the data as a histogram.

## Part 2: Flask API
A Flask API is developed to serve the results of the data analysis. It provides several routes for accessing the precipitation, station, and temperature observation data.

### Available Routes
- **`/`**: Homepage listing all available API routes.
- **`/api/v1.0/precipitation`**: Returns JSON with date as the key and precipitation as the value for the last year.
- **`/api/v1.0/stations`**: Returns JSON list of all weather stations.
- **`/api/v1.0/tobs`**: Returns JSON list of temperature observations for the most active station for the last year.
- **`/api/v1.0/<start>`**: Returns JSON list of the minimum, average, and maximum temperatures from the start date to the end of the dataset.
- **`/api/v1.0/<start>/<end>`**: Returns JSON list of the minimum, average, and maximum temperatures between the start and end dates.

## Dependencies
- Python 3.x
- Flask
- SQLAlchemy
- Pandas
- Matplotlib
- SQLite

## Running the Project
1. Clone this repository.
2. Install the required Python packages:  
   ```bash
   pip install -r requirements.txt

## Run the Flask App
1. python app.py
2. Open a browser and navigate to http://localhost:5000/ to access the API.
