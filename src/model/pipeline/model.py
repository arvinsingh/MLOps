"""
This module creates the pipeline for building, training and saving ML model.

It includes the process of data preparation, model training using
RandomForestRegressor, hyperparameter tuning with GridSearchCV,
model evaluation, and serialization of the trained model.
"""

import pickle as pkl

import pandas as pd
from loguru import logger
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, GridSearchCV

from config import model_settings
from model.pipeline.preparation import prepare_data


def build_model() -> None:
    """
    This function creates the pipeline for building,
    training and saving ML model.

    It includes the process of data preparation, data splitting,
    model training using RandomForestRegressor, evaluation of the model, and
    serialization of the trained model.
    """
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


def _get_x_y(data: pd.DataFrame, col_x: dict, col_y: str) -> tuple:
    """
    Extracts desired columns from the data for features and target.

    Args:
        data (pd.DataFrame): The data to extract features and target from.
        col_x (list): The list of column names to extract as features.
        col_y (str): The column name to extract as target.

    Returns:
        pd.Series: The features extracted from the data.
        pd.Series: The target extracted from the data.
    """
    logger.info(f'Defining X: {col_x} and Y: {col_y}')
    return data[col_x], data[col_y]


def _split_train_test(
        features: pd.DataFrame,
        target: pd.Series,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """
    Splits the data into train and test sets.

    Args:
        features (pd.Series): The features to split.
        target (pd.Series): The target to split.

    Returns:
        pd.Series: The features for training.
        pd.Series: The features for testing.
        pd.Series: The target for training.
        pd.Series: The target for testing.
    """
    logger.info('Splitting data into train and test sets')
    return train_test_split(
        features,
        target,
        test_size=0.2,
        random_state=42,
    )


def _train_model(
        x_train: pd.DataFrame,
        y_train: pd.Series,
) -> RandomForestRegressor:
    """
    Trains the model using RandomForestRegressor.
    GridSearchCV is used for hyperparameter tuning.

    Args:
        x_train (pd.Series): The features for training.
        y_train (pd.Series): The target for training.

    Returns:
        RandomForestRegressor: The trained model.
    """
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


def _evaluate_model(
        model: RandomForestRegressor,
        x_test: pd.DataFrame,
        y_test: pd.Series,
) -> float:
    """
    Evaluates the model using the test data.

    Args:
        model (RandomForestRegressor): The trained model.
        x_test (pd.Series): The features for testing.
        y_test (pd.Series): The target for testing.

    Returns:
        float: The score of the model.
    """
    model_score = model.score(x_test, y_test)
    logger.info(f'Evaluating model: {model_score}')
    return model_score


def _save_model(model: RandomForestRegressor) -> None:
    """
    Saves the trained model to the specified path.

    Args:
        model (RandomForestRegressor): The trained model to save.

    Returns:
        None
    """
    model_path = f'{model_settings.model_path}/{model_settings.model_name}'
    logger.info(f'Saving model to {model_path}')
    with open(model_path, 'wb') as model_file:
        pkl.dump(model, model_file)
