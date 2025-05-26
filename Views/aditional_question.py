import tkinter as tk
from PIL import Image, ImageTk  # Importar Pillow para manejar imágenes
import config as cfg  # Asegúrate de que config tenga los atributos necesarios
from dictionary import personas_logros, perfiles  # Importar el diccionario de sitios arqueológicos

class AdicionalQuestion(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg='#D9C3A0')

        # Widgets predefinidos para reutilización
        self.image_label = tk.Label(self, bg='#D9C3A0')
        try:
            # Abrir y redimensionar la imagen con Pillow
            image = Image.open(f"assets/alux-question.png")
            image = image.resize((253, 300))  # Ajusta el tamaño de la imagen
            photo = ImageTk.PhotoImage(image)

            # Actualizar el widget de imagen
            self.image_label.config(image=photo)
            self.image_label.image = photo  # Guardar referencia para evitar que se elimine la imagen
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")
        self.image_label.grid(row=0, column=0, columnspan=3, pady=10)

        self.name_label = tk.Label(self, text="Acaso", font=("Arial", 14), bg='#D9C3A0')
        self.name_label.grid(row=1, column=0, columnspan=2, pady=10)

        self.true_button = tk.Button(self, text="SI", font=("Arial", 14), width=10, bg='#8b7d68',
                                     command=self.second_search)
        self.true_button.grid(row=2, column=1, padx=10, pady=10)

        self.false_button = tk.Button(self, text="NO", font=("Arial", 14), width=10, bg='#8b7d68',
                                     command=self.next_question)
        self.false_button.grid(row=2, column=0, padx=10, pady=10)


        # self.nav_button = tk.Button(self, text="RETURN", font=("Arial", 14), width=10, bg='#8b7d68',
        #                             command=self.first_scene)
        # self.nav_button.grid(row=3, column=0, columnspan=2, pady=20)

        nav_button1 = tk.Button(self, text="<<", font=("Arial", 14), width=5, bg='#8b7d68',
                                command=self.previous_scene)
        nav_button1.grid(row=4, column=0, padx=10,pady=20, sticky="e")
        nav_button2 = tk.Button(self, text="INICIO", font=("Arial", 14), width=5, bg='#8b7d68',
                                command=self.first_scene)
        nav_button2.grid(row=4, column=1, padx=10,pady=20, sticky="w")

    def show_question(self, question_text):
        """Muestra en pantalla la pregunta actual."""
        # Reusa el mismo label que tienes para el texto
        self.name_label.config(text=question_text)

    def update_scene(self):
        """Actualiza los widgets con los datos actuales de cfg."""
        # Actualizar el nombre
        self.name_label.config(text=f"Acaso ... {cfg.adition_condition}")
        clave = (cfg.genero, cfg.obstaculo1, cfg.obstaculo2, cfg.campo, cfg.rol)
        preguntas = cfg.respuestas.get(clave, [])
        if preguntas and cfg.contador < len(preguntas):
            self.name_label.config(text=preguntas[cfg.contador])
        else:
            self.name_label.config(text="Sin preguntas adicionales")
        perfil = next((p for p in perfiles
                       if (p["genero"], p["obstaculo1"], p["obstaculo2"],
                           p["campo"], p["rol"]) == clave), None)
        preguntas = perfil.get("aditional_questions", []) if perfil else []

        # si no hay preguntas, saltamos a Answer
        if not preguntas:
            return self.controller.show_frame("Answer")

        # limpia la escena y muestra la primera pregunta:
        self.show_question(preguntas[cfg.contador])

        # Manejar la carga de la imagen con Pillow

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
        """Navegar a la siguiente pregunta."""
        clave=(cfg.genero,cfg.obstaculo1,cfg.obstaculo2,cfg.campo,cfg.rol)
        cfg.contador -= 1
        if cfg.contador >=0:
            cfg.adition_condition=cfg.respuestas[clave][cfg.contador]
            self.controller.show_frame("AdicionalQuestion")
        else:
            self.controller.show_frame("Scene4")

    def next_question(self):
        """Navegar a la siguiente pregunta."""
        clave=(cfg.genero,cfg.obstaculo1,cfg.obstaculo2,cfg.campo,cfg.rol)
        preguntas = cfg.respuestas.get(clave, [])
        cfg.contador += 1
        if cfg.contador < len(preguntas):
            # mostrar las preguntas
            self.show_question(preguntas[cfg.contador])
        else:
            clave=(cfg.genero,cfg.obstaculo1,cfg.obstaculo2,cfg.campo,cfg.rol)
            perfil = next((
                p for p in perfiles
                if p["genero"]     == cfg.genero
                and p["obstaculo1"] == cfg.obstaculo1
                and p["obstaculo2"] == cfg.obstaculo2
                and p["campo"]      == cfg.campo
                and p["rol"]        == cfg.rol
            ), None)
            if not perfil:
                # Si no encuentro perfil, vuelvo a adquisición
                return self.controller.show_frame("Adquisicion1")
    
            nombre      = perfil["name"]
            path_image  = perfil["image"]
            # coincide con tu clave JSON
            descripcion = perfil.get("descripcion") or perfil.get("description","")
            # (nombre,path_image,descripcion)=personas_logros[clave]
            cfg.nombre=nombre
            cfg.path_image=path_image
            cfg.descripcion=descripcion
            self.controller.show_frame("Answer")
            

    def second_search(self):
        # Busca SOLO el perfil que tenga aditional_questions (es decir, el "más específico")
        perfil = next((
            p for p in perfiles
            if p["genero"]     == cfg.genero
            and p["obstaculo1"] == cfg.obstaculo1
            and p["obstaculo2"] == cfg.obstaculo2
            and p["campo"]      == cfg.campo
            and p["rol"]        == cfg.rol
            and p.get("aditional_questions")  # el que tienen preguntas extra
        ), None)

        if not perfil:
            # Si por algún motivo no lo encuentra, busca el base
            perfil = next((
                p for p in perfiles
                if p["genero"]     == cfg.genero
                and p["obstaculo1"] == cfg.obstaculo1
                and p["obstaculo2"] == cfg.obstaculo2
                and p["campo"]      == cfg.campo
                and p["rol"]        == cfg.rol
            ), None)
            if not perfil:
                return self.controller.show_frame("Adquisicion1")

        cfg.nombre      = perfil["name"]
        cfg.path_image  = perfil["image"]
        cfg.descripcion = perfil.get("descripcion","")

        return self.controller.show_frame("Answer")