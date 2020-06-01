import numpy as np
import pandas as pd
from sklearn import model_selection
csv = './rodents.csv'


def get(inputdata):
    data = pd.read_csv(inputdata, sep=',', header=None)
    print('Length: ', len(data))
    print('Shape: ', data.shape)
    return data



def split(data):
    x = data.values[:, 1:5]
    y = data.values[:, 0]
    x_train, x_test, y_train, y_test = model_selection.train_test_split(
        x, y, test_size=0.3, random_state=100)
    return x, x_train, x_test, y, y_train, y_test