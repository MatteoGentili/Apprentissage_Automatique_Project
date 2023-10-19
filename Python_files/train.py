from sklearn import *
import pandas as pd
from sklearn.pipeline import Pipeline

# Each object of the pipeline is identified by a key ('std_scaler', 'linreg').
# You can use any value as the key of an object in the pipeline
pipeline =  Pipeline([
    ('std_scaler', StandardScaler()),
    ('linreg', SGDRegressor())
])
data = pd.read_csv('Python_files/csv_files/Data.csv')

print(data.info())

#X_train, X_test, y_train, y_test = model_selection.train_test_split(diabetes.data, diabetes.target,
    #test_size=0.30, random_state=0)


#pgrid = {"max_depth": [1, 2, 3, 4, 5, 6, 7,8,9,10,12,15,20],
      #"min_samples_split": [2, 3, 5, 10, 15, 20,25,30]}

#grid_search = GridSearchCV(DecisionTreeRegressor(), param_grid=pgrid,scoring='neg_mean_squared_error', cv=10)
#grid_search.fit(X_train, y_train)
##grid_search.best_estimator_.score(X_test, y_test)
