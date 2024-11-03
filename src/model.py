from preparation import prepare_data
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
import pickle as pkl


def build_model():
    df = prepare_data()
    X, Y = get_X_Y(df)
    X_train, X_test, Y_train, Y_test = split_train_test(X, Y)
    model = train_model(X_train, Y_train)
    score = evaluate_model(model, X_test, Y_test)
    print(f'Model score: {score}')
    save_model(model)


def get_X_Y(data,
            col_X = ['area',
                     'rooms',
                     'bedrooms',
                     'bathrooms',
                     'garden',
                     'balcony_yes', 
                     'storage_yes', 
                     'parking_yes', 
                     'furnished_yes',
                     'garage_yes'],
            col_Y = 'rent'):
    return data[col_X], data[col_Y]

def split_train_test(X, Y):
    X_train, X_test, Y_train, Y_test = train_test_split(X, 
                                                        Y, 
                                                        test_size=0.2, 
                                                        random_state=42)
    return X_train, X_test, Y_train, Y_test

def train_model(X_train, Y_train):
    grid_space = {'n_estimators': [100, 200, 300],
                  'max_depth': [10, 20, 30]}
    model = GridSearchCV(RandomForestRegressor(),
                         grid_space,
                         cv=5,
                         n_jobs=-1)
    model.fit(X_train, Y_train)

    return model.best_estimator_

def evaluate_model(model, X_test, Y_test):
    return model.score(X_test, Y_test)

def save_model(model, path='models/model'):
    pkl.dump(model, open(path, 'wb'))