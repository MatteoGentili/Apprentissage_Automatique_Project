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
Dans cette étude, des modèles de classification ont été sélectionnés et entraînés en utilisant sept algorithmes : Régression Logistique, K-Nearest Neighbor (KNN), Naïve Bayes Gaussien, Arbre de Décision, Machine à Vecteurs de Support (SVM), Forêt Aléatoire et Arbre Boosté par Gradient. Les cinq premiers de ces algorithmes sont appelés des classifieurs de base car un seul modèle de classifieur est entraîné pour chacun d'entre eux. Les deux autres algorithmes sont appelés classifieurs d'ensemble car plus d'une instance de classifieurs de base est entraînée, et leur décision collective est rapportée comme la prédiction finale. En tant que deux des algorithmes d'ensemble les plus populaires, la Forêt Aléatoire et l'Arbre Boosté par Gradient combinent plusieurs modèles individuels pour améliorer les performances en termes de précision et de variance réduite.

### Régression Logistique
La Régression Logistique est un modèle de classification linéaire qui est couramment utilisé pour prédire une variable cible binaire. Elle modélise la relation entre les variables indépendantes et la probabilité d'appartenance à une classe particulière. La régression logistique est basée sur la fonction logistique qui transforme une combinaison linéaire des variables indépendantes en une valeur entre 0 et 1, représentant la probabilité. Elle est un choix fréquent pour la classification binaire.

### K-Nearest Neighbor (KNN)
K-Nearest Neighbor est un algorithme de classification basé sur la proximité des données. Il attribue une classe à une nouvelle donnée en fonction des classes de ses voisins les plus proches. KNN repose sur une métrique de distance pour déterminer la similarité entre les données. Le paramètre "K" représente le nombre de voisins à considérer, et la classe majoritaire parmi les K voisins est attribuée à la nouvelle donnée.

### Naïve Bayes Gaussien
Le Naïve Bayes Gaussien est un algorithme de classification basé sur le théorème de Bayes. Il est particulièrement adapté aux données où les caractéristiques suivent une distribution gaussienne (normale). Il calcule la probabilité qu'une donnée appartienne à une classe donnée en utilisant les probabilités conditionnelles des caractéristiques. Il suppose que les caractéristiques sont indépendantes, d'où le terme "naïve."

### Arbre de Décision
L'Arbre de Décision est un modèle de classification qui divise récursivement les données en sous-ensembles en fonction de critères de séparation. Chaque nœud de l'arbre représente une caractéristique, et les branches représentent les décisions basées sur cette caractéristique. Les feuilles de l'arbre contiennent les classes prédites. Les arbres de décision sont faciles à interpréter et peuvent gérer des données catégorielles et numériques.

### Forêt Aléatoire
La Forêt Aléatoire est composée de différents arbres de décision qui sélectionnent l'attribut approprié pour un nœud en commençant par la racine et séparent les données en sous-ensembles en fonction de l'attribut sélectionné. Elle utilise la méthode du bagging et des modèles individuels d'arbres de décision. Les données entraînées sont divisées en sous-ensembles aléatoires, et chacun a son arbre de décision. Les données sont fournies en parallèle à tous les arbres de la forêt, et la classe prédite par la plupart des arbres est attribuée aux nouvelles données.

### Arbre Boosté par Gradient
L'Arbre Boosté par Gradient n'a qu'un seul arbre de décision au départ, qui représente la prédiction initiale pour chaque donnée d'entraînement. Il utilise une méthode de boosting, ce qui signifie que les modèles individuels sont formés séquentiellement. Un arbre est construit, et sa prédiction est évaluée en fonction de ses erreurs résiduelles. Par conséquent, chaque modèle d'arbre apprend des erreurs commises par le modèle précédent. La construction de nouveaux arbres s'arrête lorsqu'un arbre supplémentaire ne peut pas améliorer la prédiction. Les données sont fournies le long d'un seul arbre racine.

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

