# ----------------------------------------
# Test para Nivel 1: Decoradores básicos
# ----------------------------------------

from router_http import execute, get, post, put, delete

@get("/saludo")
def saludo():
    return "Hola desde GET"

@post("/crear")
def crear():
    return "Creado con POST"

@put("/actualizar")
def actualizar():
    return "Actualizado con PUT"

@delete("/borrar")
def borrar():
    return "Borrado con DELETE"

def test_nivel_1():
    # Verifica que cada verbo ejecuta la función correcta
    assert execute("GET", "/saludo") == "Hola desde GET"
    assert execute("POST", "/crear") == "Creado con POST"
    assert execute("PUT", "/actualizar") == "Actualizado con PUT"
    assert execute("DELETE", "/borrar") == "Borrado con DELETE"
    # Verifica que rutas inexistentes devuelven 404
    assert execute("GET", "/noexiste") == "404 Not Found: GET /noexiste"


# ----------------------------------------
# Test para Nivel 2: Middleware
# ----------------------------------------

from router_http import execute_mw, get_mw

@get_mw("/proceso")
def paso_1():
    print("Paso 1")
    return "Primero"

@get_mw("/proceso")
def paso_2():
    print("Paso 2")
    return "Segundo"

def test_nivel_2():
    # Verifica que se ejecutan ambas funciones en orden
    resultado = execute_mw("GET", "/proceso")
    assert resultado == "Segundo"  # Se devuelve el resultado de la última función


# ----------------------------------------
# Test para Nivel 3: Router por instancia
# ----------------------------------------

from router_http import Router

router = Router()

@router.get("/inicio")
def inicio():
    return "Inicio OK"

@router.post("/inicio")
def inicio_post():
    return "Inicio POST OK"

def test_nivel_3():
    assert router.execute("GET", "/inicio") == "Inicio OK"
    assert router.execute("POST", "/inicio") == "Inicio POST OK"
    assert router.execute("DELETE", "/inicio") == "404 Not Found: DELETE /inicio"


# ----------------------------------------
# Test para Nivel 4: Parámetros dinámicos
# ----------------------------------------

from router_http import RouterParam

router_param = RouterParam()

@router_param.get("/usuario/{id}")
def ver_usuario(id):
    return f"Usuario {id}"

@router_param.post("/usuario/{id}")
def modificar_usuario(id):
    return f"Modificando usuario {id}"

def test_nivel_4():
    assert router_param.execute("GET", "/usuario/123") == "Usuario 123"
    assert router_param.execute("POST", "/usuario/456") == "Modificando usuario 456"
    assert router_param.execute("PUT", "/usuario/789") == "404 Not Found: PUT /usuario/789"
