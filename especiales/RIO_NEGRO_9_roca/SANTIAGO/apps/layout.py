from especiales.SANTIAGO.apps.preguntasSANTIAGO import filesSANTIAGO, preguntasQueNoVanSANTIAGO
from especiales.SANTIAGO.apps.txtSANTIAGO import textosSANTIAGO
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
from txt import *
from especiales.SANTIAGO.apps.txtSANTIAGO import textosSANTIAGO
from config import *
from especiales.SANTIAGO.apps.configSANTIAGO import *
from especiales.SANTIAGO.apps.bloques import bloques_SANTIAGO
from graphs import *
from especiales.SANTIAGO.apps.txtSANTIAGO import textosSANTIAGO as textos
from permisos import trackingSANTIAGOPreguntasDeshabilitadas
from graph_imagen import plots

preguntas = {}
for bloque in bloques_SANTIAGO.values():
    for pregunta in bloque:
        preguntas[pregunta] = textosSANTIAGO["label" + pregunta]

orden_preguntas = []
for _ in bloques_SANTIAGO.values():
    orden_preguntas.extend(_)


# Layout

ps = {}

# Bloque 1

# ps['P05'] = html.Div([
#         html.H3(textosSANTIAGO['preguntaP05'], className='subtituloBloque'),
#         getBarplotWithPalette(filesSANTIAGO['csvP05'][0], 'selectTargetSANTIAGO', paletas['P05'], 'SANTIAGO-P05-1', showticklabels=False, reverse=False ),
#         #html.H3(),
#         #getTimeSeriesLineplot(filesSANTIAGO['csvP05'][1], SANTIAGOP05, 'SANTIAGO-P05-2', 'selectTargetSANTIAGO', opcionesDePreguntasInicial=3),
#         html.H3(textosSANTIAGO['cruce'], className='subtituloBloque'),
#         getCrucesStacked(filesSANTIAGO['csvP05'][2], 'SANTIAGO-P05-3', 'selectTargetSANTIAGO', '', preguntasQueNoVan = preguntasQueNoVanSANTIAGO, crucesDict = crucesDictSANTIAGO)
# ])
#
#
# ps['P06'] = html.Div([
#         html.H3(textosSANTIAGO['preguntaP06'], className='subtituloBloque'),
#         getBarplotWithPalette(filesSANTIAGO['csvP06'][0], 'selectTargetSANTIAGO', paletas['P06'], 'SANTIAGO-P06-1', showticklabels=False, reverse=False),
#         #html.H3(),
#         #getTimeSeriesLineplot(filesSANTIAGO['csvP06'][1], SANTIAGOP06, 'SANTIAGO-P06-2', 'selectTargetSANTIAGO', opcionesDePreguntasInicial=3),
#         html.H3(textosSANTIAGO['cruce'], className='subtituloBloque'),
#         getCrucesStacked(filesSANTIAGO['csvP06'][2], 'SANTIAGO-P06-3', 'selectTargetSANTIAGO', '', preguntasQueNoVan = preguntasQueNoVanSANTIAGO, crucesDict = crucesDictSANTIAGO)
# ])

ps['P07'] = html.Div([
        html.H3(textosSANTIAGO['preguntaP07'], className='subtituloBloque'),
        getBarplotWithPalette(filesSANTIAGO['csvP07'][0], 'selectTargetSANTIAGO', paletas['P07'], 'SANTIAGO-P07-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesSANTIAGO['csvP07'][1], SANTIAGOP07, 'SANTIAGO-P07-2', 'selectTargetSANTIAGO', opcionesDePreguntasInicial=3),
        html.H3(textosSANTIAGO['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesSANTIAGO['csvP07'][2], 'SANTIAGO-P07-3', 'selectTargetSANTIAGO', '', preguntasQueNoVan = preguntasQueNoVanSANTIAGO, crucesDict = crucesDictSANTIAGO)
])

ps['P08'] = html.Div([
        html.H3(textosSANTIAGO['preguntaP08'], className='subtituloBloque'),
        getBarplotWithPalette(filesSANTIAGO['csvP08'][0], 'selectTargetSANTIAGO', paletas['P08'], 'SANTIAGO-P08-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesSANTIAGO['csvP08'][1], SANTIAGOP08, 'SANTIAGO-P08-2', 'selectTargetSANTIAGO', opcionesDePreguntasInicial=3),
        html.H3(textosSANTIAGO['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesSANTIAGO['csvP08'][2], 'SANTIAGO-P08-3', 'selectTargetSANTIAGO', '', preguntasQueNoVan = preguntasQueNoVanSANTIAGO, crucesDict = crucesDictSANTIAGO)
])

ps['P08_imputados'] = html.Div([
        html.H3(textosSANTIAGO['preguntaP08_imputados'], className='subtituloBloque'),
        getBarplotWithPalette(filesSANTIAGO['csvP08_imputados'][0], 'selectTargetSANTIAGO', paletas['P08'], 'SANTIAGO-P08-1_imputados', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesSANTIAGO['csvP08'][1], SANTIAGOP08, 'SANTIAGO-P08-2', 'selectTargetSANTIAGO', opcionesDePreguntasInicial=3),
])

ps['P09'] = html.Div([
        html.H3(textosSANTIAGO['preguntaP09'], className='subtituloBloque'),
        getBarplotWithPalette(filesSANTIAGO['csvP09'][0], 'selectTargetSANTIAGO', paletas['P09'], 'SANTIAGO-P09-1', showticklabels=False, reverse=False),
        
        html.H3(textosSANTIAGO['preguntaTransferenciaGobernador'], className='subtituloBloque'),
        getTransferencia(filesSANTIAGO["TransferenciaP08-P09"][0], paletas['P09']),
        #html.H3(),
        #getTimeSeriesLineplot(filesSANTIAGO['csvP09'][1], SANTIAGOP09, 'SANTIAGO-P09-2', 'selectTargetSANTIAGO', opcionesDePreguntasInicial=3),
        html.H3(textosSANTIAGO['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesSANTIAGO['csvP09'][2], 'SANTIAGO-P09-3', 'selectTargetSANTIAGO', '', preguntasQueNoVan = preguntasQueNoVanSANTIAGO, crucesDict = crucesDictSANTIAGO)
])

ps['P10'] = html.Div([
        html.H3(textosSANTIAGO['preguntaP10'], className='subtituloBloque'),
        getBarplotWithPalette(filesSANTIAGO['csvP10'][0], 'selectTargetSANTIAGO', paletas['P10'], 'SANTIAGO-P10-1', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesSANTIAGO['csvP10'][1], SANTIAGOP10, 'SANTIAGO-P10-2', 'selectTargetSANTIAGO', opcionesDePreguntasInicial=3),
        html.H3(textosSANTIAGO['cruce'], className='subtituloBloque'),
        getCrucesStacked(filesSANTIAGO['csvP10'][2], 'SANTIAGO-P10-3', 'selectTargetSANTIAGO', '', preguntasQueNoVan = preguntasQueNoVanSANTIAGO, crucesDict = crucesDictSANTIAGO)
])

ps['P10_imputados'] = html.Div([
        html.H3(textosSANTIAGO['preguntaP10_imputados'], className='subtituloBloque'),
        getBarplotWithPalette(filesSANTIAGO['csvP10_imputados'][0], 'selectTargetSANTIAGO', paletas['P10'], 'SANTIAGO-P10-1_imputados', showticklabels=False, reverse=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesSANTIAGO['csvP08'][1], SANTIAGOP08, 'SANTIAGO-P08-2', 'selectTargetSANTIAGO', opcionesDePreguntasInicial=3),
])

#getHBarplotOpcionesWithPalette(filesNacional['csvP23'][0], 'selectTarget', 'selectOpciones', opinionColorDict, 'Nacional-P23-1'),
ps['P11']= html.Div([
        html.H3(textosSANTIAGO['preguntaP11'], className='subtituloBloque'),
        getHBarplotOpcionesWithPalette(filesSANTIAGO['csvP11'][0], 'selectTargetSANTIAGO','selectOpciones',  paletas['P11'], 'SANTIAGO-P11-1', showticklabels=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesSANTIAGO['csvP11'][1], opinionColorDict, 'SANTIAGO-P11-2', 'selectTarget', yLegendPosition=-0.7),
        html.H3(textosSANTIAGO['cruce'], className='subtituloBloque'),
        getCrucesOpinionStacked(filesSANTIAGO['csvP11'][2], 'SANTIAGO-P11-3','selectTargetSANTIAGO', 'selectOpciones', crucesDict = crucesDictSANTIAGO, preguntasQueNoVan = preguntasQueNoVanSANTIAGO, opcionesDePreguntasInicial=5),
])

ps['P12']= html.Div([
        html.H3(textosSANTIAGO['preguntaP12'], className='subtituloBloque'),
        getHBarplotOpcionesWithPalette(filesSANTIAGO['csvP12'][0], 'selectTargetSANTIAGO','selectOpciones',  paletas['P12'], 'SANTIAGO-P12-1', showticklabels=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesSANTIAGO['csvP12'][1], opinionColorDict, 'SANTIAGO-P12-2', 'selectTarget', yLegendPosition=-0.7),
        html.H3(textosSANTIAGO['cruce'], className='subtituloBloque'),
        getCrucesOpinionStacked(filesSANTIAGO['csvP12'][2], 'SANTIAGO-P12-3','selectTargetSANTIAGO', 'selectOpciones', crucesDict = crucesDictSANTIAGO, preguntasQueNoVan = preguntasQueNoVanSANTIAGO, opcionesDePreguntasInicial=5),
])

ps['P13']= html.Div([
        html.H3(textosSANTIAGO['preguntaP13'], className='subtituloBloque'),
        getHBarplotOpcionesWithPalette(filesSANTIAGO['csvP13'][0], 'selectTargetSANTIAGO','selectOpciones',  paletas['P13'], 'SANTIAGO-P13-1', showticklabels=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesSANTIAGO['csvP13'][1], opinionColorDict, 'SANTIAGO-P13-2', 'selectTarget', yLegendPosition=-0.7),
        html.H3(textosSANTIAGO['cruce'], className='subtituloBloque'),
        getCrucesOpinionStacked(filesSANTIAGO['csvP13'][2], 'SANTIAGO-P13-3','selectTargetSANTIAGO', 'selectOpciones', crucesDict = crucesDictSANTIAGO, preguntasQueNoVan = preguntasQueNoVanSANTIAGO, opcionesDePreguntasInicial=5),
])

ps['P14']= html.Div([
        html.H3(textosSANTIAGO['preguntaP14'], className='subtituloBloque'),
        getHBarplotOpcionesWithPalette(filesSANTIAGO['csvP14'][0], 'selectTargetSANTIAGO','selectOpciones',  paletas['P14'], 'SANTIAGO-P14-1', showticklabels=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesSANTIAGO['csvP14'][1], opinionColorDict, 'SANTIAGO-P14-2', 'selectTarget', yLegendPosition=-0.7),
        html.H3(textosSANTIAGO['cruce'], className='subtituloBloque'),
        getCrucesOpinionStacked(filesSANTIAGO['csvP14'][2], 'SANTIAGO-P14-3','selectTargetSANTIAGO', 'selectOpciones', crucesDict = crucesDictSANTIAGO, preguntasQueNoVan = preguntasQueNoVanSANTIAGO, opcionesDePreguntasInicial=5),
])


ps['P15']= html.Div([
        html.H3(textosSANTIAGO['preguntaP15'], className='subtituloBloque'),
        getHBarplotOpcionesWithPalette(filesSANTIAGO['csvP15'][0], 'selectTargetSANTIAGO','selectOpciones',  paletas['P15'], 'SANTIAGO-P15-1', showticklabels=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesSANTIAGO['csvP15'][1], opinionColorDict, 'SANTIAGO-P15-2', 'selectTarget', yLegendPosition=-0.7),
        html.H3(textosSANTIAGO['cruce'], className='subtituloBloque'),
        getCrucesOpinionStacked(filesSANTIAGO['csvP15'][2], 'SANTIAGO-P15-3', 'selectTargetSANTIAGO', 'selectOpciones', crucesDict = crucesDictSANTIAGO, preguntasQueNoVan = preguntasQueNoVanSANTIAGO, opcionesDePreguntasInicial=5),
])

ps['P16']= html.Div([
        html.H3(textosSANTIAGO['preguntaP16'], className='subtituloBloque'),
        getHBarplotOpcionesWithPalette(filesSANTIAGO['csvP16'][0], 'selectTargetSANTIAGO','selectOpciones',  paletas['P16'], 'SANTIAGO-P16-1', showticklabels=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesSANTIAGO['csvP16'][1], opinionColorDict, 'SANTIAGO-P16-2', 'selectTarget', yLegendPosition=-0.7),
        html.H3(textosSANTIAGO['cruce'], className='subtituloBloque'),
        getCrucesOpinionStacked(filesSANTIAGO['csvP16'][2], 'SANTIAGO-P16-3','selectTargetSANTIAGO', 'selectOpciones', crucesDict = crucesDictSANTIAGO, preguntasQueNoVan = preguntasQueNoVanSANTIAGO, opcionesDePreguntasInicial=5),
])

ps['P17']= html.Div([
        html.H3(textosSANTIAGO['preguntaP17'], className='subtituloBloque'),
        getHBarplotOpcionesWithPalette(filesSANTIAGO['csvP17'][0], 'selectTargetSANTIAGO','selectOpciones',  paletas['P17'], 'SANTIAGO-P17-1', showticklabels=False),
        #html.H3(),
        #getTimeSeriesLineplot(filesSANTIAGO['csvP17'][1], opinionColorDict, 'SANTIAGO-P17-2', 'selectTarget', yLegendPosition=-0.7),
        html.H3(textosSANTIAGO['cruce'], className='subtituloBloque'),
        getCrucesOpinionStacked(filesSANTIAGO['csvP17'][2], 'SANTIAGO-P17-3','selectTargetSANTIAGO', 'selectOpciones', crucesDict = crucesDictSANTIAGO, preguntasQueNoVan = preguntasQueNoVanSANTIAGO, opcionesDePreguntasInicial=5),
])





# Parche del grafico de imagenes por no haber time series
from graph_imagen import *

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
        cruces_component = plot_cruces(candidato, df_cruces, files, name, callbackInputTarget = callbackInputTarget, crucesDict = crucesDict,  preguntasQueNoVan = preguntasQueNoVan,opcionesDePreguntasInicial = opcionesDePreguntasInicial)
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


imagen = plots(filesSANTIAGO['csv_imagen'][0],filesSANTIAGO['csv_imagen'][3], filesSANTIAGO['Alberto Fernandez'][0], callbackInputTarget= 'selectTargetSANTIAGO',opcionesDePreguntasInicial = 3,
                            preguntasQueNoVan= preguntasQueNoVanSANTIAGO, name='SANTIAGO-Comparativo',crucesDict = crucesDictSANTIAGO, files=filesSANTIAGO, tracking='SANTIAGO'),



#
#
#
#
# # Bloque 17
#
# imagen = plots(filesSANTIAGO['csv_imagen'][0],filesSANTIAGO['csv_imagen'][3], filesSANTIAGO['Alberto Fernandez'][0], callbackInputTarget= 'selectTargetSANTIAGO',opcionesDePreguntasInicial = 3,
#                            preguntasQueNoVan= preguntasQueNoVanSANTIAGO, name='SANTIAGO-Comparativo',crucesDict = crucesDictSANTIAGO, files=filesSANTIAGO, tracking='SANTIAGO'),
#
#
ps['imagen1'] = html.Div([
                html.H3(textosSANTIAGO['pregunta_imagen'], className='subtituloBloque'),
                html.H5(textosSANTIAGO['seleccioneFigura']),
                getStackedBarplot(filesSANTIAGO['csv_imagen'][0], 'selectTargetSANTIAGO', 'selectOpciones', opinionColorDict, 'SANTIAGO-1D1A', opcionesDePreguntasInicial = 3),
                html.H3('Seleccione un dirigente o funcionario político'),
                imagen[0]
                ])

ps['imagen2'] = html.Div([
                html.H3(textosSANTIAGO['pregunta_imagen'], className='subtituloBloque'),
                html.H5(textosSANTIAGO['seleccioneFigura']),
                getStackedBarplot(filesSANTIAGO['csv_imagen'][1], 'selectTargetSANTIAGO', 'selectOpciones', opinionColorDict, 'SANTIAGO-1D1B', opcionesDePreguntasInicial = 3),
                html.H3('Seleccione un dirigente o funcionario político'),
                imagen[0]])

ps['imagen3'] = html.Div([
                html.H3(textosSANTIAGO['pregunta_imagen'], className='subtituloBloque'),
                html.H5(textosSANTIAGO['seleccioneFigura']),
                getStackedBarplot(filesSANTIAGO['csv_imagen'][2], 'selectTargetSANTIAGO', 'selectOpciones', opinionColorDict, 'SANTIAGO-1D1C', opcionesDePreguntasInicial = 3),
                html.H3('Seleccione un dirigente o funcionario político'),
                imagen[0]])





