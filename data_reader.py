# coding=utf8

import pandas as pd
import numpy as np
import time
from sklearn.cross_validation import cross_val_score

# read data
dataSet = pd.read_csv("./data/train.csv")
X_train = dataSet.values[0:, 1:]
y_train = dataSet.values[0:, 0]


# for fast evaluation
X_train_small = X_train[:10000, :]
y_train_small = y_train[:10000]


X_test = pd.read_csv("./data/test.csv").values
