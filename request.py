import config as cfg
from dictionary import personas_logros, perfiles

def search_coincidences():
    clave = (cfg.genero, cfg.obstaculo1, cfg.obstaculo2, cfg.campo, cfg.rol)
    # Si el árbol de preguntas adicionales ya está en cfg.respuestas, salimos
    if clave in cfg.respuestas:
        return

    # Buscamos un perfil que coincida con la 5-tupla
    perfil = next(
        (p for p in perfiles
         if (p["genero"],
             p["obstaculo1"],
             p["obstaculo2"],
             p["campo"],
             p["rol"]) == clave),
        None
    )

    if not perfil:
        cfg.nombre = cfg.path_image = cfg.descripcion = ""
        return

    # Cargamos campos del perfil encontrado
    cfg.nombre      = perfil["name"]
    cfg.path_image  = perfil["image"]
    cfg.descripcion = perfil.get("descripcion", "")

    # Sólo para depuración
    print(f"Nombre: {cfg.nombre}")
    print(f"Path de la imagen: {cfg.path_image}")
    print(f"Descripción: {cfg.descripcion}")

def second_search():
    """
    Búsqueda tras responder preguntas adicionales.
    Aquí volvemos a cargar el mismo perfil base (ignorando la respuesta extra)
    y actualizamos cfg con sus datos.
    """
    clave_base = (
        cfg.genero,
        cfg.obstaculo1,
        cfg.obstaculo2,
        cfg.campo,
        cfg.rol
    )

    perfil = next(
        (p for p in perfiles
         if (p["genero"],
             p["obstaculo1"],
             p["obstaculo2"],
             p["campo"],
             p["rol"]) == clave_base),
        None
    )
    if not perfil:
        cfg.nombre = cfg.path_image = cfg.descripcion = ""
        return

    cfg.nombre      = perfil["name"]
    cfg.path_image  = perfil["image"]
    cfg.descripcion = perfil.get("descripcion", "")
	
def buscar_perfil():
    for p in perfiles:
        if (
            p["genero"]     == cfg.genero and
            p["obstaculo1"] == cfg.obstaculo1 and
            p["obstaculo2"] == cfg.obstaculo2 and
            p["campo"]      == cfg.campo and
            p["rol"]        == cfg.rol
        ):
            cfg.nombre      = p["name"]
            cfg.path_image  = p["image"]
            cfg.descripcion       = p["descripcion"]
            return
    # Si no lo encontramos:
    cfg.nombre = cfg.bio = cfg.logro = "No se encontró un perfil que coincida."
    cfg.path_image = None