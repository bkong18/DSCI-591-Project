# Decoding Crime in New York City 

## Group Name: SafeCity

### Team Members 

### Pranav Menon
- Major: Data Science 
- Currently working in a IoT based firm as a Senior Engineer
- Skills: Data Acquistion, Data Cleaning, Visualizations 

### Min Sung Kim
- Major: Data Science
- Currently a student
- SKills: Data Analysis, Data Acquisition, Data Cleaning

### Brian Kong 
- Major: Data Science 
- Currently working as a Business Intelligence Engineer as part of a Data Warehousing team
- Skills: Documentation, Data Acquisition, Cleaning, and Visualizations

### Josh Lister
- Major: Data Science
- currently a Technical Project Manager at software company that designs clinical trial systems
- Skills: Data Acquistion, Visualizations, Data Analysis 


## Project Description 

Crime is a severe issue that affects society negatively in many ways. In the United States, there are thousands of crimes that are occur in every city. This can cause financial and psychological stress when dealing with aftermaths of crimes such as medical treatments of victims, replacement of damaged properties, etc. As crime rates are increasing day by day, it deteriorates safety for citizens which can cause discomfort and anxiety for the throughout the affected areas. New York City is a popular destination for travelers due to tourism and business travel. Mapping out crime hotspots would be extremely beneficial for people who are unfamiliar with the city. For example, if certain areas of the city are prone to carjacking then it might make sense to pay for parking space in a garage to reduce risk. On the contrary, it would make sense for tourists to spend time in areas less prone to crime. The information that can be gathered from this project will be useful for both residents and visitors.

The objective of this project is to do an analysis on crimes in New York city to allow police, citizens,and tourists to better maneuver around the city. By understanding the various relations to crimes and by understanding the locations of these crimes, a better and efficient system could be created to track crime and keep people and their property safe. The analysis can then be further applied to any city around the world.

We will be investigating New York City by examining data from each of the five boroughs; the Bronx, Brooklyn, Manhattan, Queens, and Staten Island. The locations of each crime within the crime data provided by the City of New York are based in latitude and longitude. In order to get a better understanding of the exact location, we will convert this location to a street address using reverse geocoding. Additionally, we are also conducting analysis on what types of crimes are common and dangerous in each section in order to find specific solutions to those crimes by producing an analysis report with graphs, charts, and explanation.

## Dataset Description 

### NYPD Data

NYC crime data, which is published by the police department (NYPD) dates from 2006 to 2020. (The dataset contains reported crimes including felonies, misdemeanors, and violations. The data is available at https://data.cityofnewyork.us/Public-Safety/NYPD-Complaint-Data-Historic/qgea-i56i. The main reason for choosing this dataset is that it is directly obtained from NYPD and has a substantial amount of data to conduct EDA. The dataset contains 35 columns and has around 0.5 million rows for each year. It is a mixture of integer, object, and float type data. There are a total of 7,375,993 complaints spanning across 14 years. This dataset was last updated on July 7, 2021 and is owned by NYC OpenData.

### Reverse Geocoding

Geocode Earth development server was used to obtain information on the street address where the crime took place based on the latitude and longitude. This dataset is used to complement the main NYC crime dataset by providing street addresses based on the coordinates of each incident. Geocode Earth provides a framework for both Forward Geocoding and Reverse Geocoding. For this project, the team utilized the Reverse Geocoding API to integrate our dataset with the street addresses.


## Files in Github
### Cap2_MLP(tensorflow).ipynb

The file "Cap2_MLP(tensorflow)" contains code to build our multilayer perceptron from the pre-processed datasets in "Cap2_classification.ipynb". Please ensure to run the initial file before attempting to build the multilayer perceptron. The file was designed to run on Google Colab, so file upload code is embedded within.

### Cap2_classification.ipynb

The code within "Cap2_classification.ipynb" contains additional preprocessing to integrate the NYC neighborhood dataset with our current NYPD dataset as well as additional pre-processing techniques in order to prepare the dataset for use in machine learning algorithms. The file also contains code for building multiple ML models such as Naive Bayes, Decision Trees, Random Forests etc.

### NY_Bronx_ML (1) Data Processing.ipynb

### NY_Bronx_ML (2) Clustering.ipynb

### NY_Bronx_ML (3) Regression.ipynb

### NY_Bronx_map.png

### NY_Brooklyn.png

### NY_Brooklyn_ML (1) Data Processing.ipynb

### NY_Brooklyn_ML (2) Clustering.ipynb

### NY_Brooklyn_ML (3) Regression.ipynb

### NY_Island_ML (1) Data Processing.ipynb

### NY_Island_ML (2) Clustering.ipynb

### NY_Island_ML (3) Regression.ipynb

### NY_Island_map.png

### NY_Manhattan_ML (1) Data Processing.ipynb

### NY_Manhattan_ML (2) Clustering.ipynb

### NY_Manhattan_ML (3) Regression.ipynb

### NY_Queens_ML (1) Data Processing.ipynb

### NY_Queens_ML (2) Clustering.ipynb

### NY_Queens_ML (3) Regression.ipynb

### NY_Queens_map.png

### NY_manhattan.png


