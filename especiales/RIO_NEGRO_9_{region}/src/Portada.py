from app import app
from flask_login import logout_user, current_user
from login import login_failed
import dash_html_components as html
import dash_core_components as dcc
from especiales.src.Encuesta import Encuesta
from txt import textos as textos_base
from dash.dependencies import Input, Output
from config import dropdownOpciones
from config import dropdownTarget
from aux import checkControlEspecial
# def dropdownOpciones(id='selectOpciones', opciones=None):
#     # Nuevo, usado en Portada de especiales
#     opciones = opciones or [
#         {'label': 'No disponible', 'value': '_4opc'}]
#     return html.Div([
#         html.Label(children='Cantidad de opciones en preguntas de opinión'),
#         dcc.Dropdown(
#             id=id,
#             options=opciones,
#             value='_4opc',
#             searchable=False,
#             clearable=False
#         )
#     ])

def ordenar_ficha(ficha, breaks:int = 3):
    """
    Ordena los datos de una ficha en sublistas de tamaño 'breaks'.

    A partir de un diccionario con clave el título de la sección y valor los datos de la sección,
    la función genera una lista de sublistas, donde cada sublista contiene 'breaks' elementos del diccionario.

    :param ficha: Diccionario con los datos de la ficha. La clave es el título de la sección y el valor son los datos.
    :param breaks: Número de elementos por sublista. Por defecto es 3.
    :return: Lista de sublistas con los datos ordenados.
    """
    # Convierte el diccionario en una lista de pares clave-valor
    pares = list(ficha.items())

    # Genera las sublistas con 'breaks' elementos cada una
    ordenado = [pares[i:i + breaks] for i in range(0, len(pares), breaks)]
    return ordenado



tabs = [
    dcc.Tab(
        label='Ficha Técnica',
        value='tab-1',
        className='custom-tab',
        selected_className='custom-tab--selected'
    ),
    dcc.Tab(
        label='Encuesta',
        value='tab-2',
        className='custom-tab',
        selected_className='custom-tab--selected'
    )
]



class Portada():
    """
    Estructura de la Portada para las encuestas.

    :param encuesta: Instancia de la clase Encuesta.
    :param layout_preguntas: Dict graficos de las preguntas.
    """
    def __init__(self, encuesta: Encuesta,layout_preguntas: html.Div, *args, **kwarts):
        """
        Constructor de clase.

        :param encuesta: Instancia de la clase Encuesta.
        :param layout_preguntas: Layout de las preguntas de la encuesta.
        """

        self._layout = None
        self.encuesta = encuesta
        self.textos = encuesta.get_textos
        self.codigo = encuesta.codigo
        self.bloques = encuesta.bloques
        self.layout_preguntas = layout_preguntas
        self.generar_layout_base()
        self.generar_callbacks()
        

    @property
    def layout(self):
        return self._layout

    @layout.setter
    def layout(self, layout):
        self.layout = layout



    def generar_layout_base(self):
        """
        Genera el layout base de la portada.

        Se crea una estructura dash html que representa la portada de la encuesta, con título,
        descripción, pestañas y pie de página.

        Las secciones dinamicas se van llenando con callbacks

        """

        layout = html.Div(
            children=[
                # dcc.Store(id='session', storage_type='session'),
                html.Div(
                    className='section-header pba',
                    children=[
                        html.Div(
                            className='section-breadcrumb',
                            children=[
                                html.P(children=textos_base['breadcrumb']),
                            ]
                        ),
                        html.H2(children=self.textos['encuesta_especial']),
                        html.P(children=self.textos['bajada_encuesta_especial']),
                        # html.P(children=textos_BASE_1['bajada_encuesta_especial2'], className="bold"),
                        html.P(children=self.textos['bajada_encuesta_especial_fecha']),
                    ]
                ),
                html.Div([

                    dcc.Tabs(
                        id=f"{self.codigo}-tabs-with-classes",
                        value='tab-1',
                        parent_className='custom-tabs',
                        className='container custom-tabs-container',
                        children=tabs),
                    html.Div(id=f'{self.codigo}-tabs-content-classes')
                ]),
                html.Div(
                    className='footer',
                    children=[
                        html.P(children=textos_base['footer'])
                    ]

                )
            ]),
        self._layout = layout
    


    def generar_callbacks(self):
        """
        Genera los callbacks de la portada.

        Se definen los callbacks para manejar los eventos de cambio de pestaña y actualización de datos en la interfaz.
        """

        @app.callback(Output(f'{self.codigo}-tabs-content-classes', 'children'),
                      [Input(f'{self.codigo}-tabs-with-classes', 'value')])
        def render_content(tab):
            """
            Renderiza el contenido de la pestaña seleccionada.

            Este callback se activa cuando se selecciona una pestaña y muestra el contenido correspondiente en la
            interfaz (ficha tecnica o graficos)

            :param tab: Valor de la pestaña seleccionada.
            :return: Contenido dash HTML de la pestaña seleccionada.
            """

            # Quizas podria generarse esto con una fucion auxiliar u otra clase
            ficha_tecnica = {k:v for k,v in self.encuesta.get_textos.items() if k.startswith('ficha_')}
            ficha_tecnica = ordenar_ficha(ficha_tecnica)
            ficha_layout = []
            for col in ficha_tecnica:
                row = []
                for dato in col:
                    row.append(
                        html.Div(
                            className='dato',
                            children=[
                                html.H3(dato[0].replace('ficha_','')),
                                html.P(dato[1])
                                    ])
                                )
                ficha_layout.append(
                    html.Div(
                        className='col-12 col-sm-4',
                        children=row)
                )


            if tab == 'tab-1':
                return html.Div(
                    children=[
                        html.Div(
                            className='ficha',
                            children=[
                                html.Div(
                                    className='container',
                                    children=[
                                        html.Div(
                                            className='row',
                                            children= ficha_layout
                                        )
                                    ]
                                )
                            ]
                        ),
                    ]
                )


            elif tab == 'tab-2':
                preguntaPorDefecto = ''
                opciones = []
                bloquesOcultos = checkControlEspecial() 
                for bloque in bloquesOcultos:
                    self.bloques.pop(bloque, None)
   
               #preguntas = self.encuesta.bloques
                for bloque in self.encuesta.bloques.keys():
                    opciones.append({'label': bloque, 'value': bloque})
                    if len(preguntaPorDefecto) == 0:
                        preguntaPorDefecto = bloque

                return html.Div(
                    className='encuesta',
                    children=[
                        html.Div(
                            className='container filtros',
                            children=[
                                html.Div(
                                    className='row',
                                    children=[
                                        html.Div(
                                            className='col-12 col-sm-9',
                                            children=[
                                                html.Label(children=textos_base['labelBloque']),
                                                dcc.Dropdown(
                                                    id=f'{self.codigo}-bloques-dropdown',
                                                    options=opciones,
                                                    value=list(self.encuesta.bloques.keys())[0],
                                                    searchable=False,
                                                    clearable=False
                                                ),
                                            ]
                                        )
                                    ]
                                ),
                                html.Div(
                                    className='row',
                                    children=[
                                        html.Div(
                                            className='col-12 col-sm-9',
                                            children=[
                                                html.Label(children=textos_base['labelTema']),
                                                html.Div(
                                                    id=f'{self.codigo}-div-tema-dropdown-container',
                                                    children=[dcc.Dropdown( id=f'{self.codigo}_tema', searchable=False, clearable=False),
                                                              dropdownOpciones(f"selectOpciones_{self.codigo}")
                                                              ])
                                            ]
                                        ),
                                        html.Div(
                                            className='col-12 col-sm-3',
                                            children=[
                                                html.Label(children=textos_base['labelTarget']),
                                                dropdownTarget(f'selectTarget{self.codigo}',opciones=self.encuesta.opciones_target)
                                            ]
                                        )
                                    ]
                                )
                            ]
                        ),
                        html.Div([
                            html.Div(
                                html.Div(id=f'{self.codigo}-bloque-content', className='content'),
                                className='content-container'
                            ),
                        ], className='container'),
                    ]
                )
                
        @app.callback(
            [Output(f'{self.codigo}_tema', 'options'), Output(f'{self.codigo}_tema', 'value')],
            [Input(f'{self.codigo}-bloques-dropdown', 'value')])
        def update_tema(pathname):
            """
            Actualiza las opciones del dropdown de temas.

            Este callback se activa cuando se selecciona un bloque en el dropdown de bloques.
            Actualiza las opciones del dropdown de temas en base al bloque seleccionado.

            :param pathname: Bloque seleccionado.
            :return: Opciones actualizadas del dropdown de temas y valor (codigo de pregunta) por defecto.
            """


        
            pregs = [p for p in self.bloques[pathname.replace('/apps/', '')]]
        
            salida = [{'label':"Bloque completo", 'value':'todo'}]
            default_value = 'todo'
        
            if pathname.replace('/apps/', '') == self.encuesta.bloque_imagen: # imagen tiene el bloque todos diferente
                salida = []
                default_value = pregs[0]
        
            salida.extend([{'label': self.textos['label' + p], 'value': p } for p in pregs])
        
        
        
            return salida, default_value
        
        
        @app.callback(
            Output(f'{self.codigo}-bloque-content', 'children'),
            [Input(f'{self.codigo}_tema', 'value'),Input(f'{self.codigo}-bloques-dropdown', 'value')])
        def update_output(pregunta, pathname):
            """
            Actualiza el contenido del bloque seleccionado.

            Este callback se activa cuando se selecciona un tema en el dropdown de temas.
            Actualiza el contenido del bloque seleccionado en base al tema seleccionado.

            :param pregunta: Pregunta seleccionada.
            :param pathname: Nombre del bloque seleccionado.
            :return: Contenido dash HTML del bloque seleccionado.
           """

            # pregunta = 'todo'
            if current_user.is_authenticated:
                if pregunta != 'todo': # Si es una sola pregunta
                    return self.layout_preguntas[pregunta] #
                
                else:
                    #if "imagen" in pathname.replace('/apps/', '').lower():  # Parche para el layout de imagen completo
                    if pathname.replace('/apps/', '') == self.encuesta.bloque_imagen:
                        return self.layout_preguntas['imagen1']
        
                    else:  # si es el bloque completo
                        return [html.Div(self.layout_preguntas[preg]) for preg in self.bloques[pathname.replace('/apps/', '')]]
            else:
                return login_failed.layout



            


