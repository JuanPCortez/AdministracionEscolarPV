import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from Formularios import Maestros

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Gestión")
        self.resize(700, 500)

        # Barra de herramientas primaria
        self.__tool_bar = QToolBar("Menú Principal")
        self.__tool_bar.setMovable(False)
        self.addToolBar(Qt.LeftToolBarArea, self.__tool_bar)

        self.addToolBar(Qt.LeftToolBarArea, self.__tool_bar)
        self.setCorner(Qt.TopLeftCorner, Qt.LeftDockWidgetArea)

        self.__botonOut = QPushButton('Cerrar Sesión')

        self.__botonOut.clicked.connect(self.cerrarSesion)
        
        # Acciones
        self.__action_avisos = QAction("Avisos", self)
        self.__action_maestros = QAction('Maestro',self)
        self.__action_admins = QAction("Administración", self)
        self.__action_profes = QAction("Profesor", self)
        self.__action_acerca = QAction("Acerca de", self)

        # Agregar acciones al ToolBar
        self.__tool_bar.addAction(self.__action_avisos)
        self.__tool_bar.addAction(self.__action_maestros)
        self.__tool_bar.addAction(self.__action_admins)
        self.__tool_bar.addAction(self.__action_profes)
        self.__tool_bar.addAction(self.__action_acerca)

        # Conectar acciones
        self.__action_maestros.triggered.connect(self.mostrar_maestros)
        self.__action_avisos.triggered.connect(self.mostrar_avisos)
        self.__action_admins.triggered.connect(self.mostrar_admins)
        self.__action_profes.triggered.connect(self.mostrar_profes)
        self.__action_acerca.triggered.connect(self.mostrar_acerca)

        # Layout principal
        self.__relleno = QLabel("Sección: Avisos")
        self.__relleno.setAlignment(Qt.AlignCenter)
        
        self.__layout_vista = QHBoxLayout()
        self.__layout_vista.addWidget(self.__relleno)
        # self.__layout_vista.addWidget(self.__scrolbar)
        
        self.__main_layout = QVBoxLayout()
        self.__main_layout.addLayout(self.__layout_vista)
        self.__main_layout.addWidget(self.__botonOut)

        self.__main = QWidget()
        self.__main.setLayout(self.__main_layout)
        self.setCentralWidget(self.__main)

        #______________BARRA PRINCIPAL____________
        self.__barraMenuPrincipal = self.menuBar()
        #_________________________________________
        
        #Maestro
        self.__menuExportar = QMenu('Exportar',self)

        #Administrador
        self.__menuUsuario = QMenu('Usuarios',self)
        self.__menuMateriaAdmin = QMenu('Materia',self)
        self.__menuMateriaProfe = QMenu('Materia',self)
        self.__menuHorarioAdmin = QMenu('Horario',self)
        self.__menuHorarioProfe = QMenu('Horario',self)
        self.__menuAnuncio = QMenu('Anuncios',self)
        self.__menuConstancias = QMenu('Constancias',self)
        self.__menuImportar = QMenu('Importar',self)
        self.__menuReportesAdmin = QMenu('Reportes',self)

        self.__agregarU = QAction('Agregar',self)
        self.__buscarU = QAction('Buscar',self)
        self.__editarU = QAction('Editar',self)
        self.__borrarU = QAction('Borrar',self)
        
        self.__menuUsuario.addAction(self.__agregarU)
        self.__menuUsuario.addAction(self.__buscarU)
        self.__menuUsuario.addAction(self.__editarU)
        self.__menuUsuario.addAction(self.__borrarU)

        self.__agregarA = QAction('Agregar',self)
        self.__editarA = QAction('Editar',self)
        self.__borrarA = QAction('Borrar',self)

        self.__menuAnuncio.addAction(self.__agregarA)
        self.__menuAnuncio.addAction(self.__editarA)
        self.__menuAnuncio.addAction(self.__borrarA)

        self.__agregarR = QAction('Agregar',self)
        self.__borrarR = QAction('Borrar',self)
        self.__buscarR = QAction('Buscar',self)
        self.__mostrarR = QAction('Mostrar',self)

        self.__menuReportesAdmin.addAction(self.__agregarR)
        self.__menuReportesAdmin.addAction(self.__borrarR)
        self.__menuReportesAdmin.addAction(self.__buscarR)
        self.__menuReportesAdmin.addAction(self.__mostrarR)

        self.__agregarM = QAction('Agregar',self)
        self.__editarM = QAction('Editar',self)
        self.__borrarM = QAction('Borrar',self)
        self.__buscarMad = QAction('Buscar',self)

        self.__menuMateriaAdmin.addAction(self.__agregarM)
        self.__menuMateriaAdmin.addAction(self.__editarM)
        self.__menuMateriaAdmin.addAction(self.__borrarM)
        self.__menuMateriaAdmin.addAction(self.__buscarMad)
        
        self.__menuHorarioAgregar = QAction('Agregar', self)
        self.__menuHorarioConsultar = QAction('Consultar',self)
        self.__menuHorarioEditar = QAction('Editar',self)
        self.__menuHorarioBorrar = QAction('Eliminar',self)
        
        self.__menuHorarioAdmin.addAction(self.__menuHorarioAgregar)
        self.__menuHorarioAdmin.addAction(self.__menuHorarioConsultar)
        self.__menuHorarioAdmin.addAction(self.__menuHorarioEditar)
        self.__menuHorarioAdmin.addAction(self.__menuHorarioBorrar)

        #Profesor
        self.__menuImportar = QMenu('Importar',self)
        self.__menuExportar = QMenu('Exportar',self)

        self.__consultarG = QAction('Consultar',self)
        self.__listaG = QAction('Lista por grupo',self)

        self.__menuGrupos = QMenu('Grupos',self)
        self.__menuActas = QMenu('Actas',self)
        self.__menuReportesPr = QMenu('Reportes',self)
    
        self.__menuGrupos.addAction(self.__consultarG)
        self.__menuGrupos.addAction(self.__listaG)

        self.__agregarAc = QAction('Agregar',self)
        self.__RevisarAc = QAction('Editar',self)

        self.__menuActas.addAction(self.__agregarAc)
        self.__menuActas.addAction(self.__RevisarAc)

        self.__menuReportesPr.addAction(self.__agregarR)
        self.__menuReportesPr.addAction(self.__borrarR)

        

        for menu in [self.__menuAnuncio, self.__menuUsuario, self.__menuMateriaAdmin,
                self.__menuMateriaProfe, self.__menuGrupos,
                self.__menuActas,
                self.__menuConstancias, self.__menuImportar, self.__menuExportar,
                self.__menuReportesAdmin, self.__menuReportesPr, self.__menuHorarioAdmin, self.__menuHorarioProfe]:
            self.__barraMenuPrincipal.addMenu(menu)
            menu.menuAction().setVisible(False)
        
        self.__menus_maestro = [self.__menuUsuario, self.__menuMateriaAdmin, self.__menuAnuncio,
                      self.__menuConstancias, self.__menuImportar,
                      self.__menuExportar, self.__menuReportesAdmin, self.__menuHorarioAdmin]


        self.__menus_admin = [self.__menuUsuario, self.__menuMateriaAdmin, self.__menuAnuncio,
                      self.__menuConstancias, self.__menuExportar, self.__menuReportesAdmin, self.__menuHorarioAdmin]

        self.__menus_profesor = [self.__menuGrupos, self.__menuActas,
                         self.__menuExportar, self.__menuReportesPr, self.__menuMateriaProfe, self.__menuHorarioProfe]
        


        self.__agregarA.triggered.connect(self.agregar_anuncio)

        
        self.setFixedSize(700, 500)
        self.__main.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)


    def mostrar_avisos(self):
        self.__mostrar_menus([])
        self.__relleno.setText("Sección: Avisos")
        self.__main_layout.addLayout(self.__layout_vista)

    def mostrar_maestros(self):
        self.__mostrar_menus([])
        self.__mostrar_menus(self.__menus_maestro)
        self.__relleno.setText('Seccion: Maestros')

    def mostrar_admins(self):
        self.__mostrar_menus(self.__menus_admin)
        self.__relleno.setText("Sección: Administradores")

    def mostrar_profes(self):
        self.__mostrar_menus(self.__menus_profesor)
        self.__relleno.setText("Sección: Profesores")

    def mostrar_acerca(self):
        QMessageBox.information(self, "Acerca de", "Sistema de Gestión\nVersión AYUDA 0.1")
        
    def __mostrar_menus(self, menus_a_mostrar):
    # Todos los menús posibles (sin repetir)
        todos_los_menus = {
            self.__menuUsuario, self.__menuAnuncio,
            self.__menuConstancias, self.__menuImportar, self.__menuExportar,
            self.__menuReportesAdmin, self.__menuReportesPr, self.__menuGrupos, self.__menuActas,
            self.__menuMateriaAdmin, self.__menuMateriaProfe, self.__menuHorarioAdmin, self.__menuHorarioProfe
        }

        for menu in todos_los_menus:
            menu.menuAction().setVisible(menu in menus_a_mostrar)
    
    def agregar_anuncio(self):
        self.__main_layout.removeItem(self.__layout_vista)
        new_anuncio = Maestros.AnuncioAgregar()
        self.__main_layout.addWidget(new_anuncio)
    
    @Slot()
    def cerrarSesion(self):
        from Sesion import Sesion 
        self.ventanaSesion = Sesion()
        self.ventanaSesion.show()
        self.close()
        del self

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VentanaPrincipal()
    window.show()
    sys.exit(app.exec())
