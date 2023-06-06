import os

import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np

from .Models.Company import Company
from .Models.StockIndex import StockIndex


# self.__model = tf.keras.models.load_model('my_model500.h5', compile=False)
# self.__model.compile(optimizer=tf.keras.optimizers.Adagrad(), loss='mse',
#                      metrics=tf.keras.metrics.RootMeanSquaredError())
class NeuralNetwork:
    __model = None
    __window_size = 40
    __scaler = None

    def __init__(self):
        self.__model = tf.keras.models.load_model('my_model.h5', compile=False)
        self.__model.compile(optimizer=tf.keras.optimizers.Adagrad(), loss='mse',
                             metrics=[tf.keras.metrics.RootMeanSquaredError(),tf.keras.metrics.MeanAbsolutePercentageError()])
        self.columns = ['date', 'open_val', 'high_val', 'low_val', 'volume_val', 'close_val']
        self.__scaler = MinMaxScaler((-10, 10))

        companies = Company.objects.all()
        ALL_data = np.empty(shape=(0, 5))

        for company in companies:
            data = StockIndex.objects.filter(symbol=company.id).order_by('date').values_list('open_val', 'high_val',
                                                                                                 'low_val',
                                                                                                 'volume_val',
                                                                                                 'close_val')
            ALL_data = np.concatenate([ALL_data, data])
        self.__scaler.fit(ALL_data)

    def preprocess_data(self, data):
        df = pd.DataFrame(columns=self.columns,
                          data=data)
        df.set_index('datetime', inplace=True)
        scaled_data = self.__scaler.transform(df[['open_val', 'high_val', 'low_val', 'volume_val', 'close_val']])
        return scaled_data[None, :]

    def predict(self, data, days: int):
        result = []
        scaled_data = self.preprocess_data(data)
        for i in range(days):
            predictions = self.__model.predict(scaled_data)
            scaled_data = np.append(scaled_data, predictions[None, :], axis=1)
            scaled_data = scaled_data[:, 1:, :]
            result.append(*predictions)
        print(result)
        transformed_pred = self.__scaler.inverse_transform(result)
        print(transformed_pred)
        return transformed_pred
