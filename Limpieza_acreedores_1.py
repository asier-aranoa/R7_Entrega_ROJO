# %%
import pandas as pd
import numpy as np
import datetime as dt

# %%
df=pd.read_csv('Datos originales/datos_sabi.csv',encoding='latin-1')
df2=pd.read_csv('Datos originales/publicidad_concursal.csv',encoding='latin-1')

# %%
df=df.drop(['Unnamed: 0'], axis=1)

# %%
columnas=[]
i=1
for a in df.columns:
    columnas.append(a)
    i=i+1

# %%
na_cols=df.isnull().sum(axis = 0)

# %%
na_cols

# %%
df.shape

# %%
na_cols=df.isnull().sum(axis = 0)
na_cols=pd.DataFrame(na_cols)
na_cols=na_cols.reset_index()
na_cols.rename(columns={'index': 'Variable', 0: 'Nas'}, inplace=True)
na_cols['Porcentaje Nas']=na_cols['Nas']/len(df[na_cols['Variable']])*100
na_cols=na_cols.sort_values(by='Porcentaje Nas',ascending=False)
na_cols[na_cols['Porcentaje Nas']!=0].head(20)

# %%
a=pd.DataFrame(df.dtypes).reset_index()
a.groupby(by=0).count()

# %%
cobjects=[]
cnum=[]
for a in columnas:
    if df[a].dtypes=='O':
        cobjects.append(a)
    else:
        cnum.append(a)

# %%
cobjects

# %%
cnum

# %%
nan_cols= [i for i in df.columns if df[i].isnull().sum()]

# %%
nan_cols

# %%
df.columns

# %%
df2.columns

# %%
df2=df2.drop(['unnamed_3'], axis=1)

# %%
df2.columns

# %%
df2=df2.drop_duplicates()

# %%
df1_nombres=df[['codigo_nif','nombre']]
df1_nombres.rename(columns={'codigo_nif': 'codigo_nif', 'nombre': 'nombre'}, inplace=True)
df2_nombres=df2[['nif','deudor']]
df2_nombres.rename(columns={'nif': 'codigo_nif', 'deudor': 'deudor'}, inplace=True)

# %%
df1_nombres.drop_duplicates(inplace=True)
df1_nombres

# %%
df2_nombres.drop_duplicates(inplace=True)
df2_nombres

# %%
for a in df2_nombres.index:
    df2_nombres.loc[a,'deudor']=' '.join(df2_nombres.loc[a,'deudor'].split())

# %%
df2_nombres

# %%
df_nombres=df1_nombres.merge(df2_nombres,how='right',on='codigo_nif')

# %%
df_nombres.columns

# %%
for a in df_nombres['nombre'].index:
    df_nombres['nombre'][a]=df_nombres['nombre'][a].upper()
    df_nombres['nombre'][a]=df_nombres['nombre'][a].strip()

for a in df_nombres['deudor'].index:
    df_nombres['deudor'][a]=df_nombres['deudor'][a].upper()
    df_nombres['deudor'][a]=df_nombres['deudor'][a].strip()

# %%
for a in df_nombres['nombre'].index:
    df_nombres['nombre'][a]=df_nombres['nombre'][a].replace(',','')
    df_nombres['nombre'][a]=df_nombres['nombre'][a].replace('.','')
    df_nombres['nombre'][a]=df_nombres['nombre'][a].replace('(','')
    df_nombres['nombre'][a]=df_nombres['nombre'][a].replace(')','')
    df_nombres['nombre'][a]=df_nombres['nombre'][a].replace('SOCIEDAD ANONIMA','SA')
    df_nombres['nombre'][a]=df_nombres['nombre'][a].replace('SOCIEDAD LIMITADA','SL')
    df_nombres['nombre'][a]=df_nombres['nombre'][a].replace('SOCIEDAD','S')
    df_nombres['nombre'][a]=df_nombres['nombre'][a].replace('SOC','S')
    df_nombres['nombre'][a]=df_nombres['nombre'][a].replace('COOP','C')
    df_nombres['nombre'][a]=df_nombres['nombre'][a].replace('COOPERATIVA','C')
    df_nombres['nombre'][a]=df_nombres['nombre'][a].replace('CIA','COMPAÑIA')
    df_nombres['nombre'][a]=df_nombres['nombre'][a].replace(' LIMITADA','L')
    df_nombres['nombre'][a]=df_nombres['nombre'][a].replace(' ANONIMA','A')
    df_nombres['nombre'][a]=df_nombres['nombre'][a].replace('Ñ','N')
    df_nombres['nombre'][a]=df_nombres['nombre'][a].replace(' LIMITADA','L')
    df_nombres['nombre'][a]=df_nombres['nombre'][a].replace(' ANONIMA','A')
    df_nombres['nombre'][a]=df_nombres['nombre'][a].replace('Í','I')
    df_nombres['nombre'][a]=df_nombres['nombre'][a].replace('Ó','O')
    df_nombres['nombre'][a]=df_nombres['nombre'][a].replace(' LABORAL','L')
    df_nombres['nombre'][a]=df_nombres['nombre'][a].replace('&','Y')
    df_nombres['nombre'][a]=df_nombres['nombre'][a].replace(' AND ','Y')
    df_nombres['nombre'][a]=df_nombres['nombre'][a].replace('<D1>','N')
    df_nombres['nombre'][a]=df_nombres['nombre'][a].replace(' UNIPERSONAL','U')
    df_nombres['nombre'][a]=df_nombres['nombre'][a].replace(' PROFESIONAL','P')
    df_nombres['nombre'][a]=df_nombres['nombre'][a].replace('-',' ')
    df_nombres['nombre'][a]=df_nombres['nombre'][a].replace('Y',' Y ')
    df_nombres['nombre'][a]=df_nombres['nombre'][a].replace('S L','SL')
    df_nombres['nombre'][a]=df_nombres['nombre'][a].replace('S C','SC')

for a in df_nombres['deudor'].index:
    df_nombres['deudor'][a]=df_nombres['deudor'][a].replace(',','')
    df_nombres['deudor'][a]=df_nombres['deudor'][a].replace('.','')
    df_nombres['deudor'][a]=df_nombres['deudor'][a].replace('(','')
    df_nombres['deudor'][a]=df_nombres['deudor'][a].replace(')','')
    df_nombres['deudor'][a]=df_nombres['deudor'][a].replace('SOCIEDAD ANONIMA','SA')
    df_nombres['deudor'][a]=df_nombres['deudor'][a].replace('SOCIEDAD LIMITADA','SL')
    df_nombres['deudor'][a]=df_nombres['deudor'][a].replace('SOCIEDAD','S')
    df_nombres['deudor'][a]=df_nombres['deudor'][a].replace('SOC','S')
    df_nombres['deudor'][a]=df_nombres['deudor'][a].replace('COOP','C')
    df_nombres['deudor'][a]=df_nombres['deudor'][a].replace('COOPERATIVA','C')
    df_nombres['deudor'][a]=df_nombres['deudor'][a].replace('CIA','COMPAÑIA')
    df_nombres['deudor'][a]=df_nombres['deudor'][a].replace(' LIMITADA','L')
    df_nombres['deudor'][a]=df_nombres['deudor'][a].replace(' ANONIMA','A')
    df_nombres['deudor'][a]=df_nombres['deudor'][a].replace('Ñ','N')
    df_nombres['deudor'][a]=df_nombres['deudor'][a].replace('Í','I')
    df_nombres['deudor'][a]=df_nombres['deudor'][a].replace('Ó','O')
    df_nombres['deudor'][a]=df_nombres['deudor'][a].replace(' LABORAL','L')
    df_nombres['deudor'][a]=df_nombres['deudor'][a].replace('&','Y')
    df_nombres['deudor'][a]=df_nombres['deudor'][a].replace(' AND ','Y')
    df_nombres['deudor'][a]=df_nombres['deudor'][a].replace('<D1>','N')
    df_nombres['deudor'][a]=df_nombres['deudor'][a].replace(' UNIPERSONAL','U')
    df_nombres['deudor'][a]=df_nombres['deudor'][a].replace(' PROFESIONAL','P')
    df_nombres['deudor'][a]=df_nombres['deudor'][a].replace('-',' ')
    df_nombres['deudor'][a]=df_nombres['deudor'][a].replace('Y',' Y ')
    df_nombres['deudor'][a]=df_nombres['deudor'][a].replace('S L','SL')
    df_nombres['deudor'][a]=df_nombres['deudor'][a].replace('S C','SC')

df_nombres

# %%
nombres=[]
for a in df_nombres[['nombre','deudor']]:
    for b in df_nombres[a]:
       nombres.append(b.split())

# %%
palabras=[]
for a in nombres:
    for b in a:
        palabras.append(b)

# %%
palabras=pd.DataFrame(palabras)
palabras['contador']=1
palabras.rename(columns={0: 'palabras', 'contador': 'contador'}, inplace=True)

# %%
group_palabras=palabras.groupby(by='palabras').sum().sort_values(by='contador',ascending=False).reset_index()
group_palabras

# %%
import Levenshtein

# %%
def levendist(col1,col2):
    dfff=pd.DataFrame(col1)
    dfff['col2']=col2
    distancias=[]
    for a in dfff.index:
        var=dfff.loc[a,:]
        distancias.append(Levenshtein.distance(var[0].strip(),var[1].strip()))
    return distancias

# %%
for a in df_nombres.index:
    df_nombres.loc[a,'nombre']==df_nombres.loc[a,'nombre'].strip()
    df_nombres.loc[a,'deudor']==df_nombres.loc[a,'deudor'].strip()

# %%
distancias=levendist(df_nombres['nombre'],df_nombres['deudor'])
df_nombres['distancia']=distancias

# %%
extinguido_nombre=df_nombres['nombre'].str.contains('EXTINGUIDA')
liquidacion_nombre=df_nombres['nombre'].str.contains('EN LIQUIDACION')
SL_nombre=df_nombres['nombre'].str.contains('SL')
SA_nombre=df_nombres['nombre'].str.contains('SA')
SLU_nombre=df_nombres['nombre'].str.contains('SLU')
SLL_nombre=df_nombres['nombre'].str.contains('SLL')
extinguido_deudor=df_nombres['deudor'].str.contains('EXTINGUIDA')
liquidacion_deudor=df_nombres['deudor'].str.contains('EN LIQUIDACION')
SL_deudor=df_nombres['deudor'].str.contains('SL')
SA_deudor=df_nombres['deudor'].str.contains('SA')
SLU_deudor=df_nombres['deudor'].str.contains('SLU')
SLL_deudor=df_nombres['deudor'].str.contains('SLL')

# %%
df_nombres['extinguido_nombre']=extinguido_nombre
df_nombres['liquidacion_nombre']=liquidacion_nombre
df_nombres['extinguido_deudor']=extinguido_deudor
df_nombres['liquidacion_deudor']=liquidacion_deudor
df_nombres['SL_nombre']=SL_nombre
df_nombres['SA_nombre']=SA_nombre
df_nombres['SLU_nombre']=SLU_nombre
df_nombres['SLL_nombre']=SLL_nombre
df_nombres['SL_deudor']=SL_deudor
df_nombres['SA_deudor']=SA_deudor
df_nombres['SLU_deudor']=SLU_deudor
df_nombres['SLL_deudor']=SLL_deudor

# %%
df_nombres.drop_duplicates(subset='codigo_nif')

# %%
for a in df_nombres['nombre'].index:
    df_nombres['nombre'][a]=df_nombres['nombre'][a].replace('EXTINGUIDA','')
    df_nombres['nombre'][a]=df_nombres['nombre'][a].replace('EN LIQUIDACION','')
    df_nombres['nombre'][a]=df_nombres['nombre'][a].replace(' SL','')
    df_nombres['nombre'][a]=df_nombres['nombre'][a].replace(' SA','')
    df_nombres['nombre'][a]=df_nombres['nombre'][a].replace(' SLU','')
    df_nombres['nombre'][a]=df_nombres['nombre'][a].replace(' SLL','')
for a in df_nombres['deudor'].index:
    df_nombres['deudor'][a]=df_nombres['deudor'][a].replace('EXTINGUIDA','')
    df_nombres['deudor'][a]=df_nombres['deudor'][a].replace('EN LIQUIDACION','')
    df_nombres['deudor'][a]=df_nombres['deudor'][a].replace(' SL','')
    df_nombres['deudor'][a]=df_nombres['deudor'][a].replace(' SA','')
    df_nombres['deudor'][a]=df_nombres['deudor'][a].replace(' SLU','')
    df_nombres['deudor'][a]=df_nombres['deudor'][a].replace(' SLL','')

df_nombres

# %%
distancias2=levendist(df_nombres['nombre'],df_nombres['deudor'])
df_nombres['distancia_limpio']=distancias2

# %%
df_nombres.columns

# %%
df_nombres_final=df_nombres[['codigo_nif','nombre','deudor','distancia_limpio']].sort_values(by='distancia_limpio')

# %%
df_nombres_final=df_nombres_final.drop_duplicates()

# %%
length1=[]
for a in df_nombres_final['deudor']:
    length1.append(len(a))

length2=[]
for a in df_nombres_final['nombre']:
    length2.append(len(a))

# %%
df_nombres_final['len_deudor']=length1
df_nombres_final['len_nombre']=length2
df_nombres_final.drop_duplicates(subset='codigo_nif')

# %%
df_nombres_final[df_nombres_final['distancia_limpio']>0].sort_values(by='codigo_nif',ascending=False)

# %%
nif_dup=df_nombres_final.groupby(by='codigo_nif').count().reset_index()
nif_dup=nif_dup[nif_dup['nombre']>2]['codigo_nif']
nif_dup

# %%
df_nombres_final[df_nombres_final['codigo_nif']=='A01021708']

# %%
df_nombres_final.drop_duplicates(subset='codigo_nif')

# %%
df_nombres_final.drop_duplicates(subset='codigo_nif')

# %%
df_nombres_final.merge(nif_dup,how='right').drop_duplicates().head(20)

# %%
df_nombres.sort_values(by='distancia_limpio',ascending=False).head(20)
df_nombres.groupby(by='distancia_limpio').count().reset_index().iloc[:,3]

# %%
df_nombres_final['codigo_nif'].drop_duplicates()

# %%
df_nombres_final[df_nombres_final['len_deudor']<df_nombres_final['distancia_limpio']*3/2].sort_values(by='codigo_nif')

# %%
df_nombres_final['concurso_acreedores']=df_nombres_final['distancia_limpio']==0

# %%
nif_resueltos=df_nombres_final[df_nombres_final['concurso_acreedores']==True].drop_duplicates(subset='codigo_nif')['codigo_nif']

# %%
nif_resueltos

# %%
nif_sin_resolver=df_nombres_final.merge(nif_resueltos, indicator='i', how='outer').query('i == "left_only"').drop('i', 1)
nif_sin_resolver.drop_duplicates(subset='codigo_nif')

# %%
nif_sin_resolver[nif_sin_resolver['len_deudor']<nif_sin_resolver['distancia_limpio']].sort_values(by='codigo_nif').drop_duplicates()

# %%
nif_sin_resolver['concurso_acreedores']=nif_sin_resolver['distancia_limpio']+nif_sin_resolver['len_deudor']==nif_sin_resolver['len_nombre']
nif_resueltos2=nif_sin_resolver[nif_sin_resolver['concurso_acreedores']==True].drop_duplicates(subset='codigo_nif')['codigo_nif']


# %%
nif_sin_resolver['concurso_acreedores']=nif_sin_resolver['distancia_limpio']+nif_sin_resolver['len_nombre']==nif_sin_resolver['len_deudor']
nif_resueltos3=nif_sin_resolver[nif_sin_resolver['concurso_acreedores']==True].drop_duplicates(subset='codigo_nif')['codigo_nif']

# %%
nif_resueltos2

# %%
nif_resueltos=nif_resueltos.append(nif_resueltos2)
nif_resueltos=nif_resueltos.append(nif_resueltos3)
nif_resueltos=nif_resueltos.drop_duplicates()
nif_resueltos

# %%
nif_sin_resolver=df_nombres_final.merge(nif_resueltos, indicator='i', how='outer').query('i == "left_only"').drop('i', 1)
nif_sin_resolver.drop_duplicates(subset='codigo_nif')

# %%
nif_sin_resolver[nif_sin_resolver['distancia_limpio']<6]

# %%
nif_sin_resolver['concurso_acreedores']=nif_sin_resolver['distancia_limpio']<6
nif_resueltos4=nif_sin_resolver[nif_sin_resolver['concurso_acreedores']==True].drop_duplicates(subset='codigo_nif')['codigo_nif']
nif_sin_resolver['concurso_acreedores']


# %%
nif_resueltos4

# %%
nif_resueltos=nif_resueltos.append(nif_resueltos4)
nif_resueltos=nif_resueltos.drop_duplicates()
nif_resueltos

# %%
nif_sin_resolver=df_nombres_final.merge(nif_resueltos, indicator='i', how='outer').query('i == "left_only"').drop('i', 1)
nif_sin_resolver.drop_duplicates(subset='codigo_nif')

# %%
nif_sin_resolver[nif_sin_resolver['distancia_limpio']>(nif_sin_resolver['len_deudor']+nif_sin_resolver['len_nombre'])/2].drop_duplicates(subset='codigo_nif')

# %%
nif_resueltos=pd.DataFrame(nif_resueltos)
nif_resueltos['concurso_acreedores']=True

# %%
nif_resueltos

# %%
nif_sin_resolver['concurso_acreedores']=nif_sin_resolver['distancia_limpio']>(nif_sin_resolver['len_deudor']+nif_sin_resolver['len_nombre'])/2
nif_resueltos5=nif_sin_resolver[nif_sin_resolver['concurso_acreedores']==True].drop_duplicates(subset='codigo_nif')['codigo_nif']
nif_resueltos5=pd.DataFrame(nif_resueltos5)
nif_resueltos5['concurso_acreedores']=False

# %%
nif_resueltos=nif_resueltos.append(nif_resueltos5)
nif_resueltos=nif_resueltos.drop_duplicates()

# %%
nif_sin_resolver=df_nombres_final.merge(nif_resueltos, indicator='i', how='outer',on='codigo_nif').query('i == "left_only"').drop('i', 1)
nif_sin_resolver.drop_duplicates(subset='codigo_nif')

# %%
nif_sin_resolver[(nif_sin_resolver['len_deudor']+nif_sin_resolver['distancia_limpio']-nif_sin_resolver['len_nombre'])<4]

# %%
nif_sin_resolver[(nif_sin_resolver['len_nombre']+nif_sin_resolver['distancia_limpio']-nif_sin_resolver['len_deudor'])<3]

# %%
nif_sin_resolver['concurso_acreedores']=(nif_sin_resolver['len_deudor']+nif_sin_resolver['distancia_limpio']-nif_sin_resolver['len_nombre'])<4
nif_resueltos6=nif_sin_resolver[nif_sin_resolver['concurso_acreedores']==True].drop_duplicates(subset='codigo_nif')['codigo_nif']
nif_resueltos6=pd.DataFrame(nif_resueltos6)
nif_resueltos6['concurso_acreedores']=True
nif_resueltos6

# %%
nif_sin_resolver['concurso_acreedores']=(nif_sin_resolver['len_nombre']+nif_sin_resolver['distancia_limpio']-nif_sin_resolver['len_deudor'])<3
nif_resueltos7=nif_sin_resolver[nif_sin_resolver['concurso_acreedores']==True].drop_duplicates(subset='codigo_nif')['codigo_nif']
nif_resueltos7=pd.DataFrame(nif_resueltos7)
nif_resueltos7['concurso_acreedores']=True
nif_resueltos7

# %%
nif_resueltos=nif_resueltos.append(nif_resueltos6)
nif_resueltos=nif_resueltos.append(nif_resueltos7)
nif_resueltos=nif_resueltos.drop_duplicates()
nif_resueltos

# %%
nif_sin_resolver=df_nombres_final.merge(nif_resueltos, indicator='i', how='outer',on='codigo_nif').query('i == "left_only"').drop('i', 1)
nif_sin_resolver.drop_duplicates(subset='codigo_nif').sort_values(by='deudor')

# %%
nif_sin_resolver['concurso_acreedores']=True
nif_resueltos8=nif_sin_resolver[nif_sin_resolver['concurso_acreedores']==True].drop_duplicates(subset='codigo_nif')['codigo_nif']
nif_resueltos8=pd.DataFrame(nif_resueltos8)
nif_resueltos8['concurso_acreedores']=False
nif_resueltos8

# %%
nif_resueltos=nif_resueltos.append(nif_resueltos8)
nif_resueltos=nif_resueltos.drop_duplicates()
nif_resueltos['concurso_acreedores'].value_counts()

# %%
nif_resueltos

# %%
df_nombres

# %%
df_nombres=df_nombres.merge(nif_resueltos,on='codigo_nif')

# %%
df_nombres

# %%
#Terminados

# %%
df

# %%
fechas=df2[['nif','fecha_resolucion']]
fechas.rename(columns={'nif': 'codigo_nif'}, inplace=True)
fechas=fechas.drop_duplicates()
fechas

# %%
df_nombres=df_nombres.drop_duplicates(subset='codigo_nif')
df_nombres

# %%
df_nombres2=df_nombres.merge(fechas,how='left',on='codigo_nif')

# %%
df_nombres2 = df_nombres2[pd.isna(df_nombres2['fecha_resolucion'])==False]

# %%
df_nombres2['fecha_resolucion'][df_nombres2['fecha_resolucion']=='- - -']=np.nan

# %%
df_nombres2 = df_nombres2[pd.isna(df_nombres2['fecha_resolucion'])==False]

# %%
df_nombres2['fecha_resolucion']

# %%
df_nombres2['fecha_resolucion']=df_nombres2['fecha_resolucion'].astype(str)

# %%
df_nombres2['fecha_resolucion'].isna().sum().sum()

# %%
df_nombres2['fecha_resolucion']

# %%
df_nombres2['fecha_resolucion'][20]

# %%
range(len(df_nombres2['fecha_resolucion']))

# %%
df_nombres2=df_nombres2.reset_index()

# %%
for a in range(len(df_nombres2['fecha_resolucion'])):
    df_nombres2['fecha_resolucion'][a]=df_nombres2['fecha_resolucion'][a].replace('- ','-')

# %%
for a in range(len(df_nombres2['fecha_resolucion'])):
    df_nombres2['fecha_resolucion'][a]=str(df_nombres2['fecha_resolucion'][a])

# %%
a=str(df_nombres2['fecha_resolucion'])

# %%
df_nombres2['fecha_resolucion']=df_nombres2['fecha_resolucion'].astype("string")

# %%
df_nombres2['fecha_resolucion']

# %%
df_nombres2['fecha_resolucion']=pd.to_datetime(df_nombres2['fecha_resolucion'], errors = 'coerce')

# %%
df_nombres2=df_nombres2.sort_values(by=['codigo_nif','fecha_resolucion'])

# %%
df_nombres2=df_nombres2.drop_duplicates(subset='codigo_nif',keep='first')

# %%
df2.shape

# %%
df.shape

# %%
df_nombres.merge(df_nombres2[['codigo_nif','fecha_resolucion']],how='left',on='codigo_nif')

# %%
df_nombres3=df_nombres.merge(df_nombres2[['codigo_nif','fecha_resolucion']],how='left',on='codigo_nif')

# %%
df_nombres3

# %%
df_final_interesante=df.merge(df_nombres3.drop(['nombre'], axis=1),on='codigo_nif',how='left')

# %%
df_final_interesante

# %%
#df_final_interesante.to_csv('df_sucio_con_deudores.csv',sep=';')


