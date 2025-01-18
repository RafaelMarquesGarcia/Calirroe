import tkinter as tk
from pynput import keyboard
from PIL import Image, ImageTk
import os
import sys
from griego import *
from latin import *
from menu import ayuda, version

# Variables de estado del teclaod griego
pending_modifiers = []  # Lista para almacenar modificadores pendientes (espíritus, acentos, etc.)
MODIFIER_ORDER = {'spirit': 1, 'accent': 2, 'iota': 3}
selected_mode = None  # Variable global para vincular los radio buttons
alt_pressed = False  # Variable para rastrear si 'Alt' está presionado

last_key_dash = False  # Para combinar con larga (-) (para teclado Latin)
last_key_asterisk = False  # Para combinar con breve (*) (para teclado Latin)





is_custom_mapping_enabled = False

# Función para alternar entre el mapeo de teclas alt+y entre normal o griego
def toggle_keyboard_mode():
    global is_custom_mapping_enabled
    if selected_mode.get() == "latin":
        return  # No alternar si está en modo "latín"
    
    if is_custom_mapping_enabled:
        set_keyboard_mode("normal")
    else:
        set_keyboard_mode("griego")
        
    # Actualizar el radio button en la interfaz
    selected_mode.set("griego" if is_custom_mapping_enabled else "normal")


def set_keyboard_mode(mode):
    """
    Establece el modo actual del teclado según el parámetro `mode`.
    """
    global is_custom_mapping_enabled
    if mode == "griego":
        is_custom_mapping_enabled = True
    else:  # Normal y latín no usan el mapeo personalizado
        is_custom_mapping_enabled = False


def comprobar_vocales(base_letter, modifiers):
    key = base_letter + ''.join(modifiers)
    return precomposed_chars.get(key, base_letter + ''.join(modifiers))

def apply_modifiers(base_letter):
    global pending_modifiers
    organized_modifiers = sorted(pending_modifiers, key=lambda mod: MODIFIER_ORDER[mod['type']])
    modifiers = [mod['value'] for mod in organized_modifiers]
    combined_letter = comprobar_vocales(base_letter, modifiers)
    pending_modifiers = []  # Reiniciar modificadores después de aplicarlos
    return combined_letter

def on_press(key):
    global pending_modifiers, alt_pressed, last_key_dash, last_key_asterisk

    try:
        # Detectar si 'Alt' está presionado
        if key == keyboard.Key.alt_l:
            alt_pressed = True

        # Detectar la combinación 'Alt + Y'
        if alt_pressed and hasattr(key, 'char') and key.char == 'y':
            toggle_keyboard_mode()
            alt_pressed = False
            return

        # Modo griego
        if is_custom_mapping_enabled and selected_mode.get() == "griego" and hasattr(key, 'char'):
            controller = keyboard.Controller()
            char = key.char

            if char in spirits or char in accents or char == "'":
                controller.press(keyboard.Key.backspace)
                controller.release(keyboard.Key.backspace)
                if char in spirits:
                    pending_modifiers.append({'type': 'spirit', 'value': spirits[char]})
                elif char in accents:
                    pending_modifiers.append({'type': 'accent', 'value': accents[char]})
                elif char == "'":
                    pending_modifiers.append({'type': 'iota', 'value': iota_subscript[char]})
                return
            elif char in vowels_mapping:
                controller.press(keyboard.Key.backspace)
                controller.release(keyboard.Key.backspace)
                modified_char = apply_modifiers(vowels_mapping[char])
                controller.type(modified_char)
            elif char in consonants_mapping:
                controller.press(keyboard.Key.backspace)
                controller.release(keyboard.Key.backspace)
                controller.type(consonants_mapping[char])
        
        # Modo latín
        elif selected_mode.get() == "latin" and hasattr(key, 'char'):
            char = key.char
            controller = keyboard.Controller()

            if last_key_dash and char in latin_largas:
                # Sustituir '-' y la vocal por la vocal con macrón
                controller.press(keyboard.Key.backspace)
                controller.release(keyboard.Key.backspace)
                controller.type(latin_largas[char])
                last_key_dash = False  # Reiniciar el estado de '-'
                return
            elif last_key_asterisk and char in latin_breves:
                # Sustituir '*' y la vocal por la vocal breve
                controller.press(keyboard.Key.backspace)
                controller.release(keyboard.Key.backspace)
                controller.type(latin_breves[char])
                last_key_asterisk = False  # Reiniciar el estado de '*'
                return
            elif char == "-":
                # Detectar y eliminar el '-' escrito automáticamente
                controller.press(keyboard.Key.backspace)
                controller.release(keyboard.Key.backspace)
                last_key_dash = True
                last_key_asterisk = False  # Reiniciar estado de '*'
                return
            elif char == "*":
                # Detectar y eliminar el '*' escrito automáticamente
                controller.press(keyboard.Key.backspace)
                controller.release(keyboard.Key.backspace)
                last_key_asterisk = True
                last_key_dash = False  # Reiniciar estado de '-'
                return
            else:
                # Si se presiona otra tecla no válida, reinicia estados
                last_key_dash = False
                last_key_asterisk = False

        # Salir si se presiona 'Esc'
        elif key == keyboard.Key.esc:
            return False
    except AttributeError:
        pass

def on_release(key):
    global alt_pressed
    if key == keyboard.Key.alt_l:
        alt_pressed = False


def create_menu(root):
    # Crear barra de menú
    menu_bar = tk.Menu(root, bg="gray")  # Cambiar el color de fondo aquí
    
    # Menú "File"
    file_menu = tk.Menu(menu_bar, tearoff=0, bg="white", fg="black")
    file_menu.add_command(label="Ayuda", command=ayuda)
    file_menu.add_command(label="Versión", command=version)
    file_menu.add_separator()
    file_menu.add_command(label="Salir", command=root.destroy)
    menu_bar.add_cascade(label="Archivo", menu=file_menu)
    
    # Configurar la barra de menú en la ventana principal
    root.config(menu=menu_bar)

def create_gui():
    global selected_mode
    root = tk.Tk()
    root.title("Calírroe")
    root.resizable(False, False)

    icon_path = os.path.join(getattr(sys, '_MEIPASS', os.path.abspath('.')), 'icono.ico')
    root.iconbitmap(icon_path)

    # Crear barra de menú
    create_menu(root)
    

    image_frame = tk.Frame(root)
    image_frame.pack()

    image_path = os.path.join(getattr(sys, '_MEIPASS', os.path.abspath('.')), 'icono.png')
    img = Image.open(image_path)
    img = img.resize((75, 75), Image.LANCZOS)
    photo = ImageTk.PhotoImage(img)

    image_label = tk.Label(image_frame, image=photo)
    image_label.image = photo
    image_label.pack(pady=10)

    content_frame = tk.Frame(root, padx=20)
    content_frame.pack()

    title_label = tk.Label(content_frame, text="CALÍRROE", font=("Cambria", 24, "bold"))
    title_label.pack()

    welcome_text = tk.Label(
        content_frame,
        text="Bienvenido a Calírroe, un teclado para escribir con diferentes fuentes antiguas.\n"
             "Seleccione uno de entre los siguientes teclados:",
        font=("Cambria", 12),
        justify="center"
    )
    welcome_text.pack(pady=10)

    radio_frame = tk.Frame(content_frame, bg="white", highlightbackground="black", highlightcolor="black", highlightthickness=2)
    radio_frame.pack(pady=10)

    selected_mode = tk.StringVar(value="normal")

    normal_rb = tk.Radiobutton(radio_frame, text="Normal", font=("Cambria", 12), variable=selected_mode, value="normal", command=lambda: set_keyboard_mode("normal"))
    latin_rb = tk.Radiobutton(radio_frame, text="Latín", font=("Cambria", 12), variable=selected_mode, value="latin", command=lambda: set_keyboard_mode("latin"))
    griego_rb = tk.Radiobutton(radio_frame, text="Griego", font=("Cambria", 12), variable=selected_mode, value="griego", command=lambda: set_keyboard_mode("griego"))
    
    
    normal_rb.pack(side="top", padx=20, pady=10)
    latin_rb.pack(side="top", padx=20, pady=10)
    griego_rb.pack(side="top", padx=20, pady=10)

    footer_frame = tk.Frame(content_frame)
    footer_frame.pack(pady=10, anchor="center")

    help_text = tk.Label(
        footer_frame,
        text="AYUDA: \n"
             "Para cambiar de teclado presione el botón correspondiente. \n"
             "Para alternar rápidamente entre Griego y Normal presione ALT+Y \n",
        font=("Cambria", 10),
        justify="center"
    )
    help_text.pack(pady=10)

    cp_text = tk.Label(
        footer_frame,
        text="© Rafael Marqués García 2024\n"
             "Versión: 1.0.1",
        font=("Cambria", 12),
        justify="center"
    )
    cp_text.pack(pady=10)

    root.mainloop()


def setup_keyboard_listener():
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()

def main():
    setup_keyboard_listener()
    create_gui()

if __name__ == "__main__":
    main()
