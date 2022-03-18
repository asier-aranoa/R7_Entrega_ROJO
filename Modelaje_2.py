# %% [markdown]
# # RANDOM FOREST

# %%
#Carga de librerias/Graficos debajo del script/Enseñar todas las columnas/filas
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
# Package imports
import missingno as msno

# %%
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# %%
# Importancia de cada variable para la hora de hacer los arboles (Te dice si son informativas o no)
#Si son muy bajas quitar alguna

# %%
# Modelo
df=pd.read_csv("Datos transformados/df_modelo.csv")


# %%
df=df.set_index("Unnamed: 0")

# %%
df=df.replace(False,0)
df=df.replace(True,1)

# %%
df=df.fillna(0)

# %%
#Numero de NA's por columna
df_na=df.isnull().sum().reset_index()
# df_na

# %%
X = df.iloc[:, 1:32]
# X.head()

# %%
y = df.iloc[:, 32]
# y.head()

# %%
# Importancia de cada variable para la hora de hacer los arboles (Te dice si son informativas o no)
#Si son muy bajas quitar alguna
print(__doc__)

import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_classification
from sklearn.ensemble import ExtraTreesClassifier, RandomForestClassifier


# Build a forest and compute the impurity-based feature importances
#forest = ExtraTreesClassifier(n_estimators=200, random_state=0)
forest = RandomForestClassifier(n_estimators=200, random_state=0)

forest.fit(X, y)
importances = forest.feature_importances_
std = np.std([tree.feature_importances_ for tree in forest.estimators_],
             axis=0)
indices = np.argsort(importances)[::-1]

# Print the feature ranking
print("Feature ranking:")

for f in range(X.shape[1]):
    print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))

# Plot the impurity-based feature importances of the forest
plt.figure()
plt.title("Feature importances")
plt.bar(range(X.shape[1]), importances[indices],
        color="r", yerr=std[indices], align="center")
plt.xticks(range(X.shape[1]), indices)
plt.xlim([-1, X.shape[1]])
plt.show()

# %%
# Gráfico
# ==============================================================================
fig, ax = plt.subplots(figsize=(6, 3.84))

sns.violinplot(
        x     = 'concurso_acreedores',
        data  = df,
        #color = "white",
        ax    = ax
    )

ax.set_title('Distribución notas de matemáticas por clase');

# %%
#Balanceo de los datos
from imblearn.combine import SMOTETomek
from collections import Counter

print('Statistics original: {}'.format(Counter(y)))

x_resampled, y_resampled = SMOTETomek(random_state=0).fit_resample(X, y)
print('\nStatistics resampled iris data: {}'.format(Counter(y_resampled)))
print('Perfectly balanced ')

# %%
#Partición de los datos
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(x_resampled, y_resampled, test_size=0.2, random_state=0)

# %%
# Feature Scaling (values in thousands or tends)
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# %%
# Indice 1

# %%
#Seleccion del algoritmo
from sklearn.ensemble import RandomForestClassifier

regressor = RandomForestClassifier(n_estimators=200, random_state=0, criterion="entropy")
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

# %%
#Evaluacion del algoritmo
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print(accuracy_score(y_test, y_pred))
#Antes el recall era 0.70

# %%
conmat = confusion_matrix(y_test, y_pred)
val = np.mat(conmat) 
classnames = list(set(y_train))
df_cm = pd.DataFrame(val, index=classnames, columns=classnames,)

import matplotlib.pyplot as plt
import seaborn as sns
plt.figure()
heatmap = sns.heatmap(df_cm, annot=True, cmap="Blues")
heatmap.yaxis.set_ticklabels(heatmap.yaxis.get_ticklabels(), rotation=0, ha='right')
heatmap.xaxis.set_ticklabels(heatmap.xaxis.get_ticklabels(), rotation=45, ha='right')

plt.ylabel('True label')
plt.xlabel('Predicted label')
plt.title('Churn Logistic Regression Model Results')
plt.show()

# %%
from sklearn.metrics import roc_curve, roc_auc_score
y_pred_proba = regressor.predict_proba(np.array(X_test))[:,1]
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)

sns.set()

plt.plot(fpr, tpr)

plt.plot(fpr, fpr, linestyle = '--', color = 'k')

plt.xlabel('False positive rate')

plt.ylabel('True positive rate')

AUROC = np.round(roc_auc_score(y_test, y_pred_proba), 2)

plt.title(f'RandomForestClassifier Model ROC curve; AUROC (Indice: Entropia): {AUROC}');

plt.show()

# %%
# Indice 2

# %%
#Seleccion del algoritmo
from sklearn.ensemble import RandomForestClassifier

regressor = RandomForestClassifier(n_estimators=200, random_state=0, criterion="gini")
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

# %%
#Evaluacion del algoritmo
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print(accuracy_score(y_test, y_pred))

# %%
conmat = confusion_matrix(y_test, y_pred)
val = np.mat(conmat) 
classnames = list(set(y_train))
df_cm = pd.DataFrame(val, index=classnames, columns=classnames,)

import matplotlib.pyplot as plt
import seaborn as sns
plt.figure()
heatmap = sns.heatmap(df_cm, annot=True, cmap="Blues")
heatmap.yaxis.set_ticklabels(heatmap.yaxis.get_ticklabels(), rotation=0, ha='right')
heatmap.xaxis.set_ticklabels(heatmap.xaxis.get_ticklabels(), rotation=45, ha='right')

plt.ylabel('True label')
plt.xlabel('Predicted label')
plt.title('Churn Logistic Regression Model Results')
plt.show()

# %%
from sklearn.metrics import roc_curve, roc_auc_score
y_pred_proba = regressor.predict_proba(np.array(X_test))[:,1]
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)

sns.set()

plt.plot(fpr, tpr)

plt.plot(fpr, fpr, linestyle = '--', color = 'k')

plt.xlabel('False positive rate')

plt.ylabel('True positive rate')

AUROC = np.round(roc_auc_score(y_test, y_pred_proba), 2)

plt.title(f'RandomForestClassifier Model ROC curve; AUROC (Indice:Gini): {AUROC}');

plt.show()

# %% [markdown]
# # REGRESIÓN LOGISTICA

# %%
# Tratamiento de datos
# ==============================================================================
import pandas as pd
import numpy as np

# Gráficos
# ==============================================================================
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns

# Preprocesado y modelado  
# ==============================================================================
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats.weightstats import ttest_ind

# Configuración matplotlib
# ==============================================================================
plt.rcParams['image.cmap'] = "bwr"
#plt.rcParams['figure.dpi'] = "100"
plt.rcParams['savefig.bbox'] = "tight"
style.use('ggplot') or plt.style.use('ggplot')

# Configuración warnings
# ==============================================================================
import warnings
warnings.filterwarnings('ignore')

# %%
# Creación del modelo
# ==============================================================================
# Para no incluir ningún tipo de regularización en el modelo se indica
# penalty='none'
modelo = LogisticRegression(penalty='none')
modelo.fit(X = x_resampled, y = y_resampled)

# %%
# Información del modelo
# ==============================================================================
print("Intercept:", modelo.intercept_)
print("Coeficiente:", list(zip(X.columns, modelo.coef_.flatten(), )))
print("Accuracy de entrenamiento:", modelo.score(X, y))

# %%
# Predicciones con clasificación final
# ==============================================================================
# Con .predict() se obtiene, para cada observación, la clasificación predicha por
# el modelo. Esta clasificación se corresponde con la clase con mayor probabilidad.
predicciones = modelo.predict(X = X_test)
predicciones

# %%
#Evaluacion del algoritmo
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

print(confusion_matrix(y_test,predicciones))
print(classification_report(y_test,predicciones))
print(accuracy_score(y_test, predicciones))

# %%
conmat = confusion_matrix(y_test, y_pred)
val = np.mat(conmat) 
classnames = list(set(y_train))
df_cm = pd.DataFrame(val, index=classnames, columns=classnames,)

import matplotlib.pyplot as plt
import seaborn as sns
plt.figure()
heatmap = sns.heatmap(df_cm, annot=True, cmap="Blues")
heatmap.yaxis.set_ticklabels(heatmap.yaxis.get_ticklabels(), rotation=0, ha='right')
heatmap.xaxis.set_ticklabels(heatmap.xaxis.get_ticklabels(), rotation=45, ha='right')

plt.ylabel('True label')
plt.xlabel('Predicted label')
plt.title('Churn Logistic Regression Model Results')
plt.show()

# %%
from sklearn.metrics import roc_curve, roc_auc_score
y_pred_proba = modelo.predict_proba(np.array(X_test))[:,1]
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)

sns.set()

plt.plot(fpr, tpr)

plt.plot(fpr, fpr, linestyle = '--', color = 'k')

plt.xlabel('False positive rate')

plt.ylabel('True positive rate')

AUROC = np.round(roc_auc_score(y_test, y_pred_proba), 2)

plt.title(f'RandomForestClassifier Model ROC curve; AUROC: {AUROC}');

plt.show()

# %% [markdown]
# ## XGBOOST

# %%
# Modelo
df=pd.read_csv("Datos transformados/df_modelo_industria.csv")

# %%
df=df.replace(False,0)
df=df.replace(True,1)

# %%
df=df.fillna(0)

# %%
df["concurso_acreedores"].value_counts()

# %%
df=df.set_index("Unnamed: 0")
# df=df.replace(False,0)
# df=df.replace(True,1)

# %%
X = df.iloc[:, 0:32]
X.head()

# %%
y = df.iloc[:, 32]
y.head()

# %%
#Balanceo de los datos
from imblearn.combine import SMOTETomek
from collections import Counter

print('Statistics original: {}'.format(Counter(y)))

x_resampled, y_resampled = SMOTETomek(random_state=0).fit_resample(X, y)
print('\nStatistics resampled iris data: {}'.format(Counter(y_resampled)))
print('(Almost) perfectly balanced again!!!')

# %%
#Partición de los datos
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(x_resampled, y_resampled, test_size=0.33, random_state=0)

# %%
# Feature Scaling (values in thousands or tends)
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# %%
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

# %%
#Evaluacion del algoritmo
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print(accuracy_score(y_test, y_pred))

# %%
conmat = confusion_matrix(y_test, y_pred)
val = np.mat(conmat) 
classnames = list(set(y_train))
df_cm = pd.DataFrame(val, index=classnames, columns=classnames,)

import matplotlib.pyplot as plt
import seaborn as sns
plt.figure()
heatmap = sns.heatmap(df_cm, annot=True, cmap="Blues")
heatmap.yaxis.set_ticklabels(heatmap.yaxis.get_ticklabels(), rotation=0, ha='right')
heatmap.xaxis.set_ticklabels(heatmap.xaxis.get_ticklabels(), rotation=45, ha='right')

plt.ylabel('True label')
plt.xlabel('Predicted label')
plt.title('Churn Logistic Regression Model Results')
plt.show()

# %%
from sklearn.metrics import roc_curve, roc_auc_score
y_pred_proba = model.predict_proba(np.array(X_test))[:,1]
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)

sns.set()

plt.plot(fpr, tpr)

plt.plot(fpr, fpr, linestyle = '--', color = 'k')

plt.xlabel('False positive rate')

plt.ylabel('True positive rate')

AUROC = np.round(roc_auc_score(y_test, y_pred_proba), 2)

plt.title(f'XGBoost Model ROC curve; AUROC: {AUROC}');

plt.show()

# %%
# tic-toc (Para saber cuanto tardan los modelos en compilar)
def tic():
    import time
    global startTime_for_tictoc
    startTime_for_tictoc = time.time()

    
def toc(verbose=True):
    import time
    gap = time.time() - startTime_for_tictoc
    if verbose:
        if 'startTime_for_tictoc' in globals():
            print("Elapsed time is " + str(gap) + " seconds.")
        else:
            print("Toc: start time not set")
    else:
        return gap

# Usage:
# tic()
# [here your code]
# toc()


