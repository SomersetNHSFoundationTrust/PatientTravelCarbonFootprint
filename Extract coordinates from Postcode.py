#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 09:44:08 2023

@author: oi
"""

import pandas as pd
from geopy.geocoders import Nominatim

# Function to get coordinates from postcode
def get_coordinates_from_postcode(postcode):
    geolocator = Nominatim(user_agent="my_geocoder")
    location = geolocator.geocode(postcode)
    
    if location:
        return location.latitude, location.longitude
    else:
        return None, None

# Read the CSV file into a pandas DataFrame
csv_file_path = '/Users/oi/Documents/UoB/Internship./Sample Data./TA postcodes 1.csv'  # Replace with the actual path to your CSV file
df = pd.read_csv(csv_file_path)

# Create new columns for latitude and longitude
df['Origin Latitude'] = None
df['Origin Longitude'] = None
df['Destination Latitude'] = None
df['Destination Longitude'] = None

# Iterate through each row and get coordinates
for index, row in df.iterrows():
    origin_postcode = row['Origin Postcode']  # Replace 'Postcode' with the actual column name in your CSV file
    latitude, longitude = get_coordinates_from_postcode(origin_postcode)
    df.at[index, 'Origin Latitude'] = latitude
    df.at[index, 'Origin Longitude'] = longitude
    destination_postcode = row['Destination Postcode']  # Replace 'Postcode' with the actual column name in your CSV file
    latitude, longitude = get_coordinates_from_postcode(destination_postcode)
    df.at[index, 'Destination Latitude'] = latitude
    df.at[index, 'Destination Longitude'] = longitude

# Write the updated DataFrame to the same CSV file with two new tabs
output_csv_path_1 = '/Users/oi/Documents/UoB/Internship./Sample Data./TA postcodes + coordinates 1.csv'  # Replace with the desired output file path
df.to_csv(output_csv_path_1, index=False)

print(f"Coordinates added and saved to {output_csv_path_1}")
