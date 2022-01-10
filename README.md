# SQLAlchemy - Surfing 

# Background

Using Python and SQLAlchemy, I wanted to find basic climate data regarding rainfall. Additionally, I wanted to see which weather stations were compiling the data. 

# Precipitation Analysis

•	Found the most recent date in the data set.

•	Using this date, retrieve the last 12 months of precipitation data by querying the 12 preceding months of data. 

•	Loaded the query results into a Pandas DataFrame 

•	Sorted the DataFrame values by date

•	Plotted the results

•	Use Pandas to print the summary statistics for the precipitation data.

![image](https://user-images.githubusercontent.com/87212158/148709448-432bd171-b721-459f-a69b-ce9ba7887964.png)

![image](https://user-images.githubusercontent.com/87212158/148709452-5ccca740-dc4e-452b-83ce-3911956f7067.png)
 
# Station Analysis

•	Designed a query to calculate the total number of stations in the dataset.

•	Designed a query to find the most active stations 

o	Listed the stations and observation counts in descending order.

o	Using the most active station id, calculate the lowest, highest, and average temperature.

![image](https://user-images.githubusercontent.com/87212158/148709459-b908033a-19e8-4db0-82ba-acb0ac3b0e44.png)

•	Designed a query to retrieve the last 12 months of temperature observation data (TOBS).

o	Filtered by the station with the highest number of observations.

o	Queried the last 12 months of temperature observation data for this station.

o	Plotted the results as a histogram with bins

![image](https://user-images.githubusercontent.com/87212158/148709468-64bd8a51-01d8-4ea3-be32-9b050c01c8c9.png)
