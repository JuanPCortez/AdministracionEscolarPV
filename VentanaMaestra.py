import sys
import os
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from Formularios import Maestros

class VentanaMaestra(QMainWindow):
    def __init__(self):
        super().__init__()
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

        # Anuncios
        page_agregar_anuncios = QLabel("Formulario Agregar Anuncio (Simulado)")
        page_editar_anuncios = QLabel("Formulario Editar Anuncio (Simulado)")
        page_borrar_anuncios = QLabel("Formulario Borrar Anuncio (Simulado)")

        page_agregar_usuario = QLabel("Formulario Agregar Usuario (Simulado)")
        page_buscar_usuario = QLabel("Formulario Buscar Usuario (Simulado)")
        page_editar_usuario = QLabel("Formulario Editar Usuario (Simulado)")
        page_borrar_usuario = QLabel("Formulario Borrar Usuario (Simulado)")
        
        # Materia
        page_agregar_materia = QLabel("Formulario Agregar Usuario (Simulado)")
        page_editar_materia = QLabel("Formulario Buscar Usuario (Simulado)")
        page_borrar_materia = QLabel("Formulario Editar Usuario (Simulado)")
        page_buscar_materia = QLabel("Formulario Borrar Usuario (Simulado)")

        # Reportes 
        page_agregar_reporte = QLabel("Formulario Agregar Reporte (Simulado)")
        page_buscar_reporte = QLabel("Formulario Buscar Reporte (Simulado)")
        page_mostrar_reporte = QLabel("Formulario Borrar Reporte (Simulado)")
        
        # Agregar Widgets Anuncios al Stack
        self.__right_panel.addWidget(page_avisos)
        self.__right_panel.addWidget(page_agregar_anuncios)
        self.__right_panel.addWidget(page_editar_anuncios)
        self.__right_panel.addWidget(page_borrar_anuncios)
        
        # Agregar Widgets Usuarios al Stack
        self.__right_panel.addWidget(page_agregar_usuario)
        self.__right_panel.addWidget(page_buscar_usuario)
        self.__right_panel.addWidget(page_editar_usuario)
        self.__right_panel.addWidget(page_borrar_usuario)
        
        # Agregar Widgets Materia al Stack
        self.__right_panel.addWidget(page_agregar_materia)
        self.__right_panel.addWidget(page_editar_materia)
        self.__right_panel.addWidget(page_borrar_materia)
        self.__right_panel.addWidget(page_buscar_materia)

        # Agregar Widgets Reporte al Stack
        self.__right_panel.addWidget(page_agregar_reporte)
        self.__right_panel.addWidget(page_buscar_reporte)
        self.__right_panel.addWidget(page_mostrar_reporte)

        # Layout principal
        self.__main_layout = QVBoxLayout()
        self.__main_layout.addWidget(self.__right_panel)

        self.__main = QWidget()
        self.__main.setLayout(self.__main_layout)


        
        self.setCentralWidget(self.__main)

        #______________BARRA DE MENU____________
        self.__barraMenuPrincipal = self.menuBar()
        
        # MENU DE ACCIONES
        self.__menuAnuncio = QMenu('Anuncios',self)
        self.__agregarA = QAction('Agregar',self)
        self.__editarA = QAction('Editar',self)
        self.__borrarA = QAction('Borrar',self)
        self.__menuAnuncio.addAction(self.__agregarA)
        self.__menuAnuncio.addAction(self.__editarA)
        self.__menuAnuncio.addAction(self.__borrarA)
        
        self.__menuUsuario = QMenu('Usuarios',self)
        self.__agregarU = QAction('Agregar',self)
        self.__buscarU = QAction('Buscar',self)
        self.__editarU = QAction('Editar',self)
        self.__borrarU = QAction('Borrar',self)
        self.__menuUsuario.addAction(self.__agregarU)
        self.__menuUsuario.addAction(self.__buscarU)
        self.__menuUsuario.addAction(self.__editarU)
        self.__menuUsuario.addAction(self.__borrarU)
        
        self.__menuMateria = QMenu('Materia',self)
        self.__agregarM = QAction('Agregar',self)
        self.__editarM = QAction('Editar',self)
        self.__borrarM = QAction('Borrar',self)
        self.__buscarM = QAction('Buscar',self)
        self.__menuMateria.addAction(self.__agregarM)
        self.__menuMateria.addAction(self.__editarM)
        self.__menuMateria.addAction(self.__borrarM)
        self.__menuMateria.addAction(self.__buscarM)
        
        self.__menuHorario = QMenu('Horario',self)
        self.__menuHorarioAgregar = QAction('Agregar', self)
        self.__menuHorarioConsultar = QAction('Consultar',self)
        self.__menuHorarioEditar = QAction('Editar',self)
        self.__menuHorarioBorrar = QAction('Eliminar',self)
        self.__menuHorario.addAction(self.__menuHorarioAgregar)
        self.__menuHorario.addAction(self.__menuHorarioConsultar)
        self.__menuHorario.addAction(self.__menuHorarioEditar)
        self.__menuHorario.addAction(self.__menuHorarioBorrar)
        
        self.__menuReportes = QMenu('Reportes',self)
        self.__agregarR = QAction('Agregar',self)
        self.__borrarR = QAction('Borrar',self)
        self.__buscarR = QAction('Buscar',self)
        self.__mostrarR = QAction('Mostrar',self)
        self.__menuReportes.addAction(self.__agregarR)
        self.__menuReportes.addAction(self.__borrarR)
        self.__menuReportes.addAction(self.__buscarR)
        self.__menuReportes.addAction(self.__mostrarR)

        self.__menuAsignacion = QMenu('Asignaciones', self)
        self.__asignarMP = QAction('Asignar Materia a Profesor', self)
        self.__asignarMA= QAction('Asignar Materia a Alumno',self)
        self.__menuAsignacion.addAction(self.__asignarMP)
        self.__menuAsignacion.addAction(self.__asignarMA)
        
        self.__barraMenuPrincipal.addMenu(self.__menuAnuncio)
        self.__barraMenuPrincipal.addMenu(self.__menuUsuario)
        self.__barraMenuPrincipal.addMenu(self.__menuMateria)
        self.__barraMenuPrincipal.addMenu(self.__menuReportes)
        self.__barraMenuPrincipal.addMenu(self.__menuHorario)
        self.__barraMenuPrincipal.addMenu(self.__menuAsignacion)
        
        # Conectar acciones
        self.__action_avisos.triggered.connect(self.mostrar_avisos)
        self.__action_acerca.triggered.connect(self.mostrar_acerca)
        self.__botonOut.triggered.connect(self.cerrarSesion)
        
        self.__agregarA.triggered.connect(self.agregar_anuncio)
        self.__editarA.triggered.connect(self.editar_anuncio)
        self.__borrarA.triggered.connect(self.borrar_anuncio)
        
        self.__agregarU.triggered.connect(self.agregar_usuario)
        self.__buscarU.triggered.connect(self.buscar_usuario)
        self.__editarU.triggered.connect(self.editar_usuario)
        self.__borrarU.triggered.connect(self.borrar_usuario)
        
        self.__agregarM.triggered.connect(self.agregar_materia)
        self.__buscarM.triggered.connect(self.buscar_materia)
        self.__editarM.triggered.connect(self.editar_materia)
        self.__borrarM.triggered.connect(self.borrar_materia)

        self.__agregarR.triggered.connect(self.agregar_reporte)
        self.__borrarR.triggered.connect(self.borrar_reporte)
        self.__buscarR.triggered.connect(self.buscar_reporte)
        self.__mostrarR.triggered.connect(self.mostrar_reporte)

        self.__asignarMP.triggered.connect(self.asignar_materia_profesor)
        self.__asignarMA.triggered.connect(self.asignar_materia_alumno)

        self.__menuHorarioAgregar.triggered.connect(self.agregar_horario)
        self.__menuHorarioConsultar.triggered.connect(self.consultar_horario)
        self.__menuHorarioEditar.triggered.connect(self.editar_horario)
        self.__menuHorarioBorrar.triggered.connect(self.borrar_horario)

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
    def agregar_anuncio(self):
        widget = Maestros.AnuncioAgregar()
        widget.subirSignal.connect(self.mostrar_avisos)
        widget.cancelarSignal.connect(self.mostrar_avisos)
        self.__right_panel.addWidget(widget)
        self.__right_panel.setCurrentWidget(widget)

    @Slot() 
    def editar_anuncio(self):
        widget = Maestros.AnuncioEditar()
        widget.editarSignal.connect(self.mostrar_avisos)
        widget.cancelarSignal.connect(self.mostrar_avisos)
        self.__right_panel.addWidget(widget)
        self.__right_panel.setCurrentWidget(widget)

    @Slot() 
    def borrar_anuncio(self):
        widget = Maestros.AnuncioBorrar()
        widget.borrarSignal.connect(self.mostrar_avisos)
        widget.cancelarSignal.connect(self.mostrar_avisos)
        self.__right_panel.addWidget(widget)
        self.__right_panel.setCurrentWidget(widget)

    @Slot() 
    def agregar_usuario(self):
        widget = Maestros.UsuarioAgregar()
        widget.agregarSignal.connect(self.mostrar_avisos)
        widget.cancelarSignal.connect(self.mostrar_avisos)
        self.__right_panel.addWidget(widget)
        self.__right_panel.setCurrentWidget(widget)

    @Slot()            
    def buscar_usuario(self):
        widget = Maestros.UsuarioBuscar()
        widget.cancelarSignal.connect(self.mostrar_avisos)
        widget.salirSignal.connect(self.mostrar_avisos)
        self.__right_panel.addWidget(widget)
        self.__right_panel.setCurrentWidget(widget)

    @Slot() 
    def editar_usuario(self):
        widget = Maestros.UsuarioEditar()
        widget.editarSignal.connect(self.mostrar_avisos)
        widget.cancelarSignal.connect(self.mostrar_avisos)
        self.__right_panel.addWidget(widget)
        self.__right_panel.setCurrentWidget(widget)

    @Slot() 
    def borrar_usuario(self):
        widget = Maestros.UsuarioEliminar()
        widget.borrarSignal.connect(self.mostrar_avisos)
        widget.cancelarSignal.connect(self.mostrar_avisos)
        self.__right_panel.addWidget(widget)
        self.__right_panel.setCurrentWidget(widget)

    @Slot()
    def agregar_materia(self):
        widget = Maestros.MateriaAgregar()
        widget.agregarSignal.connect(self.mostrar_avisos)
        widget.cancelarSignal.connect(self.mostrar_avisos)
        self.__right_panel.addWidget(widget)
        self.__right_panel.setCurrentWidget(widget)

    @Slot()  
    def buscar_materia(self):
        widget = Maestros.BuscarMateria()
        widget.salirSignal.connect(self.mostrar_avisos)
        widget.cancelarSignal.connect(self.mostrar_avisos)
        self.__right_panel.addWidget(widget)
        self.__right_panel.setCurrentWidget(widget)

    @Slot() 
    def editar_materia(self):
        widget = Maestros.EditarMateria()
        widget.editarSignal.connect(self.mostrar_avisos)
        widget.cancelarSignal.connect(self.mostrar_avisos)
        self.__right_panel.addWidget(widget)
        self.__right_panel.setCurrentWidget(widget)

    @Slot()
    def borrar_materia(self):
        widget = Maestros.BorrarMateria()
        widget.borrarSignal.connect(self.mostrar_avisos)
        widget.cancelarSignal.connect(self.mostrar_avisos)
        self.__right_panel.addWidget(widget)
        self.__right_panel.setCurrentWidget(widget)
    
    @Slot()
    def agregar_reporte(self):
        widget = Maestros.ReporteAgregar()
        widget.subirSignal.connect(self.mostrar_avisos)
        widget.cancelarSignal.connect(self.mostrar_avisos)
        self.__right_panel.addWidget(widget)
        self.__right_panel.setCurrentWidget(widget)

    @Slot()
    def borrar_reporte(self):
        widget = Maestros.ReporteBorrar()
        widget.borrarSignal.connect(self.mostrar_avisos)
        widget.cancelarSignal.connect(self.mostrar_avisos)
        self.__right_panel.addWidget(widget)
        self.__right_panel.setCurrentWidget(widget)

    @Slot()
    def buscar_reporte(self):
       widget=Maestros.ReporteBuscar()
       widget.cancelarSignal.connect(self.mostrar_avisos)
       widget.salirSignal.connect(self.mostrar_avisos)
       self.__right_panel.addWidget(widget)
       self.__right_panel.setCurrentWidget(widget)

       
    @Slot()
    def mostrar_reporte(self):
        widget=Maestros.ReporteMostrar()
        widget.cancelarSignal.connect(self.mostrar_avisos)
        widget.salirSignal.connect(self.mostrar_avisos)
        self.__right_panel.addWidget(widget)
        self.__right_panel.setCurrentWidget(widget)
        pass

    @Slot()
    def asignar_materia_profesor(self):
        widget = Maestros.AsignarMateriaProfesor()
        widget.cancelarSignal.connect(self.mostrar_avisos)
        widget.salirSignal.connect(self.mostrar_avisos)
        self.__right_panel.addWidget(widget)
        self.__right_panel.setCurrentWidget(widget)

    @Slot ()
    def asignar_materia_alumno(self):
        widget=Maestros.AsignarGrupoAlumno()
        widget.cancelarSignal.connect(self.mostrar_avisos)
        self.__right_panel.addWidget(widget)
        self.__right_panel.setCurrentWidget(widget)
    
    @Slot()
    def agregar_horario(self):
        widget = Maestros.HorarioAgregar()
        widget.agregarSignal.connect(self.mostrar_avisos)
        widget.cancelarSignal.connect(self.mostrar_avisos)
        self.__right_panel.addWidget(widget)
        self.__right_panel.setCurrentWidget(widget)

    @Slot()
    def consultar_horario(self):
        widget = Maestros.HorarioConsultar()
        widget.salirSignal.connect(self.mostrar_avisos)
        widget.cancelarSignal.connect(self.mostrar_avisos)
        self.__right_panel.addWidget(widget)
        self.__right_panel.setCurrentWidget(widget)
        
    @Slot()
    def editar_horario(self):
        widget = Maestros.HorarioEditar()
        widget.editarSignal.connect(self.mostrar_avisos)
        widget.cancelarSignal.connect(self.mostrar_avisos)
        self.__right_panel.addWidget(widget)
        self.__right_panel.setCurrentWidget(widget)

    @Slot()
    def borrar_horario(self):
        widget = Maestros.HorarioEliminar()
        widget.eliminarSignal.connect(self.mostrar_avisos)
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    with open("estilo.qss", "r") as f:
        app.setStyleSheet(f.read())
    window = VentanaMaestra()
    window.show()
    sys.exit(app.exec())
