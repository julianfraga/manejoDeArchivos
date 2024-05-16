from especiales.SAN_ISIDRO_1.apps.preguntasSAN_ISIDRO_1 import filesSAN_ISIDRO_1, preguntasQueNoVanSAN_ISIDRO_1
from especiales.SAN_ISIDRO_1.apps.txtSAN_ISIDRO_1 import textosSAN_ISIDRO_1
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
from txt import *
from especiales.SAN_ISIDRO_1.apps.txtSAN_ISIDRO_1 import textosSAN_ISIDRO_1
from config import *
from especiales.SAN_ISIDRO_1.apps.configSAN_ISIDRO_1 import *
from especiales.SAN_ISIDRO_1.apps.bloquesSAN_ISIDRO_1 import bloques_SAN_ISIDRO_1
from graphs import *
from especiales.SAN_ISIDRO_1.apps.txtSAN_ISIDRO_1 import textosSAN_ISIDRO_1 as textos
from permisos import trackingSANTIAGOPreguntasDeshabilitadas
from graph_imagen import plots

preguntas = {}
for bloque in bloques_SAN_ISIDRO_1.values():
    for pregunta in bloque:
        preguntas[pregunta] = textosSAN_ISIDRO_1["label" + pregunta]

orden_preguntas = []
for _ in bloques_SAN_ISIDRO_1.values():
    orden_preguntas.extend(_)


# Layout

ps = {}

ps['P09'] = html.Div([
        html.H3(textosSAN_ISIDRO_1['preguntaP09'], className='subtituloBloque'),
        getBarplotWithPalette(filesSAN_ISIDRO_1['csvP09'][0], 'selectTargetSAN_ISIDRO_1', paletas['P09'], 'SAN_ISIDRO_1-P09-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesSAN_ISIDRO_1['csvP09'][1], SAN_ISIDRO_1P09, 'SAN_ISIDRO_1-P09-2', 'selectTargetSAN_ISIDRO_1', opcionesDePreguntasInicial=3),
        html.H3(textosSAN_ISIDRO_1['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesSAN_ISIDRO_1['csvP09'][2], 'SAN_ISIDRO_1-P09-3', 'selectTargetSAN_ISIDRO_1', '', preguntasQueNoVan = preguntasQueNoVanSAN_ISIDRO_1, crucesDict = crucesDictSAN_ISIDRO_1, reorder=False)
])

ps['P14'] = html.Div([
        html.H3(textosSAN_ISIDRO_1['preguntaP14'], className='subtituloBloque'),
        getBarplotWithPalette(filesSAN_ISIDRO_1['csvP14'][0], 'selectTargetSAN_ISIDRO_1', paletas['P14'], 'SAN_ISIDRO_1-P14-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesSAN_ISIDRO_1['csvP14'][1], SAN_ISIDRO_1P14, 'SAN_ISIDRO_1-P14-2', 'selectTargetSAN_ISIDRO_1', opcionesDePreguntasInicial=3),
        html.H3(textosSAN_ISIDRO_1['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesSAN_ISIDRO_1['csvP14'][2], 'SAN_ISIDRO_1-P14-3', 'selectTargetSAN_ISIDRO_1', '', preguntasQueNoVan = preguntasQueNoVanSAN_ISIDRO_1, crucesDict = crucesDictSAN_ISIDRO_1, reorder=False)
])


ps['P16'] = html.Div([
        html.H3(textosSAN_ISIDRO_1['preguntaP16'], className='subtituloBloque'),
        getBarplotWithPalette(filesSAN_ISIDRO_1['csvP16'][0], 'selectTargetSAN_ISIDRO_1', paletas['P16'], 'SAN_ISIDRO_1-P16-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesSAN_ISIDRO_1['csvP16'][1], SAN_ISIDRO_1P16, 'SAN_ISIDRO_1-P16-2', 'selectTargetSAN_ISIDRO_1', opcionesDePreguntasInicial=3),
        html.H3(textosSAN_ISIDRO_1['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesSAN_ISIDRO_1['csvP16'][2], 'SAN_ISIDRO_1-P16-3', 'selectTargetSAN_ISIDRO_1', '', preguntasQueNoVan = preguntasQueNoVanSAN_ISIDRO_1, crucesDict = crucesDictSAN_ISIDRO_1, reorder=False)
])

ps['P18'] = html.Div([
        html.H3(textosSAN_ISIDRO_1['preguntaP18'], className='subtituloBloque'),
        getBarplotWithPalette(filesSAN_ISIDRO_1['csvP18'][0], 'selectTargetSAN_ISIDRO_1', paletas['P18'], 'SAN_ISIDRO_1-P18-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesSAN_ISIDRO_1['csvP18'][1], SAN_ISIDRO_1P18, 'SAN_ISIDRO_1-P18-2', 'selectTargetSAN_ISIDRO_1', opcionesDePreguntasInicial=3),
        html.H3(textosSAN_ISIDRO_1['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesSAN_ISIDRO_1['csvP18'][2], 'SAN_ISIDRO_1-P18-3', 'selectTargetSAN_ISIDRO_1', '', preguntasQueNoVan = preguntasQueNoVanSAN_ISIDRO_1, crucesDict = crucesDictSAN_ISIDRO_1, reorder=False)
])


ps['P19'] = html.Div([
        html.H3(textosSAN_ISIDRO_1['preguntaP19'], className='subtituloBloque'),
        getBarplotWithPalette(filesSAN_ISIDRO_1['csvP19'][0], 'selectTargetSAN_ISIDRO_1', paletas['P19'], 'SAN_ISIDRO_1-P19-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesSAN_ISIDRO_1['csvP19'][1], SAN_ISIDRO_1P19, 'SAN_ISIDRO_1-P19-2', 'selectTargetSAN_ISIDRO_1', opcionesDePreguntasInicial=3),
        html.H3(textosSAN_ISIDRO_1['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesSAN_ISIDRO_1['csvP19'][2], 'SAN_ISIDRO_1-P19-3', 'selectTargetSAN_ISIDRO_1', '', preguntasQueNoVan = preguntasQueNoVanSAN_ISIDRO_1, crucesDict = crucesDictSAN_ISIDRO_1, reorder=False)
])

ps['P20'] = html.Div([
        html.H3(textosSAN_ISIDRO_1['preguntaP20'], className='subtituloBloque'),
        getBarplotWithPalette(filesSAN_ISIDRO_1['csvP20'][0], 'selectTargetSAN_ISIDRO_1', paletas['P20'], 'SAN_ISIDRO_1-P20-1', showticklabels=False, reverse=True),
        #html.H3(),
        #getTimeSeriesLineplot(filesSAN_ISIDRO_1['csvP20'][1], SAN_ISIDRO_1P20, 'SAN_ISIDRO_1-P20-2', 'selectTargetSAN_ISIDRO_1', opcionesDePreguntasInicial=3),
        html.H3(textosSAN_ISIDRO_1['cruce'], className='subtituloBloque'),
        getCrucesStackedReverse(filesSAN_ISIDRO_1['csvP20'][2], 'SAN_ISIDRO_1-P20-3', 'selectTargetSAN_ISIDRO_1', '', preguntasQueNoVan = preguntasQueNoVanSAN_ISIDRO_1, crucesDict = crucesDictSAN_ISIDRO_1, reorder=False)
])




# Modelo
# ps['PXX'] = html.Div([
#         html.H3(textosSAN_ISIDRO_1['preguntaPXX'], className='subtituloBloque'),
#         getBarplotWithPalette(filesSAN_ISIDRO_1['csvPXX'][0], 'selectTargetSAN_ISIDRO_1', paletas['PXX'], 'SAN_ISIDRO_1-PXX-1', showticklabels=False, reverse=False),
#         #html.H3(),
#         #getTimeSeriesLineplot(filesSAN_ISIDRO_1['csvPXX'][1], SAN_ISIDRO_1PXX, 'SAN_ISIDRO_1-PXX-2', 'selectTargetSAN_ISIDRO_1', opcionesDePreguntasInicial=3),
#         html.H3(textosSAN_ISIDRO_1['cruce'], className='subtituloBloque'),
#         getCrucesStacked(filesSAN_ISIDRO_1['csvPXX'][2], 'SAN_ISIDRO_1-PXX-3', 'selectTargetSAN_ISIDRO_1', '', preguntasQueNoVan = preguntasQueNoVanSAN_ISIDRO_1, crucesDict = crucesDictSAN_ISIDRO_1)
# ])




# Parche del grafico de imagenes por no haber time series
from graph_imagen import *



def plot_cruces(candidato,df_cruces,files, name, preguntasQueNoVan, callbackInputTarget, crucesDict = crucesDict,opcionesDePreguntasInicial='', reorder=True):
    filesCandidato = files

    tracking = get_tracking(list(files.values())[0][0])


    if reorder:
        orden_cruces = orden[tracking]
    else:
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
         Input("selectOpciones", 'value'), ])
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



# def get_tracking(csv):
#     if "tracking" in csv:
#         return csv.split("/")[1]
#     else:
#         return csv.split("/")[2]

def plots(csv_hbp,csv_ts, csv_cruces, callbackInputTarget = '', crucesDict = crucesDict, opcionesDePreguntasInicial = 4, preguntasQueNoVan = "", preguntasDeshabilitadas = '', name = '', tracking='Nacional', files=''):
    tracking = get_tracking(csv_hbp)


    suf = 'conGalmarini' if 'conGalmarini' in csv_hbp else ''

    if not opcionesDePreguntasInicial is None:
        df_hbp = pd.read_csv(insertString(csv_hbp, '_' + str(opcionesDePreguntasInicial) + 'opc', -4))
    else:
        df_hbp = pd.read_csv(csv_hbp)




    df_cruces = pd.read_csv(csv_cruces)
    # removemos las variables de control interno: cuan frecuente es que responda / esá interesado en que lo contactemos
    df_cruces = df_cruces[~df_cruces['var'].isin(preguntasQueNoVan)]


    candidatos = df_hbp.clase.unique().tolist()

    selector_candidato = dcc.Dropdown(
        options=[{'label':'Todos', 'value':'todos'}] + [{'value':candidato, 'label':candidato} for candidato in candidatos],
        value='todos',
        #placeholder="Selección por target",
        id=tracking + 'select_candidato',
        clearable=False,
        searchable=False
    )

    candidatos_plots = {}
    for candidato in candidatos:
        df_cruces = pd.read_csv(files[candidato][-1])
        df_cruces = df_cruces[~df_cruces['var'].isin(preguntasQueNoVan)]
        plots = []

        hbarplot  = plot_hbarplot(csv_hbp, df_hbp, candidato, callbackInputTarget, 'selectOpciones', opinionColorDict, name, opcionesDePreguntasInicial = opcionesDePreguntasInicial)
        cruces_component = plot_cruces(candidato, df_cruces, files, name, callbackInputTarget = callbackInputTarget, crucesDict = crucesDict,  preguntasQueNoVan = preguntasQueNoVan,opcionesDePreguntasInicial = opcionesDePreguntasInicial, reorder=False)
        plots.append(
            html.Div(id = tracking + candidato + "_imagen_div"+ suf,
            children = [html.H4(candidato), hbarplot, html.H3(), html.H3(), cruces_component]
                     )
        )
        candidatos_plots[candidato] = html.Div(plots)
        componentes = html.Div(children=[selector_candidato,html.H3(),
                                         html.Div(
                                         html.Div(list(candidatos_plots.values())
                                             , id=tracking + 'plots_candidatos_div_ss' + suf), id='plots_candidatos_div')])

    @app.callback(
        [Output(tracking + candidato + "_imagen_div" + suf, 'style') for candidato in candidatos]
        ,[Input(tracking + 'select_candidato', 'value')])
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
    return componentes


imagen = plots(filesSAN_ISIDRO_1['csv_imagen'][0],filesSAN_ISIDRO_1['csv_imagen'][3], filesSAN_ISIDRO_1['Alberto Fernandez'][0], callbackInputTarget= 'selectTargetSAN_ISIDRO_1',opcionesDePreguntasInicial = 3,
                            preguntasQueNoVan= preguntasQueNoVanSAN_ISIDRO_1, name='SAN_ISIDRO_1-Comparativo',crucesDict = crucesDictSAN_ISIDRO_1, files=filesSAN_ISIDRO_1, tracking='SAN_ISIDRO_1'),



ps['imagen1'] = html.Div([
                html.H3(textosSAN_ISIDRO_1['pregunta_imagen'], className='subtituloBloque'),
                html.H5(textosSAN_ISIDRO_1['seleccioneFigura']),
                getStackedBarplot(filesSAN_ISIDRO_1['csv_imagen'][0], 'selectTargetSAN_ISIDRO_1', 'selectOpciones', opinionColorDict, 'SAN_ISIDRO_1-1D1A', opcionesDePreguntasInicial = 3),
                html.H3('Seleccione un dirigente o funcionario político'),
                imagen[0]
                ])

ps['imagen2'] = html.Div([
                html.H3(textosSAN_ISIDRO_1['pregunta_imagen'], className='subtituloBloque'),
                html.H5(textosSAN_ISIDRO_1['seleccioneFigura']),
                getStackedBarplot(filesSAN_ISIDRO_1['csv_imagen'][1], 'selectTargetSAN_ISIDRO_1', 'selectOpciones', opinionColorDict, 'SAN_ISIDRO_1-1D1B', opcionesDePreguntasInicial = 3),
                html.H3('Seleccione un dirigente o funcionario político'),
                imagen[0]])

ps['imagen3'] = html.Div([
                html.H3(textosSAN_ISIDRO_1['pregunta_imagen'], className='subtituloBloque'),
                html.H5(textosSAN_ISIDRO_1['seleccioneFigura']),
                getStackedBarplot(filesSAN_ISIDRO_1['csv_imagen'][2], 'selectTargetSAN_ISIDRO_1', 'selectOpciones', opinionColorDict, 'SAN_ISIDRO_1-1D1C', opcionesDePreguntasInicial = 3),
                html.H3('Seleccione un dirigente o funcionario político'),
                imagen[0]])





