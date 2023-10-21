# Prédiction des Retards de TGV :railway_track:
_Projet 3ème année à CentraleSupelec sur le sujet suivant : Prédiction des retards de TGV_

Le groupe se compose de 4 étudiants: 
  * Matteo Gentili :train2:
  * Agathe Poulain :light_rail:
  * Ambroise Marché :monorail:
  * Henri Eloy :bullettrain_side:

Ce projet vise à **prédire le temps de retard des TGV** à l'arrivée ainsi que **la raison de leur retard** le cas échéant, en se concentrant sur les trains réservés par la SNCF.:alarm_clock:

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


# Projet TGV - Classification avec des Modèles d'Ensemble

## Introduction
Dans cette étude, des modèles de classification ont été sélectionnés et entraînés en utilisant sept algorithmes : 


### K-Nearest Neighbor (KNN) : Voisinage pour la Classification et la Régression
K-Nearest Neighbor est un algorithme de classification basé sur la proximité des données. Il attribue une classe à une nouvelle donnée en fonction des classes de ses voisins les plus proches. KNN repose sur une métrique de distance pour déterminer la similarité entre les données. Le paramètre "K" représente le nombre de voisins à considérer, et la classe majoritaire parmi les K voisins est attribuée à la nouvelle donnée.

### TimeSeries : Analyser le Passé, Prédire l'Avenir
Les séries temporelles sont des données chronologiques mesurées à des intervalles réguliers ou irréguliers. Elles sont utilisées pour comprendre les modèles et les tendances passées, ainsi que pour prédire des événements futurs. Les séries temporelles sont couramment utilisées dans des domaines tels que la finance, la météorologie et la gestion de la chaîne d'approvisionnement. L'analyse des séries temporelles nécessite des techniques spécifiques pour tenir compte de la dépendance temporelle entre les observations. Elle est cruciale pour la prise de décisions éclairées et la prévision dans de nombreux contextes.

### Forêt Aléatoire : Quand les Arbres Deviennent une Forêt pour des Prédictions Fiables
La Forêt Aléatoire est composée de différents arbres de décision qui sélectionnent l'attribut approprié pour un nœud en commençant par la racine et séparent les données en sous-ensembles en fonction de l'attribut sélectionné. Elle utilise la méthode du bagging et des modèles individuels d'arbres de décision. Les données entraînées sont divisées en sous-ensembles aléatoires, et chacun a son arbre de décision. Les données sont fournies en parallèle à tous les arbres de la forêt, et la classe prédite par la plupart des arbres est attribuée aux nouvelles données.

### Analyse en Composantes Principales (ACP) : Réduire la Complexité, Révéler les Tendances
L'Analyse en Composantes Principales (ACP) est une technique d'exploration de données qui simplifie des ensembles complexes de données en identifiant les variables les plus significatives et en les réduisant à un petit nombre de composantes principales. L'objectif est de conserver l'essentiel de l'information tout en éliminant le bruit. En appliquant l'ACP aux données, on peut révéler des tendances cachées, des relations et des structures, ce qui facilite la prise de décisions éclairées. L'ACP est couramment utilisée dans des domaines tels que la finance, la biologie, et l'analyse de séries temporelles pour extraire des informations cruciales à partir de données complexes.

## Méthodes d'Évaluation
La performance du classifieur peut être calculée à partir de la matrice de confusion. Après avoir été comparés au résultat réel, les résultats du classifieur peuvent générer quatre valeurs :

- Vrai Positif (TP) : la valeur prédite est positive ; la valeur réelle est positive.
- Vrai Négatif (TN) : la valeur prédite est négative ; la valeur réelle est négative.
- Faux Positif (FP) : la valeur prédite est positive ; la valeur réelle est négative.
- Faux Négatif (FN) : la valeur prédite est négative ; la valeur réelle est positive.

Quatre mesures ont été utilisées pour évaluer la performance des algorithmes sélectionnés :Accuracy,Precision, Recall, F1 score. Ces mesures sont toutes liées positivement à la qualité des algorithmes. Par conséquent, pour un algorithme spécifique, plus les valeurs de ces mesures sont élevées, meilleures sont ses performances.

Les valeurs des quatre mesures peuvent être obtenues par des calculs en utilisant ces paramètres :
- Accuracy = (TP + TN) / (TP + TN + FP + FN)
- Precision = TP / (TP + FP)
- Recall = TP / (TP + FN)
- F1 Score = 2 * Recall * Precision / (Recall + Precision) 

