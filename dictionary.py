import json, os

DATA_FILE = 'personas_logros.json'

# # Si ya existe, leemos la lista de perfiles; si no, partimos de una lista vacía
# if os.path.exists(DATA_FILE):
#     with open(DATA_FILE, 'r', encoding='utf-8') as f:
#         perfiles = json.load(f)
# else:
#     perfiles = [
#         # Opcional: perfiles “de fábrica”
#         {
#             "genero": "Femenino",
#             "obstaculo1": "Condición médica",
#             "obstaculo2": "Sin extremidad/es",
#             "campo": "Deportes",
#             "rol": "Atleta",
#             "name": "Wilma Rudolph",
#             "image": "imagenes/wilma.jpg",
#             "descripcion": "Superó polio y ganó 3 oros en Roma 1960."
#         },
#         # … más objetos iniciales si quieres
#     ]
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        perfiles = json.load(f)
else:
    perfiles = [
        # …tus perfiles “de fábrica”…
        {
            "genero": "Femenino",
            "obstaculo1": "Condición médica",
            "obstaculo2": "Sin extremidad/es",
            "campo": "Deportes",
            "rol": "Atleta",
            "name": "Wilma Rudolph",
            "image": "imagenes/wilma.jpg",
            "descripcion": "Superó polio y ganó 3 oros en Roma 1960."
        }
    ]

# Reconstruimos el diccionario de lookup
personas_logros = {
    (
        p["genero"],
        p["obstaculo1"],
        p["obstaculo2"],
        p["campo"],
        p["rol"],
    ): (
        p["name"],
        p["image"],
        p.get("descripcion") or p.get("description", "")
    )
    for p in perfiles
}

personas_logros = {
    ("Masculino", "Condición médica", "Enanismo", "Deportes", "Futbolista"): ("Messi", "imagenes/Futbolista/mesi.jpg", "INFO"),
    ("Femenino", "Exclusión social", "Discriminación", "Ciencias", "Matemático"): ("Katherine Johnson", "imagenes/Matematico/katheri.jpg", "INFO"),
}