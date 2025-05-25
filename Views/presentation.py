import tkinter as tk
from PIL import Image, ImageTk  # Importar Pillow para manejar imágenes
import config as cfg  


class Main(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg='#D9C3A0')  # Establecer el fondo del frame
        self.grid_columnconfigure(0, weight=1, minsize=100)  # Primera columna  
        self.grid_columnconfigure(1, weight=1, minsize=100)  # Segunda columna

        self.image_label = tk.Label(self, bg='#D9C3A0')
        try:
            # Abrir y redimensionar la imagen con Pillow
            image = Image.open(f"assets/presentacion.png")
            image = image.resize((253, 300))  # Ajusta el tamaño de la imagen
            photo = ImageTk.PhotoImage(image)

            # Actualizar el widget de imagen
            self.image_label.config(image=photo)
            self.image_label.image = photo  # Guardar referencia para evitar que se elimine la imagen
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")
        self.image_label.grid(row=0, column=0, columnspan=3, pady=10)
        # Título con la pregunta
        question_label = tk.Label(self, text="Bienvenido a la \"La guia de la inclusion\"",
                                  font=("Arial", 14, "bold"), bg='#D9C3A0')
        question_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="n")
        question_label = tk.Label(self, text="Sistema diseñado para el la recolecion y almacenamiento de las personas sobresalientes en su campo apesar de dificultades sociales o medicas",
                                  font=("Arial", 12), bg='#D9C3A0', wraplength=490)
        question_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="n")
        button = tk.Button(self, text="INICIAR", font=("Arial", 12), width=15, bg='#8b7d68',
                                            command=self.begin_process)
        button.grid(row=3, column=0, columnspan=2, padx=1, pady=1)
       
    def begin_process(self):
        self.controller.show_frame("Scene1")


# if __name__ == "__main__":
#     # Ejemplo mínimo para probar
#     class App(tk.Tk):
#         def __init__(self):
#             super().__init__()
#             self.title("Cultura Quiz")
#             self.geometry("400x500")
#             container = tk.Frame(self)
#             container.pack(fill="both", expand=True)
#             self