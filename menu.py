import tkinter as tk
import os
import sys
from PIL import Image, ImageTk

def ayuda():
    # Crear una nueva ventana de ayuda
    ayuda_ventana = tk.Toplevel()
    ayuda_ventana.title("Ayuda")  # Título de la nueva ventana
    ayuda_ventana.resizable(False, False)

    # Establecer icono
    icon_path = os.path.join(getattr(sys, '_MEIPASS', os.path.abspath('.')), 'icono.ico')
    ayuda_ventana.iconbitmap(icon_path)

    # Crear un marco con borde negro y fondo blanco
    marco = tk.Frame(
        ayuda_ventana,
        bg="white",                  # Fondo blanco
        highlightbackground="black",  # Color del borde
        highlightthickness=2,         # Grosor del borde
        padx=20,                      # Padding interno horizontal
        pady=20                       # Padding interno vertical
    )
    marco.pack(padx=10, pady=10, fill="both", expand=True)

    # Título principal "Caracteres Especiales" centrado
    titulo_label = tk.Label(
        marco,
        text="Caracteres Especiales", 
        font=("Cambria", 16, "bold"),
        bg="white",
        anchor="center"
    )
    titulo_label.pack(fill="x", pady=(0, 10))  # Centrando el título y separando del siguiente contenido

    # Subtítulo "Griego" alineado a la izquierda
    griego_label = tk.Label(
        marco,
        text="Griego",
        font=("Cambria", 13, "bold"),
        bg="white",
        anchor="w"
    )
    griego_label.pack(anchor="w", pady=(0, 10))  # Separación inferior

    # Texto explicativo para griego
    griego_text = tk.Label(
        marco,
        text="Espíritu suave: >  Espíritu áspero: <\n"
             "Acento agudo: ´  Acento grave: `  Acento circunflejo: ^\n"
             "Iota suscrita: '",
        font=("Cambria", 10),
        bg="white",
        justify="left",
        anchor="w"
    )
    griego_text.pack(anchor="w", pady=(0, 20))  # Separación inferior

    # Subtítulo "Latín" alineado a la izquierda
    latin_label = tk.Label(
        marco,
        text="Latín",
        font=("Cambria", 13, "bold"),
        bg="white",
        anchor="w"
    )
    latin_label.pack(anchor="w", pady=(0, 10))  # Separación inferior

    # Texto explicativo para latín
    latin_text = tk.Label(
        marco,
        text="Vocal larga: -a  Vocal breve: *a",
        font=("Cambria", 10),
        bg="white",
        justify="left",
        anchor="w"
    )
    latin_text.pack(anchor="w")

def version():
    # Crear una nueva ventana de ayuda
    version_ventana = tk.Toplevel()
    version_ventana.title("Version")  # Título de la nueva ventana
    version_ventana.resizable(False, False)

    # Establecer icono
    icon_path = os.path.join(getattr(sys, '_MEIPASS', os.path.abspath('.')), 'icono.ico')
    version_ventana.iconbitmap(icon_path)

    # Crear un marco con borde negro y fondo blanco
    marco = tk.Frame(
        version_ventana,
        bg="white",                  # Fondo blanco
        highlightbackground="black",  # Color del borde
        highlightthickness=2,         # Grosor del borde
        padx=20,                      # Padding interno horizontal
        pady=20                       # Padding interno vertical
    )
    marco.pack(padx=10, pady=10, fill="both", expand=True)

    # Título principal "Caracteres Especiales" centrado
    titulo_label = tk.Label(
        marco,
        text="ACTUALIZACIONES", 
        font=("Cambria", 16, "bold"),
        bg="white",
        anchor="center"
    )
    titulo_label.pack(fill="x", pady=(0, 10))  # Centrando el título y separando del siguiente contenido

    # Subtítulo "Griego" alineado a la izquierda
    v101_label = tk.Label(
        marco,
        text="1.0.1",
        font=("Cambria", 13, "bold"),
        bg="white",
        anchor="w"
    )
    v101_label.pack(anchor="w", pady=(0, 10))  # Separación inferior

    # Texto explicativo para griego
    v101_text = tk.Label(
        marco,
        text="-Nueva combinación de teclas para cambiar el teclado (Alt+Y)\n"
            "-Nuevo menú con páginas de ayuda y de versión\n"
            "-Sistema de 3 teclados: Normal, Latín, Griego\n"
            "-Griego: vocales con modificadores (espíritus, acentos...) en Unicode\n"
            "-Latín: teclado para la escritura de vocales largas (-a) y breves (*a)",
        font=("Cambria", 10),
        bg="white",
        justify="left",
        anchor="w"
    )
    v101_text.pack(anchor="w", pady=(0, 20))  # Separación inferior

    # Subtítulo "Latín" alineado a la izquierda
    v100_label = tk.Label(
        marco,
        text="1.0.0",
        font=("Cambria", 13, "bold"),
        bg="white",
        anchor="w"
    )
    v100_label.pack(anchor="w", pady=(0, 10))  # Separación inferior

    # Texto explicativo para latín
    v100_text = tk.Label(
        marco,
        text="-Primera versión estable de la Aplicación\n"
             "-Teclado para escribir en letras griegas cualquier caracter",
        font=("Cambria", 10),
        bg="white",
        justify="left",
        anchor="w"
    )
    v100_text.pack(anchor="w")
