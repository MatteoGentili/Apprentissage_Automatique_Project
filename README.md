# Prédiction des Retards de TGV :bullettrain_side:
_Projet 5ème année à CentraleSupelec sur le sujet suivant : Prédiction des retards de TGV_

Le groupe se compose de 4 étudiants: 
  * Matteo Gentili :train2:
  * Agathe Poulain :light_rail:
  * Ambroise Marché :monorail:
  * Henri Eloy :train:

:alarm_clock:
Ce projet vise à **prédire le temps de retard des TGV** à l'arrivée ainsi que **la raison de leur retard** le cas échéant, en se concentrant sur les trains réservés par la SNCF.

## Obtention des Données

Les données nécessaires pour ce projet peuvent être obtenues en suivant ces étapes :

1. Rendez-vous sur cette [page](https://www.data.gouv.fr/fr/datasets/regularite-mensuelle-tgv-par-liaisons/).
2. Descendez jusqu'en bas de la page.
3. Téléchargez le fichier au format CSV.

Les données peuvent ensuite être utilisées en Python en utilisant la librairie Pandas. 
Vous pouvez trouver un tutoriel pour vous aider à manipuler cette librairie [ici](https://pandas.pydata.org/docs/).

Pour visualiser les données avant de les traiter avec Python, nous utiliserons différents graphiques en utilisant des bibliothèques de visualisation telles que [Matplotlib](https://matplotlib.org/stable/index.html) ou [Seaborn](https://seaborn.pydata.org/).

## Préparation de l'Environnement de Travail

Assurez-vous d'avoir Python installé sur votre système. Vous pouvez utiliser un environnement virtuel pour gérer les dépendances de ce projet. Voici comment créer un environnement virtuel avec Python 3 :

```bash
python3 -m venv env
source env/bin/activate  # Pour activer l'environnement virtuel (sous Linux/macOS)
```

Ensuite, installez les dépendances requises en exécutant la commande suivante :

```bash
pip install -r requirements.txt
```

## Structure du Projet (à changer lors de la communication de la structure)

- `data/`: Répertoire pour stocker les données téléchargées.
- `src/`: Répertoire pour le code source Python du projet.
- `reports/`: Répertoire pour stocker les rapports et résultats.

## Objectifs du Projet

Les objectifs du projet sont les suivants :

1. Appliquer différentes approches vues en cours et en TD sur ce dataset pour prédire le temps de retard des trains à l'arrivée sur les 6 derniers mois (tous les mois de 2023), ainsi que les principales causes de ces retards (c’est-à-dire sur les différents pourcentages relevés dans le dataset). Le dataset de test correspondra donc aux mois de 2023, tandis que celui d'entraînement sera basé sur les données des années précédentes. :bar_chart:	

2. Comparer les performances de ces différents modèles grâce aux métriques vues en cours. :chart_with_upwards_trend:

3. Conclure sur l'approche la plus appropriée pour prédire le retard des trains et les différentes causes. :clipboard:	

4. Écrire un rapport d'environ 5 pages sur le travail effectué et les résultats obtenus. :page_facing_up:	



