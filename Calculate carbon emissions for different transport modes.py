#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 10:42:59 2023

@author: oi
"""

import pandas as pd

# Read the CSV file into a pandas DataFrame
csv_file_path = '/Users/oi/Documents/UoB/Internship./Distances between coordinates.csv'  # Replace with the actual path to your CSV file
df = pd.read_csv(csv_file_path)

# Carbon emisiions (Kg/Km) for different types of transport are as follows (converted from Kg/~393 - ~399 miles):
    # Walking = 0.
    
    # Cycling = 0.
    
    # Motorbike = 92Kg/399miles.
    #           = 0.3710768Kg/Km
    
    # Small Petrol Car = 77/399miles.
    #                  = 0.3105752Kg/Km
    
    # Medium Petrol Car = 97/399miles.
    #                   = 0.391244Kg/Km
    
    # Average Petrol Car = 89/399miles.
    #                    = 0.3589765Kg/Km
    
    # Large Petrol Car = 149/399miles.
    #                  = 0.6009831Kg/Km
    
    # Small Diesel Car = 75/399miles.
    #                  = 0.3025083Kg/Km
    
    # Medium Diesel Car = 89/399miles.
    #                   = 0.3589765Kg/Km
    
    # Average Diesel Car = 91/399miles.
    #                    = 0.3670434Kg/Km
    
    # Large Diesel Car = 111/399miles.
    #                  = 0.4477122Kg/Km
    
    # Small Hybrid Car = 55/99miles.
    #                  = 0.2218394Kg/Km
    
    # Medium Hybrid Car = 59/399miles.
    #                   = 0.2379732Kg/Km
    
    # Average Hybrid Car = 64/399miles.
    #                    = 0.2581404Kg/Km
    
    # Large Hybrid Car = 82/399miles.
    #                  = 0.3307424Kg/Km
    
    # Small Plug-in Hybrid Car = 29/399miles.
    #                          = 0.1169699Kg/Km
    
    # Medium Plug-in Hybrid Car = 46/399miles.
    #                           = 0.1855384Kg/Km
    
    # Average Plug-in Hybrid Car = 50/399miles.
    #                            = 0.2016722Kg/Km
    
    # Large Plug-in Hybrid Car = 54/399miles.
    #                          = 0.217806Kg/Km
    
    # Small Electric Car = 25/399miles.
    #                    = 0.1008361Kg/Km
    
    # Medium Electric Car = 28/399miles.
    #                     = 0.1129364Kg/Km
    
    # Average Electric Car = 29/399miles.
    #                      = 0.1169699Kg/Km
    
    # Large Electric Car = 30/399miles.
    #                    = 0.1210033Kg/Km
    
    # Bus (coach) = 21/399miles.
    #             = 0.08470232Kg/Km
    
    # Train (National Rail) = 28/393miles.
    #                       = 0.1146606Kg/Km
    
    
# Data sources:
#     https://www.gov.uk/government/publications/transport-energy-and-environment-statistics-notes-and-definitions/journey-emissions-comparisons-methodology-and-guidance
    
#     https://maps.dft.gov.uk/journey-emission-comparisons-interactive-dashboard/index.html




# List of columns and their respective values
columns_and_values = {
    'Walking (0Kg/Km)': 0,
    'Bicycle (0Kg/Km)': 0,
    'Motorbike (0.3710768Kg/Km)': 0.3710768,
    'Small Petrol Car (0.3105752Kg/Km)': 0.3105752,
    'Medium Petrol Car (0.391244Kg/Km)': 0.391244,
    'Average Petrol Car (0.3589765Kg/Km)': 0.3589765,
    'Large Petrol Car (0.6009831Kg/Km)': 0.6009831,
    'Small Diesel Car (0.3025083Kg/Km)': 0.3025083,
    'Medium Diesel Car (0.3589765Kg/Km)': 0.3589765,
    'Average Diesel Car (0.3670434Kg/Km)': 0.3670434,
    'Large Diesel Car (0.4477122Kg/Km)': 0.4477122,
    'Small Hybrid Car (0.2218394Kg/Km)': 0.2218394,
    'Medium Hybrid Car (0.2379732Kg/Km)': 0.2379732,
    'Average Hybrid Car (0.2581404Kg/Km)': 0.2581404,
    'Large Hybrid Car (0.3307424Kg/Km)': 0.3307424,
    'Small Plug-in Hybrid Car (0.1169699Kg/Km)': 0.1169699,
    'Medium Plug-in Hybrid Car (0.1855384Kg/Km)': 0.1855384,
    'Average Plug-in Hybrid Car (0.2016722Kg/Km)': 0.2016722,
    'Large Plug-in Hybrid Car (0.217806Kg/Km)': 0.217806,
    'Small Electric Car (0.1008361Kg/Km)': 0.1008361,
    'Medium Electric Car (0.1129364Kg/Km)': 0.1129364,
    'Average Electric Car (0.1169699Kg/Km)': 0.1169699,
    'Large Electric Car (0.1210033Kg/Km)': 0.1210033,
    'Bus - Coach (0.08470232Kg/Km)': 0.08470232,
    'Train - National Rail (0.1146606Kg/Km)': 0.1146606
}

# Iterate over columns and calculate the product
for column, value in columns_and_values.items():
    df[column] = df['Distance (km)'] * value

# Save the updated DataFrame to a new CSV file
output_csv_path_3 = '/Users/oi/Documents/UoB/Internship./Emissions by Transport Mode.csv'
df.to_csv(output_csv_path_3, index=False)

print(f"Emission columns added and saved to {output_csv_path_3}")

