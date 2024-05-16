from especiales.TIGRE.apps.preguntasTIGRE import filesTIGRE, preguntasQueNoVanTIGRE
from especiales.TIGRE.apps.txtTIGRE import textosTIGRE
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
from txt import *
from especiales.TIGRE.apps.txtTIGRE import textosTIGRE
from config import *
from especiales.TIGRE.apps.configTIGRE import *
from especiales.TIGRE.apps.bloquesTIGRE import bloques_TIGRE
from graphs import *
from especiales.TIGRE.apps.txtTIGRE import textosTIGRE as textos
from permisos import trackingSANTIAGOPreguntasDeshabilitadas
from graph_imagen import plots

preguntas = {}
for bloque in bloques_TIGRE.values():
    for pregunta in bloque:
        preguntas[pregunta] = textosTIGRE["label" + pregunta]

orden_preguntas = []
for _ in bloques_TIGRE.values():
    orden_preguntas.extend(_)


# Layout

ps = {}

ps['P07'] = html.Div([
        html.H3(textosTIGRE['preguntaP07'], className='subtituloBloque'),
        getBarplotWithPalette(filesTIGRE['csvP07'][0], 'selectTargetTIGRE', paletas['P07'], 'TIGRE-P07-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesTIGRE['csvP07'][1], TIGREP07, 'TIGRE-P07-2', 'selectTargetTIGRE', opcionesDePreguntasInicial=3),
        html.H3(textosTIGRE['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesTIGRE['csvP07'][2], 'TIGRE-P07-3', 'selectTargetTIGRE', '', preguntasQueNoVan = preguntasQueNoVanTIGRE, crucesDict = crucesDictTIGRE, reorder=False)
])

ps['P08'] = html.Div([
        html.H3(textosTIGRE['preguntaP08'], className='subtituloBloque'),
        getBarplotWithPalette(filesTIGRE['csvP08'][0], 'selectTargetTIGRE', paletas['P08'], 'TIGRE-P08-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesTIGRE['csvP08'][1], TIGREP08, 'TIGRE-P08-2', 'selectTargetTIGRE', opcionesDePreguntasInicial=3),
        html.H3(textosTIGRE['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesTIGRE['csvP08'][2], 'TIGRE-P08-3', 'selectTargetTIGRE', '', preguntasQueNoVan = preguntasQueNoVanTIGRE, crucesDict = crucesDictTIGRE, reorder=False)
])

ps['P09'] = html.Div([
        html.H3(textosTIGRE['preguntaP09'], className='subtituloBloque'),
        getBarplotWithPalette(filesTIGRE['csvP09'][0], 'selectTargetTIGRE', paletas['P09'], 'TIGRE-P09-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesTIGRE['csvP09'][1], TIGREP09, 'TIGRE-P09-2', 'selectTargetTIGRE', opcionesDePreguntasInicial=3),
        html.H3(textosTIGRE['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesTIGRE['csvP09'][2], 'TIGRE-P09-3', 'selectTargetTIGRE', '', preguntasQueNoVan = preguntasQueNoVanTIGRE, crucesDict = crucesDictTIGRE, reorder=False)
])

ps['P10'] = html.Div([
        html.H3(textosTIGRE['preguntaP10'], className='subtituloBloque'),
        getBarplotWithPalette(filesTIGRE['csvP10'][0], 'selectTargetTIGRE', paletas['P10'], 'TIGRE-P10-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesTIGRE['csvP10'][1], TIGREP10, 'TIGRE-P10-2', 'selectTargetTIGRE', opcionesDePreguntasInicial=3),
        html.H3(textosTIGRE['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesTIGRE['csvP10'][2], 'TIGRE-P10-3', 'selectTargetTIGRE', '', preguntasQueNoVan = preguntasQueNoVanTIGRE, crucesDict = crucesDictTIGRE, reorder=False)
])

ps['P11'] = html.Div([
        html.H3(textosTIGRE['preguntaP11'], className='subtituloBloque'),
        getBarplotWithPalette(filesTIGRE['csvP11'][0], 'selectTargetTIGRE', paletas['P11'], 'TIGRE-P11-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesTIGRE['csvP11'][1], TIGREP11, 'TIGRE-P11-2', 'selectTargetTIGRE', opcionesDePreguntasInicial=3),
        html.H3(textosTIGRE['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesTIGRE['csvP11'][2], 'TIGRE-P11-3', 'selectTargetTIGRE', '', preguntasQueNoVan = preguntasQueNoVanTIGRE, crucesDict = crucesDictTIGRE, reorder=False)
])

ps['P12'] = html.Div([
        html.H3(textosTIGRE['preguntaP12'], className='subtituloBloque'),
        getBarplotWithPalette(filesTIGRE['csvP12'][0], 'selectTargetTIGRE', paletas['P12'], 'TIGRE-P12-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesTIGRE['csvP12'][1], TIGREP12, 'TIGRE-P12-2', 'selectTargetTIGRE', opcionesDePreguntasInicial=3),
        html.H3(textosTIGRE['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesTIGRE['csvP12'][2], 'TIGRE-P12-3', 'selectTargetTIGRE', '', preguntasQueNoVan = preguntasQueNoVanTIGRE, crucesDict = crucesDictTIGRE, reorder=False)
])

ps['P13'] = html.Div([
        html.H3(textosTIGRE['preguntaP13'], className='subtituloBloque'),
        getBarplotWithPalette(filesTIGRE['csvP13'][0], 'selectTargetTIGRE', paletas['P13'], 'TIGRE-P13-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesTIGRE['csvP13'][1], TIGREP13, 'TIGRE-P13-2', 'selectTargetTIGRE', opcionesDePreguntasInicial=3),
        html.H3(textosTIGRE['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesTIGRE['csvP13'][2], 'TIGRE-P13-3', 'selectTargetTIGRE', '', preguntasQueNoVan = preguntasQueNoVanTIGRE, crucesDict = crucesDictTIGRE, reorder=False)
])
ps['P14'] = html.Div([
        html.H3(textosTIGRE['preguntaP14'], className='subtituloBloque'),
        getBarplotWithPalette(filesTIGRE['csvP14'][0], 'selectTargetTIGRE', paletas['P14'], 'TIGRE-P14-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesTIGRE['csvP14'][1], TIGREP14, 'TIGRE-P14-2', 'selectTargetTIGRE', opcionesDePreguntasInicial=3),
        html.H3(textosTIGRE['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesTIGRE['csvP14'][2], 'TIGRE-P14-3', 'selectTargetTIGRE', '', preguntasQueNoVan = preguntasQueNoVanTIGRE, crucesDict = crucesDictTIGRE, reorder=False)
])
ps['P15'] = html.Div([
        html.H3(textosTIGRE['preguntaP15'], className='subtituloBloque'),
        getBarplotWithPalette(filesTIGRE['csvP15'][0], 'selectTargetTIGRE', paletas['P15'], 'TIGRE-P15-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesTIGRE['csvP15'][1], TIGREP15, 'TIGRE-P15-2', 'selectTargetTIGRE', opcionesDePreguntasInicial=3),
        html.H3(textosTIGRE['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesTIGRE['csvP15'][2], 'TIGRE-P15-3', 'selectTargetTIGRE', '', preguntasQueNoVan = preguntasQueNoVanTIGRE, crucesDict = crucesDictTIGRE, reorder=False)
])
ps['P16'] = html.Div([
        html.H3(textosTIGRE['preguntaP16'], className='subtituloBloque'),
        getBarplotOpcionesWithPalette(filesTIGRE['csvP16'][0], 'selectTargetTIGRE','selectOpciones', opinionColorDict, 'TIGRE-P16-1', showticklabels=False),
        html.H3(textosTIGRE['cruce'], className='subtituloBloque'),
        getCrucesOpinionStacked(filesTIGRE['csvP16'][2], 'TIGRE-P16-3', 'selectTargetTIGRE', 'selectOpciones', preguntasQueNoVan = preguntasQueNoVanTIGRE, crucesDict = crucesDictTIGRE, opcionesDePreguntasInicial=4, reorder = False)
])



# Modelo
# ps['PXX'] = html.Div([
#         html.H3(textosTIGRE['preguntaPXX'], className='subtituloBloque'),
#         getBarplotWithPalette(filesTIGRE['csvPXX'][0], 'selectTargetTIGRE', paletas['PXX'], 'TIGRE-PXX-1', showticklabels=False, reverse=False),
#         #html.H3(),
#         #getTimeSeriesLineplot(filesTIGRE['csvPXX'][1], TIGREPXX, 'TIGRE-PXX-2', 'selectTargetTIGRE', opcionesDePreguntasInicial=3),
#         html.H3(textosTIGRE['cruce'], className='subtituloBloque'),
#         getCrucesStacked(filesTIGRE['csvPXX'][2], 'TIGRE-PXX-3', 'selectTargetTIGRE', '', preguntasQueNoVan = preguntasQueNoVanTIGRE, crucesDict = crucesDictTIGRE)
# ])


# Parche del grafico de imagenes por no haber time series
from graph_imagen import *

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


imagen = plots(filesTIGRE['csv_imagen'][0],filesTIGRE['csv_imagen'][3], filesTIGRE['Alberto Fernandez'][0], callbackInputTarget= 'selectTargetTIGRE',opcionesDePreguntasInicial = 4,
                            preguntasQueNoVan= preguntasQueNoVanTIGRE, name='TIGRE-Comparativo',crucesDict = crucesDictTIGRE, files=filesTIGRE, tracking='TIGRE'),

ps['imagen1'] = html.Div([
                html.H3(textosTIGRE['pregunta_imagen'], className='subtituloBloque'),
                html.H5(textosTIGRE['seleccioneFigura']),
                getStackedBarplot(filesTIGRE['csv_imagen'][0], 'selectTargetTIGRE', 'selectOpciones', opinionColorDict, 'TIGRE-1D1A', opcionesDePreguntasInicial = 4),
                html.H3('Seleccione un dirigente o funcionario político'),
                imagen[0]
                ])

ps['imagen2'] = html.Div([
                html.H3(textosTIGRE['pregunta_imagen'], className='subtituloBloque'),
                html.H5(textosTIGRE['seleccioneFigura']),
                getStackedBarplot(filesTIGRE['csv_imagen'][1], 'selectTargetTIGRE', 'selectOpciones', opinionColorDict, 'TIGRE-1D1B', opcionesDePreguntasInicial = 4),
                html.H3('Seleccione un dirigente o funcionario político'),
                imagen[0]])

ps['imagen3'] = html.Div([
                html.H3(textosTIGRE['pregunta_imagen'], className='subtituloBloque'),
                html.H5(textosTIGRE['seleccioneFigura']),
                getStackedBarplot(filesTIGRE['csv_imagen'][2], 'selectTargetTIGRE', 'selectOpciones', opinionColorDict, 'TIGRE-1D1C', opcionesDePreguntasInicial = 4),
                html.H3('Seleccione un dirigente o funcionario político'),
                imagen[0]])





