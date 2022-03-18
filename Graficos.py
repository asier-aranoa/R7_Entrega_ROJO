# %%
import pandas as pd
import matplotlib.pyplot as plt

# %%
df = pd.read_csv('Datos transformados/df_modelo_limpio.csv',sep=",")
df.head()

# %%
df = df[df['anyo'] != 'ult_ano_disp']

# %%
df['anyo'].unique()

# %% [markdown]
# ### EMPRESAS QUE HAN ENTRADO EN CONCURSO

# %%
concurso = df[df['concurso_acreedores'] == True]
#concurso['nombre'].sample(n=4)
empresas = ['HARINSA NAVASFALT SA (EN LIQUIDACION)','RESTAURANTE YANDIOLA SL  (EXTINGUIDA)',"BIDEBIDE 2010 SL (EXTINGUIDA)",'ENGINEERING AND MANUFACTURING TECHNOLOGIES SL. (EN LIQUIDACION)']
df_cuatro_empresas = df[df['nombre'].isin(empresas)]

# %%
empresa1 = df_cuatro_empresas[df_cuatro_empresas['nombre'] =='HARINSA NAVASFALT SA (EN LIQUIDACION)']
empresa2 = df_cuatro_empresas[df_cuatro_empresas['nombre'] =='RESTAURANTE YANDIOLA SL  (EXTINGUIDA)']
empresa3 = df_cuatro_empresas[df_cuatro_empresas['nombre'] =='BIDEBIDE 2010 SL (EXTINGUIDA)']
empresa4 = df_cuatro_empresas[df_cuatro_empresas['nombre']=='ENGINEERING AND MANUFACTURING TECHNOLOGIES SL. (EN LIQUIDACION)']

# %%
empresa1.columns

# %%
#EMPRESA1

fig1,ax1 = plt.subplots(3,2)



ax1[0,0].plot(empresa1["anyo"],empresa1["Ratio_de_deuda"],color = 'red')
ax1[0,1].plot(empresa1["anyo"],empresa1["Fondo_de_maniobra"],color='red')
ax1[1,0].plot(empresa1["anyo"],empresa1["Ratio_de_liquidez"],color='red')
ax1[1,1].plot(empresa1["anyo"],empresa1["Ratio_de_apalancamiento_financiero"],color='red')
ax1[2,1].plot(empresa1["anyo"],empresa1["ROA_(Rentabilidad_Económica)"],color='red')
ax1[2,0].plot(empresa1["anyo"],empresa1["ROE_(Rentabilidad_Financiera)"],color='red')


ax1[0,0].fill_between(empresa1["anyo"],empresa1["Ratio_de_deuda"],alpha=0.2,color = 'red')
ax1[0,1].fill_between(empresa1["anyo"],empresa1["Fondo_de_maniobra"],alpha=0.2,color='red')
ax1[1,0].fill_between(empresa1["anyo"],empresa1["Ratio_de_liquidez"],alpha=0.2,color='red')
ax1[1,1].fill_between(empresa1["anyo"],empresa1["Ratio_de_apalancamiento_financiero"],alpha=0.2,color='red')
ax1[2,1].fill_between(empresa1["anyo"],empresa1["ROA_(Rentabilidad_Económica)"],alpha=0.2,color='red')
ax1[2,0].fill_between(empresa1["anyo"],empresa1["ROE_(Rentabilidad_Financiera)"],alpha=0.2,color='red')


ax1[0,0].set_title('Ratio de deuda',size =30)
ax1[0,1].set_title('Fondo de maniobra',size =30)
ax1[1,0].set_title('Ratio de liquidez',size =30)
ax1[1,1].set_title('Ratio de apalancamiento financiero',size =30)
ax1[2,1].set_title('ROA',size =30)
ax1[2,0].set_title('ROE',size =30)

fig1.set_size_inches(30,15)
fig1.set_dpi(130)

# %%
#EMPRESA2

fig2,ax2 = plt.subplots(3,2)

ax2[0,0].plot(empresa2["anyo"],empresa2["Ratio_de_deuda"],color = 'blue')
ax2[0,1].plot(empresa2["anyo"],empresa2["Fondo_de_maniobra"],color='blue')
ax2[1,0].plot(empresa2["anyo"],empresa2["Ratio_de_liquidez"],color='blue')
ax2[1,1].plot(empresa2["anyo"],empresa2["Ratio_de_apalancamiento_financiero"],color='blue')
ax2[2,1].plot(empresa2["anyo"],empresa2["ROA_(Rentabilidad_Económica)"],color='blue')
ax2[2,0].plot(empresa2["anyo"],empresa2["ROE_(Rentabilidad_Financiera)"],color='blue')


ax2[0,0].fill_between(empresa2["anyo"],empresa2["Ratio_de_deuda"],alpha=0.2,color = 'blue')
ax2[0,1].fill_between(empresa2["anyo"],empresa2["Fondo_de_maniobra"],alpha=0.2,color='blue')
ax2[1,0].fill_between(empresa2["anyo"],empresa2["Ratio_de_liquidez"],alpha=0.2,color='blue')
ax2[1,1].fill_between(empresa2["anyo"],empresa2["Ratio_de_apalancamiento_financiero"],alpha=0.2,color='blue')
ax2[2,1].fill_between(empresa2["anyo"],empresa2["ROA_(Rentabilidad_Económica)"],alpha=0.2,color='blue')
ax2[2,0].fill_between(empresa2["anyo"],empresa2["ROE_(Rentabilidad_Financiera)"],alpha=0.2,color='blue')


ax2[0,0].set_title('Ratio de deuda',size =30)
ax2[0,1].set_title('Fondo de maniobra',size =30)
ax2[1,0].set_title('Ratio de liquidez',size =30)
ax2[1,1].set_title('Ratio de apalancamiento financiero',size =30)
ax2[2,1].set_title('ROA',size =30)
ax2[2,0].set_title('ROE',size =30)

fig2.set_size_inches(30,15)
fig2.set_dpi(130)


# %%
#EMPRESA3

fig3,ax3 = plt.subplots(3,2)

ax3[0,0].plot(empresa3["anyo"],empresa3["Ratio_de_deuda"],color = 'green')
ax3[0,1].plot(empresa3["anyo"],empresa3["Fondo_de_maniobra"],color='green')
ax3[1,0].plot(empresa3["anyo"],empresa3["Ratio_de_liquidez"],color='green')
ax3[1,1].plot(empresa3["anyo"],empresa3["Ratio_de_apalancamiento_financiero"],color='green')
ax3[2,1].plot(empresa3["anyo"],empresa3["ROA_(Rentabilidad_Económica)"],color='green')
ax3[2,0].plot(empresa3["anyo"],empresa3["ROE_(Rentabilidad_Financiera)"],color='green')


ax3[0,0].fill_between(empresa3["anyo"],empresa3["Ratio_de_deuda"],alpha=0.2,color = 'green')
ax3[0,1].fill_between(empresa3["anyo"],empresa3["Fondo_de_maniobra"],alpha=0.2,color='green')
ax3[1,0].fill_between(empresa3["anyo"],empresa3["Ratio_de_liquidez"],alpha=0.2,color='green')
ax3[1,1].fill_between(empresa3["anyo"],empresa3["Ratio_de_apalancamiento_financiero"],alpha=0.2,color='green')
ax3[2,1].fill_between(empresa3["anyo"],empresa3["ROA_(Rentabilidad_Económica)"],alpha=0.2,color='green')
ax3[2,0].fill_between(empresa3["anyo"],empresa3["ROE_(Rentabilidad_Financiera)"],alpha=0.2,color='green')


ax3[0,0].set_title('Ratio de deuda',size =30)
ax3[0,1].set_title('Fondo de maniobra',size =30)
ax3[1,0].set_title('Ratio de liquidez',size =30)
ax3[1,1].set_title('Ratio de apalancamiento financiero',size =30)
ax3[2,1].set_title('ROA',size =30)
ax3[2,0].set_title('ROE',size =30)

fig3.set_size_inches(30,15)
fig3.set_dpi(130)

# %%
#EMPRESA4

fig4,ax4 = plt.subplots(3,2)

ax4[0,0].plot(empresa4["anyo"],empresa4["Ratio_de_deuda"],color = 'orange')
ax4[0,1].plot(empresa4["anyo"],empresa4["Fondo_de_maniobra"],color='orange')
ax4[1,0].plot(empresa4["anyo"],empresa4["Ratio_de_liquidez"],color='orange')
ax4[1,1].plot(empresa4["anyo"],empresa4["Ratio_de_apalancamiento_financiero"],color='orange')
ax4[2,1].plot(empresa4["anyo"],empresa4["ROA_(Rentabilidad_Económica)"],color='orange')
ax4[2,0].plot(empresa4["anyo"],empresa4["ROE_(Rentabilidad_Financiera)"],color='orange')


ax4[0,0].fill_between(empresa4["anyo"],empresa4["Ratio_de_deuda"],alpha=0.2,color = 'orange')
ax4[0,1].fill_between(empresa4["anyo"],empresa4["Fondo_de_maniobra"],alpha=0.2,color='orange')
ax4[1,0].fill_between(empresa4["anyo"],empresa4["Ratio_de_liquidez"],alpha=0.2,color='orange')
ax4[1,1].fill_between(empresa4["anyo"],empresa4["Ratio_de_apalancamiento_financiero"],alpha=0.2,color='orange')
ax4[2,1].fill_between(empresa4["anyo"],empresa4["ROA_(Rentabilidad_Económica)"],alpha=0.2,color='orange')
ax4[2,0].fill_between(empresa4["anyo"],empresa4["ROE_(Rentabilidad_Financiera)"],alpha=0.2,color='orange')


ax4[0,0].set_title('Ratio de deuda',size =30)
ax4[0,1].set_title('Fondo de maniobra',size =30)
ax4[1,0].set_title('Ratio de liquidez',size =30)
ax4[1,1].set_title('Ratio de apalancamiento financiero',size =30)
ax4[2,1].set_title('ROA',size =30)
ax4[2,0].set_title('ROE',size =30)

fig4.set_size_inches(30,15)
fig4.set_dpi(130)

# %% [markdown]
# ### EMPRESAS QUE NO HAN ENTRADO EN CONCURSO

# %%
no_concurso = df[df['concurso_acreedores'] == False]
empresas_no_concurso = ['HARINSA NAVASFALT SA (EN LIQUIDACION)','RESTAURANTE YANDIOLA SL  (EXTINGUIDA)',"BIDEBIDE 2010 SL (EXTINGUIDA)",'ENGINEERING AND MANUFACTURING TECHNOLOGIES SL. (EN LIQUIDACION)']
df_cuatro_empresas = df[df['nombre'].isin(empresas)]

# %%


# %%
no_concurso = df[df['concurso_acreedores'] == False]
#no_concurso['nombre'].sample(n=4)
empresas_no_concurso = ['HOTEL YOLDI SL','INNOVALIGHT INVESTIGACION SL','BAR RESTAURANTE BARAZAR SL','ALMALUGA SERVICIOS HOSTELEROS SL']
df_cuatro_empresas_2 = df[df['nombre'].isin(empresas_no_concurso)]

# %%
empresa5 = df_cuatro_empresas_2[df_cuatro_empresas_2['nombre'] =='HOTEL YOLDI SL']
empresa6 = df_cuatro_empresas_2[df_cuatro_empresas_2['nombre'] =='INNOVALIGHT INVESTIGACION SL']
empresa7 = df_cuatro_empresas_2[df_cuatro_empresas_2['nombre'] =='BAR RESTAURANTE BARAZAR SL']
empresa8 = df_cuatro_empresas_2[df_cuatro_empresas_2['nombre']=='ALMALUGA SERVICIOS HOSTELEROS SL']

# %%
#EMPRESA5

fig5,ax5 = plt.subplots(3,2)



ax5[0,0].plot(empresa5["anyo"],empresa5["Ratio_de_deuda"],color = 'red')
ax5[0,1].plot(empresa5["anyo"],empresa5["Fondo_de_maniobra"],color='red')
ax5[1,0].plot(empresa5["anyo"],empresa5["Ratio_de_liquidez"],color='red')
ax5[1,1].plot(empresa5["anyo"],empresa5["Ratio_de_apalancamiento_financiero"],color='red')
ax5[2,1].plot(empresa5["anyo"],empresa5["ROA_(Rentabilidad_Económica)"],color='red')
ax5[2,0].plot(empresa5["anyo"],empresa5["ROE_(Rentabilidad_Financiera)"],color='red')


ax5[0,0].fill_between(empresa5["anyo"],empresa5["Ratio_de_deuda"],alpha=0.2,color = 'red')
ax5[0,1].fill_between(empresa5["anyo"],empresa5["Fondo_de_maniobra"],alpha=0.2,color='red')
ax5[1,0].fill_between(empresa5["anyo"],empresa5["Ratio_de_liquidez"],alpha=0.2,color='red')
ax5[1,1].fill_between(empresa5["anyo"],empresa5["Ratio_de_apalancamiento_financiero"],alpha=0.2,color='red')
ax5[2,1].fill_between(empresa5["anyo"],empresa5["ROA_(Rentabilidad_Económica)"],alpha=0.2,color='red')
ax5[2,0].fill_between(empresa5["anyo"],empresa5["ROE_(Rentabilidad_Financiera)"],alpha=0.2,color='red')


ax5[0,0].set_title('Ratio de deuda',size =30)
ax5[0,1].set_title('Fondo de maniobra',size =30)
ax5[1,0].set_title('Ratio de liquidez',size =30)
ax5[1,1].set_title('Ratio de apalancamiento financiero',size =30)
ax5[2,1].set_title('ROA',size =30)
ax5[2,0].set_title('ROE',size =30)

fig5.set_size_inches(30,15)
fig5.set_dpi(130)

# %%
#EMPRESA6

fig6,ax6 = plt.subplots(3,2)



ax6[0,0].plot(empresa6["anyo"],empresa6["Ratio_de_deuda"],color = 'blue')
ax6[0,1].plot(empresa6["anyo"],empresa6["Fondo_de_maniobra"],color='blue')
ax6[1,0].plot(empresa6["anyo"],empresa6["Ratio_de_liquidez"],color='blue')
ax6[1,1].plot(empresa6["anyo"],empresa6["Ratio_de_apalancamiento_financiero"],color='blue')
ax6[2,1].plot(empresa6["anyo"],empresa6["ROA_(Rentabilidad_Económica)"],color='blue')
ax6[2,0].plot(empresa6["anyo"],empresa6["ROE_(Rentabilidad_Financiera)"],color='blue')


ax6[0,0].fill_between(empresa6["anyo"],empresa6["Ratio_de_deuda"],alpha=0.2,color = 'blue')
ax6[0,1].fill_between(empresa6["anyo"],empresa6["Fondo_de_maniobra"],alpha=0.2,color='blue')
ax6[1,0].fill_between(empresa6["anyo"],empresa6["Ratio_de_liquidez"],alpha=0.2,color='blue')
ax6[1,1].fill_between(empresa6["anyo"],empresa6["Ratio_de_apalancamiento_financiero"],alpha=0.2,color='blue')
ax6[2,1].fill_between(empresa6["anyo"],empresa6["ROA_(Rentabilidad_Económica)"],alpha=0.2,color='blue')
ax6[2,0].fill_between(empresa6["anyo"],empresa6["ROE_(Rentabilidad_Financiera)"],alpha=0.2,color='blue')


ax6[0,0].set_title('Ratio de deuda',size =30)
ax6[0,1].set_title('Fondo de maniobra',size =30)
ax6[1,0].set_title('Ratio de liquidez',size =30)
ax6[1,1].set_title('Ratio de apalancamiento financiero',size =30)
ax6[2,1].set_title('ROA',size =30)
ax6[2,0].set_title('ROE',size =30)

fig6.set_size_inches(30,15)
fig6.set_dpi(130)

# %%
#EMPRESA7

fig7,ax7 = plt.subplots(3,2)



ax7[0,0].plot(empresa7["anyo"],empresa7["Ratio_de_deuda"],color = 'green')
ax7[0,1].plot(empresa7["anyo"],empresa7["Fondo_de_maniobra"],color='green')
ax7[1,0].plot(empresa7["anyo"],empresa7["Ratio_de_liquidez"],color='green')
ax7[1,1].plot(empresa7["anyo"],empresa7["Ratio_de_apalancamiento_financiero"],color='green')
ax7[2,1].plot(empresa7["anyo"],empresa7["ROA_(Rentabilidad_Económica)"],color='green')
ax7[2,0].plot(empresa7["anyo"],empresa7["ROE_(Rentabilidad_Financiera)"],color='green')


ax7[0,0].fill_between(empresa7["anyo"],empresa7["Ratio_de_deuda"],alpha=0.2,color = 'green')
ax7[0,1].fill_between(empresa7["anyo"],empresa7["Fondo_de_maniobra"],alpha=0.2,color='green')
ax7[1,0].fill_between(empresa7["anyo"],empresa7["Ratio_de_liquidez"],alpha=0.2,color='green')
ax7[1,1].fill_between(empresa7["anyo"],empresa7["Ratio_de_apalancamiento_financiero"],alpha=0.2,color='green')
ax7[2,1].fill_between(empresa7["anyo"],empresa7["ROA_(Rentabilidad_Económica)"],alpha=0.2,color='green')
ax7[2,0].fill_between(empresa7["anyo"],empresa7["ROE_(Rentabilidad_Financiera)"],alpha=0.2,color='green')


ax7[0,0].set_title('Ratio de deuda',size =30)
ax7[0,1].set_title('Fondo de maniobra',size =30)
ax7[1,0].set_title('Ratio de liquidez',size =30)
ax7[1,1].set_title('Ratio de apalancamiento financiero',size =30)
ax7[2,1].set_title('ROA',size =30)
ax7[2,0].set_title('ROE',size =30)

fig7.set_size_inches(30,15)
fig7.set_dpi(130)

# %%
#EMPRESA8

fig8,ax8 = plt.subplots(3,2)

ax8[0,0].plot(empresa8["anyo"],empresa8["Ratio_de_deuda"],color = 'orange')
ax8[0,1].plot(empresa8["anyo"],empresa8["Fondo_de_maniobra"],color='orange')
ax8[1,0].plot(empresa8["anyo"],empresa8["Ratio_de_liquidez"],color='orange')
ax8[1,1].plot(empresa8["anyo"],empresa8["Ratio_de_apalancamiento_financiero"],color='orange')
ax8[2,1].plot(empresa8["anyo"],empresa8["ROA_(Rentabilidad_Económica)"],color='orange')
ax8[2,0].plot(empresa8["anyo"],empresa8["ROE_(Rentabilidad_Financiera)"],color='orange')


ax8[0,0].fill_between(empresa8["anyo"],empresa8["Ratio_de_deuda"],alpha=0.2,color = 'orange')
ax8[0,1].fill_between(empresa8["anyo"],empresa8["Fondo_de_maniobra"],alpha=0.2,color='orange')
ax8[1,0].fill_between(empresa8["anyo"],empresa8["Ratio_de_liquidez"],alpha=0.2,color='orange')
ax8[1,1].fill_between(empresa8["anyo"],empresa8["Ratio_de_apalancamiento_financiero"],alpha=0.2,color='orange')
ax8[2,1].fill_between(empresa8["anyo"],empresa8["ROA_(Rentabilidad_Económica)"],alpha=0.2,color='orange')
ax8[2,0].fill_between(empresa8["anyo"],empresa8["ROE_(Rentabilidad_Financiera)"],alpha=0.2,color='orange')


ax8[0,0].set_title('Ratio de deuda',size =30)
ax8[0,1].set_title('Fondo de maniobra',size =30)
ax8[1,0].set_title('Ratio de liquidez',size =30)
ax8[1,1].set_title('Ratio de apalancamiento financiero',size =30)
ax8[2,1].set_title('ROA',size =30)
ax8[2,0].set_title('ROE',size =30)

fig8.set_size_inches(30,15)
fig8.set_dpi(130)


