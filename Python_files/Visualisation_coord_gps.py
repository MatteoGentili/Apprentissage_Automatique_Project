import folium
import pandas as pd

# Charger les données depuis le fichier CSV
data = pd.read_csv(r"C:\Users\MatyG\Documents\2023_2024\ApprAuto\Apprentissage_Automatique_Project\Python_files\csv_files\coord_gps_gares.csv")

# Créer une carte centrée sur une position initiale (par exemple, Paris)
m = folium.Map(location=[48.866667, 2.333333], zoom_start=5)

# Ajouter un marqueur pour chaque gare
for index, row in data.iterrows():
    lat, lon = row['Latitude'], row['Longitude']
    gare = row['Gare']
    folium.Marker([lat, lon], tooltip=gare).add_to(m)

# Enregistrer la carte dans un fichier HTML
m.save('carte_des_gares.html')
