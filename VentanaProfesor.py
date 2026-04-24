import sys
import os
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from Formularios import Profesor

class VentanaProfesor(QMainWindow):
    def __init__(self,clave_profesor):
        super().__init__()
        self.clave_profesor = clave_profesor
        self.setWindowTitle("Sistema de Gestión")
        self.resize(700, 500)

        
        rutaActual = os.path.dirname(os.path.abspath(__file__))
        rAnuncio = os.path.join(rutaActual,'Anuncio.ico')
        rAcerca = os.path.join(rutaActual,'AcercaDe.ico')
        rCerrarS = os.path.join(rutaActual,'CerrarSesion.ico')

        iAnuncio = QIcon(rAnuncio)
        iAcerca = QIcon(rAcerca)
        iCerrar = QIcon(rCerrarS)

        # --- Barra de herramientas ---
        self.__tool_bar = QToolBar("Menú Principal")
        self.__tool_bar.setMovable(False)
        self.addToolBar(Qt.LeftToolBarArea, self.__tool_bar)
        self.setCorner(Qt.TopLeftCorner, Qt.LeftDockWidgetArea)
        
        # Acciones
        self.__action_avisos = QAction(iAnuncio,"Avisos", self)
        self.__action_acerca = QAction(iAcerca,"Acerca de", self)
        self.__botonOut = QAction(iCerrar,'Cerrar Sesión', self)

        # Agregar acciones al ToolBar
        self.__tool_bar.addAction(self.__action_avisos)
        self.__tool_bar.addAction(self.__action_acerca)
        self.__tool_bar.addAction(self.__botonOut)

        # Panel dinámico con QStackedWidget
        self.__right_panel = QStackedWidget()

        # Mostrar Anuncios
        page_avisos = QWidget()
        layout_avisos = QHBoxLayout(page_avisos)
        self.__contenedor_avisos = QVBoxLayout()
        self.__contenedor_avisos.setAlignment(Qt.AlignTop)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        contenedor_scroll = QWidget()
        contenedor_scroll.setLayout(self.__contenedor_avisos)
        scroll.setWidget(contenedor_scroll)

        layout_avisos.addWidget(scroll)

        # Materia
        page_mostar_anuncios = QLabel("Formulario Mostrar Materia (Simulado)")
        
        # Grupos
        page_consultar_grupo = QLabel("Formulario Consultar Grupo (Simulado)")
        page_lista_grupo = QLabel("Formulario Lista Grupo (Simulado)")
        
        # Actas
        page_agregar_acta = QLabel("Formulario Agregar Acta (Simulado)")
        page_editar_acta = QLabel("Formulario Editar Acta (Simulado)")

        # Reportes 
        page_agregar_reporte = QLabel("Formulario Agregar Reporte (Simulado)")
        page_buscar_reporte = QLabel("Formulario Buscar Reporte (Simulado)")
        
        # Agregar Widget Anuncio al Stack
        self.__right_panel.addWidget(page_avisos)
        
        # Agregar Widget Materia al Stack
        self.__right_panel.addWidget(page_mostar_anuncios)
        
        # Agregar Widgets Grupos al Stack
        self.__right_panel.addWidget(page_consultar_grupo)
        self.__right_panel.addWidget(page_lista_grupo)
        
        # Agregar Widgets Actas al Stack
        self.__right_panel.addWidget(page_agregar_acta)
        self.__right_panel.addWidget(page_editar_acta)

        # Agregar Widgets Reporte al Stack
        self.__right_panel.addWidget(page_agregar_reporte)
        self.__right_panel.addWidget(page_buscar_reporte)

        # Layout principal
        self.__main_layout = QVBoxLayout()
        self.__main_layout.addWidget(self.__right_panel)

        self.__main = QWidget()
        self.__main.setLayout(self.__main_layout)
        self.setCentralWidget(self.__main)

        #______________BARRA DE MENU____________
        self.__barraMenuPrincipal = self.menuBar()
        
        
        # MENU DE ACCIONES
        self.__menuMateria = QMenu('Materia',self)
        self.__mis_materias = QAction('Mis materias', self)
        self.__todas_materias = QAction('Todas las materias', self)
        self.__menuMateria.addAction(self.__mis_materias)
        self.__menuMateria.addAction(self.__todas_materias)

        self.__menuuGrupo = QMenu('Grupos',self)
        self.__consultar_grupo = QAction('Consultar',self)
        self.__lista_grupo = QAction('Lista Grupos',self)
        self.__menuuGrupo.addAction(self.__consultar_grupo)
        self.__menuuGrupo.addAction(self.__lista_grupo)
        
        self.__menuActas = QMenu('Actas',self)
        self.__agregar_acta = QAction('Agregar',self)
        self.__menuActas.addAction(self.__agregar_acta)
        
        self.__menuReportes = QMenu('Reportes',self)
        self.__agregarR = QAction('Agregar',self)
        self.__borrarR = QAction('Borrar',self)
        self.__menuReportes.addAction(self.__agregarR)
        self.__menuReportes.addAction(self.__borrarR)
        
        self.__barraMenuPrincipal.addMenu(self.__menuMateria)
        self.__barraMenuPrincipal.addMenu(self.__menuuGrupo)
        self.__barraMenuPrincipal.addMenu(self.__menuActas)
        self.__barraMenuPrincipal.addMenu(self.__menuReportes)
        
        # Conectar acciones
        self.__action_avisos.triggered.connect(self.mostrar_avisos)
        self.__action_acerca.triggered.connect(self.mostrar_acerca)
        self.__botonOut.triggered.connect(self.cerrarSesion)
        
        self.__consultar_grupo.triggered.connect(self.consultar_grupo)
        self.__lista_grupo.triggered.connect(self.lista_grupo)
        
        self.__agregar_acta.triggered.connect(self.agregar_acta)
        
        self.__agregarR.triggered.connect(self.agregar_reporte)
        self.__borrarR.triggered.connect(self.borrar_reporte)

        self.__mis_materias.triggered.connect(self.mostrar_mis_materias)
        self.__todas_materias.triggered.connect(self.mostrar_todas_materias)

        
        self.mostrar_avisos()
        self.setFixedSize(700, 500)
        self.__main.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    
    @Slot()
    def mostrar_avisos(self):
        from Conexion import obtener_anuncios_recientes

        while self.__contenedor_avisos.count():
            item = self.__contenedor_avisos.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

        anuncios = obtener_anuncios_recientes()
        if not anuncios:
            mensaje = QLabel("No hay anuncios recientes.")
            mensaje.setAlignment(Qt.AlignCenter)
            self.__contenedor_avisos.addWidget(mensaje)
        else:
            for anuncio in anuncios:
                titulo = QLabel(f"Título: {anuncio['titulo']}")
                descripcion = QLabel(f"Descripción: {anuncio['descripcion']}")
                fecha = QLabel(f"Publicado: {anuncio['fecha_publicacion']}")
                separador = QFrame()
                separador.setFrameShape(QFrame.HLine)
                separador.setFrameShadow(QFrame.Sunken)

                for widget in [titulo, descripcion, fecha]:
                    widget.setWordWrap(True)
                    self.__contenedor_avisos.addWidget(widget)

                self.__contenedor_avisos.addWidget(separador)

        self.__right_panel.setCurrentIndex(0)

    @Slot()
    def consultar_grupo(self):
        widget = Profesor.ConsularGrupos(self.clave_profesor)
        widget.consultarSignal.connect(self.mostrar_avisos)
        widget.cancelarSignal.connect(self.mostrar_avisos)
        widget.salirSignal.connect(self.mostrar_avisos)
        self.__right_panel.addWidget(widget)
        self.__right_panel.setCurrentWidget(widget)

    @Slot() 
    def lista_grupo(self):
        widget = Profesor.ListaGrupo(self.clave_profesor)
        widget.listaSignal.connect(self.mostrar_avisos)
        widget.cancelarSignal.connect(self.mostrar_avisos)
        widget.salirSignal.connect(self.mostrar_avisos)
        self.__right_panel.addWidget(widget)
        self.__right_panel.setCurrentWidget(widget)

    @Slot() 
    def agregar_acta(self):
        widget = Profesor.GenerarActa()
        widget.generarSignal.connect(self.mostrar_avisos)
        widget.salirSignal.connect(self.mostrar_avisos)  # <- Esta es la nueva línea
        self.__right_panel.addWidget(widget)
        self.__right_panel.setCurrentWidget(widget)

    @Slot()
    def agregar_reporte(self):
        widget = Profesor.ReporteAgregar()
        widget.subirSignal.connect(self.mostrar_avisos)
        widget.cancelarSignal.connect(self.mostrar_avisos)
        self.__right_panel.addWidget(widget)
        self.__right_panel.setCurrentWidget(widget)

    @Slot()
    def borrar_reporte(self):
        widget = Profesor.ReporteBorrar()
        widget.borrarSignal.connect(self.mostrar_avisos)
        widget.cancelarSignal.connect(self.mostrar_avisos)
        self.__right_panel.addWidget(widget)
        self.__right_panel.setCurrentWidget(widget)

    @Slot()  
    def cerrarSesion(self):
        from Sesion import Sesion 
        self.ventanaSesion = Sesion()
        self.ventanaSesion.show()
        self.close()
        del self

    @Slot() 
    def mostrar_acerca(self):
        mensaje = (
            "Sistema de Gestión Escolar - Uamitos High School\n"
            "Versión 1.1.0\n"
            "\n"
            "Desarrollado por:\n"
            " - Alejandra Santiago Hernández\n"
            " - Juan Pablo Pineda Cortez\n"
            " - Diego Adalberto Almazán Espinoza\n"
            "\n"
            "Empresa desarrolladora:\n"
            "  EDUCORE Technologies S.A. de C.V.\n"
            "  Soluciones inteligentes para el aprendizaje\n"
            "\n"
            "Todos los derechos reservados © 2025"
        )
        QMessageBox.information(self, "Acerca de", mensaje)

    @Slot()
    def mostrar_mis_materias(self):
        from Conexion import crear_conexion
        clave_profesor = self.obtener_usuario_actual()  # método que debes implementar si no lo tienes
        conexion = crear_conexion()
        cursor = conexion.cursor(dictionary=True)
        query = """
            SELECT m.clave, m.nombre, m.grado, pmg.grupo
            FROM profesor_materia_grupo pmg
            JOIN materia m ON pmg.clave_materia = m.clave
            WHERE pmg.clave_profesor = %s
        """
        cursor.execute(query, (clave_profesor,))
        datos = cursor.fetchall()
        cursor.close()
        conexion.close()

        tabla = QTableWidget(len(datos), 4)
        tabla.setHorizontalHeaderLabels(['CLAVE', 'NOMBRE', 'GRADO', 'GRUPO'])
        for i, materia in enumerate(datos):
            tabla.setItem(i, 0, QTableWidgetItem(materia['clave']))
            tabla.setItem(i, 1, QTableWidgetItem(materia['nombre']))
            tabla.setItem(i, 2, QTableWidgetItem(str(materia['grado'])))
            tabla.setItem(i, 3, QTableWidgetItem(materia['grupo']))

        page = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("MIS MATERIAS"))
        layout.addWidget(tabla)
        page.setLayout(layout)

        self.__right_panel.addWidget(page)
        self.__right_panel.setCurrentWidget(page)

    @Slot()
    def mostrar_todas_materias(self):
        from Conexion import obtener_materias

        materias = obtener_materias()
        tabla = QTableWidget(len(materias), 3)
        tabla.setHorizontalHeaderLabels(['CLAVE', 'NOMBRE', 'GRADO'])
        for i, materia in enumerate(materias):
            tabla.setItem(i, 0, QTableWidgetItem(materia['clave']))
            tabla.setItem(i, 1, QTableWidgetItem(materia['nombre']))
            tabla.setItem(i, 2, QTableWidgetItem(str(materia['grado'])))

        page = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("TODAS LAS MATERIAS"))
        layout.addWidget(tabla)
        page.setLayout(layout)

        self.__right_panel.addWidget(page)
        self.__right_panel.setCurrentWidget(page)
    
    def obtener_usuario_actual(self):
        return self.clave_profesor


if __name__ == '__main__':
    app = QApplication(sys.argv)
    with open("estilo.qss", "r") as f:
        app.setStyleSheet(f.read())
    window = VentanaProfesor()
    window.show()
    sys.exit(app.exec())