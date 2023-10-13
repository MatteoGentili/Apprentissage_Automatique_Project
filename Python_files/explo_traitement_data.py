# Imports
import pandas as pd
import numpy as np

# PARTIE 1 : Exploration de la base de données
df = pd.read_csv('csv_files/regularite-mensuelle-tgv-aqst.csv',sep=';')
print('Information : ', '\n', df.info())
print('Description statistique de chaque colonne : ', '\n', df.describe())
print('Donées manquantes : ', '\n', df.isnull().sum())
print('Type des données : ', '\n', df.dtypes)

# PARTIE 2 : Traitement de la base de données

# On observe que les seules valeurs manquante sont pour les features commentaires : commentaire_annulation, commentaire_retards_depart
# et commentaire_retard_arrivee
# Pour une première approche simplificatrice du dataset, on prend la décision de supprimier le