import sqlite3
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import time

# Configuración de la base de datos
def setup_database():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    conn.commit()
    conn.close()

setup_database()


# Clase para la ventana de inicio de sesión
import sqlite3
import tkinter as tk
from tkinter import messagebox
import time



# Clase para el cronómetro
class Cronometro:
    def __init__(self, master):
        self.master = master
        self.master.title("Cronómetro")
        
        self.tiempo = 0
        self.corriendo = True  # Inicia el cronómetro al abrir la ventana

        self.label_tiempo = tk.Label(master, text="Tiempo: 0 segundos")
        self.label_tiempo.pack()

        self.boton_detener = tk.Button(master, text="Detener", command=self.detener)
        self.boton_detener.pack()

        self.boton_desloguear = tk.Button(master, text="Desloguear", command=self.desloguear)
        self.boton_desloguear.pack()

        # Evitar cerrar con la X
        self.master.protocol("WM_DELETE_WINDOW", self.ignorar_cierre)

        # Iniciar el cronómetro inmediatamente
        self.actualizar_cronometro()

    def actualizar_cronometro(self):
        if self.corriendo:
            self.tiempo += 1
            self.label_tiempo.config(text=f"Tiempo: {self.tiempo} segundos")
            self.master.after(1000, self.actualizar_cronometro)  # Llamar cada segundo

    def detener(self):
        self.corriendo = False

    def desloguear(self):
        self.detener()  # Detener el cronómetro si está corriendo
        self.master.destroy()  # Cerrar la ventana del cronómetro

    def ignorar_cierre(self):
        # Método vacío para ignorar el intento de cerrar la ventana con la X
        pass

# Clase para la ventana de inicio de sesión
class LoginWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Inicio de Sesión")

        self.label_user = tk.Label(master, text="Nombre de Usuario:")
        self.label_user.pack()
        self.entry_user = tk.Entry(master)
        self.entry_user.pack()

        self.label_pass = tk.Label(master, text="Contraseña:")
        self.label_pass.pack()
        self.entry_pass = tk.Entry(master, show="*")
        self.entry_pass.pack()

        self.button_login = tk.Button(master, text="Iniciar Sesión", command=self.login)
        self.button_login.pack()

    def login(self):
        usuario = self.entry_user.get()
        contrasena = self.entry_pass.get()

        # Conexión a la base de datos
        conexion = sqlite3.connect('usuarios.db')
        cursor = conexion.cursor()

        # Consulta para verificar las credenciales
        cursor.execute('''
            SELECT * FROM usuarios WHERE usuario = ? AND contrasena = ?
        ''', (usuario, contrasena))

        resultado = cursor.fetchone()  # Obtiene el primer resultado

        # Verificación de las credenciales
        if resultado:
            messagebox.showinfo("Éxito", f"Usuario {usuario} ha iniciado sesión.")
            self.master.destroy()  # Cierra la ventana de login
            self.open_cronometro()  # Abre el cronómetro
        else:
            messagebox.showerror("Error", "Credenciales incorrectas.")

        # Cerrar la conexión
        conexion.close()

    def open_cronometro(self):
        cronometro_window = tk.Tk()  # Nueva ventana para el cronómetro
        Cronometro(cronometro_window)
        cronometro_window.mainloop()

# Crear la ventana principal
root = tk.Tk()
app = LoginWindow(root)
root.mainloop()
