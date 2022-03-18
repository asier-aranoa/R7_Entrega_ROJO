import os
import datetime as dt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.image as mimg
import seaborn as sns
from seaborn import load_dataset

df=pd.read_csv("df_modelo_industria.csv")

df=df.replace(False,0)
df=df.replace(True,1)
df=df.fillna(0)
df=df.set_index("Unnamed: 0")
X = df.iloc[:, 0:32]
X.head()
y = df.iloc[:, 32]
from imblearn.combine import SMOTETomek
from collections import Counter
x_resampled, y_resampled = SMOTETomek(random_state=0).fit_resample(X, y)
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(x_resampled, y_resampled, test_size=0.33, random_state=0)
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
from numpy import mean
from numpy import std
from sklearn.datasets import make_classification
from xgboost import XGBClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedStratifiedKFold
from matplotlib import pyplot

model = XGBClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

import pickle
with open('model_industria.pkl','wb') as handle:
    pickle.dump(model,handle)