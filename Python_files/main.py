from demande_trajet import *


######################################
######################################
############## PATHS #################
######################################
######################################
path_gare = r'C:\Users\MatyG\Documents\2023_2024\ApprAuto\Apprentissage_Automatique_Project\Python_files\csv_files\regularite-mensuelle-tgv-aqst.csv'
path_clean = r'C:\Users\MatyG\Documents\2023_2024\ApprAuto\Apprentissage_Automatique_Project\Python_files\csv_files\pred_retard.csv'
path_model_knn= r"C:\Users\MatyG\Documents\2023_2024\ApprAuto\Apprentissage_Automatique_Project\Python_files\modele_knn.joblib"


demande_trajet_user(path_gare,path_clean,path_model_knn)