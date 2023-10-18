import pandas as pd
from geopy.distance import great_circle


data = pd.read_csv("Python_files\csv_files\coord_gps_gares.csv")
distances = pd.DataFrame(columns=["Gare 1", "Gare 2", "Distance (km)"])

# Calculer les distances 
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        gare1 = (data.loc[i, "Latitude"], data.loc[i, "Longitude"])
        gare2 = (data.loc[j, "Latitude"], data.loc[j, "Longitude"])
        distance = great_circle(gare1, gare2).kilometers
        distances = pd.concat([distances, pd.DataFrame({"Gare 1": [data.loc[i, "Gare"]],
                                                      "Gare 2": [data.loc[j, "Gare"]],
                                                      "Distance (km)": [distance]})], ignore_index=True)

distances.to_csv("distances_gares2.csv", index=False)
