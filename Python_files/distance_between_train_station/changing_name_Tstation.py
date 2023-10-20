import pandas as pd
import os
import re
import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from geopy.distance import great_circle
import folium


######################################
####                              ####
#### Var for get_gare_coordinates ####
####                              ####
######################################
gares = [
        "Paris-Lyon", "Paris-Montparnasse", "Paris-Nord", "Tourcoing", "Paris-Vaugirard", "Paris-Est", "Lyon-Part-Dieu",
        "Marseille-Saint-Charles", "Rennes", "Lille", "Montpellier", "Marne-la-Vallée-Chessy", "Madrid-Atocha", "Strasbourg",
        "Reims", "Metz", "Nancy", "Francfort", "Stuttgart", "Chambéry-Challes-les-Eaux", "Mulhouse-Ville", "Nice-Ville",
        "Barcelone-Sants", "Genève", "Bellegarde (Ain)", "Mâcon-Loché-TGV", "Perpignan", "Toulon", "Lausanne",
        "Besançon-Franche-Comté TGV", "Grenoble", "Nîmes", "Saint-Étienne-Châtereuse", "Italie", "Zurich", "Annecy",
        "Avignon TGV", "Valence-TGV", "Aix-en-Provence TGV", "Dijon-Ville", "Le Creusot-Montceau-Montchanin",
        "Bordeaux-Saint-Jean", "La Rochelle-Ville", "Quimper", "Saint-Pierre-des-Corps", "Tours", "Brest", "Poitiers",
        "Toulouse-Matabiau", "Angers-Saint-Laud", "Angoulême", "Nantes", "Vannes", "Laval", "Le Mans", "Saint-Malo",
        "Dunkerque", "Douai", "Arras"
    ]
url = "https://www.coordonnees-gps.fr/communes/paris-/75100"



######################################
#####                           ######
##### Var for update_gare_names ######
#####                           ######
######################################

gares_liste = ['PARIS LYON', 'PARIS MONTPARNASSE', 'PARIS NORD', 'TOURCOING', 'PARIS VAUGIRARD', 'PARIS EST',
                'LYON PART DIEU', 'MARSEILLE ST CHARLES', 'RENNES', 'LILLE', 'MONTPELLIER', 'MARNE LA VALLEE',
                'MADRID', 'STRASBOURG', 'REIMS', 'METZ', 'NANCY', 'FRANCFORT', 'STUTTGART',
                'CHAMBERY CHALLES LES EAUX', 'MULHOUSE VILLE', 'NICE VILLE', 'BARCELONA',
                'GENEVE', 'BELLEGARDE (AIN)', 'MACON LOCHE', 'PERPIGNAN', 'TOULON',
                'LAUSANNE', 'BESANCON FRANCHE COMTE TGV', 'GRENOBLE', 'NIMES',
                'SAINT ETIENNE CHATEAUCREUX', 'ITALIE', 'ZURICH', 'ANNECY',
                'AVIGNON TGV', 'VALENCE ALIXAN TGV', 'AIX EN PROVENCE TGV',
                'DIJON VILLE', 'LE CREUSOT MONTCEAU MONTCHANIN',
                'BORDEAUX ST JEAN', 'LA ROCHELLE VILLE', 'QUIMPER',
                'ST PIERRE DES CORPS', 'TOURS', 'BREST', 'POITIERS',
                'TOULOUSE MATABIAU', 'ANGERS SAINT LAUD', 'ANGOULEME',
                'NANTES', 'VANNES', 'LAVAL', 'LE MANS', 'ST MALO', 'DUNKERQUE', 'DOUAI', 'ARRAS']

def get_gare_coordinates(gares, url, output_file):

    if os.path.exists(output_file):
        print(f"Le fichier '{output_file}' existe déjà. Aucune opération ne sera effectuée.")
        return
    else : 
        # Instancier un navigateur web (assurez-vous d'avoir installé Selenium et le driver du navigateur)
        driver = webdriver.Chrome()

        # Charger la page web
        driver.get(url)
        time.sleep(3)

        # Accepter le pop-up de cookies (si présent)
        try:
            accept_button = driver.find_element(By.XPATH, '//a[@id="allcookies"]')
            accept_button.click()
            time.sleep(2)  # Attendre quelques secondes après avoir accepté les cookies
        except Exception as e:
            print("Pop-up de cookies non trouvé ou déjà accepté.")

    
    
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Gare', 'Latitude', 'Longitude','coordonnées']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            # Sélectionner le champ d'adresse
            address_input = driver.find_element(By.XPATH, '//input[@id="address"]')

            # Parcourir la liste des gares
            for gare in gares:
                address_input.clear()  # Effacer le champ précédent (s'il y en a un)
                address_input.send_keys("Gare de " + gare)
                
                # Cliquez sur le bouton "Obtenir les coordonnées GPS"
                button = driver.find_element(By.XPATH, '//button[contains(text(), "Obtenir les coordonnées GPS")]')
                button.click()
                time.sleep(1) # obligé sinon le site n'était pas assez rapide 
                #driver.implicitly_wait(10)  # Attendre quelques secondes

                # Extraire les coordonnées
                coord_gps_element = driver.find_element(By.XPATH, '//input[@id="latlong"]')
                coord_gps = coord_gps_element.get_attribute("value")

                # Écrire les données dans le fichier CSV
                writer.writerow({'Gare': gare, 'Latitude': coord_gps.split(",")[0], 'Longitude': coord_gps.split(",")[1],
                                  'Coordonnées':coord_gps})

        # Fermer le navigateur
    driver.quit()

def calculate_distances(input_file, output_file):
    if os.path.exists(output_file):
        print(f"Le fichier '{output_file}' existe déjà. Aucune opération ne sera effectuée.")
        return
    else : 
        data = pd.read_csv(input_file)
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

        distances.to_csv(output_file, index=False)


def update_gare_names(input_file, output_file, gares_liste):
    if os.path.exists(output_file):
        print(f"Le fichier '{output_file}' existe déjà. Aucune opération ne sera effectuée.")
        return 
    else : 
        # Charger les données des gares depuis le fichier CSV
        data = pd.read_csv(input_file)

        # Fonction pour faire correspondre les noms de gares en ignorant la casse
        def correspondance_ignorant_casse(gare_csv, gare_liste):
            
            gare_csv = gare_csv.replace("Marseille-Saint-Charles","Marseille-St-Charles")
            gare_csv = gare_csv.replace("Marne-la-Vallée-Chessy","Marne-la-Vallee")
            gare_csv = gare_csv.replace("Chambéry-Challes-les-Eaux","Chambery-Challes-les-Eaux")
            gare_csv = gare_csv.replace("Barcelone-Sants","Barcelona")
            gare_csv = gare_csv.replace("Mâcon-Loché-TGV","Macon-Loche")
            gare_csv = gare_csv.replace("Saint-Étienne-Châtereuse","Saint-Etienne-Chateaucreux")
            gare_csv = gare_csv.replace("Besançon-Franche-Comté TGV","Besancon-Franche-Comte TGV")
            gare_csv = gare_csv.replace("Nîmes","Nimes")     
            gare_csv = gare_csv.replace("Valence-TGV","Valence alixan tgv")
            gare_csv = gare_csv.replace("Bordeaux-Saint-Jean","Bordeaux-St-Jean")
            gare_csv = gare_csv.replace("Genève","Geneve")          
            gare_csv = gare_csv.replace("Saint-Pierre-des-Corps","St-Pierre-des-Corps")
            gare_csv = gare_csv.replace("Angoulême","Angouleme")
            gare_csv = gare_csv.replace("Saint-Malo","St-Malo")

            
            gare_csv = gare_csv.replace("-", " ")
            
            for gare in gares_liste:
                if re.search(re.escape(gare), gare_csv, re.IGNORECASE):
                    return gare
            return None

        if input_file == r"Python_files\csv_files\distances_gares.csv" : 
            # Appliquer la fonction de correspondance pour mettre à jour les noms dans le DataFrame
            data["Gare 1"] = data["Gare 1"].apply(lambda x: correspondance_ignorant_casse(x, gares_liste))
            data["Gare 2"] = data["Gare 2"].apply(lambda x: correspondance_ignorant_casse(x, gares_liste))
        elif input_file == r"Python_files\csv_files\coord_gps_gares.csv":
            data["Gare"] = data["Gare"].apply(lambda x: correspondance_ignorant_casse(x, gares_liste))

        # Enregistrer le DataFrame mis à jour dans un nouveau fichier CSV
        data.to_csv(output_file, index=False)

def visualisation_coord(input_file,output_file):
    if os.path.exists(output_file):
        print(f"Le fichier '{output_file}' existe déjà. Aucune opération ne sera effectuée.")
        return 
    else : 
        # Charger les données depuis le fichier CSV
        data = pd.read_csv(input_file)

        # Créer une carte centrée sur une position initiale (par exemple, Paris)
        m = folium.Map(location=[48.866667, 2.333333], zoom_start=5)

        # Ajouter un marqueur pour chaque gare
        for index, row in data.iterrows():
            lat, lon = row['Latitude'], row['Longitude']
            gare = row['Gare']
            folium.Marker([lat, lon], tooltip=gare).add_to(m)

        # Enregistrer la carte dans un fichier HTML
        m.save(output_file)



######################################
####                              ####
####     Lancement fonctions      ####
####                              ####
######################################

get_gare_coordinates(gares, url, r'Python_files\csv_files\coord_gps_gares.csv')
update_gare_names(r"Python_files\csv_files\coord_gps_gares.csv",r"Python_files\csv_files\coord_gps_gares_mis_a_jour.csv",gares_liste)
calculate_distances(r'Python_files\csv_files\coord_gps_gares.csv',r"Python_files\csv_files\distances_gares.csv")
update_gare_names(r"Python_files\csv_files\distances_gares.csv",r"Python_files\csv_files\distance_gares_mis_a_jour.csv",gares_liste)
visualisation_coord(r"Python_files\csv_files\coord_gps_gares_mis_a_jour.csv",r"Python_files\distance_between_train_station\carte_des_gares.html")