# %%
import pandas as pd
import numpy as np
import datetime as dt

# %%
dataset=pd.read_csv('Datos transformados/df_deudores_sinna_balance.csv',sep=';')

# %%
dataset=dataset.drop(['Unnamed: 0','index'], axis=1)

# %%
dataset.columns

# %%
dataset['fecha_resolucion']=pd.to_datetime(dataset['fecha_resolucion']).dt.strftime('%Y')

# %%
dataset['ultimo_ano_disponible']=pd.to_datetime(dataset['ultimo_ano_disponible']).dt.strftime('%Y')

# %%
dataset[['codigo_nif','fecha_resolucion','ultimo_ano_disponible']][pd.isna(dataset['fecha_resolucion'])==False]

# %%
dataset['anyo_referencia']=dataset['fecha_resolucion']

# %%
range(len(dataset['anyo_referencia']))

# %%
for a in range(len(dataset['anyo_referencia'])):
    if pd.isna(dataset['anyo_referencia'][a]) ==True:
        dataset['anyo_referencia'][a]=dataset['ultimo_ano_disponible'][a]

# %%
dataset[['codigo_nif','fecha_resolucion','ultimo_ano_disponible','anyo_referencia']][pd.isna(dataset['fecha_resolucion'])==False]

# %%
dataset2=dataset.drop(dataset.columns[2:6], axis=1)

# %%
dataset2

# %%
dataset2=dataset2.drop(dataset2.columns[3:9], axis=1)

# %%
dataset2=dataset2.drop(dataset2.columns[4:90], axis=1)

# %%
dataset2=dataset2.sort_values(by=['codigo_nif','anyo'])

# %%
for index, row in dataset2[['anyo','ultimo_ano_disponible']].iterrows():
    if row[0] == 'ult_ano_disp':
        dataset2.loc[index,'anyo']=dataset2.loc[index,'ultimo_ano_disponible']

# %%
dataset2

# %%
dataset2=dataset2.drop_duplicates()

# %%
grupos=dataset2.groupby(by='codigo_nif').count()

# %%
grupos=grupos.reset_index()

# %%
grupos

# %%
empresas_pivot=grupos[grupos['anyo']>=4]

# %%
empresas_pivot

# %%
empresas_pivot=empresas_pivot['codigo_nif']

# %%
empresas_pivot=pd.DataFrame(empresas_pivot)

# %%
pivot=empresas_pivot.merge(dataset,how='left',on='codigo_nif')

# %%
pivot['anyo']

# %%
for index, row in pivot[['anyo','ultimo_ano_disponible']].iterrows():
    if row[0] == 'ult_ano_disp':
        pivot.loc[index,'anyo']=pivot.loc[index,'ultimo_ano_disponible']

# %%
pivot=pivot.sort_values(by=['codigo_nif','anyo'],ascending=False)

# %%
pivot=pivot.drop_duplicates()

# %%
pivot=pivot.reset_index()

# %%
pivot

# %%
pivott=pivot.groupby('codigo_nif').head(4)

# %%
pivott=pivott.reset_index()
pivott=pivott.drop(['level_0','index'], axis=1)

# %%
pivott['anyo_relativo']=1

# %%
for a in pivott['anyo_relativo'].index:
    if a==0:
        pivott.loc[a,'anyo_relativo']='anyo_objetivo'
    if a==1:
        pivott.loc[a,'anyo_relativo']='anyo_objetivo-1'
    if a==2:
        pivott.loc[a,'anyo_relativo']='anyo_objetivo-2'
    if a==3:
        pivott.loc[a,'anyo_relativo']='anyo_objetivo-3'
    if a>=4:
        pivott.loc[a,'anyo_relativo']=pivott.loc[a-4,'anyo_relativo']
    
    

# %%
#pivott.to_csv('df_modelos2.csv',sep=';')


