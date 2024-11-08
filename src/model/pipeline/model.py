import pickle as pkl

from loguru import logger
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, GridSearchCV

from config import model_settings
from model.pipeline.preparation import prepare_data


def build_model():
    logger.info('Model building pipeline started')
    df = prepare_data()
    feature_names = [
        'area',
        'rooms',
        'bedrooms',
        'bathrooms',
        'garden',
        'balcony_yes',
        'storage_yes',
        'parking_yes',
        'furnished_yes',
        'garage_yes',
    ]
    target_name = 'rent'
    X, Y = _get_x_y(
        df,
        feature_names,
        target_name,
    )
    X_train, X_test, Y_train, Y_test = _split_train_test(X, Y)
    model = _train_model(X_train, Y_train)
    _evaluate_model(model, X_test, Y_test)
    _save_model(model)


def _get_x_y(data, col_x, col_y):
    logger.info(f'Defining X: {col_x} and Y: {col_y}')
    return data[col_x], data[col_y]


def _split_train_test(features, target):
    logger.info('Splitting data into train and test sets')
    return train_test_split(
        features,
        target,
        test_size=0.2,
        random_state=42,
    )


def _train_model(x_train, y_train):
    logger.info('Training model')
    grid_space = {
        'n_estimators': [100, 200, 300],
        'max_depth': [10, 20, 30],
    }
    model = GridSearchCV(
        RandomForestRegressor(),
        grid_space,
        cv=5,
        n_jobs=-1,
    )
    model.fit(x_train, y_train)
    return model.best_estimator_


def _evaluate_model(model, x_test, y_test):
    model_score = model.score(x_test, y_test)
    logger.info(f'Evaluating model: {model_score}')
    return model_score


def _save_model(model):
    model_path = f'{model_settings.model_path}/{model_settings.model_name}'
    logger.info(f'Saving model to {model_path}')
    with open(model_path, 'wb') as model_file:
        pkl.dump(model, model_file)
