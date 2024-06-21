
Overview:
This project involves performing a basic climate analysis and data exploration of a climate database using Python and SQLAlchemy ORM queries, Pandas, and Matplotlib. Additionally, a Flask API is created to serve the analysis results. I used chatgpt to help me with the Flask portion. The tasks are divided into two main parts: data analysis and designing a climate app.

Data Analysis:
-Precipitation Analysis
1. Find the most recent date in the dataset.
2. Get the previous 12 months of precipitation data.
3. Load the results into a Pandas DataFrame.
4. Sort the DataFrame by date.
5. Plot the data.
6. Print summary statistics.

Station Analysis:
1. Calculate the total number of stations.
2. Find the most active stations and list them in descending order.
3. Calculate the lowest, highest, and average temperatures for the most active station.
4. Get the previous 12 months of temperature observation data for the most active station.
5. Plot the data as a histogram.

Flask API
Routes:
/ : Homepage listing all available routes.
/api/v1.0/precipitation : Returns JSON with date as the key and precipitation as the value for the last year.
/api/v1.0/stations : Returns JSON list of all stations.
/api/v1.0/tobs : Returns JSON list of temperature observations for the most active station for the last year.
/api/v1.0/<start> : Returns JSON list of min, avg, and max temperatures from the start date to the end of the dataset.
/api/v1.0/<start>/<end> : Returns JSON list of min, avg, and max temperatures from the start date to the end date.

