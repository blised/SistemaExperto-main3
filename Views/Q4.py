import tkinter as tk
from PIL import Image, ImageTk  # Importar Pillow para manejar imágenes
import config as cfg  


class Scene4(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg='#D9C3A0')  # Establecer el fondo del frame
        self.grid_columnconfigure(0, weight=1, minsize=100)  # Primera columna  
        self.grid_columnconfigure(1, weight=1, minsize=100)  # Segunda columna

        self.dynamic_buttons = []  
        self.image_label = tk.Label(self, bg='#D9C3A0')
        try:
            # Abrir y redimensionar la imagen con Pillow
            image = Image.open(f"assets/bot11.png")
            image = image.resize((253, 300))  # Ajusta el tamaño de la imagen
            photo = ImageTk.PhotoImage(image)

            # Actualizar el widget de imagen
            self.image_label.config(image=photo)
            self.image_label.image = photo  # Guardar referencia para evitar que se elimine la imagen
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")
        self.image_label.grid(row=0, column=0, columnspan=3, pady=10)
        # Título con la pregunta
        question_label = tk.Label(self, text="¿Cuál es el campo donde se desarrolló la persona?",
                                  font=("Arial", 14), bg='#D9C3A0')
        question_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="n")


    def update_scene(self):
        for button in self.dynamic_buttons:
            button.destroy()  # Elimina los botones previos

        self.dynamic_buttons.clear()  # Limpia la lista

        row = 2
        column = 0
        for campo in cfg.campos:
            if campo == list(cfg.campos.keys())[-1]:
                button = tk.Button(self, text=campo, font=("Arial", 12), width=15, bg='#8b7d68',
                                            command=lambda c=campo: self.on_campo_selected(c))
                button.grid(row=row, column=column, columnspan=2, padx=10, pady=20)
                self.dynamic_buttons.append(button)  # Guarda el botón en la lista
            else:
                button = tk.Button(self, text=campo, font=("Arial", 12), width=15, bg='#8b7d68',
                                command=lambda c=campo: self.on_campo_selected(c))
                button.grid(row=row, column=column, padx=10, pady=20)
                self.dynamic_buttons.append(button)  # Guarda el botón en la lista
                column += 1
                if column > 1:  # Cambiar a la siguiente fila después de 2 botones
                    column = 0
                    row += 1

        # Botones de navegación
        nav_button1 = tk.Button(self, text="←", font=("Arial", 14), width=5, bg='#8b7d68',
                                command=self.previous_scene)
        nav_button1.grid(row=row + 1, column=0, pady=20)
        self.dynamic_buttons.append(nav_button1)
        nav_button2 = tk.Button(self, text="Home", font=("Arial", 14), width=5, bg='#8b7d68',
                                command=self.first_scene)
        nav_button2.grid(row=row + 1, column=1, pady=20)
        self.dynamic_buttons.append(nav_button2)

    def on_campo_selected(self, campo):
        """Acción al seleccionar una cultura."""
        cfg.campo = campo
        self.controller.show_frame("Scene5")
        print(f"Cultura seleccionada: {campo}")
        # Aquí puedes manejar el cambio de escena u otra acción

    def previous_scene(self):
        """Cambiar a la escena anterior."""
        print("Navegar a la escena anterior")
        self.controller.show_frame("Scene3")
        

    def first_scene(self):
        """Cambiar a la primera escena."""
        print("Navegar a la primera escena")
        self.controller.show_frame("Main")


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
