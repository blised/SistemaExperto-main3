import tkinter as tk
from PIL import Image, ImageTk  # Importar Pillow para manejar imágenes
import config as cfg  # Asegúrate de que config tenga los atributos necesarios

class AnswerDetails(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg='#D9C3A0')
        self.grid_columnconfigure(0, weight=1, minsize=75)  # Primera columna  
        self.grid_columnconfigure(1, weight=1, minsize=50)  # Segunda columna
        self.grid_columnconfigure(2, weight=1, minsize=75)  # Segunda columna

        # Widgets predefinidos para reutilización
        self.image_label = tk.Label(self, bg='#D9C3A0')
        self.image_label.grid(row=0, column=0, columnspan=3, pady=10)

        self.name_label = tk.Label(self, text="Nombre", font=("Arial", 14, "bold"), bg='#D9C3A0')
        self.name_label.grid(row=1, column=0, columnspan=3, pady=10)

        self.descripcion_label = tk.Label(self, text="Descripción", font=("Arial", 12), bg='#D9C3A0', wraplength=500, justify="left")
        self.descripcion_label.grid(row=2, column=0, columnspan=3, pady=10)

         #botones de navegacion
        self.nav_button = tk.Button(self, text="<<", font=("Arial", 14), width=5, bg='#8b7d68',
                                    command=self.previous_scene)
        self.nav_button.grid(row=3, column=0, pady=20, sticky="e")

        self.nav_button = tk.Button(self, text="Home", font=("Arial", 14), width=5, bg='#8b7d68',
                                    command=self.first_scene)
        self.nav_button.grid(row=3, column=1, pady=20)
        
        self.nav_button = tk.Button(self, text="Add", font=("Arial", 14), width=5, bg='#8b7d68',
                                    command=self.append_adquisicion)
        self.nav_button.grid(row=3, column=2, pady=20, sticky="w")




    def update_scene(self):
        """Actualiza los widgets con los datos actuales de cfg."""
        # Actualizar el nombre
        self.name_label.config(text=cfg.nombre)
        self.name_label.config(text=self.name_label.cget("text").upper())

        # Manejar la carga de la imagen con Pillow
        try:
            # Abrir y redimensionar la imagen con Pillow
            image = Image.open(cfg.path_image)
            #image = image.resize((float(image.height), 200))  # Ajusta el tamaño de la imagen
            fixed_height = 200
            image = image.resize((int(image.width * (fixed_height / image.height)), fixed_height))
            photo = ImageTk.PhotoImage(image)

            # Actualizar el widget de imagen
            self.image_label.config(image=photo)
            self.image_label.image = photo  # Guardar referencia para evitar que se elimine la imagen
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")  # Mostrar el error en la consola

        # Actualizar la descripción
        self.descripcion_label.config(text=cfg.descripcion)

    def first_scene(self):
        """Navegar a la primera escena."""
        cfg.nombre = ""
        cfg.path_image = ""
        cfg.descripcion = ""
        cfg.obstaculo1 = ""
        cfg.obstaculo2 = ""
        cfg.campo = ""
        cfg.rol = ""
        cfg.genero = ""
        cfg.adition_condition = ""
        self.controller.show_frame("Main")

    def previous_scene(self):
        """Cambiar a la escena anterior."""
        print("Navegar a la escena anterior")
        self.controller.show_frame("Answer")

    def append_adquisicion(self):
        """Navegar a la primera escena."""
        self.controller.show_frame("Adquisicion2")
