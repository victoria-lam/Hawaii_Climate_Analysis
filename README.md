
# Destination Getaway: Honolulu, Hawaii

<img src="honolulu.png" width="400">

### Data Engineering
Step 1 was completed in the Jupyter Notebook titled 'data_engineering.ipynb'.

The raw data was read and converted into pandas dataframes. Rows that contained NaN values were removed to avoid speculations and assumptions. Cleaned CSV files were saved and used for later analysis. 

### Database Engineering
Step 2 was completed in the Jupyter Notebook titled 'database_engineering.ipynb'.

Using Python and SQLAlchemy, an engine was created in order to connect to a sqlite database ("hawaii.sqlite"). Two ORM classes, "Measurements" and "Stations", were made. The cleaned data sets were populated into the tables. 

### Climate Analysis and Exploration
Step 3 was completed in the Jupyter Notebook titled 'climate_analysis.ipynb'.

Python and SQLAlchemy was used to explore data on precipitation and temperature information recorded by various weather stations.

### Climate App
Step 4 was completed in the Python file titled 'app.py'.

Using the Flask extension in SQLAlchemy, I designed a Flask api based on previous queries.
