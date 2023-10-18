import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Liste des gares à rechercher
gares = [
    "Italie", "Zurich", "Annecy",
    "Avignon TGV", "Valence-TGV", "Aix-en-Provence TGV", "Dijon-Ville", "Le Creusot-Montceau-Montchanin",
    "Bordeaux-Saint-Jean", "La Rochelle-Ville", "Quimper", "Saint-Pierre-des-Corps", "Tours", "Brest", "Poitiers",
    "Toulouse-Matabiau", "Angers-Saint-Laud", "Angoulême", "Nantes", "Vannes", "Laval", "Le Mans", "Saint-Malo",
    "Dunkerque", "Douai", "Arras"
]

# URL de la page à scraper
url = "https://www.coordonnees-gps.fr/communes/paris-/75100"

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


with open('coord_gps_gares.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Gare', 'Latitude', 'Longitude']
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
        writer.writerow({'Gare': gare, 'Latitude': coord_gps.split(",")[0], 'Longitude': coord_gps.split(",")[1]})

# Fermer le navigateur
driver.quit()
