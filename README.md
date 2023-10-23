# Prédiction des Retards de TGV :railway_track:
_Projet 3ème année à CentraleSupelec sur le sujet suivant : Prédiction des retards de TGV_

Le groupe se compose de 4 étudiants: 
  * Matteo Gentili :train2:
  * Agathe Poulain :light_rail:
  * Ambroise Marché :monorail:
  * Henri Eloy :bullettrain_side:

Ce projet vise à **prédire le temps de retard des TGV** à l'arrivée ainsi que **la raison de leur retard** le cas échéant, en se concentrant sur les trains réservés par la SNCF.:alarm_clock:

![]([https://gifer.com/embed/AHRo](https://i.gifer.com/AHRo.gif))

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



Installez les dépendances requises en exécutant la commande suivante :

```bash
pip install -r requirements.txt
```

## Structure du Projet (à changer lors de la communication de la structure)

- `.vscode/`: Répertoire pour vscode.
- `Python_files/`: Répertoire pour le code source Python du projet.
- `csv_files/`: Répertoire pour stocker les csv.

## Objectifs du Projet

Les objectifs du projet sont les suivants :

1. Appliquer différentes approches vues en cours et en TD sur ce dataset pour prédire le temps de retard des trains à l'arrivée sur les 6 derniers mois (tous les mois de 2023), ainsi que les principales causes de ces retards (c’est-à-dire sur les différents pourcentages relevés dans le dataset). Le dataset de test correspondra donc aux mois de 2023, tandis que celui d'entraînement sera basé sur les données des années précédentes. :bar_chart:	

2. Comparer les performances de ces différents modèles grâce aux métriques vues en cours. :chart_with_upwards_trend:

3. Conclure sur l'approche la plus appropriée pour prédire le retard des trains et les différentes causes. :clipboard:	

4. Écrire un rapport d'environ 5 pages sur le travail effectué et les résultats obtenus. :page_facing_up:	


# Projet TGV - Classification avec des Modèles d'Ensemble

## Introduction
L'utilisation de la régression est cruciale dans le contexte de la prédiction des retards des TGV. Les problèmes de retard des trains sont essentiellement des problèmes de régression, car ils impliquent la prédiction d'une valeur numérique (le temps de retard) en fonction de diverses caractéristiques et variables indépendantes. Voici quelques raisons pour lesquelles la régression est appropriée pour ce type de prédiction :

1. **Nature continue des retards** : Les retards des TGV sont généralement des valeurs continues, mesurées en minutes. Par conséquent, il est naturel d'appliquer des techniques de régression pour prédire ces valeurs continues.

2. **Relation complexe entre les caractéristiques et les retards** : Les retards des trains peuvent être influencés par de nombreuses variables, telles que la période de l'année, les gares de départ et d'arrivée, les conditions météorologiques, la capacité des trains, etc. La régression permet de modéliser ces relations complexes en capturant les effets de multiples variables indépendantes.

3. **Prédiction de la quantité de retard** : L'objectif principal est de prédire la quantité de retard, ce qui est une tâche de régression. Les passagers et les gestionnaires de réseau ferroviaire sont intéressés par des prévisions précises du temps de retard pour prendre des mesures appropriées.

4. **Évaluation des performances** : Les modèles de régression permettent d'évaluer les performances en utilisant des métriques spécifiques, telles que la MSE (Mean Squared Error) ou le RMSE (Root Mean Squared Error), qui mesurent l'écart entre les valeurs prédites et les valeurs réelles de retard. Ces métriques sont importantes pour évaluer la qualité des modèles.

Ainsi, la régression est un choix naturel pour ce projet, car elle permet de prédire de manière quantitative les retards des TGV en fonction des caractéristiques du trajet, des conditions météorologiques et d'autres facteurs pertinents. L'utilisation d'autres algorithmes de régression, tels que le K-Nearest Neighbor (KNN) et la Forêt Aléatoire, peut également être explorée pour déterminer quel modèle offre les meilleures performances prédictives.


### [K-Nearest Neighbor KNN](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html) : Voisinage pour la Classification et la Régression
K-Nearest Neighbor est un algorithme de classification basé sur la proximité des données. Il attribue une classe à une nouvelle donnée en fonction des classes de ses voisins les plus proches. KNN repose sur une métrique de distance pour déterminer la similarité entre les données. Le paramètre "K" représente le nombre de voisins à considérer, et la classe majoritaire parmi les K voisins est attribuée à la nouvelle donnée.

### [TimeSeries](https://pandas.pydata.org/docs/user_guide/timeseries.html) : Analyser le Passé, Prédire l'Avenir
Les séries temporelles sont des données chronologiques mesurées à des intervalles réguliers ou irréguliers. Elles sont utilisées pour comprendre les modèles et les tendances passées, ainsi que pour prédire des événements futurs. Les séries temporelles sont couramment utilisées dans des domaines tels que la finance, la météorologie et la gestion de la chaîne d'approvisionnement. L'analyse des séries temporelles nécessite des techniques spécifiques pour tenir compte de la dépendance temporelle entre les observations. Elle est cruciale pour la prise de décisions éclairées et la prévision dans de nombreux contextes.

### [Forêt Aléatoire](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html) : Quand les Arbres Deviennent une Forêt pour des Prédictions Fiables
La Forêt Aléatoire est composée de différents arbres de décision qui sélectionnent l'attribut approprié pour un nœud en commençant par la racine et séparent les données en sous-ensembles en fonction de l'attribut sélectionné. Elle utilise la méthode du bagging et des modèles individuels d'arbres de décision. Les données entraînées sont divisées en sous-ensembles aléatoires, et chacun a son arbre de décision. Les données sont fournies en parallèle à tous les arbres de la forêt, et la classe prédite par la plupart des arbres est attribuée aux nouvelles données.

### [Analyse en Composantes Principales (ACP)](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html) : Réduire la Complexité, Révéler les Tendances
L'Analyse en Composantes Principales (ACP) est une technique d'exploration de données qui simplifie des ensembles complexes de données en identifiant les variables les plus significatives et en les réduisant à un petit nombre de composantes principales. L'objectif est de conserver l'essentiel de l'information tout en éliminant le bruit. En appliquant l'ACP aux données, on peut révéler des tendances cachées, des relations et des structures, ce qui facilite la prise de décisions éclairées. L'ACP est couramment utilisée dans des domaines tels que la finance, la biologie, et l'analyse de séries temporelles pour extraire des informations cruciales à partir de données complexes.

Méthodes d'Évaluation
L'évaluation de la performance des modèles de régression dans ce projet repose sur des métriques spécifiques adaptées à la nature continue des retards des TGV. Deux métriques clés largement utilisées sont la MSE (Mean Squared Error) et la RMSE (Root Mean Squared Error).

Mean Squared Error (MSE)
La MSE est une métrique fondamentale qui mesure l'erreur quadratique moyenne entre les valeurs prédites par le modèle et les valeurs réelles. Plus précisément, pour chaque exemple de test, la MSE calcule la différence entre la valeur prédite et la valeur réelle, élève cette différence au carré pour éviter des annulations positives et négatives, puis prend la moyenne de ces carrés.

Formellement, la MSE peut être calculée comme suit :

```math
MSE = (1/n) Σ (yᵢ - ŷᵢ)²
```

Où :

**n** est le nombre d'exemples de test.  
**yᵢ** est la valeur réelle du retard pour le i-ème exemple.  
**ŷᵢ** est la valeur prédite du retard pour le i-ème exemple.  
Une MSE plus faible indique une meilleure adéquation du modèle aux données, c'est-à-dire que les prédictions du modèle se rapprochent davantage des valeurs réelles.

Root Mean Squared Error (RMSE)
Le RMSE est une métrique dérivée de la MSE, qui est plus interprétable car elle est exprimée dans la même unité que la variable que nous essayons de prédire (dans ce cas, les minutes de retard). Le RMSE est simplement la racine carrée de la MSE, ce qui revient à annuler l'opération d'élévation au carré effectuée dans la MSE.

Formellement, le RMSE peut être calculé comme suit :

```math
RMSE = \sqrt{MSE}
```
Le RMSE est particulièrement utile pour évaluer la précision des prédictions en termes de temps de retard, car il indique en moyenne à quel point les prédictions du modèle sont éloignées de la réalité en minutes.

Ces métriques permettent d'évaluer la performance des modèles de régression en tenant compte de la nature continue des retards des TGV. Plus le RMSE est faible, plus le modèle est capable de prédire avec précision les retards, ce qui est essentiel pour fournir des informations utiles aux passagers et aux gestionnaires de réseau ferroviaire.

