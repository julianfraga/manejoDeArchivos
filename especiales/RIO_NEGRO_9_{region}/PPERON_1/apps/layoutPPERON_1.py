from especiales.PPERON_1.apps.preguntasPPERON_1 import filesPPERON_1, preguntasQueNoVanPPERON_1
from especiales.PPERON_1.apps.txtPPERON_1 import textosPPERON_1
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
from txt import *
from especiales.PPERON_1.apps.txtPPERON_1 import textosPPERON_1
from config import *
from especiales.PPERON_1.apps.configPPERON_1 import *
from especiales.PPERON_1.apps.bloquesPPERON_1 import bloques_PPERON_1
from graphs import *
from especiales.PPERON_1.apps.txtPPERON_1 import textosPPERON_1 as textos
from permisos import trackingSANTIAGOPreguntasDeshabilitadas
from graph_imagen import plots

preguntas = {}
for bloque in bloques_PPERON_1.values():
    for pregunta in bloque:
        preguntas[pregunta] = textosPPERON_1["label" + pregunta]

orden_preguntas = []
for _ in bloques_PPERON_1.values():
    orden_preguntas.extend(_)


# Layout

ps = {}

ps['P05'] = html.Div([
        html.H3(textosPPERON_1['preguntaP05'], className='subtituloBloque'),
        getBarplotWithPalette(filesPPERON_1['csvP05'][0], 'selectTargetPPERON_1', paletas['P05'], 'PPERON_1-P05-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesPPERON_1['csvP05'][1], PPERON_1P05, 'PPERON_1-P05-2', 'selectTargetPPERON_1', opcionesDePreguntasInicial=3),
        html.H3(textosPPERON_1['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesPPERON_1['csvP05'][2], 'PPERON_1-P05-3', 'selectTargetPPERON_1', '', preguntasQueNoVan = preguntasQueNoVanPPERON_1, crucesDict = crucesDictPPERON_1, reorder=False)
])

ps['P08'] = html.Div([
        html.H3(textosPPERON_1['preguntaP08'], className='subtituloBloque'),
        getBarplotWithPalette(filesPPERON_1['csvP08'][0], 'selectTargetPPERON_1', paletas['P08'], 'PPERON_1-P08-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesPPERON_1['csvP08'][1], PPERON_1P08, 'PPERON_1-P08-2', 'selectTargetPPERON_1', opcionesDePreguntasInicial=3),
        html.H3(textosPPERON_1['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesPPERON_1['csvP08'][2], 'PPERON_1-P08-3', 'selectTargetPPERON_1', '', preguntasQueNoVan = preguntasQueNoVanPPERON_1, crucesDict = crucesDictPPERON_1, reorder=False)
])

ps['P09'] = html.Div([
        html.H3(textosPPERON_1['preguntaP09'], className='subtituloBloque'),
        getBarplotWithPalette(filesPPERON_1['csvP09'][0], 'selectTargetPPERON_1', paletas['P09'], 'PPERON_1-P09-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesPPERON_1['csvP09'][1], PPERON_1P09, 'PPERON_1-P09-2', 'selectTargetPPERON_1', opcionesDePreguntasInicial=3),
        html.H3(textosPPERON_1['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesPPERON_1['csvP09'][2], 'PPERON_1-P09-3', 'selectTargetPPERON_1', '', preguntasQueNoVan = preguntasQueNoVanPPERON_1, crucesDict = crucesDictPPERON_1, reorder=False)
])





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


#
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


imagen = plots(filesPPERON_1['csv_imagen'][0],filesPPERON_1['csv_imagen'][3], filesPPERON_1['Alberto Fernandez'][0], callbackInputTarget= 'selectTargetPPERON_1',opcionesDePreguntasInicial = 3,
                            preguntasQueNoVan= preguntasQueNoVanPPERON_1, name='PPERON_1-Comparativo',crucesDict = crucesDictPPERON_1, files=filesPPERON_1, tracking='PPERON_1'),



ps['imagen1'] = html.Div([
                html.H3(textosPPERON_1['pregunta_imagen'], className='subtituloBloque'),
                html.H5(textosPPERON_1['seleccioneFigura']),
                getStackedBarplot(filesPPERON_1['csv_imagen'][0], 'selectTargetPPERON_1', 'selectOpciones', opinionColorDict, 'PPERON_1-1D1A', opcionesDePreguntasInicial = 3),
                html.H3('Seleccione un dirigente o funcionario político'),
                imagen[0]
                ])

ps['imagen2'] = html.Div([
                html.H3(textosPPERON_1['pregunta_imagen'], className='subtituloBloque'),
                html.H5(textosPPERON_1['seleccioneFigura']),
                getStackedBarplot(filesPPERON_1['csv_imagen'][1], 'selectTargetPPERON_1', 'selectOpciones', opinionColorDict, 'PPERON_1-1D1B', opcionesDePreguntasInicial = 3),
                html.H3('Seleccione un dirigente o funcionario político'),
                imagen[0]])

ps['imagen3'] = html.Div([
                html.H3(textosPPERON_1['pregunta_imagen'], className='subtituloBloque'),
                html.H5(textosPPERON_1['seleccioneFigura']),
                getStackedBarplot(filesPPERON_1['csv_imagen'][2], 'selectTargetPPERON_1', 'selectOpciones', opinionColorDict, 'PPERON_1-1D1C', opcionesDePreguntasInicial = 3),
                html.H3('Seleccione un dirigente o funcionario político'),
                imagen[0]])





