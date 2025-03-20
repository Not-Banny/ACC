import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit, QCheckBox, QRadioButton, QComboBox, QVBoxLayout

class VentanaPyQt(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplicación con PyQt6")
        self.setGeometry(100, 100, 400, 400)

        layout = QVBoxLayout()

        # ─────────────────────── CREACIÓN DE WIDGETS ───────────────────────

        # Etiqueta
        layout.addWidget(QLabel("Nombre:"))

        # Entrada de texto
        self.entrada = QLineEdit()
        layout.addWidget(self.entrada)

        # Botón
        boton = QPushButton("Mostrar")
        boton.clicked.connect(self.mostrar_texto)
        layout.addWidget(boton)

        # Área de texto
        self.texto = QTextEdit()
        layout.addWidget(self.texto)

        # Casilla de verificación
        self.check = QCheckBox("Aceptar términos")
        layout.addWidget(self.check)

        # RadioButton
        self.radio1 = QRadioButton("Opción 1")
        self.radio1.setChecked(True)
        layout.addWidget(self.radio1)

        self.radio2 = QRadioButton("Opción 2")
        layout.addWidget(self.radio2)

        # Lista desplegable
        self.combo = QComboBox()
        self.combo.addItems(["Python", "Java", "C++", "JavaScript"])
        layout.addWidget(self.combo)

        # ───────────────────── MINI FORMULARIO DE INICIO DE SESIÓN ─────────────────────

        layout.addWidget(QLabel("Inicio de Sesión"))

        layout.addWidget(QLabel("Usuario:"))
        self.usuario = QLineEdit()
        layout.addWidget(self.usuario)

        layout.addWidget(QLabel("Contraseña:"))
        self.contraseña = QLineEdit()
        self.contraseña.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.contraseña)

        boton_login = QPushButton("Iniciar Sesión")
        boton_login.clicked.connect(self.iniciar_sesion)
        layout.addWidget(boton_login)

        self.setLayout(layout)

    def mostrar_texto(self):
        self.texto.append(f"Hola, {self.entrada.text()}!")

    def iniciar_sesion(self):
        usuario = self.usuario.text()
        contraseña = self.contraseña.text()
        print(f"Usuario: {usuario}, Contraseña: {contraseña}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPyQt()
    ventana.show()
    sys.exit(app.exec())
