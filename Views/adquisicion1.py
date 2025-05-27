import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import json, os, shutil
import config as cfg
from dictionary import personas_logros, perfiles, DATA_FILE

class Adquisicion1(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg='#D9C3A0')  # Fondo beige como en la UI
        self.grid_columnconfigure(0, weight=1, minsize=75)
        self.grid_columnconfigure(1, weight=1, minsize=50)
        self.grid_columnconfigure(2, weight=1, minsize=75)
        # Variables para almacenar datos
        self.name_var = tk.StringVar()
        self.descripcion_var = tk.StringVar()
        self.image_path = None  # Para almacenar la ruta de la imagen seleccionada

        self.image_label = tk.Label(self, bg='#D9C3A0')
        try:
            # Abrir y redimensionar la imagen con Pillow
            image = Image.open(f"assets/bot2.png")
            image = image.resize((int(474/2), int(266/2)))  # Ajusta el tamaño de la imagen
            photo = ImageTk.PhotoImage(image)

            # Actualizar el widget de imagen
            self.image_label.config(image=photo)
            self.image_label.image = photo  # Guardar referencia para evitar que se elimine la imagen
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")
        self.image_label.grid(row=0, column=0, columnspan=3, pady=10)
        # Título
        title_label = tk.Label(self, text="Oops!!\nParece que no conocemos a la persona.",
                               font=("Arial", 16, "bold"), bg='#D9C3A0', fg="black", justify="left")
        title_label.grid(row=1, column=0, columnspan=3, sticky="w", padx=20, pady=10)

        # Subtítulo
        subtitle_label = tk.Label(self, text="Ayúdanos a identificarlo con los pasos que se presentan a continuación",
                                  font=("Arial", 12), bg='#D9C3A0', fg="black", justify="left")
        subtitle_label.grid(row=2, column=0, columnspan=3, sticky="w", padx=20)


        # Campo para ingresar el nombre
        name_label = tk.Label(self, text="Ingresa el nombre", font=("Arial", 12, "bold"),
                              bg='#D9C3A0', fg="black", anchor="w")
        name_label.grid(row=4, column=0, columnspan=3, sticky="w", padx=20, pady=(10, 0))
        self.name_entry = tk.Entry(self, textvariable=self.name_var, font=("Arial", 12), width=30, background="#8b7d68")
        self.name_entry.grid(row=5, column=0, columnspan=3, padx=20, pady=5)

        # Botón para subir imagen
        image_button_label = tk.Label(self, text="Sube una Imagen", font=("Arial", 12, "bold"),
                                      bg='#D9C3A0', fg="black", anchor="w")
        image_button_label.grid(row=6, column=0, columnspan=3, sticky="w", padx=20, pady=(10, 0))
        self.image_button = tk.Button(self, text="📷", font=("Arial", 14), bg="#8b7d68", width=25, relief="solid",
                                 command=self.upload_image)
        self.image_button.grid(row=7, column=0, columnspan=3, padx=20, pady=5)

        # Campo para ingresar descripción
        descripcion_label = tk.Label(self, text="Ingresa una breve descripción", font=("Arial", 12, "bold"),
                                     bg='#D9C3A0', fg="black", anchor="w")
        descripcion_label.grid(row=8, column=0, columnspan=3, sticky="w", padx=20, pady=(10, 0))
        descripcion_text = tk.Text(self, font=("Arial", 12),background="#8b7d68" ,height=5, width=30, wrap="word")
        descripcion_text.grid(row=9, column=0, columnspan=3, padx=20, pady=5)
        self.descripcion_text_widget = descripcion_text  # Referencia para obtener el texto después


        # Botones de acción
        nav_button1 = tk.Button(self, text="<<", font=("Arial", 14), bg="white", width=5, relief="solid",
                                command=self.previous_scene)
        nav_button1.grid(row=12, column=0, pady=20, padx=10, sticky="e")

        nav_button2 = tk.Button(self, text="✔", font=("Arial", 14), bg="white", width=5, relief="solid",
                                command=self.submit_data)
        nav_button2.grid(row=12, column=1, pady=20, padx=10)

        nav_button3 = tk.Button(self, text="X", font=("Arial", 14), bg="white", width=5, relief="solid",
                                command=self.cancel)
        nav_button3.grid(row=12, column=2, pady=20, padx=10, sticky="w")

        self.nav_button = tk.Button(self, text="Home", font=("Arial", 14), bg="white", width=5, relief="solid",
                                    command=self.first_scene)
        self.nav_button.grid(row=16, column=2, pady=20, padx=10, sticky="w")

    def upload_image(self):
        """Abrir un diálogo para seleccionar una imagen."""
        file_path = filedialog.askopenfilename(filetypes=[("Imagenes", "*.png;*.jpg;*.jpeg;*.gif")])
        self.image_button.config(text="📷✔")
        if file_path:
            self.image_path = file_path
            # Crear la carpeta 'imagenes' si no existe


            # Actualizar la etiqueta de la imagen
            self.image_label.config(text=f"Imagen: {os.path.basename(file_path)}")
            # self.image_label.config(text=f"Imagen: {file_path.split('/')[-1]}")

    def previous_scene(self):
        """Cambiar a la escena anterior."""
        print("Navegar a la escena anterior")
        self.controller.show_frame("Scene5")

    def submit_data(self):
        """Obtener los datos de los inputs y mostrar un mensaje."""
        name = self.name_var.get()
        descripcion = self.descripcion_text_widget.get("1.0", tk.END).strip()

        if not name or not descripcion or not self.image_path:
            messagebox.showerror("Error", "Por favor, completa todos los campos y sube una imagen.")
            return

        # Aquí puedes manejar los datos recolectados
        print(f"Nombre: {name}")
        print(f"Descripción: {descripcion}")
        print(f"Personas con logros: {personas_logros}")
        print(f"Ruta de la imagen: {self.image_path}")

        if not os.path.exists('imagenes'):
            os.makedirs('imagenes')
        # Copiar la imagen a la carpeta 'imagenes'
        destination_path = os.path.join('imagenes', os.path.basename(self.image_path))
        shutil.copy(self.image_path, destination_path)
        # personas_logros[(cfg.genero,cfg.obstaculo1,cfg.obstaculo2,
        #                  cfg.campo,cfg.rol)]=(name,destination_path,descripcion)
        # Se pasa una clave que tiene los atributos de la personas
        # luego eso se guarda en el diccionario (baseDatos)
        # key = (cfg.genero, cfg.obstaculo1, cfg.obstaculo2, cfg.campo, cfg.rol)
        # personas_logros[key] = (name, destination_path, descripcion)
        print(f"Datos guardados: {personas_logros}")
        messagebox.showinfo("Éxito", "Los datos se han enviado correctamente.")
        nuevo = {
            "genero":      cfg.genero,
            "obstaculo1":  cfg.obstaculo1,
            "obstaculo2":  cfg.obstaculo2,
            "campo":       cfg.campo,
            "rol":         cfg.rol,
            "name":        name,#self.name_var.get(),
            "image":       destination_path,
            "descripcion": descripcion #self.desc_text.get("1.0", "end").strip()
        }

        # agregar a la lista y se pone en el JSON
        perfiles.append(nuevo)
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(perfiles, f, ensure_ascii=False, indent=2)

        # Feedback de consola
        print(f"[INFO] Perfil guardado. Total perfiles: {len(perfiles)}")

    def cancel(self):
        """Cancelar y cerrar la aplicación (puedes modificar para navegar a otra escena)."""
        self.name_entry.delete(0, tk.END)
        self.descripcion_text_widget.delete("1.0", tk.END)
        self.image_path = None
        self.controller.show_frame("Adquisicion1")

    def first_scene(self):
        """Cambiar a la primera escena."""
        print("Navegar a la primera escena")
        self.controller.show_frame("Main")