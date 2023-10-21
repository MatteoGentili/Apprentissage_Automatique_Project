######################################
######################################
############## Import ################
######################################
######################################
import pandas as pd
from datetime import datetime
######################################
######################################
############ Variables ###############
######################################
######################################



def demande_trajet_user(path_gare):
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
            gare_depart_correspondante = matches_depart[0]
            break
        elif len(matches_depart) > 1:
            print("Gares de départ valides :")
            for match in matches_depart:
                print("- ", match)
        else:
            print("Aucune correspondance trouvée pour la gare de départ. Essayez à nouveau.")

    # Filtrer le DataFrame en fonction de la gare de départ
    filtre = df_retard_gares['gare_depart'].str.lower() == gare_depart_correspondante.lower()
    gares_arrivee_uniques = df_retard_gares.loc[filtre, 'gare_arrivee'].unique()

    # Afficher la liste des gares d'arrivée uniques
    if gares_arrivee_uniques.any():
        print("\nGares d'arrivée uniques depuis", gare_depart_correspondante, ":")
        for i, gare in enumerate(gares_arrivee_uniques, start=1):
            print(f"{i}. {gare}")

        # Demander à l'utilisateur de choisir une gare d'arrivée
        while True:
            choix = input("\nChoisissez une gare d'arrivée en entrant son numéro (ou 'q' pour quitter) : ")
            if choix.lower() == 'q':
                break  # Quitter le programme
            try:
                choix = int(choix)
                if 1 <= choix <= len(gares_arrivee_uniques):
                    gare_arrivee_choisie = gares_arrivee_uniques[choix - 1]
                    # Demander à l'utilisateur de choisir une date au format "année-mois" (par exemple, "2018-01")
                    while True:
                        date_user = input("Entrez la date au format 'année-mois' (compris entre 2023-01 et 2023-06) : ").strip()

                        # Vérifier que la date est au bon format (année-mois)
                        try:
                            year, month = map(int, date_user.split('-'))
                            if (1 <= month <= 6 and year == 2023):
                                break  # Date valide
                            else:
                                print("Date invalide. Essayez à nouveau.")
                        except ValueError:
                            print("Format de date incorrect. Utilisez le format 'année-mois' (compris entre '2023-01' et '2023-06').")
                    filtre_trajet = (df_retard_gares['gare_depart'].str.lower() == gare_depart_correspondante.lower()) & \
                                    (df_retard_gares['gare_arrivee'].str.lower() == gare_arrivee_choisie.lower())
                    durees_moyennes = df_retard_gares.loc[filtre_trajet, 'duree_moyenne']
                    nb_trains_moyen = df_retard_gares.loc[filtre_trajet, 'nb_train_prevu']
                    if not durees_moyennes.empty:
                        somme_durees = durees_moyennes.sum()
                        moyenne_duree = somme_durees / len(durees_moyennes)
                        heure=int(moyenne_duree//60)
                        minute=int(moyenne_duree%60)
                    if not nb_trains_moyen.empty:
                        somme_nb_trains_moyen = nb_trains_moyen.sum()
                        moyenne_nb_trains_moyen = int(somme_nb_trains_moyen / len(nb_trains_moyen))

                    # Maintenant, vous pouvez utiliser la date choisie pour effectuer des opérations supplémentaires
                    print(f"\nVous avez choisi comme trajet : {gare_depart_correspondante} - {gare_arrivee_choisie}")
                    print(f"Pour la date : {date_user}")
                    print(f"Le trajet durera en moyenne : {heure} heures et {minute} minutes\n")

                    print(f"à enlever/ nb trains prévus en moyenne : {moyenne_nb_trains_moyen}")

                    break  # Sortir de la boucle
                else:
                    print("Numéro invalide. Veuillez réessayer.")
            except ValueError:
                print("Saisie invalide. Veuillez entrer un numéro valide.")
    else:
        print("Aucune gare d'arrivée trouvée depuis", gare_depart_correspondante)

    print('Prédisons le retard pour votre trajet ....\n')



path_gare = r'Python_files\csv_files\regularite-mensuelle-tgv-aqst.csv'
demande_trajet_user(path_gare)