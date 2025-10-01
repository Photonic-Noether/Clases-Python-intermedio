def filtrar_por_patron(nombres, patron):
    return [nombre for nombre in nombres if nombre.lower().startswith(patron.lower())]
