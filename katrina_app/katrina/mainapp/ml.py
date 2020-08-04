import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn import ensemble

def getPrediction(arr):
    Hlat, Hlong, MaxSusWinds, Clat, Clong, Pop, Area = arr
    #reading my csv file from the url
    data = pd.read_csv("https://raw.githubusercontent.com/AmiBuch/HurricaneKat-python-ml-data/master/HurricaneDat.csv")
    #specifying the data on which the casualties/deaths are predicted
    x = data[['Hlat', 'Hlong', 'MaxSusWinds', 'Clat', 'Clong', 'Pop', 'Area']]
    y = data['Death']
    #training my model
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.1, random_state = 1)
    reg = linear_model.LinearRegression()
    clf = ensemble.GradientBoostingRegressor(n_estimators = 400, max_depth = 5, min_samples_split = 2, learning_rate = 0.1, loss = 'ls')
    clf.fit(x_train, y_train)
    
    input_variables = pd.DataFrame([[Hlat, Hlong, MaxSusWinds, Clat, Clong, Pop, Area]], columns = ['Hlat', 'Hlong', '<axSusWinds', 'Clat', 'Clong', 'Pop', 'Area'], dtype=float)
    prediction = clf.predict(input_variables)
    if prediction < 0:
        prediction = 0
    return prediction