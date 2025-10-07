# Nivel 1: Decoradores simples: una función por verbo y ruta

ROUTES = {"GET": {}, "POST": {}, "PUT": {}, "DELETE": {}}

def get(url):
    def decorador(func):
        ROUTES["GET"][url] = func
        return func
    return decorador

def post(url):
    def decorador(func):
        ROUTES["POST"][url] = func
        return func
    return decorador

def put(url):
    def decorador(func):
        ROUTES["PUT"][url] = func
        return func
    return decorador

def delete(url):
    def decorador(func):
        ROUTES["DELETE"][url] = func
        return func
    return decorador

def execute(method, url, *args, **kwargs):
    func = ROUTES.get(method.upper(), {}).get(url)
    if func:
        return func(*args, **kwargs)
    return f"404 Not Found: {method} {url}"


# Nivel 2: Middleware: múltiples funciones por verbo y ruta

ROUTES_MW = {"GET": {}, "POST": {}, "PUT": {}, "DELETE": {}, "PATCH": {}}

def _add_route(method, url, func):
    ROUTES_MW.setdefault(method, {}).setdefault(url, []).append(func)

def get_mw(url): return lambda f: _add_route("GET", url, f) or f
def post_mw(url): return lambda f: _add_route("POST", url, f) or f
def put_mw(url): return lambda f: _add_route("PUT", url, f) or f
def delete_mw(url): return lambda f: _add_route("DELETE", url, f) or f
def patch_mw(url): return lambda f: _add_route("PATCH", url, f) or f

def execute_mw(method, url, *args, **kwargs):
    funcs = ROUTES_MW.get(method.upper(), {}).get(url, [])
    if not funcs:
        return f"404 Not Found: {method} {url}"
    resultado = None
    for f in funcs:
        resultado = f(*args, **kwargs)
    return resultado


# Nivel 3: Clase Router: múltiples enrutadores

class Router:
    def __init__(self):
        self.routes = {"GET": {}, "POST": {}, "PUT": {}, "DELETE": {}, "PATCH": {}}

    def _add(self, method, url, func):
        self.routes.setdefault(method, {}).setdefault(url, []).append(func)

    def get(self, url): return lambda f: self._add("GET", url, f) or f
    def post(self, url): return lambda f: self._add("POST", url, f) or f
    def put(self, url): return lambda f: self._add("PUT", url, f) or f
    def delete(self, url): return lambda f: self._add("DELETE", url, f) or f
    def patch(self, url): return lambda f: self._add("PATCH", url, f) or f

    def execute(self, method, url, *args, **kwargs):
        funcs = self.routes.get(method.upper(), {}).get(url, [])
        if not funcs:
            return f"404 Not Found: {method} {url}"
        resultado = None
        for f in funcs:
            resultado = f(*args, **kwargs)
        return resultado

# Nivel 4: Rutas con parámetros dinámicos como /user/{id}

import re

class RouterParam:
    def __init__(self):
        self.routes = {"GET": [], "POST": [], "PUT": [], "DELETE": [], "PATCH": []}

    def _add(self, method, path, func):
        pattern = re.sub(r"{(\w+)}", r"(?P<\1>[^/]+)", path)
        regex = re.compile(f"^{pattern}$")
        self.routes[method].append((regex, func))

    def get(self, path): return lambda f: self._add("GET", path, f) or f
    def post(self, path): return lambda f: self._add("POST", path, f) or f
    def put(self, path): return lambda f: self._add("PUT", path, f) or f
    def delete(self, path): return lambda f: self._add("DELETE", path, f) or f
    def patch(self, path): return lambda f: self._add("PATCH", path, f) or f

    def execute(self, method, url, *args, **kwargs):
        for regex, func in self.routes.get(method.upper(), []):
            match = regex.match(url)
            if match:
                return func(*args, **match.groupdict(), **kwargs)
        return f"- 404 Not Found: {method} {url}"


# Ejemplo de uso avanzado

router = RouterParam()

@router.get("/user/{id}")
def mostrar_usuario(id):
    return f"- Mostrando usuario con id: {id}"

@router.post("/user/{id}")
def actualizar_usuario(id):
    return f"- Actualizando usuario con id: {id}"

# Ejecutar rutas
if __name__ == "__main__":
    print(router.execute("GET", "/user/42"))       # → Mostrando usuario con id 42
    print(router.execute("POST", "/user/42"))      # → Actualizando usuario con id 42
    print(router.execute("DELETE", "/user/42"))    # → 404 Not Found


# CODIGOO CON COMENTARIOS EXPLICATIVOS POR NIVELES ******

# ----------------------------------------
# Nivel 1: Esto lo vimos en clase
# Decoradores básicos: cada ruta tiene una única función por verbo HTTP
# ----------------------------------------

# ROUTES se define en mayúsculas porque es una estructura global compartida.
# Aunque no es una constante estricta, se trata como tal por convención:
# - Está fuera de cualquier función o clase
# - Se usa como registro central
# - No debería redefinirse, solo modificarse su contenido
ROUTES = {"GET": {}, "POST": {}, "PUT": {}, "DELETE": {}}

# Cada decorador registra una función en el diccionario ROUTES bajo su verbo y URL
def get(url):
    def decorador(func):
        ROUTES["GET"][url] = func
        return func
    return decorador

def post(url):
    def decorador(func):
        ROUTES["POST"][url] = func
        return func
    return decorador

def put(url):
    def decorador(func):
        ROUTES["PUT"][url] = func
        return func
    return decorador

def delete(url):
    def decorador(func):
        ROUTES["DELETE"][url] = func
        return func
    return decorador

# Ejecuta la función asociada al verbo y URL, si existe
def execute(method, url, *args, **kwargs):
    func = ROUTES.get(method.upper(), {}).get(url)
    if func:
        return func(*args, **kwargs)
    return f"404 Not Found: {method} {url}"


# ----------------------------------------
# Nivel 2: Soy de los mejores de clase
# Middleware: permite múltiples funciones por ruta y verbo, ejecutadas en orden
# ----------------------------------------

# Igual que ROUTES, esta estructura se define en mayúsculas por ser global y compartida
ROUTES_MW = {"GET": {}, "POST": {}, "PUT": {}, "DELETE": {}, "PATCH": {}}

# Añade la función a una lista de funciones asociadas a la ruta y verbo
def _add_route(method, url, func):
    ROUTES_MW.setdefault(method, {}).setdefault(url, []).append(func)

# Decoradores que permiten registrar múltiples funciones (middleware) por ruta y verbo.
# Cada función se ejecutará en orden cuando se llame a execute_mw().
# La variable 'f' representa la función que se está decorando.
# Es decir, si haces @get_mw("/ruta"), 'f' será la función que sigue justo debajo.
# Se registra en ROUTES_MW y luego se devuelve sin modificar.
def get_mw(url): return lambda f: _add_route("GET", url, f) or f
def post_mw(url): return lambda f: _add_route("POST", url, f) or f
def put_mw(url): return lambda f: _add_route("PUT", url, f) or f
def delete_mw(url): return lambda f: _add_route("DELETE", url, f) or f
def patch_mw(url): return lambda f: _add_route("PATCH", url, f) or f

# Ejecuta todas las funciones registradas en orden, devolviendo el último resultado
def execute_mw(method, url, *args, **kwargs):
    funcs = ROUTES_MW.get(method.upper(), {}).get(url, [])
    if not funcs:
        return f"404 Not Found: {method} {url}"
    resultado = None
    for f in funcs:
        resultado = f(*args, **kwargs)
    return resultado


# ----------------------------------------
# Nivel 3: Steve Jobs de Hacendado
# Clase Router: permite instancias independientes con sus propias rutas
# ----------------------------------------

class Router:
    def __init__(self):
        # Diccionario por verbo HTTP, cada uno con sus rutas
        self.routes = {"GET": {}, "POST": {}, "PUT": {}, "DELETE": {}, "PATCH": {}}

    # Registra una función en la instancia actual
    def _add(self, method, url, func):
        self.routes.setdefault(method, {}).setdefault(url, []).append(func)

    # Decoradores por instancia que permiten registrar funciones en rutas específicas
    # La variable 'f' representa la función decorada, que se añade a la lista de funciones
    def get(self, url): return lambda f: self._add("GET", url, f) or f
    def post(self, url): return lambda f: self._add("POST", url, f) or f
    def put(self, url): return lambda f: self._add("PUT", url, f) or f
    def delete(self, url): return lambda f: self._add("DELETE", url, f) or f
    def patch(self, url): return lambda f: self._add("PATCH", url, f) or f

    # Ejecuta todas las funciones asociadas a la ruta y verbo
    def execute(self, method, url, *args, **kwargs):
        funcs = self.routes.get(method.upper(), {}).get(url, [])
        if not funcs:
            return f"404 Not Found: {method} {url}"
        resultado = None
        for f in funcs:
            resultado = f(*args, **kwargs)
        return resultado


# ----------------------------------------
# Nivel 4: Steve Jobs Tajamar Edition
# Rutas con parámetros dinámicos como /user/{id}
# ----------------------------------------

import re

class RouterParam:
    def __init__(self):
        # Cada verbo tiene una lista de tuplas (regex, función)
        self.routes = {"GET": [], "POST": [], "PUT": [], "DELETE": [], "PATCH": []}

    # Convierte la ruta con {param} en una expresión regular con grupos nombrados
    def _add(self, method, path, func):
        pattern = re.sub(r"{(\w+)}", r"(?P<\1>[^/]+)", path)
        regex = re.compile(f"^{pattern}$")
        self.routes[method].append((regex, func))

    # Decoradores por instancia que permiten rutas con parámetros dinámicos
    # La variable 'f' representa la función decorada, que se asocia a la expresión regular
    def get(self, path): return lambda f: self._add("GET", path, f) or f
    def post(self, path): return lambda f: self._add("POST", path, f) or f
    def put(self, path): return lambda f: self._add("PUT", path, f) or f
    def delete(self, path): return lambda f: self._add("DELETE", path, f) or f
    def patch(self, path): return lambda f: self._add("PATCH", path, f) or f

    # Busca coincidencias con la URL y ejecuta la función pasando los parámetros extraídos
    def execute(self, method, url, *args, **kwargs):
        for regex, func in self.routes.get(method.upper(), []):
            match = regex.match(url)
            if match:
                return func(*args, **match.groupdict(), **kwargs)
        return f"404 Not Found: {method} {url}"


# ----------------------------------------
# Ejemplo de uso avanzado
# ----------------------------------------

router = RouterParam()

@router.get("/user/{id}")
def mostrar_usuario(id):
    return f"Mostrando usuario con id {id}"

@router.post("/user/{id}")
def actualizar_usuario(id):
    return f"Actualizando usuario con id {id}"

# Pruebas de ejecución
if __name__ == "__main__":
    print(router.execute("GET", "/user/42"))       # → Mostrando usuario con id 42
    print(router.execute("POST", "/user/42"))      # → Actualizando usuario con id 42
    print(router.execute("DELETE", "/user/42"))    # → 404 Not Found
