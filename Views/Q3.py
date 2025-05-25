import tkinter as tk
from PIL import Image, ImageTk  # Importar Pillow para manejar imágenes
import config as cfg  
from dictionary import personas_logros

class Scene3(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg='#D9C3A0')
        self.grid_columnconfigure(0, weight=1, minsize=250)  # Primera columna  
        self.grid_columnconfigure(1, weight=1, minsize=250)  # Segunda columna

        self.dynamic_buttons = []  # Lista para almacenar botones dinámicos
        self.image_label = tk.Label(self, bg='#D9C3A0')
        try:
            # Abrir y redimensionar la imagen con Pillow
            image = Image.open(f"assets/alux-question2.png")
            image = image.resize((253, 300))  # Ajusta el tamaño de la imagen
            photo = ImageTk.PhotoImage(image)

            # Actualizar el widget de imagen
            self.image_label.config(image=photo)
            self.image_label.image = photo  # Guardar referencia para evitar que se elimine la imagen
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")
        self.image_label.grid(row=0, column=0, columnspan=3, pady=10)
        
        question_label = tk.Label(self, text="¿A qué se dedicó principalmente?", font=("Arial", 14), bg='#D9C3A0', wraplength=490)
        question_label.grid(row=1, column=0, columnspan=2, pady=10)
        

        

    def update_scene(self):
        """Actualiza los botones dinámicamente basados en `cfg.cultura`."""
        for button in self.dynamic_buttons:
            button.destroy()  # Elimina los botones previos

        self.dynamic_buttons.clear()  # Limpia la lista

        row, column = 2, 0
        for opc2 in cfg.sufrio.get(cfg.obstaculo1, []):
            button = tk.Button(self, text=opc2, font=("Arial", 12),width=15, bg='#8b7d68',
                               command=lambda e=opc2: self.on_opciones_selected(e))
            button.grid(row=row, column=column, padx=10, pady=5)
            self.dynamic_buttons.append(button)  # Guarda el botón en la lista
            column += 1
            if column > 1:
                column = 0
                row += 1
        
        nav_button1 = tk.Button(self, text="<<", font=("Arial", 14), width=5, bg='#8b7d68',
                                command=self.previous_scene)
        nav_button1.grid(row=row + 1, column=0, padx=10, pady=20, sticky="e")
        self.dynamic_buttons.append(nav_button1)
        nav_button2 = tk.Button(self, text="X", font=("Arial", 14), width=5, bg='#8b7d68',
                                command=self.first_scene)
        nav_button2.grid(row=row + 1, column=1, padx=10, pady=20, sticky="w")
        self.dynamic_buttons.append(nav_button2)

    def on_opciones_selected(self, opc2):
        """Acción al seleccionar la geografia."""
        cfg.obstaculo2 = opc2 
        self.controller.show_frame("Scene4")
        print(f"Geografia seleccionada: {opc2}")

    def previous_scene(self):
        """Cambiar a la escena anterior."""
        print("Navegar a la escena anterior")
        self.controller.show_frame("Scene2")
        

    def first_scene(self):
        """Cambiar a la primera escena."""
        print("Navegar a la primera escena")
        self.controller.show_frame("Main")