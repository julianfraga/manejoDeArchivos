from graph_imagen import *
from config import *

def plot_cruces(candidato,df_cruces,files, name, preguntasQueNoVan, callbackInputTarget, crucesDict = crucesDict,opcionesDePreguntasInicial='', reorder=True, codigo=""):
    filesCandidato = files

    orden_cruces = df_cruces['var'].unique().tolist()

    xaxisTitle = ''
    yaxisTitle = ''
    opciones = {'_6opc': 0, '_4opc': 1, '_5opc': 0, '_3opc': 1}
    cruces_graph_id = 'enhanced-graph-cruces-'+ name + candidato.replace(" ", '_')
    layout = go.Layout(
        xaxis={'title': 'x-axis', 'fixedrange': True, 'title_text': xaxisTitle, 'ticks': '',
               'showticklabels': False, 'visible': False},
        yaxis={'title': 'y-axis', 'fixedrange': True, 'title_text': yaxisTitle, 'ticks': '',
               'showticklabels': False, },
        barmode='stack', template="plotly_white")



    cruces_component = html.Div([
        dcc.Dropdown(
            id='selectCruce' + name + candidato,
            options=[{'label': crucesDict[i][0], 'value': i} for i in reorder_cruces(df_cruces['var'].unique(), orden_cruces)],
            placeholder='Seleccioná una pregunta para ver el cruce',
            clearable=False,
            searchable=False,
            optionHeight=50,
        ),
        dcc.Graph(
            figure=go.Figure(layout=layout),
            # style={'height': crucesHeight},
            id=cruces_graph_id
            ),
        ])


    @app.callback(
        Output(cruces_graph_id, 'figure'),
        [Input('selectCruce' + name + candidato, 'value'),
         Input(callbackInputTarget, 'value'),
         Input(f"selectOpciones_{codigo}", 'value'), ])
    def update_figure(selected_cruce, selected_target, selected_opciones):
        if selected_target != 'Todos':
            layout = go.Layout(
                xaxis={'title': 'x-axis', 'fixedrange': True, 'title_text': xaxisTitle, 'ticks': '',
                       'showticklabels': False},
                yaxis={'title': 'y-axis', 'fixedrange': True, 'title_text': yaxisTitle, 'ticks': '',
                       'showticklabels': False},
                barmode='stack',
                annotations=[{
                    'x': 0,
                    'y': -100,
                    'xref': 'x',
                    'yref': 'y',
                    'text': 'Por favor seleccione "Todos"<br>los targets para visualizar el cruce',
                    'showarrow': False,
                    'ax': 0,
                    'ay': -100,
                    'font': dict(size=25),
                }]
            )
            return {'data': [go.Bar()], 'layout': layout}
        if selected_opciones == '_2opc':
            layout = go.Layout(
                xaxis={'title': 'x-axis', 'fixedrange': True, 'title_text': xaxisTitle, 'ticks': '',
                       'showticklabels': False},
                yaxis={'title': 'y-axis', 'fixedrange': True, 'title_text': yaxisTitle, 'ticks': '',
                       'showticklabels': False},
                barmode='stack',
                annotations=[{
                    'x': 0,
                    'y': -100,
                    'xref': 'x',
                    'yref': 'y',
                    'text': 'Seleccioná 4 o 6 opciones<br>para visualizar el cruce',
                    'showarrow': False,
                    'ax': 0,
                    'ay': -100,
                    'font': dict(size=25),
                }]
            )
            return {'data': [go.Bar()], 'layout': layout}

        if selected_cruce:
            # Update dropdown dinamically
            if not opcionesDePreguntasInicial is None:
                df = pd.read_csv(filesCandidato[candidato][opciones[selected_opciones]])
            else:
                df = pd.read_csv(filesCandidato[candidato][0])
            df = df[~df['var'].isin(preguntasQueNoVan)]
            layout = go.Layout(
                height=800,
                legend=dict(orientation='h', x=0, y=-0.2),
                xaxis={'title': 'x-axis', 'fixedrange': True, 'title_text': xaxisTitle},
                yaxis={'title': 'y-axis', 'fixedrange': True, 'title_text': yaxisTitle},
                barmode='stack',
                # margin=go.layout.Margin(b=200),
            )

            palette = crucesDict[selected_cruce][1]
            dfloc = df.loc[df['var'] == selected_cruce].drop('var', axis=1).set_index('categoria').iloc[::-1]
            data = []
            # Fix for variable ammount of categories.
            if palette is None:
                clases = dfloc.index.tolist()
                if "No sabe" in clases:  # Si No sabe está presente lo ponemos al final
                    clases.remove("No sabe")
                    clases.append("No sabe")

                palette = list2dictPalette([clase for clase in clases], diverging)

            iclase = 0
            for i in dfloc.index:
                # Fix for variable ammount of categories.
                if type(palette).__name__ == "_ColorPalette":
                    color = palette[iclase]
                    iclase = iclase + 1
                else:
                    color = palette[i]

                trace = go.Bar(x=dfloc.columns,
                               y=dfloc.loc[i],
                               name='<br>'.join(textwrap.wrap(i, width=wrapWidht)),
                               marker={'color': color})
                data.append(trace)

            return {'data': data, 'layout': layout}
        else:
            layout = go.Layout(
                xaxis={'title': 'x-axis', 'fixedrange': True, 'title_text': xaxisTitle, 'ticks': '',
                       'showticklabels': False},
                yaxis={'title': 'y-axis', 'fixedrange': True, 'title_text': yaxisTitle, 'ticks': '',
                       'showticklabels': False},
                barmode='stack',
            )
            return {'data': [go.Bar()], 'layout': layout}
    return cruces_component


def insertString (source_str, insert_str, pos):
    return source_str[:pos]+insert_str+source_str[pos:]


#%%
import pandas as pd
from especiales.TRACKING_NACIONAL_215.apps.paletas_TRACKING_NACIONAL_215 import paletas
cruces_dict = {}
for pregunta, paleta in paletas.items():
    if pregunta not in encuesta.preguntas_ocultas:
        cruces_dict[pregunta] = [encuesta.get_textos['label' + pregunta], paleta]

csv_hbp =files_TRACKING_NACIONAL_215['csv_imagen'][0] #imagen orden positiva
csv_ts =  files_TRACKING_NACIONAL_215['csv_imagen'][3] #serie imagen
csv_cruces = files_TRACKING_NACIONAL_215["Patricia Bullrich"][0] #cruce pregunta_4opc #TODO
callbackInputTarget = 'selectTargetTRACKING_NACIONAL_215'
crucesDict = cruces_dict
opcionesDePreguntasInicial = 4 
preguntasQueNoVan= encuesta.preguntas_ocultas 
name='TRACKING_NACIONAL_215-Comparativo'
files = files_TRACKING_NACIONAL_215 
codigo='TRACKING_NACIONAL_215'
series = False
from graphsTimeSeries import getTimeSeriesLineplot
suf = 'conGalmarini' if 'conGalmarini' in csv_hbp else ''

if not opcionesDePreguntasInicial is None: #si opciones es algo
    df_hbp = pd.read_csv(insertString(csv_hbp, '_' + str(opcionesDePreguntasInicial) + 'opc', -4)) #leer a csv _#nro opc.csv
    df_series = pd.read_csv(insertString(csv_ts, '_' + str(opcionesDePreguntasInicial) + 'opc', -4)) 
else:
    df_hbp = pd.read_csv(csv_hbp) #si no, lee el de imagen positiva sin opciones
    df_series = pd.read_csv(csv_ts)


df_cruces = pd.read_csv(csv_cruces)
# removemos las variables de control interno: cuan frecuente es que responda / esá interesado en que lo contactemos
df_cruces = df_cruces[~df_cruces['var'].isin(preguntasQueNoVan)]



candidatos = df_hbp.clase.unique().tolist() #estopodría usarse para no hardcodear PATRICIA BULLRICH

selector_candidato = dcc.Dropdown(
    options=[{'label':'Todos', 'value':'todos'}] + [{'value':candidato, 'label':candidato} for candidato in candidatos],
    value='todos',
    #placeholder="Selección por target",
    id=codigo + 'select_candidato',
    clearable=False,
    searchable=False
)

candidatos_plots = {}
for candidato in candidatos:
    df_cruces = pd.read_csv(files[candidato][-1])
    df_cruces = df_cruces[~df_cruces['var'].isin(preguntasQueNoVan)]
    df_serie_candidato = df_series[df_series['clase']==candidato]
    plots = []

    hbarplot  = plot_hbarplot(csv_hbp, df_hbp, candidato, callbackInputTarget, f'selectOpciones_{codigo}', opinionColorDict, name, opcionesDePreguntasInicial = opcionesDePreguntasInicial)
    cruces_component = plot_cruces(candidato, df_cruces, files, name, 
                                   callbackInputTarget = callbackInputTarget, crucesDict = crucesDict,  
                                   preguntasQueNoVan = preguntasQueNoVan,opcionesDePreguntasInicial = opcionesDePreguntasInicial, reorder=False, codigo=codigo)
    
    #estoy queriendo agregar a los plots de imagen,la serie individual de imagen en el tiempo
    series_plot = getTimeSeriesLineplot(csv_ts,opinionColorDict, name, callbackInputTarget, callbackOpciones = f'selectOpciones_{codigo}')

    plots.append(
        html.Div(id = codigo + candidato + "_imagen_div"+ suf,
        children = [html.H4(candidato), hbarplot, html.H3(), html.H3(), cruces_component]
                 )
    )
    candidatos_plots[candidato] = html.Div(plots)
    componentes = html.Div(children=[selector_candidato,html.H3(),
                                     html.Div(
                                     html.Div(list(candidatos_plots.values())
                                         , id=codigo + 'plots_candidatos_div_ss' + suf), id='plots_candidatos_div')])

@app.callback(
    [Output(codigo + candidato + "_imagen_div" + suf, 'style') for candidato in candidatos]
    ,[Input(codigo + 'select_candidato', 'value')])
def update_candidato(candidato):
    c = candidato
    uid = {candidato: i for i, candidato in enumerate(candidatos)}
    if candidato == 'todos':
       salida = html.Div(list(candidatos_plots.values()))
       estilo = [{'display':'inline'}] * len(candidatos)
    else:
       salida = html.Div(candidatos_plots[candidato])
       estilo = [{'display': 'none'}] * len(candidatos)
       estilo[uid[c]] = {'visible': 'inline'}
    return estilo

#%%
imagen_individual = plots(files_TRACKING_NACIONAL_215['csv_imagen'][0],
                          files_TRACKING_NACIONAL_215['csv_imagen'][3], 
                          files_TRACKING_NACIONAL_215["Patricia Bullrich"][0],
                          callbackInputTarget= 'selectTargetTRACKING_NACIONAL_215',opcionesDePreguntasInicial = 4,
                              preguntasQueNoVan= encuesta.preguntas_ocultas, 
                              name='TRACKING_NACIONAL_215-Comparativo',
                              crucesDict = cruces_dict, 
                              files=files_TRACKING_NACIONAL_215, codigo='TRACKING_NACIONAL_215')

