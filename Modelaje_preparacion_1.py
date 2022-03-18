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
df=pd.read_csv("Datos transformados/df_modelos2.csv",sep=";")

# %%
#Numero de NA's por columna
df_na=df.isnull().sum().reset_index()
# df_na

# %%
df["sector"].value_counts()

# %%
df=df[["inmovilizado_mil_eur","activo_circulante_mil_eur","total_activo_mil_eur","fondos_propios_mil_eur","pasivo_fijo_mil_eur","pasivo_liquido_mil_eur","total_pasivo_y_capital_propio_mil_eur","rentabilidad_sobre_el_activo_total_percent_percent","rentabilidad_sobre_recursos_propios_percent_percent","concurso_acreedores","existencias_mil_eur","sector","anyo_relativo","nombre"]]

# %%
df[df["inmovilizado_mil_eur"].isna()]

# %%
df["concurso_acreedores"]=df["concurso_acreedores"].fillna(False)

# %%
df=df.dropna()

# %%
#Numero de NA's por columna
df_na=df.isnull().sum().reset_index()
# df_na


# %%
#Analisis de liquidez
df["Fondo_de_maniobra"]=df["activo_circulante_mil_eur"]-df["pasivo_liquido_mil_eur"]
df["Ratio_de_liquidez"]=df["activo_circulante_mil_eur"]/df["pasivo_liquido_mil_eur"]

# %%
#Analisis de solvencia
df["Ratio_de_endeudamiento"]=(df["pasivo_fijo_mil_eur"] + df['pasivo_liquido_mil_eur']) / df['fondos_propios_mil_eur'] 
df["Ratio_de_endeudamiento_a_largo_plazo"] = df['pasivo_fijo_mil_eur'] / df['fondos_propios_mil_eur']
df["Ratio_de_deuda"] = (df['pasivo_fijo_mil_eur'] + df['pasivo_liquido_mil_eur']) / df['total_activo_mil_eur']
df["Ratio_de_apalancamiento_financiero"] = df['total_activo_mil_eur'] / df['fondos_propios_mil_eur'] 

# %%
#Analisis de rentabilidad
df["ROA_(Rentabilidad_Económica)"] = df['rentabilidad_sobre_el_activo_total_percent_percent'] 
df["ROE_(Rentabilidad_Financiera)"] = df['rentabilidad_sobre_recursos_propios_percent_percent'] 

# %%
df=df.drop(['inmovilizado_mil_eur', 'activo_circulante_mil_eur',
       'total_activo_mil_eur', 'fondos_propios_mil_eur', 'pasivo_fijo_mil_eur',
       'pasivo_liquido_mil_eur', 'total_pasivo_y_capital_propio_mil_eur',
       'rentabilidad_sobre_el_activo_total_percent_percent',
       'rentabilidad_sobre_recursos_propios_percent_percent', 'existencias_mil_eur'],axis=1)

# %%
df.replace([np.inf, -np.inf], np.nan, inplace=True) 


# %%
df=df.dropna()

# %%
df.columns

# %%
df=df[['nombre','anyo_relativo','sector','Fondo_de_maniobra', 'Ratio_de_liquidez', 'Ratio_de_endeudamiento',
       'Ratio_de_endeudamiento_a_largo_plazo', 'Ratio_de_deuda',
       'Ratio_de_apalancamiento_financiero', 'ROA_(Rentabilidad_Económica)',
       'ROE_(Rentabilidad_Financiera)','concurso_acreedores']]

# %%
#Numero de NA's por columna
df_na=df.isnull().sum().reset_index()
# df_na

# %%
df2=df.copy()

# %%
df2=df2[df2["sector"]=="Industria"]

# %%
df2=df2.drop("sector",axis=1)

# %%
df2.shape

# %%
# df.to_csv("df_modelo.csv")

# %%
y=df2["concurso_acreedores"].copy()

# %%
df2=df2.drop("concurso_acreedores",axis=1)

# %%
df2=pd.pivot_table(df2,index=['nombre'],columns=["anyo_relativo"])

# %%
df2.columns = ["_".join((j,i)) for i,j in df2.columns]


# %%
import numpy as np
from sklearn.impute import SimpleImputer
imp_mean = SimpleImputer(missing_values=np.nan, strategy='mean')
imp_mean.fit(df2.values[:,])
datos=imp_mean.transform(df2)

# %%
df2=pd.DataFrame(data=datos,columns=df2.columns)

# %%
df2["concurso_acreedores"]=y

# %%
df2["concurso_acreedores"].value_counts()

# %%
#df2.to_csv("df_modelo_industria.csv")

# %%
# df.head()

# %%
# df=df.set_index("Unnamed: 0")

# %%
#Numero de NA's por columna
df_na=df.isnull().sum().reset_index()
# df_na

# %%
y=df["concurso_acreedores"].copy()

# %%
df=df.drop("concurso_acreedores",axis=1)

# %%
df=pd.pivot_table(df,index=['nombre'],columns=["anyo_relativo"])

# %%
#Numero de NA's por columna
df_na=df.isnull().sum().reset_index()

# %%
df.columns = ["_".join((j,i)) for i,j in df.columns]


# %%
import numpy as np
from sklearn.impute import SimpleImputer
imp_mean = SimpleImputer(missing_values=np.nan, strategy='mean')
imp_mean.fit(df.values[:,])
datos=imp_mean.transform(df)

# %%
df=pd.DataFrame(data=datos,columns=df.columns)

# %%
df["concurso_acreedores"]=y

# %%
#df.to_csv("df_modelo.csv")


