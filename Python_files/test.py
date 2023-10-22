from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
import pandas as pd
import matplotlib.pyplot as plt
from mlxtend.feature_selection import SequentialFeatureSelector
from sklearn.feature_selection import SelectKBest, f_regression
import numpy as np
import logging
from sklearn.model_selection import train_test_split

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score



logging.basicConfig(filename='resultats.log', level=logging.INFO)


# file csv to panda

nom_du_fichier_csv = r'C:\Users\henri\Desktop\CS\ML\Apprentissage_Automatique_Project\Python_files\csv_files\pred_retard.csv'
data = pd.read_csv(nom_du_fichier_csv)



#choose here the label you want to train for among the following list;["prct_cause_infra","prct_cause_gestion_trafic","prct_cause_materiel_roulant","prct_cause_prise_en_charge_voyageurs","prct_cause_externe","prct_cause_gestion_gare"]:
label_list=["retard_moyen_tous_trains_arrivee"]
for l_list in label_list:

    label = l_list
    data_prct = data.copy()

    y = data[label]
    X = data_prct

    # Diviser le jeu de données en ensembles d'entraînement et de test

    separation_date = 2023

    # Masque pour les données de test (annee == 2023)
    test_mask = (data['annee'] == separation_date)

    # Masque pour les données d'entraînement (annee < 2023)
    train_mask = (data['annee'] < separation_date)

    # Séparez les données en ensembles d'entraînement et de test
    X_train = data_prct[train_mask]
    y_train = y[train_mask]
    X_test = data_prct[test_mask]
    y_test = y[test_mask]

    logging.info("X_train : %s", X_train)
    logging.info("y_train : %s", y_train)
    logging.info("X_test : %s", X_test)
    logging.info("y_test : %s", y_test)


    #correlation entre les features et le label sélectionné:

    correlation_matrix = X.corrwith(y)

    pd.set_option('display.max_rows', None)

    # Afficher le vecteur de corrélation
    abs_mat = correlation_matrix.abs()

    sorted_correlation = abs_mat.sort_values(ascending=False)

    #print(sorted_correlation)
    logging.info("sorted_correlation : %s", sorted_correlation)



    # pipeline
    random_forest_regression_pipeline = Pipeline([
        ('scaler', StandardScaler()),  # Étape de mise à l'échelle
        ('regressor', RandomForestRegressor())  # Utilisez RandomForestRegressor comme modèle de régression
    ])



    # Créez des listes pour stocker les scores et les valeurs de k
    best_scores = []
    best_ks = []
    best_mse = np.inf  # Initialisez la meilleure MSE à une valeur maximale

    # Créez une liste vide pour stocker les caractéristiques sélectionnées
    selected_features = []

    # Parcourez les noms de caractéristiques en ordre
    for k in range(1, len(X.columns) + 1):
        # Ajoutez le nom de la k-ème caractéristique de sorted_correlation à la liste selected_features
        selected_features.append(sorted_correlation.index[k - 1])

        # Créez la pipeline avec les caractéristiques sélectionnées
        random_forest_regression_pipeline = Pipeline([
            ('scaler', StandardScaler()),  # Étape de mise à l'échelle
            ('regressor', RandomForestRegressor())  # Modèle de régression
        ])

        # Entraînez le modèle avec la pipeline
        random_forest_regression_pipeline.fit(X_train[selected_features], y_train)

        # Évaluez le modèle en calculant la MSE
        y_pred = random_forest_regression_pipeline.predict(X_test[selected_features])
        mse = mean_squared_error(y_test, y_pred)

        # Mettez à jour la meilleure MSE et la meilleure valeur de k si nécessaire
        logging.info("mse : %s", mse)
        print(mse)

        if mse < best_mse:
            best_mse = mse
            best_k = k

        # Ajoutez la MSE actuelle et la valeur de k aux listes
        best_scores.append(mse)
        best_ks.append(k)

    # Créez un graphique de l'évolution de la MSE en fonction de k
    plt.figure()
    plt.plot(best_ks, best_scores, marker='o')
    plt.title("Évolution de la MSE en fonction de k")
    plt.xlabel("Valeur de k")
    plt.ylabel("MSE")
    plt.grid(True)

    # Trouvez la valeur de k où la MSE est minimale
    min_mse_k = best_ks[np.argmin(best_scores)]
    min_mse = min(best_scores)

    # Tracez un point à l'emplacement de la MSE minimale
    plt.scatter(min_mse_k, min_mse, color='red', label=f'Min MSE (k={min_mse_k})')

    # Affichez la légende
    plt.legend()

    # Affichez le graphique
    plt.show()
    plt.savefig(f'{l_list}plot_label.png')


    # Affichez la meilleure valeur de k et la meilleure MSE
    logging.info("Meilleur k : %s", min_mse_k)
    logging.info("Meilleur MSE : %s", min_mse)



    # Définissez une grille d'hyperparamètres que vous souhaitez tester
    param_grid = {
        'regressor__n_estimators': [10, 50, 100],
        'regressor__max_depth': [None, 10, 20, 30],
        'regressor__min_samples_split': [2, 5, 10],
        'regressor__min_samples_leaf': [1, 2, 4]
    }

    best_features = sorted_correlation.index[:min_mse_k]
    X_best= X[best_features]


    model = random_forest_regression_pipeline

    # Créez l'objet GridSearchCV avec la métrique appropriée (négatif de l'erreur quadratique moyenne)
    grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, scoring='neg_mean_squared_error')

    # Effectuez la recherche sur grille en ajustant le modèle aux données
    grid_search.fit(X_best, y)

    # Obtenez les meilleurs hyperparamètres et la meilleure performance (négatif de l'erreur quadratique moyenne)
    best_params = grid_search.best_params_
    best_performance = -grid_search.best_score_

    # Perform cross-validation on the best model
    best_model = grid_search.best_estimator_
    cross_val_scores = -cross_val_score(best_model, X, y, cv=5, scoring='neg_mean_squared_error')

    # Imprimez les résultats

    logging.info("Meilleurs hyperparamètres : %s", best_params)
    logging.info("Meilleure performance (MSE négatif) : %s", best_performance)
    logging.info("Performances de validation croisée (MSE négatif) : %s", cross_val_scores)
    logging.info("Moyenne des performances de validation croisée : %s", np.mean(cross_val_scores))


def best(best_params, X_train,y_train,y_test,X_test):
    # Créez la pipeline avec la mise à l'échelle et le modèle Random Forest Regressor en utilisant les meilleurs hyperparamètres
    model_final_pipeline = Pipeline([
        ('scaler', StandardScaler()),  # Étape de mise à l'échelle (peut être omise si les données sont déjà normalisées)
        ('regressor', RandomForestRegressor(**best_params))  # Modèle Random Forest avec les meilleurs hyperparamètres
    ])
    model_final_pipeline .fit(X_train, y_train)
    modele_final_mse = mean_squared_error(y_test, model_final_pipeline .predict(X_test))
    logging.info("Erreur quadratique moyenne (MSE) du modèle Random Forest en régression : %.2f", modele_final_mse)

best(best_params, X_train,y_train,y_test,X_test)