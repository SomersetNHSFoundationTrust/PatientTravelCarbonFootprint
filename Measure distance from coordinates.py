#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 10:42:59 2023

@author: oi
"""



# VINCENTY FORMULA:

from geopy.distance import geodesic
import pandas as pd

# Read the CSV file into a pandas DataFrame
csv_file_path = '/Users/oi/Documents/UoB/Internship./Sample Data./TA postcodes + coordinates 1.csv'  # Replace with the actual path to your CSV file
df = pd.read_csv(csv_file_path)

# Check if the specified columns exist in the DataFrame
required_columns = ['Origin Latitude', 'Origin Longitude', 'Destination Latitude', 'Destination Longitude']

if all(col in df.columns for col in required_columns):
    # Drop rows with NaN values in the specified columns
    df = df.dropna(subset=required_columns)

# Calculate distance for each row using the Vincenty formula
df['Distance (km)'] = df.apply(lambda row: geodesic(
    (row['Origin Latitude'], row['Origin Longitude']),
    (row['Destination Latitude'], row['Destination Longitude'])
).kilometers, axis=1)

# Save the updated DataFrames to a new CSV file with only the necessary columns
output_csv_path_2 = '/Users/oi/Documents/UoB/Internship./Sample Data./Distances between coordinates.csv'  # Replace with the desired output file path
df[['Origin Latitude', 'Origin Longitude', 'Destination Latitude', 'Destination Longitude', 'Distance (km)']].to_csv(output_csv_path_2, index=False)

output_csv_path_3 = '/Users/oi/Documents/UoB/Internship./Sample Data./Distances between postcodes.csv'  # Replace with the desired output file path
df[['Origin Postcode', 'Destination Postcode', 'Distance (km)']].to_csv(output_csv_path_3, index=False)

print(f"Distances calculated using Vincenty formula and saved to {output_csv_path_2}")
