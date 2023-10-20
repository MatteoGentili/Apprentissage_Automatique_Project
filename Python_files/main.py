######################################
######################################
############## Import ################
######################################
######################################
import pandas as pd

######################################
######################################
############ Variables ###############
######################################
######################################
path_gare = r'Python_files\csv_files\regularite-mensuelle-tgv-aqst.csv'
df_retard_gares = pd.read_csv(path_gare, sep=';')

noms_gares = df_retard_gares['gare_depart'].unique()


######################################
######################################
## Demande des gares départ/arrivée ##
######################################
######################################

# Demande à l'utilisateur quelle gare de départ il souhaite
# Créez un dictionnaire pour mapper les paires de gares vers les détails du trajet
trajets = {}

# Remplissez le dictionnaire à partir du DataFrame
for index, row in df_retard_gares.iterrows():
    gare_depart = row['gare_depart'].lower()
    gare_arrivee = row['gare_arrivee'].lower()
    trajets[(gare_depart, gare_arrivee)] = row

# Demande à l'utilisateur quelle gare de départ il souhaite
# Demande à l'utilisateur quelle gare de départ il souhaite
# Demande à l'utilisateur quelle gare de départ il souhaite
while True:
    gare_depart_user = input("Quelle gare de départ souhaitez-vous ? : \n").strip().lower()

    # Recherche de correspondances partielles pour la gare de départ
    matches_depart = [nom_gare for nom_gare in noms_gares if gare_depart_user in nom_gare.lower()]

    if len(matches_depart) == 1:
        break  # Sortez de la boucle, car l'entrée est valide
    elif len(matches_depart) > 1:
        print("Gares de départ valides :")
        for match in matches_depart:
            print("- ", match)
    else:
        print("Aucune correspondance trouvée pour la gare de départ. Essayez à nouveau.")

# Trouver toutes les gares d'arrivée possibles depuis la gare de départ choisie
gares_arrivee_possibles = set()
for index, row in df_retard_gares.iterrows():
    gare_depart = row['gare_depart'].lower()
    gare_arrivee = row['gare_arrivee'].lower()

    if gare_depart == matches_depart[0].lower:
        gares_arrivee_possibles.add(gare_arrivee)
        print(gares_arrivee_possibles)

# Afficher la liste des gares d'arrivée possibles
if gares_arrivee_possibles:
    print("Gares d'arrivée possibles depuis", matches_depart[0], ":")
    for gare in gares_arrivee_possibles:
        print("- ", gare)
else:
    print("Aucune gare d'arrivée trouvée depuis", matches_depart[0])
