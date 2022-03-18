# %%
# Importamos librerías Dash.
import jupyter_dash as dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

# Importamos Plotly Express para realizar graficos.
import plotly.express as px

# Importamos Pandas para cargar y tratar datos.
import pandas as pd
import numpy as np

# %%
df = pd.read_csv("Datos transformados/df_deudores_sinna_balance.csv", sep = ';')
#df = round(df,2)
df.head()

# %%
df2 = pd.read_csv("Datos transformados/df_modelo_limpio2.csv", sep = ',')
#df2 = round(df2,0)
df2.head()

# %%
# Creación de la aplicación
external_stylesheets = [
    "https://codepen.io/chriddyp/pen/bWLwgP.css"
]

# Creamos la aplicacion Dash y especificamos CSS
tabs_styles = {
    'height': '44px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px'
}

markdown_text = """
######
"""
markdown= """
##### **2. Página: ¡Más gráficos descriptivos!**
"""
markdown2= """
##### **3. Página: ¡Gráficos de los ratios utilizados!**
"""

# Creamos la aplicacion Dash y especificamos CSS.
app = dash.JupyterDash(
    __name__, 
    external_stylesheets = external_stylesheets
)

app.layout = html.Div(
    children = [
        html.Div(
            className = "row",
            children = [
                html.H1(
                    children = "Elkargi",
                    style = {
                        "textAlign": "center"
                    }
                ),
                html.H4(
                    children = "Visualización de los datos del Reto 7 mediante aplicación Dash",
                    style = {
                        "textAlign": "center"
                    }
                )
            ],
        ),
        dcc.Tabs([
            dcc.Tab(
                label = "Gráficos descriptivos",
                style =tab_style,
                selected_style=tab_selected_style,
                children = [
                    html.Div(
                        className = "row",
                        children = [
                            html.H5("Primero haremos visualizaciones de los datos iniciales"),
                            dcc.Markdown(children = markdown_text),
                            dcc.Markdown(id = "primero")
                        ]
                    ),
                    html.Div(
                        className = "row",
                        children = [
                            html.Div(
                                children = [
                                    html.H6("Estado"),
                                    dcc.Dropdown(
                                        id = "segundo",
                                        options = [{
                                            "label": str(name),
                                            "value": name
                                        } for name  in list(np.sort(df["estado"].unique()))],
                                        value = [],
                                        placeholder = "Selecciona el estado:",
                                        multi = True
                                    ),
                                    html.H6("Sector"),
                                    dcc.Dropdown(
                                        id = "cuarto",
                                        options = [{
                                            "label": str(name),
                                            "value": name
                                        } for name  in list(np.sort(df["sector"].unique()))],
                                        value = [],
                                        placeholder = "Selecciona los sectores:",
                                        multi = True
                                    ),
                                ],
                                className = "twelve columns"
                            ),
                            html.Div(
                                children = [
                                    dcc.Graph(id = "quinto"),
                                ],
                                className = "ten columns"
                            ),
                            html.Div(
                                children = [
                                    dcc.Graph(id = "sexto")
                                ],
                                className = "ten columns"
                            )
                        ]
                    )
                ]
            ),
            dcc.Tab(
                label = "Más gráficos descriptivos",
                style =tab_style,
                selected_style=tab_selected_style,
                children = [
                    html.Div(
                        className = "row",
                        children = [
                            dcc.Markdown(children= markdown),
                            dcc.Markdown(id = "septimo")
                            
                        ]
                    ),
                    html.Div(
                        className = "row",
                        children = [
                            html.Div(
                                children = [
                                    html.H6("Sector"),
                                    dcc.Dropdown(
                                        id = "octavo",
                                        options = [{
                                            "label": str(name),
                                            "value": name
                                        } for name  in list(np.sort(df["sector"].unique()))],
                                        value = [],
                                        placeholder = "Selecciona el sector/es:",
                                        multi = True
                                    ),
                                
                                    html.H6("Rango de activo circulante:"),
                                    dcc.RangeSlider(
                                        id = "decimo",
                                        min = df["activo_circulante_mil_eur"].min(),
                                        max = 1000,
                                        step = 200,
                                        value = [df["activo_circulante_mil_eur"].min(), 1000]
                                    ),
                                ],
                                className = "two columns"
                            ),
                            html.Div(
                                children = [
                                    dcc.Graph(id = "once"),
                                ],
                                className = "five columns"
                            ),
                            html.Div(
                                children = [
                                    dcc.Graph(id = "doce")
                                ],
                                className = "five columns"
                            ),
                            html.Div(
                                children = [
                                    dcc.Graph(id = "trece")
                                ],
                                className = "twelve columns"
                            )
                        ]
                    )
                ]
            ),
            dcc.Tab(                         #################################################################################################################################################################################
                label = "Gráficos con los ratios",
                style =tab_style,
                selected_style=tab_selected_style,
                children = [
                    html.Div(
                        className = "row",
                        children = [
                            dcc.Markdown(children = markdown2),
                            dcc.Markdown(id = "catorce")
                            
                        ]
                    ),
                    html.Div(
                        className = "row",
                        children = [
                            html.Div(
                                children = [
                                    html.H4("¿Concurso acreedores?"),
                                    dcc.Dropdown(
                                        id = "quince",
                                        options = [{
                                            "label": str(name),
                                            "value": name
                                        } for name  in list(np.sort(df2["concurso_acreedores"].unique()))],
                                        value = [],
                                        placeholder = "Selecciona True = concurso de acreedores, False = NO concurso de acreedores:",
                                        multi = True
                                    ),
                                    html.H4("Rango del ROE:"),
                                    dcc.RangeSlider(
                                        id = "dieciseis",
                                        min = -2692134.411,
                                        max = 327947.137,
                                        step = 500000,
                                        value = [-2692134.411, 350000]
                                    ),
                                ],
                                className = "two columns"
                            ),
                            html.Div(
                                children = [
                                    dcc.Graph(id = "graf1"),
                                ],
                                className = "ten columns"
                            ),
                            html.Div(
                                children = [
                                    dcc.Graph(id = "graf2")
                                ],
                                className = "ten columns"
                            ),
                            html.Div(
                                children = [
                                    dcc.Graph(id = "graf3")
                                ],
                                className = "ten columns"
                            )
                        ]
                    )
                ] 
            )
        ])
    ]
)
#############################################################################################################################
@app.callback(
    Output(
        component_id = "quinto", 
        component_property = "figure"
    ),
    Output(
        component_id = "sexto", 
        component_property = "figure"
    ),
    
    Input(
        component_id = "segundo",
        component_property = "value"
    ),
    Input(
        component_id = "cuarto",
        component_property = "value"
    )
)
def update_figure(estado, sector):
    dff = df[df["estado"].isin(estado)]
    dff = dff[dff["sector"].isin(sector)]

    # Creamos la figura.
    fig1 = px.histogram(
        dff,
        x = "estado",
        color = "sector",
        labels = {
            "estado": "Estado",
            "sector": "Sector"
        }
    )
    # Actualizamos el layout.
    fig1.update_layout(
        title = "Histograma estado y sectores",
        xaxis_title = "Sector",
        yaxis_title = "Cantidad de empresas",
        bargap = 0.1
    )

    # Quesitos
    fig2 = px.pie(
    dff,
    values = "existencias_mil_eur", 
    names = "estado",
    hole = 0.5
    )

    fig2.update_layout(
        title = "Gráfico de tarta del porcentaje de existencias (miles de euros) por el estado",
        xaxis_title = "Porcentaje de existencias (miles de euros)"
    )

    # # Creamos la figura.
    # fig2 = px.histogram(
    #     dff,
    #     x = "existencias_mil_eur",
    #     color = "estado",
    #     labels = {
    #         "existencias_mil_eur": "existencias_mil_eur"
    #     }
    # )

    # # Actualizamos el layout.
    # fig2.update_layout(
    #     title = "Histograma gastos de personal y estado",
    #     xaxis_title = "existencias_mil_eur",
    #     yaxis_title = "----",
    #     bargap = 0.1
    # )

    return fig1, fig2


@app.callback(
    Output(
        component_id = "once", 
        component_property = "figure"
    ),
    Output(
        component_id = "doce", 
        component_property = "figure"
    ),
    Output(
        component_id = "trece", 
        component_property = "figure"
    ),
    Output(
        component_id = "septimo",
        component_property = "children"
    ),
    Input(
        component_id = "octavo",
        component_property = "value"
    ),
    
    Input(
        component_id = "decimo",
        component_property = "value"
    )
)

def update_figuree(sector, activo_circulante_mil_eur):
    dff1 = df[df["sector"].isin(sector)]
    dff1 = dff1[dff1["activo_circulante_mil_eur"].between(*activo_circulante_mil_eur)]

    # Figura scatter 
    df44 = df[df["capital_suscrito_mil_eur"] > 0]
    fig4 = px.scatter(
        df44,
        x = "capital_suscrito_mil_eur",
        y= "activo_circulante_mil_eur",
        size = "capital_suscrito_mil_eur",
        opacity= 0.9,
        color = "sector",
        labels = {
            "sector": "Sector",
            "activo_circulante_mil_eur": "Activo circulante (miles euros)"
        }
    )

    # Actualizamos el layout.
    fig4.update_layout(
        title = "Gráfico de dispersión del Capital Suscrito y Activo circulante",
        xaxis_title = "Capital suscrito (miles euros)",
        yaxis_title = "Activo circulante (miles euros)"
    )

    # Figura Scatter
    df55 = df[df["coste_medio_de_los_empleados_mil"] < 100]
    fig5 = px.histogram(
        df55,
        x = "coste_medio_de_los_empleados_mil",
        color = "sector",
        title = "Histograma del coste medio de los empleados por sectores"
    )

    # Actualizamos el layout.
    fig5.update_layout(
        xaxis_title = "Coste medio de los empleados (miles euros)",
        yaxis_title = "Cantidad"
    )

    # Creamos la figura.
    fig6 = px.histogram(
        dff1,
        x = "activo_circulante_mil_eur",
        color = "sector",
        labels = {
            "sector": "Sector",
            "activo_circulante_mil_eur": "Activo circulante (miles euros)"
        }
    )
    
    # Actualizamos el layout.
    fig6.update_layout(
        title = "Histogramas en relación al activo circulante (en miles de euros)",
        xaxis_title = "Activo circulante (miles euros)",
        yaxis_title = "Cantidad",
        xaxis_range = activo_circulante_mil_eur,
        bargap = 0.1
    )
    
     # Actualizamos el texto Markdown
    text_prices2 = """
    ###### (El **rango de activo circulante** está entre {0:.0f} y {1:.0f}.)
    """.format(*activo_circulante_mil_eur)

    return fig4, fig5, fig6, text_prices2
#########################################################################################################################################################################################################################################################################

@app.callback(
    Output(
        component_id = "graf1", 
        component_property = "figure"
    ),
    Output(
        component_id = "graf2", 
        component_property = "figure"
    ),
    Output(
        component_id = "graf3", 
        component_property = "figure"
    ),
    Output(
        component_id = "catorce",
        component_property = "children"
    ),
    Input(
        component_id = "quince",
        component_property = "value"
    ),
    
    Input(
        component_id = "dieciseis",
        component_property = "value"
    )
    
)

def update_figureee(concurso_acreedores, ROE):
    df3 = df2[df2["concurso_acreedores"].isin(concurso_acreedores)]
    df3 = df3[df3["ROE_(Rentabilidad_Financiera)"].between(*ROE)]

    # Line plot
    fig7 = px.line(df3, x='anyo', y="ROE_(Rentabilidad_Financiera)", color='sector')

    # Actualizamos el layout.
    fig7.update_layout(
        title = "Gráfico de línea del año y el ROE",
        xaxis_title = "Año",
        yaxis_title = "ROE", 
    )

    # Bar plot
    fig8 = px.bar(
    df3,
    x = "sector",
    y = "tesoreria_mil_eur",
    color= "sector",
    labels={"sector": "Sector",
    "tesoreria_mil_eur" : "Tesoreria (miles de euros)",
    "sector": "Sector"}
    )

    fig8.update_layout(
        title = "Gráfico de barras de la Tesoreria (miles de euros) por sectores",
        xaxis = {
            "dtick" : 1    #para poner las barras de una en una
            }
    )


     # Bar plot
    fig9 = px.bar(
    df3,
    x = "concurso_acreedores",
    y = "ROE_(Rentabilidad_Financiera)",
    color= "sector",
    labels={"sector": "Sector",
    "ROE_(Rentabilidad_Financiera)" : "ROE",
    "concurso_acreedores": "Concurso acreedores"}
    )

    fig9.update_layout(
        title = "Gráfico de barras del concurso de acreedores y el ROE",
        xaxis = {
            "dtick" : 1    #para poner las barras de una en una
            }
    )

    # # Grafico
    # fig9 = px.line(df3, x='concurso_acreedores', y="ROE_(Rentabilidad_Financiera)", color='sector')

    # # Actualizamos el layout.
    # fig9.update_layout(
    #     title = "Gráfico de línea del concurso de acreedores y el ROE",
    #     xaxis_title = "Concurso acreedores",
    #     yaxis_title = "ROE", 
    # )

    # # Quesitos
    # fig9 = px.pie(
    # df3,
    # values = "ultimo_ano_disponible", 
    # names = "localidad",
    # hole = 0.5
    # )

    # fig9.update_layout(
    #     title = "Gráfico de tarta del porcentaje de existencias (miles de euros) por la localidad",
    #     xaxis_title = "Porcentaje de ultimo_ano_disponible"
    # )

    # # Quesitos
    # fig9 = px.pie(
    # df3,
    # values = "Ratio_de_liquidez", 
    # names = "Ratio_de_liquidez",
    # hole = 0.5
    # )

    # fig9.update_layout(
    #     title = "Gráfico de tarta del Ratio de liquidez",
    #     xaxis_title = "Porcentaje de las diferentes opciones"
    # )
    
     # Actualizamos el texto Markdown
    text_prices3 = """
    ###### El **rango del ROE** está entre {0:.0f} y {1:.0f}.
    """.format(*ROE)

    return fig7, fig8, fig9, text_prices3 

# Solamente se ejecuta si ejecutamos este script directamente.
if __name__ == "__main__":
    app.run_server(mode = "external", debug = True)


