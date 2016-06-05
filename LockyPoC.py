# -*- coding: utf-8 -*-


import sys
import os
import base64
from PyQt4 import QtGui, QtCore


class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 750, 435)
        self.setWindowTitle("Dolbuck Lab: Locky PoC Tool")
        self.setWindowIcon(QtGui.QIcon("./dbkAntiLockyTEMP/logo.png"))
        self.paleta = QtGui.QPalette()
        self.paleta.setColor(QtGui.QPalette.Background,
                                QtGui.QColor(255, 191, 0))
        self.setPalette(self.paleta)

        #Definimos las acciones del boton
        #Accion Salir
        extAction = QtGui.QAction("&Salir", self)
        extAction.setShortcut("Ctrl+Q")
        extAction.setStatusTip(str("Sale de la aplicación").decode("utf-8"))
        extAction.triggered.connect(self.close_application)
        #Accion de la version
        verAction = QtGui.QAction(str("&Versión").decode("utf-8"), self)
        verAction.setShortcut("Ctrl+V")
        verAction.setStatusTip(
            str("Indica la version actual del software").decode("utf-8"))
        verAction.triggered.connect(self.get_version)
        #Accion del help
        helAction = QtGui.QAction("&Ayuda", self)
        helAction.setShortcut("Ctrl+H")
        helAction.setStatusTip("Muestra el texto de ayuda")
        helAction.triggered.connect(self.ayuda)
        #Accion del patch de las instantáneas
        insAction = QtGui.QAction("Patch", self)
        insAction.setShortcut("Ctrl+U")
        insAction.setStatusTip("Parcheo de las instantaneas de sistema")
        insAction.triggered.connect(self.patchvss)
        #Accion del unpatch de las instantáneas
        ins2Action = QtGui.QAction("unPatch", self)
        ins2Action.setShortcut("Ctrl+I")
        ins2Action.setStatusTip("Reestablece el fichero vssadmin.exe")
        ins2Action.triggered.connect(self.unpatchvss)
        #Accion de Licencia
        licAction = QtGui.QAction("Licencia", self)
        licAction.setShortcut("Ctrl+L")
        licAction.setStatusTip(str("Información de licencia").decode("utf-8"))
        licAction.triggered.connect(self.licencia)

        #Llamamos al statusbar
        self.statusBar()
        #Montamos la Barra de menu, anadimos los elementos
        mainMenu = self.menuBar()
        archMenu = mainMenu.addMenu("&Archivo")
        archMenu.addAction(extAction)
        loc1Menu = mainMenu.addMenu(str("&Instantáneas").decode("utf-8"))
        loc1Menu.addAction(insAction)
        loc1Menu.addAction(ins2Action)
        ayudaMenu = mainMenu.addMenu("&Ayuda")
        ayudaMenu.addAction(verAction)
        ayudaMenu.addAction(helAction)
        ayudaMenu.addAction(licAction)

        self.home()

    def home(self):
        #Botones eliminados de la anterior BETA
        #Boton Locky 1 Patch, llama a la funcion para parchear el registro
        #self.btn = QtGui.QPushButton("Locky1 Patch", self)
        #self.btn.clicked.connect(self.patchnew2)
        #self.btn.resize(self.btn.minimumSizeHint())
        #btn.move(0,100)
        #self.btn.setGeometry(640, 60, 100, 30)
        #self.btn.setStatusTip('Parchea el registro CURRENT USER')
        #boton2 locky1 Unpatch, llama a la funcion de reestablecimiento
        #self.btn2 = QtGui.QPushButton("Locky1 Unpatch", self)
        #self.btn2.clicked.connect(self.unpatchnew2)
        #self.btn2.resize(self.btn2.minimumSizeHint())
        #self.btn2.setGeometry(640, 95, 100, 30)
        #self.btn2.setStatusTip('Reestablece privilegios CURRENT USER')
        #boton3 locky Nuevo
        #self.btn3 = QtGui.QPushButton("Locky2 Patch ", self)
        #self.btn3.clicked.connect(self.patchnew)
        #self.btn3.resize(self.btn3.minimumSizeHint())
        #self.btn3.setGeometry(640, 130, 100, 30)
        #self.btn3.setStatusTip('Parche para LOCALMACHINE SOFTWARE')
        #boton4 locky Nuevo
        #self.btn4 = QtGui.QPushButton("Locky2 UNPatch ", self)
        #self.btn4.clicked.connect(self.unpatchnew)
        #self.btn4.resize(self.btn4.minimumSizeHint())
        #self.btn4.setGeometry(640, 165, 100, 30)
        #self.btn4.setStatusTip('Desprotege el registro para instalar normalmente')
        #boton5 vssadmin rename patch
        self.btn5 = QtGui.QPushButton("Patch", self)
        self.btn5.clicked.connect(self.patchvss)
        self.btn5.resize(self.btn5.minimumSizeHint())
        self.btn5.setGeometry(600, 155, 60, 30)
        self.btn5.setStatusTip('Proteccion para VSSADMIN.exe ')
        #boton6 vssadmin rename unpatch
        self.btn6 = QtGui.QPushButton("unPatch", self)
        self.btn6.clicked.connect(self.unpatchvss)
        self.btn6.resize(self.btn6.minimumSizeHint())
        self.btn6.setGeometry(660, 155, 60, 30)
        self.btn6.setStatusTip('Desroteccion para VSSADMIN.exe ')
        #boton7 patch all reg
        self.btn7 = QtGui.QPushButton("Patch", self)
        self.btn7.clicked.connect(self.patchall)
        self.btn7.resize(self.btn7.minimumSizeHint())
        self.btn7.setGeometry(600, 85, 60, 30)
        self.btn7.setStatusTip('Protege las claves usadas en Locky1 y Locky2 ')
        #boton8 unpatch all reg
        self.btn8 = QtGui.QPushButton("unPatch", self)
        self.btn8.clicked.connect(self.unpatchall)
        self.btn8.resize(self.btn8.minimumSizeHint())
        self.btn8.setGeometry(660, 85, 60, 30)
        self.btn8.setStatusTip('Desprotege las claves usadas en Locky1 y Locky2 ')
        #boton9 patch cryptsp
        self.btn9 = QtGui.QPushButton("Patch", self)
        self.btn9.clicked.connect(self.patchcryptsp)
        self.btn9.resize(self.btn9.minimumSizeHint())
        self.btn9.setGeometry(600, 225, 60, 30)
        self.btn9.setStatusTip('Renombra el fichero cryptsp.dll ')
        #boton10 unpatch cryptsp
        self.btn10 = QtGui.QPushButton("unPatch", self)
        self.btn10.clicked.connect(self.unpatchcryptsp)
        self.btn10.resize(self.btn10.minimumSizeHint())
        self.btn10.setGeometry(660, 225, 60, 30)
        self.btn10.setStatusTip('Renombra el fichero cryptsp.dll a su nombre original')
        #TextEdit caja de texto para mostrar el resultado shell
        self.txt2 = QtGui.QTextEdit(self)
        self.txt2.setGeometry(5, 60, 590, 350)
        self.txt2.acceptRichText()
        self.txt2.setReadOnly(True)
        #Label para mostrar titulo
        self.lbl1 = QtGui.QLabel("Dolbuck Lab: Anti LOCKY PoC", self)
        self.lbl1.setGeometry(150, 25, 450, 30)
        self.lbl1.setFont(QtGui.QFont('SansSerif', 20))
        #Label para mostrar Patch Registro
        self.lbl2 = QtGui.QLabel("REGISTRO", self)
        self.lbl2.setGeometry(600, 55, 200, 30)
        self.lbl2.setFont(QtGui.QFont('SansSerif', 14))
        #Label para mostrar Patch VSSADMIN
        self.lbl3 = QtGui.QLabel("VSSADMIN", self)
        self.lbl3.setGeometry(600, 130, 200, 30)
        self.lbl3.setFont(QtGui.QFont('SansSerif', 14))
        #Label para mostrar Patch VSSADMIN
        self.lbl4 = QtGui.QLabel("CRYPTSP.DLL", self)
        self.lbl4.setGeometry(600, 200, 200, 30)
        self.lbl4.setFont(QtGui.QFont('SansSerif', 14))
        #Label para mostrar FOTO LAB
        self.lbl5 = QtGui.QLabel(self)
        self.imagen = QtGui.QImage("./dbkAntiLockyTEMP/logo.png")
        self.lbl5.setGeometry(600, 250, 150, 150)
        self.pxmp = QtGui.QPixmap.fromImage(self.imagen)
        self.pxmp.scaled(100, 84, QtCore.Qt.KeepAspectRatio)
        self.lbl5.setPixmap(self.pxmp)
        self.show()

    def close_application(self, evento):
        cerrarapp(self, evento)

    def ayuda(self):
        txt = str("""
<h1>Ayuda general:</h1>
<p>Este software es un conjunto de pruebas de concepto para la mitigación y \
prevención del ransomware Locky. Las últimas muestras analizadas\
muestran que <b>actualmente el ransomware Locky no usa el registro de Windows \
para almacenar información</b> por tanto la prueba de concepto del registro \
ya no funcionará en las versiones posteriores. Si se desea probar tan sólo hay \
que buscar una muestra anterior y comprobar que al estar las llaves del \
registro bloqueadas, el ransomware no se ejecuta completamente y se detiene \
antes de tratar de contactar con el C&C.
Los parcheos podrían interferir en otras instalaciones, por tanto se recomienda\
quitar los parches cuando se vaya a realizar una instalación.</p>
\n<p><h3>VSSADMIN Patch:</h3> Se encarga de otorgar privilegios para poder \
manipular el archivo vssadmin.exe, una vez otorgados los privilegios renombra \
el fichero vssadmin.exe (no lo borra), con esto Locky no podrá borrar las \
instantáneas de sistema y se podrán recuperar después de una infección.\
Este proceso no interfiere con la creación de las instantáneas de sistema</p>\n
\n<p><h3>Patch Todo y unPatch Todo:</h3> Este parche consiste en limitar los \
privilegios de las claves de registro Software impidiendo que Locky pueda crear\
 su registro ahí y su posterior ejecución, además renombra el archivo vssadmin.\
 exe para que no pueda borrar las instantáneas de sistema.</p><p><h3>Patch\
  CRYPTSP.DLL\
 </h3> Este parche está en desarrollo, por ahora renombra el fichero para que \
 Locky no lo encuentre</p><p><h3>Patch Locky Antiguo</h3> Este parche crea la \
 llave de registro Locky y le quita los privilegios para que la primera versión\
 genere una excepción y no se ejecute.</p>
 <p><h3>Atajos de teclado</h3> <b>Ctrl + Q</b> = Salir<br>
 <b>Ctrl + V</b> = Muestra el mensaje de la versión del software.<br>
 <b>Ctrl + U</b> = Parchea el archivo vssadmin.exe y protege las instantáneas<br>
 <b>Ctrl + I</b> = Renombra el archivo vssadmin.exe a su nombre original<br>
 <b>Ctrl + H</b> = Muestra éste texto de ayuda</p>
 """).decode("utf-8")
        self.txt2.setHtml(txt)

    def licencia(self):
        licensetext = str("""
<h1>Licencia</h1> \
<p>Este programa se distribuye con licencia GNU Public License, por tanto \
puedes usarlo, modificarlo... pero por favor, si realizas \
modificaciones de este software <b>PUBLICALO</b>, esta herramienta\
ha salido de una empresa privada con el simple objetivo de que ayude a todo el que \
sea posible. Si queréis colaborar en el desarrollo o tenéis sugerencias de \
nuevas funcionalidades, poneos en contacto en el correo info@dolbuck.net</p>
        """).decode("utf-8")
        self.txt2.setHtml(licensetext)

    def get_version(self):
        show_version()

    def patchantiguo(self):
        try:
            s = ("HKEY_LOCAL_MACHINE\\Software\\Locky [2 8 19]")
            filename = ('pro.txt')
            with open(filename, 'wb') as f:
                f.write(s)
            c = str("reg add HKLM\\Software\\Locky")
            b = str("regini pro.txt")
            sal = os.popen4(c)[1].read()
            sal += os.popen4(b)[1].read()
            sal += str("\nProceso de parcheo de Locky antiguo completado")
            self.txt2.setText(str(sal))
        except Exception as e:
            er = ("<h2 style=\"color: red;\">HA OCURRIDO EL SIGUIENTE ERROR:</h2>")
            er += ("\n" + str("<h4>" + str(e) + "</h4>"))
            self.txt2.setText(str(er))

    def patchnew(self):
        try:
            s = ("HKEY_LOCAL_MACHINE\\Software [2 8 19]")
            filename = ('pro.txt')
            with open(filename, 'wb') as f:
                f.write(s)
            b = str("regini pro.txt")
            sal = os.popen4(b)[1].read()
            sal += str("\nPatchNew1: Proceso de parcheo de la clave de registro completado")
            self.txt2.setText(str(sal))
        except Exception as e:
            er = ("<h2 style=\"color: red;\">HA OCURRIDO EL SIGUIENTE ERROR:</h2>")
            er += ("\n" + str("<h4>" + str(e) + "</h4>"))
            self.txt2.setText(str(er))

    def unpatchnew(self):
        try:
            s = ("HKEY_LOCAL_MACHINE\\Software [1 5 17 7]")
            filename = ('pro.txt')
            with open(filename, 'wb') as f:
                f.write(s)
            b = str("regini pro.txt")
            sal = os.popen4(b)[1].read()
            sal += ("\n PatchNew1: Permisos reestablecidos")
            self.txt2.setText(str(sal))
        except Exception as e:
            er = ("<h2 style=\"color: red;\">HA OCURRIDO EL SIGUIENTE ERROR:</h2>")
            er += ("\n" + str("<h4>" + str(e) + "</h4>"))
            self.txt2.setText(str(er))

    def patchnew2(self):
        try:
            s = ("HKEY_CURRENT_USER\\Software [2 8 19]")
            filename = ('pro.txt')
            with open(filename, 'wb') as f:
                f.write(s)
            b = str("regini pro.txt")
            sal = os.popen4(b)[1].read()
            sal += str("""\nPatchNew2: Proceso de parcheo de la clave \
de registro completado""")
            self.txt2.setText(str(sal))
        except Exception as e:
            er = ("<h2 style=\"color: red;\">HA OCURRIDO EL SIGUIENTE ERROR:</h2>")
            er += ("\n" + str("<h4>" + str(e) + "</h4>"))
            self.txt2.setText(str(er))

    def unpatchnew2(self):
        try:
            s = ("HKEY_CURRENT_USER\\Software [1 5 17 7]")
            filename = ('pro.txt')
            with open(filename, 'wb') as f:
                f.write(s)
            b = str("regini pro.txt")
            sal = os.popen4(b)[1].read()
            sal += ("\n UnpatchNew2: Permisos reestablecidos")
            self.txt2.setText(str(sal))
        except Exception as e:
            er = ("<h2 style=\"color: red;\">HA OCURRIDO EL SIGUIENTE ERROR:</h2>")
            er += ("\n" + str("<h4>" + str(e) + "</h4>"))
            self.txt2.setText(str(er))

    def patchvss(self):
        try:
            c1 = str("takeown /F %WinDir%\\system32\\vssadmin.exe /A")
            c2 = str("icacls %WinDir%\\system32\\vssadmin.exe /grant *S-1-1-0:(F)")
            sal = os.popen4(c1)[1].read()
            sal += os.popen4(c2)[1].read()
            os.rename("C:\\WINDOWS\\System32\\vssadmin.exe",
            "C:\\WINDOWS\\System32\\ptch64.exe")
            sal += str("\n Renombrado fichero vssadmin.exe a ptch64.exe \
se encuentra ubicado en la ruta C:\\WINDOWS\\system32\\")
            self.txt2.setText(str(sal))
        except Exception as e:
            er = ("<h2 style=\"color: red;\">HA OCURRIDO EL SIGUIENTE ERROR:</h2>")
            er += ("\n" + str("<h4>" + str(e) + "</h4>"))
            self.txt2.setText(str(er))

    def unpatchvss(self):
        try:
            c1 = str("takeown /F %WinDir%\\system32\\ptch64.exe /A")
            c2 = str("icacls %WinDir%\\system32\\ptch64.exe /grant *S-1-1-0:(F)")
            sal = os.popen4(c1)[1].read()
            sal += os.popen4(c2)[1].read()
            os.rename("C:\\WINDOWS\\System32\\ptch64.exe",
            "C:\\WINDOWS\\System32\\vssadmin.exe")
            sal += str("\n Renombrado fichero ptch64.exe a su nombre original \
vssadmin.exe, se encuentra ubicado en la ruta C:\\WINDOWS\\system32\\")
            self.txt2.setText(str(sal))
        except Exception as e:
            er = ("<h2 style=\"color: red;\">HA OCURRIDO EL SIGUIENTE ERROR:</h2>")
            er += ("\n" + str("<h4>" + str(e) + "</h4>"))
            self.txt2.setHtml(str(er))

    def patchcryptsp(self):
        try:
            c1 = str("takeown /F %WinDir%\\system32\\cryptsp.dll /A")
            c2 = str("icacls %WinDir%\\system32\\cryptsp.dll /grant *S-1-1-0:(F)")
            sal = os.popen4(c1)[1].read()
            sal += os.popen4(c2)[1].read()
            os.rename("C:\\WINDOWS\\System32\\cryptsp.dll",
            "C:\\WINDOWS\\System32\\ptchsp.dll")
            sal += str("\n Renombrado fichero cryptsp.dll a ptchsp.dll \
se encuentra ubicado en la ruta C:\\WINDOWS\\system32\\")
            self.txt2.setText(str(sal))
        except Exception as e:
            er = ("<h2 style=\"color: red;\">HA OCURRIDO EL SIGUIENTE ERROR:</h2>")
            er += ("\n" + str("<h4>" + str(e) + "</h4>"))
            self.txt2.setText(str(er))

    def unpatchcryptsp(self):
        try:
            c1 = str("takeown /F %WinDir%\\system32\\ptchsp.dll /A")
            c2 = str("icacls %WinDir%\\system32\\ptchsp.dll /grant *S-1-1-0:(F)")
            sal = os.popen4(c1)[1].read()
            sal += os.popen4(c2)[1].read()
            os.rename("C:\\WINDOWS\\System32\\ptchsp.dll",
            "C:\\WINDOWS\\System32\\cryptsp.dll")
            sal += str("\n Renombrado fichero cryptsp.dll a su nombre original \
vssadmin.exe, se encuentra ubicado en la ruta C:\\WINDOWS\\system32\\")
            self.txt2.setText(str(sal))
        except Exception as e:
            er = ("<h2 style=\"color: red;\">HA OCURRIDO EL SIGUIENTE ERROR:</h2>")
            er += ("\n" + str("<h4>" + str(e) + "</h4>"))
            self.txt2.setHtml(str(er))

    def patchall(self):
        try:
            self.patchnew()
            self.patchnew2()
            self.patchvss()
            self.txt2.setHtml("<h3>Parcheo del registro completado</h3>")
        except Exception as e:
            er = ("<h2 style=\"color: red;\">HA OCURRIDO EL SIGUIENTE ERROR:</h2>")
            er += ("\n" + str("<h4>" + str(e) + "</h4>"))
            self.txt2.setHtml(str(er))

    def unpatchall(self):
        try:
            self.unpatchnew()
            self.unpatchnew2()
            self.unpatchvss()
            self.txt2.setHtml("<h3>Restauraci&oacute;n del registro completado</h3>")
        except Exception as e:
            er = ("<h2 style=\"color: red;\">HA OCURRIDO EL SIGUIENTE ERROR:</h2>")
            er += ("\n" + str("<h4>" + str(e) + "</h4>"))
            self.txt2.setHtml(str(er))

    def closeEvent(self, evento):
        cerrarapp(self, evento)


class SystemTrayIcon(QtGui.QSystemTrayIcon):

    def __init__(self, icon, g, parent=None):
        self.gui = g
        QtGui.QSystemTrayIcon.__init__(self, icon, parent)
        menu = QtGui.QMenu(parent)
        exitAction = menu.addAction("Exit")
        exitAction.triggered.connect(self.close_application)
        strver = str("Versión").decode("utf-8")
        versionAction = menu.addAction(strver)
        versionAction.triggered.connect(self.get_version)
        pallAction = menu.addAction("Patch All")
        pallAction.triggered.connect(self.pallbtn)
        pallAction = menu.addAction("unPatch All")
        pallAction.triggered.connect(self.unpallbtn)
        self.setContextMenu(menu)

    def close_application(self, ev):
        cerrarapp(self.gui, ev)

    def get_version(self, ev):
        show_version()

    def pallbtn(self):
        self.gui.patchall()
        self.gui.txt2.setHtml("<h1>Patch del registro HECHO</h1>")
        show_msg("Registro Parcheado")

    def unpallbtn(self):
        self.gui.unpatchall()
        self.gui.txt2.setHtml("<h1>Reestablecimiento del registro HECHO</h1>")
        show_msg("Registro Reestablecido")


def iconito():
    stringimagen = ("iVBORw0KGgoAAAANSUhEUgAAAJYAAACWCAYAAAA8AXHiAAAACXBIWXMAAAsTAAALEwEAmpwYAAABNmlDQ1BQaG90b3Nob3AgSUNDIHByb2ZpbGUAAHjarY6xSsNQFEDPi6LiUCsEcXB4kygotupgxqQtRRCs1SHJ1qShSmkSXl7VfoSjWwcXd7/AyVFwUPwC/0Bx6uAQIYODCJ7p3MPlcsGo2HWnYZRhEGvVbjrS9Xw5+8QMUwDQCbPUbrUOAOIkjvjB5ysC4HnTrjsN/sZ8mCoNTIDtbpSFICpA/0KnGsQYMIN+qkHcAaY6addAPAClXu4vQCnI/Q0oKdfzQXwAZs/1fDDmADPIfQUwdXSpAWpJOlJnvVMtq5ZlSbubBJE8HmU6GmRyPw4TlSaqo6MukP8HwGK+2G46cq1qWXvr/DOu58vc3o8QgFh6LFpBOFTn3yqMnd/n4sZ4GQ5vYXpStN0ruNmAheuirVahvAX34y/Axk/96FpPYgAAOjVpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+Cjx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuNS1jMDIxIDc5LjE1NTc3MiwgMjAxNC8wMS8xMy0xOTo0NDowMCAgICAgICAgIj4KICAgPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4KICAgICAgPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIKICAgICAgICAgICAgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIgogICAgICAgICAgICB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIKICAgICAgICAgICAgeG1sbnM6c3RFdnQ9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZUV2ZW50IyIKICAgICAgICAgICAgeG1sbnM6ZGM9Imh0dHA6Ly9wdXJsLm9yZy9kYy9lbGVtZW50cy8xLjEvIgogICAgICAgICAgICB4bWxuczpwaG90b3Nob3A9Imh0dHA6Ly9ucy5hZG9iZS5jb20vcGhvdG9zaG9wLzEuMC8iCiAgICAgICAgICAgIHhtbG5zOnRpZmY9Imh0dHA6Ly9ucy5hZG9iZS5jb20vdGlmZi8xLjAvIgogICAgICAgICAgICB4bWxuczpleGlmPSJodHRwOi8vbnMuYWRvYmUuY29tL2V4aWYvMS4wLyI+CiAgICAgICAgIDx4bXA6Q3JlYXRvclRvb2w+QWRvYmUgUGhvdG9zaG9wIENDIDIwMTQgKFdpbmRvd3MpPC94bXA6Q3JlYXRvclRvb2w+CiAgICAgICAgIDx4bXA6Q3JlYXRlRGF0ZT4yMDE2LTA1LTIwVDEyOjM2OjUyKzAyOjAwPC94bXA6Q3JlYXRlRGF0ZT4KICAgICAgICAgPHhtcDpNZXRhZGF0YURhdGU+MjAxNi0wNS0yMFQxMjozNjo1MiswMjowMDwveG1wOk1ldGFkYXRhRGF0ZT4KICAgICAgICAgPHhtcDpNb2RpZnlEYXRlPjIwMTYtMDUtMjBUMTI6MzY6NTIrMDI6MDA8L3htcDpNb2RpZnlEYXRlPgogICAgICAgICA8eG1wTU06SW5zdGFuY2VJRD54bXAuaWlkOjQwODA3Yjc0LWZlMzktMjY0Zi1hOGRlLWQxNTg4MWE0ZjcyYzwveG1wTU06SW5zdGFuY2VJRD4KICAgICAgICAgPHhtcE1NOkRvY3VtZW50SUQ+YWRvYmU6ZG9jaWQ6cGhvdG9zaG9wOmE5NWJlNjAyLTFlNzYtMTFlNi1iODAzLWM4ZDdhM2M4MDA1YzwveG1wTU06RG9jdW1lbnRJRD4KICAgICAgICAgPHhtcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD54bXAuZGlkOmYxZWJjOGM3LWYwNDctMTQ0OS04OTg2LTRjNThhYmIxNTIyMjwveG1wTU06T3JpZ2luYWxEb2N1bWVudElEPgogICAgICAgICA8eG1wTU06SGlzdG9yeT4KICAgICAgICAgICAgPHJkZjpTZXE+CiAgICAgICAgICAgICAgIDxyZGY6bGkgcmRmOnBhcnNlVHlwZT0iUmVzb3VyY2UiPgogICAgICAgICAgICAgICAgICA8c3RFdnQ6YWN0aW9uPmNyZWF0ZWQ8L3N0RXZ0OmFjdGlvbj4KICAgICAgICAgICAgICAgICAgPHN0RXZ0Omluc3RhbmNlSUQ+eG1wLmlpZDpmMWViYzhjNy1mMDQ3LTE0NDktODk4Ni00YzU4YWJiMTUyMjI8L3N0RXZ0Omluc3RhbmNlSUQ+CiAgICAgICAgICAgICAgICAgIDxzdEV2dDp3aGVuPjIwMTYtMDUtMjBUMTI6MzY6NTIrMDI6MDA8L3N0RXZ0OndoZW4+CiAgICAgICAgICAgICAgICAgIDxzdEV2dDpzb2Z0d2FyZUFnZW50PkFkb2JlIFBob3Rvc2hvcCBDQyAyMDE0IChXaW5kb3dzKTwvc3RFdnQ6c29mdHdhcmVBZ2VudD4KICAgICAgICAgICAgICAgPC9yZGY6bGk+CiAgICAgICAgICAgICAgIDxyZGY6bGkgcmRmOnBhcnNlVHlwZT0iUmVzb3VyY2UiPgogICAgICAgICAgICAgICAgICA8c3RFdnQ6YWN0aW9uPnNhdmVkPC9zdEV2dDphY3Rpb24+CiAgICAgICAgICAgICAgICAgIDxzdEV2dDppbnN0YW5jZUlEPnhtcC5paWQ6NDA4MDdiNzQtZmUzOS0yNjRmLWE4ZGUtZDE1ODgxYTRmNzJjPC9zdEV2dDppbnN0YW5jZUlEPgogICAgICAgICAgICAgICAgICA8c3RFdnQ6d2hlbj4yMDE2LTA1LTIwVDEyOjM2OjUyKzAyOjAwPC9zdEV2dDp3aGVuPgogICAgICAgICAgICAgICAgICA8c3RFdnQ6c29mdHdhcmVBZ2VudD5BZG9iZSBQaG90b3Nob3AgQ0MgMjAxNCAoV2luZG93cyk8L3N0RXZ0OnNvZnR3YXJlQWdlbnQ+CiAgICAgICAgICAgICAgICAgIDxzdEV2dDpjaGFuZ2VkPi88L3N0RXZ0OmNoYW5nZWQ+CiAgICAgICAgICAgICAgIDwvcmRmOmxpPgogICAgICAgICAgICA8L3JkZjpTZXE+CiAgICAgICAgIDwveG1wTU06SGlzdG9yeT4KICAgICAgICAgPGRjOmZvcm1hdD5pbWFnZS9wbmc8L2RjOmZvcm1hdD4KICAgICAgICAgPHBob3Rvc2hvcDpDb2xvck1vZGU+MzwvcGhvdG9zaG9wOkNvbG9yTW9kZT4KICAgICAgICAgPHBob3Rvc2hvcDpJQ0NQcm9maWxlPkFkb2JlIFJHQiAoMTk5OCk8L3Bob3Rvc2hvcDpJQ0NQcm9maWxlPgogICAgICAgICA8dGlmZjpPcmllbnRhdGlvbj4xPC90aWZmOk9yaWVudGF0aW9uPgogICAgICAgICA8dGlmZjpYUmVzb2x1dGlvbj43MjAwMDAvMTAwMDA8L3RpZmY6WFJlc29sdXRpb24+CiAgICAgICAgIDx0aWZmOllSZXNvbHV0aW9uPjcyMDAwMC8xMDAwMDwvdGlmZjpZUmVzb2x1dGlvbj4KICAgICAgICAgPHRpZmY6UmVzb2x1dGlvblVuaXQ+MjwvdGlmZjpSZXNvbHV0aW9uVW5pdD4KICAgICAgICAgPGV4aWY6Q29sb3JTcGFjZT42NTUzNTwvZXhpZjpDb2xvclNwYWNlPgogICAgICAgICA8ZXhpZjpQaXhlbFhEaW1lbnNpb24+MTUwPC9leGlmOlBpeGVsWERpbWVuc2lvbj4KICAgICAgICAgPGV4aWY6UGl4ZWxZRGltZW5zaW9uPjE1MDwvZXhpZjpQaXhlbFlEaW1lbnNpb24+CiAgICAgIDwvcmRmOkRlc2NyaXB0aW9uPgogICA8L3JkZjpSREY+CjwveDp4bXBtZXRhPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgIAo8P3hwYWNrZXQgZW5kPSJ3Ij8+cVNSjAAAACBjSFJNAAB6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")
    imgdecodificada = base64.b64decode(stringimagen)
    nombrearchivo = "./dbkAntiLockyTEMP/logo.png"
    with open(nombrearchivo, "wb") as a:
        a.write(imgdecodificada)


def show_msg(m):
    msg = QtGui.QMessageBox()
    msg.setIcon(QtGui.QMessageBox.Information)
    msg.setText(m)
    msg.setWindowTitle("Dolbuck Locky PoC")
    msg.setStandardButtons(QtGui.QMessageBox.Ok)
    msg.exec_()


def show_version():
    msg = QtGui.QMessageBox()
    msg.setIcon(QtGui.QMessageBox.Information)
    msg.setText(str("Versión 0.01 BETA").decode("utf-8"))
    msg.setInformativeText(str("Versión de Pruebas").decode("utf-8"))
    strtitulo = str("Versión").decode("utf-8")
    msg.setWindowTitle(strtitulo)
    strinf = str("""Hasta ahora se ha conseguido implementar con PyQT \
su ventana principal, compilar todo en un sólo ejecutable y añadir las \
funcionalidads básicas de la prueba de concepto. En las últimas muestras de \
Locky hemos comprobado que ya no usa el registro de windows, así que las \
vacunas relacionadas con el registro no serán efectivas en las nuevas \
versiones""").decode("utf-8")
    msg.setDetailedText(strinf)
    msg.setStandardButtons(QtGui.QMessageBox.Ok)
    msg.exec_()


def cerrarapp(self, evento):
    result = QtGui.QMessageBox.question(self, 'Salir',
        str("¿Está seguro de que quiere salir del programa?").decode("utf-8"),
        QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
    if result == QtGui.QMessageBox.Yes:
        stri = """
Gracias por usar nuestra beta, esperamos mejorarla pronto. Para \
obetener mas información, visite nuestra web en http://lab.dolbuck.net
        """
        QtGui.QMessageBox.information(self, "Salir", stri.decode("utf-8"))
        os.remove("./dbkAntiLockyTEMP/logo.png")
        os.rmdir("./dbkAntiLockyTEMP/")
        sys.exit()
    elif result == QtGui.QMessageBox.No:
        if evento:
            evento.ignore()


def main():
    app = QtGui.QApplication(sys.argv)
    os.makedirs("./dbkAntiLockyTEMP/")
    iconito()
    GUI = Window()
    icon = QtGui.QIcon("./dbkAntiLockyTEMP/logo.png")
    trayIcon = SystemTrayIcon(icon, GUI)
    trayIcon.show()
    sys.exit(app.exec_())


main()