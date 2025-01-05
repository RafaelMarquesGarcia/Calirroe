import tkinter as tk
from tkinter import messagebox
from pynput import keyboard
from PIL import Image, ImageTk
import os
import sys

# Diccionarios para letras griegas
consonants_mapping = {
    'b': 'β', 'c': 'χ', 'd': 'δ', 'f': 'φ', 'g': 'γ', 'j': 'ς', 'k': 'κ',
    'l': 'λ', 'm': 'μ', 'n': 'ν', 'p': 'π', 'q': 'θ', 'r': 'ρ', 's': 'σ',
    't': 'τ', 'v': 'ϝ', 'y': 'ψ', 'x': 'ξ', 'z': 'ζ',
    'B': 'Β', 'C': 'Χ', 'D': 'Δ', 'F': 'Φ', 'G': 'Γ', 'J': 'Σ', 'K': 'Κ',
    'L': 'Λ', 'M': 'Μ', 'N': 'Ν', 'P': 'Π', 'Q': 'Θ', 'R': 'Ρ', 'S': 'Σ',
    'T': 'Τ', 'V': 'Ϝ', 'Y': 'Ψ', 'X': 'Ξ', 'Z': 'Ζ'
}

vowels_mapping = {
    # Minúsculas
    'a': 'α', 'e': 'ε', 'i': 'ι', 'o': 'ο', 'u': 'υ', 'h': 'η', 'w': 'ω',
    # Mayúsculas
    'A': 'Α', 'E': 'Ε', 'I': 'Ι', 'O': 'Ο', 'U': 'Υ', 'H': 'Η', 'W': 'Ω'
}

# Combinaciones posibles
spirits = {'>': '̓', '<': '̔'}  # Espíritu suave y áspero
accents = {"´": '́', '`': '̀', '^': '͂', "´": '́'}  # Agudo, grave y circunflejo (agudo con alternativa "´")
iota_subscript = {"'": 'ͅ'}  # Iota suscrita cambiada a ' (tecla derecha del 0)

# Variables de estado
is_custom_mapping_enabled = False
pending_modifiers = []  # Lista para almacenar modificadores pendientes (espíritus, acentos, etc.)

# Orden de los modificadores
MODIFIER_ORDER = {'spirit': 1, 'accent': 2, 'iota': 3}

# Función para alternar entre el mapeo de teclas (normal o griego)
def set_keyboard_mode(mode):
    global is_custom_mapping_enabled
    if mode == "griego":
        is_custom_mapping_enabled = True
    else:
        is_custom_mapping_enabled = False

# Función para construir una letra con combinaciones
# Reorganiza los modificadores según el orden correcto antes de aplicarlos
def apply_modifiers(base_letter):
    global pending_modifiers
    organized_modifiers = sorted(pending_modifiers, key=lambda mod: MODIFIER_ORDER[mod['type']])
    combined_letter = base_letter
    for modifier in organized_modifiers:
        combined_letter += modifier['value']
    pending_modifiers = []  # Reiniciar modificadores después de aplicarlos
    return combined_letter

# Función que reemplaza la tecla presionada por el símbolo mapeado
def on_press(key):
    global pending_modifiers

    try:
        if is_custom_mapping_enabled and hasattr(key, 'char'):
            controller = keyboard.Controller()
            char = key.char

            if char in spirits or char in accents or char == "'":
                # Eliminar carácter especial del buffer
                controller.press(keyboard.Key.backspace)
                controller.release(keyboard.Key.backspace)

                # Añadir el modificador pendiente con su tipo
                if char in spirits:
                    pending_modifiers.append({'type': 'spirit', 'value': spirits[char]})
                elif char in accents:
                    pending_modifiers.append({'type': 'accent', 'value': accents[char]})
                elif char == "'":
                    pending_modifiers.append({'type': 'iota', 'value': iota_subscript[char]})
                return
            elif char in vowels_mapping:
                # Aplicar modificadores a vocal
                controller.press(keyboard.Key.backspace)
                controller.release(keyboard.Key.backspace)
                modified_char = apply_modifiers(vowels_mapping[char])
                controller.type(modified_char)
            elif char in consonants_mapping:
                # Escribir consonante directamente
                controller.press(keyboard.Key.backspace)
                controller.release(keyboard.Key.backspace)
                controller.type(consonants_mapping[char])
        elif key == keyboard.Key.esc:
            # Finaliza el programa si se presiona 'Esc'
            return False
    except AttributeError:
        # Ignorar otras teclas como Shift, Ctrl, etc.
        pass

# Configuración de la interfaz gráfica (Tkinter)
def create_gui():
    root = tk.Tk()
    root.title("Calírroe")  # Título de la ventana
    root.resizable(False, False)


    # Ruta del icono, compatible con PyInstaller
    icon_path = os.path.join(
        getattr(sys, '_MEIPASS', os.path.abspath('.')),
        'icono.ico'
    )
    root.iconbitmap(icon_path)

    # Crear un marco para la imagen
    image_frame = tk.Frame(root)
    image_frame.pack()

    # Ruta de la imagen, compatible con PyInstaller
    image_path = os.path.join(
        getattr(sys, '_MEIPASS', os.path.abspath('.')),
        'icono.png'
    )

    # Cargar y redimensionar la imagen
    img = Image.open(image_path)
    img = img.resize((75, 75), Image.LANCZOS)  # Ajusta el tamaño según lo necesites
    photo = ImageTk.PhotoImage(img)

    # Crear un label para la imagen
    image_label = tk.Label(image_frame, image=photo)
    image_label.image = photo  # Evitar recolección de basura
    image_label.pack(pady=10)


    # Crear un marco para el resto del contenido
    content_frame = tk.Frame(root, padx=20)
    content_frame.pack()

    title_label = tk.Label(content_frame, text="CALÍRROE", font=("Cambria", 24, "bold"))
    title_label.pack()

    # Texto de bienvenida
    welcome_text = tk.Label(
        content_frame,
        text="Bienvenido a Calírroe, un teclado para escribir con diferentes fuentes antiguas.\n"
             "Seleccione uno de entre los siguientes teclados:",
        font=("Cambria", 12),
        justify="center"
    )
    welcome_text.pack(pady=10)

    # Crear un marco para los radio buttons
    radio_frame = tk.Frame(content_frame, bg="white", highlightbackground="black", highlightcolor="black", highlightthickness=2)
    radio_frame.pack(pady=10)  # Centramos los botones

    # Variable que almacena el modo seleccionado en los radio buttons
    selected_mode = tk.StringVar(value="normal")  # Por defecto, "normal"

    # Radio buttons para seleccionar el modo de teclado
    normal_rb = tk.Radiobutton(radio_frame, text="Itálico", font=("Cambria", 12), variable=selected_mode, value="normal", command=lambda: set_keyboard_mode(selected_mode.get()))
    griego_rb = tk.Radiobutton(radio_frame, text="Griego", font=("Cambria", 12), variable=selected_mode, value="griego", command=lambda: set_keyboard_mode(selected_mode.get()))

    # Empaquetar los radio buttons
    normal_rb.pack(side="top", padx=20, pady=10)
    griego_rb.pack(side="top", padx=20, pady=10)

    # Crear un marco para los radio buttons
    footer_frame = tk.Frame(content_frame)
    footer_frame.pack(pady=10, anchor="center")  # Centramos los botones
    
    # Texto de ayuda
    help_text = tk.Label(
        footer_frame,
        text="AYUDA: \n"
        "Espíritu suave: > Espíritu áspero: < \n"
        "Acento agudo: ´ Acento grave: ` Acento circunflejo: ^ \n"
        "Iota suscrita: '",
        font=("Cambria", 10),
        justify="center"
    )
    help_text.pack(pady=10)

    # Copyright
    cp_text = tk.Label(
        footer_frame,
        text="© Rafael Marqués García 2024\n"
        "Versión: 1.0",
        font=("Cambria", 12),
        justify="center"
    )
    cp_text.pack(pady=10)

    # Ejecutar la interfaz gráfica
    root.mainloop()

# Configuración del listener global para capturar las teclas
def setup_keyboard_listener():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()  # Iniciar el listener en segundo plano

# Función principal
def main():
    setup_keyboard_listener()  # Configurar el listener de teclas
    create_gui()  # Crear la interfaz gráfica

if __name__ == "__main__":
    main()
