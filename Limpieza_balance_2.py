# %%
import pandas as pd
import numpy as np
import datetime as dt

# %%
df_final_interesante=pd.read_csv('Datos transformados/df_sucio_con_deudores.csv',sep=';')

# %%
df_final_interesante.columns
df_final_interesante=df_final_interesante.drop(['Unnamed: 0'], axis=1)

# %%
df_final_interesante.shape

# %%
##balance

# %%
def balance(df, columna1, columna2):
    columna1=[columna1]
    columna=[]
    columna.append(columna1)
    columna.append(columna2)
    columnas=[]
    for a in columna:
        for b in a:
            columnas.append(b)
    for index, row in df[columnas].iterrows():
        if pd.isna(row[columnas]).sum().sum() ==1:
            if pd.isna(row[columna1][0]):
                df.loc[index,columna1]=df.loc[index,columna2].sum()
            if pd.isna(row[columna2]).sum().sum() ==1:
                row2=pd.DataFrame(row[columna2]).isnull().sum(axis = 1)
                for num in range(len(columna2)) :
                    if row2[num]!=0:
                        columna3=columna2.copy()
                        columna3.remove(row2.index[num])
                        df.loc[index,[row2.index[num]]]=df.loc[index,columna1].sum()-df.loc[index,columna3].sum() 

# %%
na_cols=df_final_interesante[['rentabilidad_sobre_recursos_propios_percent_percent','rentabilidad_sobre_el_activo_total_percent_percent','total_pasivo_y_capital_propio_mil_eur','pasivo_liquido_mil_eur','pasivo_fijo_mil_eur','fondos_propios_mil_eur','total_activo_mil_eur','activo_circulante_mil_eur','inmovilizado_mil_eur']].isnull().sum(axis = 0)
na_cols=pd.DataFrame(na_cols)
na_cols=na_cols.reset_index()
na_cols.rename(columns={'index': 'Variable', 0: 'Nas'}, inplace=True)
na_cols['Porcentaje Nas']=na_cols['Nas']/len(df_final_interesante[na_cols['Variable']])*100
na_cols=na_cols.sort_values(by='Porcentaje Nas',ascending=False)
na_cols[na_cols['Porcentaje Nas']!=0].head(20)

# %%
df_sinna=df_final_interesante.iloc[:,14:85]

# %%
df_sinna

# %%
na_cols=df_sinna.isnull().sum(axis = 1)
na_cols=pd.DataFrame(na_cols)
na_cols=na_cols.reset_index()
na_cols.rename(columns={'index': 'Variable', 0: 'Nas'}, inplace=True)
na_rows=na_cols[na_cols['Nas']==70]

# %%
na_rows

# %%
na_rows['Variable']

# %%
df_final=df_final_interesante.drop(na_rows['Variable'])

# %%
df_final

# %%
na_cols=df_final.isnull().sum(axis = 0)
na_cols=pd.DataFrame(na_cols)
na_cols=na_cols.reset_index()
na_cols.rename(columns={'index': 'Variable', 0: 'Nas'}, inplace=True)
na_cols['Porcentaje Nas']=na_cols['Nas']/len(df_final_interesante[na_cols['Variable']])*100
na_cols=na_cols.sort_values(by='Porcentaje Nas',ascending=False)
na_cols[na_cols['Porcentaje Nas']!=0].head(20)

# %%
balance(df_final,'inmovilizado_mil_eur',['inmovilizado_material_mil_eur','inmovilizado_inmaterial_mil_eur','otros_activos_fijos_mil_eur'])

# %%
balance(df_final,'activo_circulante_mil_eur',['deudores_mil_eur','existencias_mil_eur','otros_activos_liquidos_mil_eur'])

# %%
balance(df_final,'total_activo_mil_eur',['inmovilizado_mil_eur','activo_circulante_mil_eur'])

# %%
balance(df_final,'fondos_propios_mil_eur',['capital_suscrito_mil_eur','otros_fondos_propios_mil_eur'])

# %%
balance(df_final,'pasivo_fijo_mil_eur',['acreedores_a_l_p_mil_eur','otros_pasivos_fijos_mil_eur'])

# %%
balance(df_final,'pasivo_liquido_mil_eur',['acreedores_comerciales_mil_eur','deudas_financieras_mil_eur','otros_pasivos_liquidos_mil_eur'])

# %%
balance(df_final,'total_pasivo_y_capital_propio_mil_eur',['fondos_propios_mil_eur','pasivo_fijo_mil_eur','pasivo_liquido_mil_eur'])

# %%
# df_final.to_csv('df_sucio_con_deudores_sinna_balance.csv',sep=';')

# %%
df_final=df_final.reset_index()

# %%
indexpas=df_final[df_final['total_activo_mil_eur']==df_final['fondos_propios_mil_eur']][['total_activo_mil_eur','fondos_propios_mil_eur']]

# %%
indexpas=pd.DataFrame(indexpas.reset_index())

# %%
indexpas

# %%
na_cols=df_final[['rentabilidad_sobre_recursos_propios_percent_percent','rentabilidad_sobre_el_activo_total_percent_percent','total_pasivo_y_capital_propio_mil_eur','pasivo_liquido_mil_eur','pasivo_fijo_mil_eur','fondos_propios_mil_eur','total_activo_mil_eur','activo_circulante_mil_eur','inmovilizado_mil_eur']].isnull().sum(axis = 0)
na_cols=pd.DataFrame(na_cols)
na_cols=na_cols.reset_index()
na_cols.rename(columns={'index': 'Variable', 0: 'Nas'}, inplace=True)
na_cols['Porcentaje Nas']=na_cols['Nas']/len(df_final_interesante[na_cols['Variable']])*100
na_cols=na_cols.sort_values(by='Porcentaje Nas',ascending=False)
na_cols[na_cols['Porcentaje Nas']!=0].head(20)

# %%
df_final.loc[indexpas['index'],['pasivo_liquido_mil_eur','pasivo_fijo_mil_eur']]=0

# %%
df_final.iloc[indexpas['index'],:][['pasivo_liquido_mil_eur','pasivo_fijo_mil_eur']]

# %%
na_cols=df_final[['rentabilidad_sobre_recursos_propios_percent_percent','rentabilidad_sobre_el_activo_total_percent_percent','total_pasivo_y_capital_propio_mil_eur','pasivo_liquido_mil_eur','pasivo_fijo_mil_eur','fondos_propios_mil_eur','total_activo_mil_eur','activo_circulante_mil_eur','inmovilizado_mil_eur']].isnull().sum(axis = 0)
na_cols=pd.DataFrame(na_cols)
na_cols=na_cols.reset_index()
na_cols.rename(columns={'index': 'Variable', 0: 'Nas'}, inplace=True)
na_cols['Porcentaje Nas']=na_cols['Nas']/len(df_final_interesante[na_cols['Variable']])*100
na_cols=na_cols.sort_values(by='Porcentaje Nas',ascending=False)
na_cols[na_cols['Porcentaje Nas']!=0].head(20)

# %%
df_final[pd.isna(df_final['rentabilidad_sobre_recursos_propios_percent_percent'])==True]

# %%
df_final[pd.isna(df_final['rentabilidad_sobre_el_activo_total_percent_percent'])==True]

# %%
df_final[pd.isna(df_final['pasivo_liquido_mil_eur'])==True]

# %%
df_final[pd.isna(df_final['pasivo_fijo_mil_eur'])==True]

# %%
df_final[pd.isna(df_final['activo_circulante_mil_eur'])==True]

# %%
df_final[pd.isna(df_final['inmovilizado_mil_eur'])==True]

# %%
#df_final.to_csv('df_deudores_sinna_balance.csv',sep=';')


