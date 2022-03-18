import os
import datetime as dt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.image as mimg
import seaborn as sns
from seaborn import load_dataset
pd.options.display.max_columns = None
pd.set_option("display.max_rows", None)

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df=pd.read_csv("df_modelo.csv")
df=df.set_index("Unnamed: 0")
df=df.replace(False,0)
df=df.replace(True,1)
df=df.fillna(0)
df_na=df.isnull().sum().reset_index()
X = df.iloc[:, 0:32]
y = df.iloc[:, 32]
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_classification
from sklearn.ensemble import ExtraTreesClassifier, RandomForestClassifier


from imblearn.combine import SMOTETomek
from collections import Counter
x_resampled, y_resampled = SMOTETomek(random_state=0).fit_resample(X, y)
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(x_resampled, y_resampled, test_size=0.2, random_state=0)
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
from sklearn.ensemble import RandomForestClassifier

regressor = RandomForestClassifier(n_estimators=200, random_state=0, criterion="entropy")
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

import pickle
with open('model2.pkl','wb') as handle:
    pickle.dump(regressor,handle)