# from dataclasses import dataclass, asdict

# @dataclass
# class Config:
#     """
#     Configuración general de la aplicación.
#     Pensada para serializarse fácilmente y ser legible por humanos.
#     """
#     nombre_app: str         # Nombre visible de la aplicación
#     entorno: str            # 'producción', 'desarrollo', 'test'
#     debug: bool             # Activar modo debug/logs extendidos
#     puerto: int             # Puerto de escucha del servidor
#     base_datos_url: str     # URL de conexión a la base de datos

#     def como_dict(self):
#         """
#         Devuelve la configuración como diccionario.
#         Útil para exportar a JSON, YAML o logs.
#         """
#         return asdict(self)
# # Ejemplo de uso
# cfg = Config(
#     nombre_app="Plataforma Inmobiliaria",
#     entorno="desarrollo",
#     debug=True,
#     puerto=8080,
#     base_datos_url="postgresql://usuario:clave@localhost:5432/inmuebles"
# )

# print(cfg.como_dict())

# dataclass Config + constructor desde dict

from dataclasses import dataclass, asdict

@dataclass
class Config:
    """
    Configuración general de la aplicación.
    Pensada para serializarse fácilmente y ser legible.
    """
    nombre_app: str         # Nombre visible de la aplicación
    entorno: str            # 'producción', 'desarrollo', 'test'
    debug: bool             # Activar modo debug/logs extendidos
    puerto: int             # Puerto de escucha del servidor
    base_datos_url: str     # URL de conexión a la base de datos

    def como_dict(self):
        """
        Devuelve la configuración como diccionario.
        Útil para exportar a JSON, YAML o logs.
        """
        return asdict(self)

    @classmethod
    def desde_dict(cls, datos: dict):
        """
        Crea una instancia de Config a partir de un diccionario.
        Usa dicts para construir DataFrames.
        """
        return cls(**datos)
# Ejemplo de uso
# Diccionario recibido (por ejemplo desde JSON, formulario o archivo)
datos_config = {
    "nombre_app": "Plataforma Inmobiliaria",
    "entorno": "producción",
    "debug": False,
    "puerto": 443,
    "base_datos_url": "postgresql://usuario:clave@dbserver:5432/inmuebles"
}

# Crear instancia desde dict
cfg = Config.desde_dict(datos_config)

# Mostrar como diccionario
print(cfg.como_dict())
