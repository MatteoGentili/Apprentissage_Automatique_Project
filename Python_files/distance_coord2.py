import pandas as pd
from geopy.distance import great_circle

data = pd.read_csv("Python_files\csv_files\coord_gps_gares.csv")

gares = data["Gare"]
distances = pd.DataFrame(index=gares, columns=gares)

for gare1 in gares:
    for gare2 in gares:
        if gare1 == gare2:
            distances.loc[gare1, gare2] = 0  # La distance d'une gare à elle-même est 0
        else:
            coords1 = (data.loc[data["Gare"] == gare1, "Latitude"].values[0],
                       data.loc[data["Gare"] == gare1, "Longitude"].values[0])
            coords2 = (data.loc[data["Gare"] == gare2, "Latitude"].values[0],
                       data.loc[data["Gare"] == gare2, "Longitude"].values[0])
            distance = great_circle(coords1, coords2).kilometers
            distances.loc[gare1, gare2] = distance
            distances.loc[gare2, gare1] = distance  # La distance est symétrique

# Enregistrer les distances dans un nouveau fichier CSV
distances.to_csv("distances_gares.csv")
