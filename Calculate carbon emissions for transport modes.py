#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 10:42:59 2023

@author: oi
"""

import pandas as pd


csv_file_path = '/Users/oi/Documents/UoB/Internship./Sample Data./Distances between postcodes.csv'  # Replace with the actual path to your CSV file

df = pd.read_csv(csv_file_path)

# Carbon emisiions (Kg/Km) for different types of transport are as follows (converted from Kg/~393 - ~399 miles):
#     Walking = 0.
    
#     Cycling = 0.
    
#     Motorbike = 92Kg/399miles.
#               = 0.1432736Kg/Km
    
#     Small Petrol Car = 77/399miles.
#                       = 0.1199137Kg/Km
    
#     Medium Petrol Car = 97/399miles.
#                       = 0.1510602Kg/Km
    
#     Average Petrol Car = 89/399miles.
#                         = 0.1386016Kg/Km
    
#     Large Petrol Car = 149/399miles.
#                       = 0.2320409Kg/Km
    
#     Small Diesel Car = 75/399miles.
#                       = 0.1167991Kg/Km
    
#     Medium Diesel Car = 89/399miles.
#                       = 0.1386016Kg/Km
    
#     Average Diesel Car = 91/399miles.
#                         = 0.1417162Kg/Km
    
#     Large Diesel Car = 111/399miles.
#                       = 0.1728627Kg/Km
    
#     Small Hybrid Car = 55/399miles.
#                       = 0.08565267Kg/Km
    
#     Medium Hybrid Car = 59/399miles.
#                       = 0.09188196Kg/Km
    
#     Average Hybrid Car = 64/399miles.
#                         = 0.09966856Kg/Km
    
#     Large Hybrid Car = 82/399miles.
#                       = 0.1277003Kg/Km
    
#     Small Plug-in Hybrid Car = 29/399miles.
#                               = 0.04516232Kg/Km
    
#     Medium Plug-in Hybrid Car = 46/399miles.
#                               = 0.07163678Kg/Km
    
#     Average Plug-in Hybrid Car = 50/399miles.
#                                 = 0.07786606Kg/Km
    
#     Large Plug-in Hybrid Car = 54/399miles.
#                               = 0.08409535Kg/Km
    
#     Small Electric Car = 25/399miles.
#                         = 0.03893303Kg/Km
    
#     Medium Electric Car = 28/399miles.
#                         = 0.043605Kg/Km
    
#     Average Electric Car = 29/399miles.
#                           = 0.04516232Kg/Km
    
#     Large Electric Car = 30/399miles.
#                         = 0.04671964Kg/Km
    
#     Bus (coach) = 21/399miles.
#                 = 0.03270375Kg/Km
    
#     Train (National Rail) = 28/393miles.
#                           = 0.04427072Kg/Km
    
#     Plane = 175.55/370miles.
#           = 0.2948154Kg/Km
    
    
    
# Data sources:
#     https://www.gov.uk/government/publications/transport-energy-and-environment-statistics-notes-and-definitions/journey-emissions-comparisons-methodology-and-guidance
    
#     https://maps.dft.gov.uk/journey-emission-comparisons-interactive-dashboard/index.html




# List of columns and their respective values
columns_and_values = {
    'Walking (0kg/km)': 0,
    'Bicycle (0kg/km)': 0,
    'Motorbike (0.1432736kg/km)': 0.1432736,
    'Small Petrol Car (0.1199137kg/km)': 0.1199137,
    'Medium Petrol Car (0.1510602kg/km)': 0.1510602,
    'Average Petrol Car (0.1386016kg/km)': 0.1386016,
    'Large Petrol Car (0.2320409kg/km)': 0.2320409,
    'Small Diesel Car (0.1167991kg/km)': 0.1167991,
    'Medium Diesel Car (0.1386016kg/km)': 0.1386016,
    'Average Diesel Car (0.1417162kg/km)': 0.1417162,
    'Large Diesel Car (0.1728627kg/km)': 0.1728627,
    'Small Hybrid Car (0.08565267kg/km)': 0.08565267,
    'Medium Hybrid Car (0.09188196kg/km)': 0.09188196,
    'Average Hybrid Car (0.09966856kg/km)': 0.09966856,
    'Large Hybrid Car (0.1277003kg/km)': 0.1277003,
    'Small Plug-in Hybrid Car (0.04516232kg/km)': 0.04516232,
    'Medium Plug-in Hybrid Car (0.07163678kg/km)': 0.07163678,
    'Average Plug-in Hybrid Car (0.07786606kg/km)': 0.07786606,
    'Large Plug-in Hybrid Car (0.08409535kg/km)': 0.08409535,
    'Small Electric Car (0.03893303kg/km)': 0.03893303,
    'Medium Electric Car (0.043605kg/km)': 0.043605,
    'Average Electric Car (0.04516232kg/km)': 0.04516232,
    'Large Electric Car (0.04671964kg/km)': 0.04671964,
    'Bus - Coach (0.03270375kg/km)': 0.03270375,
    'Train - National Rail (0.04427072kg/km)': 0.04427072,
    'Plane (0.2948154kg/km)': 0.2948154
}

# Iterate over columns and calculate the product
for column, value in columns_and_values.items():
    df[column] = df['Distance (km)'] * value

# Save the updated DataFrame to a new CSV file
output_csv_path_4 = '/Users/oi/Documents/UoB/Internship./Sample Data./Emissions for Transport Modes.csv'
df.to_csv(output_csv_path_4, index=False)

print(f"Distances columns added and saved to {output_csv_path_4}")

