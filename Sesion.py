import sys
import os
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from Conexion import obtener_usuario

class Sesion(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inicio de Sesión")

        self.__uamitos = QLabel('UAMITOS HIGH SCHOOL')
        self.__uamitos.setAlignment(Qt.AlignCenter)

        self.__usuario = QLineEdit()
        self.__usuario.setPlaceholderText("Usuario")

        self.__contraseña = QLineEdit()
        self.__contraseña.setEchoMode(QLineEdit.Password)
        self.__contraseña.setPlaceholderText("Contraseña")

        self.__botonLogin = QPushButton('Iniciar Sesión')
        self.__version = QLabel('Versión 1.1.0')
        self.__version.setAlignment(Qt.AlignRight)

        self.__botonLogin.clicked.connect(self.mostrarPrincipal)

        layoutQV = QVBoxLayout()
        layoutQV.addWidget(self.__uamitos)
        layoutQV.addWidget(self.__usuario)
        layoutQV.addWidget(self.__contraseña)
        layoutQV.addWidget(self.__botonLogin)
        layoutQV.addWidget(self.__version)

        widget_principal = QWidget()
        widget_principal.setLayout(layoutQV)
        self.setFixedSize(300, 175)
        self.setCentralWidget(widget_principal)
    
    @Slot()
    def mostrarPrincipal(self):
        clave = self.__usuario.text().strip()
        contrasena = self.__contraseña.text().strip()

        if not clave or not contrasena:
            QMessageBox.warning(self, "Error", "Por favor ingrese usuario y contraseña.")
            return

        usuario = obtener_usuario(clave)

        if not usuario:
            QMessageBox.warning(self, "Error", "Usuario no encontrado.")
            return

        if usuario['contrasena'] != contrasena:
            QMessageBox.warning(self, "Error", "Contraseña incorrecta.")
            return

        tipo = clave[0]

        if tipo == 'M':
            from VentanaMaestra import VentanaMaestra
            self.vPrincipal = VentanaMaestra()
        elif tipo == 'A':
            from VentanaAdministrador import VentanaAdministrador
            self.vPrincipal = VentanaAdministrador()
        elif tipo == 'P':
            from VentanaProfesor import VentanaProfesor
            self.vPrincipal = VentanaProfesor(clave)
        elif tipo == 'E':
            QMessageBox.information(self, "En desarrollo", "El módulo estudiantil está en desarrollo.")
            return
        else:
            QMessageBox.warning(self, "Error", "Tipo de usuario no válido.")
            return

        self.vPrincipal.show()
        self.hide()

if __name__ == '__main__':
    app = QApplication()
    ruta_base = os.path.dirname(os.path.abspath(__file__))
    ruta_estilo = os.path.join(ruta_base, "estilo.qss")
    with open(ruta_estilo, "r") as f:
        app.setStyleSheet(f.read())
        
    ventana = Sesion()
    ventana.show()
    app.exec()
