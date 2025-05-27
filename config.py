campos = {
    "Ciencias": ["Matemático", "Físico", "Químico"],
    "Artes": ["Escritor", "Cantante", "Actor"],
    "Deportes": ["Futbolista", "Atleta", "Peleador"],
}

sufrio = {
    "Exclusión social": ["Discriminación", 
                         "Racismo", 
                         "Genero/LGBTQIA+", 
                         ],
    "Condición médica": ["Enfermedades Crónicas", 
                         "Trastorno",
                         "Sin extremidad/es"]
}

generos = ["Masculino", "Femenino"]
respuestas={
	#("Masculino","Condición médica","Ciencias","Físico"): ["descripcion"]
}

#config.py
obstaculo1: str = "" 
obstaculo2: str = "" 
campo: str = "" 
rol: str = "" 
genero: str = "" 

# Para el resultado final
nombre: str = ""
path_image: str = ""
descripcion: str = ""

######
contador=0
adition_condition=""

