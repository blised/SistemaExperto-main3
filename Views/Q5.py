import tkinter as tk
from PIL import Image, ImageTk  # Importar Pillow para manejar imágenes
import config as cfg  
from dictionary import personas_logros, perfiles

class Scene5(tk.Frame):
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
        for rol in cfg.campos.get(cfg.campo, []):
            button = tk.Button(self, text=rol, font=("Arial", 12),width=15, bg='#8b7d68',
                               command=lambda e=rol: self.on_rol_selected(e))
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

    def on_rol_selected(self, rol):
        """Acción al seleccionar la geografia."""
        cfg.rol = rol
        clave=(cfg.genero,cfg.obstaculo1,cfg.obstaculo2,cfg.campo,cfg.rol)
        print(clave)
        # cfg.cultura = cfg.estado = cfg.geography = cfg.estructura = ""
        # 1️ ¿Hay aditional_questions? — si las encontramos, vamos a esa escena
        perfil = next((
            p for p in perfiles
            if (p["genero"],p["obstaculo1"],p["obstaculo2"],p["campo"],p["rol"]) == clave
            and p.get("aditional_questions")
        ), None)
        if perfil:
            cfg.respuestas = { clave: perfil["aditional_questions"] }
            cfg.contador   = 0
            return self.controller.show_frame("AdicionalQuestion")

        # 2️ Si no, buscamos el perfil base
        perfil = next((
            p for p in perfiles
            if (p["genero"],p["obstaculo1"],p["obstaculo2"],p["campo"],p["rol"]) == clave
        ), None)
        if perfil:
            cfg.nombre      = perfil["name"]
            cfg.path_image  = perfil["image"]
            cfg.descripcion = perfil.get("descripcion","")
            return self.controller.show_frame("Answer")

        # 3 Si no existe, vamos a Adquisicion1
        return self.controller.show_frame("Adquisicion1")

    def previous_scene(self):
        """Cambiar a la escena anterior."""
        print("Navegar a la escena anterior")
        cfg.respuestas.clear()
        cfg.contador = 0
        self.controller.show_frame("Scene4")
        

    def first_scene(self):
        """Cambiar a la primera escena."""
        print("Navegar a la primera escena")
        cfg.respuestas.clear()
        cfg.contador = 0
        self.controller.show_frame("Main")