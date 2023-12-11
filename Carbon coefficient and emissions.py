#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 09:41:30 2023

@author: oi
"""

import pandas as pd

# Data source: https://gbr01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.gov.uk%2Fgovernment%2Fstatistical-data-sets%2Fnts99-travel-by-region-and-area-type-of-residence%23%3A~%3Atext%3DNTS9903&data=05%7C01%7C2304399%40buckingham.ac.uk%7C47371dac481b4186739708dbf4d96961%7Ceba4640024e64c07a7c6cc061e0f8d26%7C0%7C0%7C638372986843237326%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=RJaPrzv7nTgDnrHN590Fl60vZ2NII5%2BsZrSMk%2F7J4mY%3D&reserved=0

# Assuming 'your_file.csv' is the path to your CSV file
csv_file_path = '/Users/oi/Documents/UoB/Internship./Sample Data./nts9904.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Specify the condition for filtering rows (replace 'ColumnName' and 'desired_value' with your actual conditions)
condition = (df['Year'] == '2022') & (df["Region of residence"] == "South West")

# Apply the condition to filter rows
southwest_2022 = df[condition]

# Now, filtered_rows is a DataFrame containing rows that satisfy the specified condition
print(southwest_2022)

selected_columns = ['Walk [note 4]',	'Walks of over a mile',	"Pedal cycle [note 5]",	"Car or van driver",	"Car or van passenger",	"Motorcycle", "Other private transport [note 6]",	"Other local bus", 'Surface Rail',	'Taxi or minicab']

southwest_2022[selected_columns]

# Integrating "selected_columns" above into modes of transport from "Emissions for Transport Modes".

# List of columns and their respective values
columns_and_values = {
    'Walking (0kg/km)': [0, 642.1283],
    'Bicycle (0kg/km)': [0, 88.51392],
    'Motorbike (0.1432736kg/km)': [0.1432736, 74.02982],
    'Car or van (0.09375074kg/km)': [0.09375074, 8416.869],
    "Other private transport (0.132683778kg/km)": [0.132683778, 181.8559],
    "Other local bus (0.03270375kg/km)": [0.132683778, 186.6839],
    'Train (0.04427072kg/km)': [0.04427072, 363.7117],
    'Taxi or minicab (0.09375074kg/km)': [0.09375074, 75.63917]
}

print(columns_and_values)

integrated_df = pd.DataFrame(columns_and_values)

print(integrated_df)

# Calculate the product of values in the specified rows
total_carbon_per_mode = integrated_df.loc[0] * integrated_df.loc[1]


# Total distance traveled:

distance_grand_total = integrated_df.loc[1].sum()

carbon_grand_total = total_carbon_per_mode.sum()

carbon_coefficient = carbon_grand_total / distance_grand_total
print(carbon_coefficient)



csv_file_path = '/Users/oi/Documents/UoB/Internship./Sample Data./Distances between postcodes.csv'  # Replace with the actual path to your CSV file

df_1 = pd.read_csv(csv_file_path)

df_1['Carbon emitted'] = df_1['Distance (km)'] * carbon_coefficient


# Save the updated DataFrame to a new CSV file
output_csv_path_5 = '/Users/oi/Documents/UoB/Internship./Sample Data./Overall carbon emitted.csv'
df_1.to_csv(output_csv_path_5, index=False)

print(f"Distances columns added and saved to {output_csv_path_5}")


