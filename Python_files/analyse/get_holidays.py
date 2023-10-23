from vacances_scolaires_france import SchoolHolidayDates
import pandas as pd

def get_holidays(datetime_format=True):
    #creation de l'objet vacances
    d = SchoolHolidayDates()

    #creation du dataframe des jours de vacances de 2018 a fin 2023
    vac = pd.DataFrame()
    for annee in range(2018,2024):
        vac = pd.concat([vac, pd.DataFrame(d.holidays_for_year(annee)).T])

    vac["date"] = pd.to_datetime(vac["date"])  #enregistrement des dates en pandas datetime (pour le traitement suivant)

    date_list = pd.date_range(start='2018-01-01', end='2023-06-01', freq='MS') #liste des mois de notre dataset
    df_mois = pd.DataFrame({'mois': pd.to_datetime(date_list), 'nb_jour_vacances':0}) #mise en dataframe


    # Pour chaque jour de vacances, est ajouté 1 au mois concerné
    # Ainsi, on compte le nombre de jours de vacances toutes zones confondues
    for date in vac["date"] :
        for i in df_mois.index :
            mois = df_mois["mois"][i]
            mois_suivant = mois + pd.DateOffset(months=1)
            if (date >= mois) and (date < mois_suivant) :
                df_mois.loc[i,"nb_jour_vacances"] += 1
                break

    if not datetime_format :
        df_mois['annee'] = df_mois['mois'].dt.year
        df_mois['mois'] = df_mois['mois'].dt.month
        df_mois = df_mois[["annee", "mois", "nb_jour_vacances"]]
        

    return df_mois
