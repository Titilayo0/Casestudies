import math

"""
1. Renowned physicist Dr. Emma conducts an experiment to measure 
average radiation levels in environments with radioactive waste.
2. Data is collected over weeks from diverse locations (urban to dense forests), 
considering varying distances from radiation sources.
3. Measurements, including average radiation, standard deviation, 
and relevant metrics, are taken at different times of the day.
4. The program efficiently manages numerous measurements for each location.
5. Input includes average radiation level, standard deviation, 
and other metrics to identify patterns or anomalies in the data.
"""

#to calculate and display average radiation levels for each location using a dictionary
locations = {"City_Centre": [22,19,20, 31,28],
             "Industrial_Zone": [35,32,30,37,40], 
             "Residential_District": [15,12,18,20,14], 
             "Rural_Outskirts": [9,13,16,14,7],
             "Downtown": [25,18,22,21,26]
             }
def calculate_average (levels):
    return sum(levels)/len(levels)

for locations, levels in locations.items():
    print(f"{locations} Average Radiation level: {calculate_average(levels)}")

def calculate_standard_deviation(levels):
    mean = calculate_average(levels)
    variance = sum((x - mean) ** 2 for x in levels) / len(levels)
    std_deviation = math.sqrt(variance)
    return std_deviation


std_deviation = calculate_standard_deviation(levels)
print(f"Standard Deviation: {std_deviation:.2f}")