import pytest
from markdown import Markdown
from markdown_mm import TocExtension

@pytest.fixture
def markdown_con_indice():
    """
    Instancia de Markdown con la extensión personalizada TocExtension.
    """
    return Markdown(extensions=[TocExtension()])

@pytest.fixture
def contenido_markdown():
    """
    Contenido de prueba con encabezados Markdown de distintos niveles.
    """
    return """
# Bienvenida

Este documento sirve como ejemplo para probar la generación automática de índices.

## Objetivos

- Comprender el uso de encabezados en Markdown.
- Validar la extensión personalizada en Python.

### Detalles técnicos

La extensión debe detectar encabezados `h1`, `h2`, `h3`, etc., y construir un índice navegable.

## Metodología

Se utilizará `pytest` para validar la salida HTML generada por la extensión.

### Casos de prueba

- Encabezados consecutivos
- Texto intermedio
- Encabezados anidados

## Conclusión

La extensión debe insertar el índice al inicio del documento HTML.
"""

def test_indice_html_generado(markdown_con_indice, contenido_markdown):
    """
    Verifica que el índice se genera correctamente y contiene los encabezados esperados.
    """
    html = markdown_con_indice.convert(contenido_markdown)

    # Validaciones estructurales
    assert '<div class="toc">' in html
    assert '<p class="nivel-1">' in html
    assert '<p class="nivel-2">' in html
    assert '<p class="nivel-3">' in html

    # Validaciones de contenido
    assert '# Bienvenida' in html
    assert '## Objetivos' in html
    assert '### Detalles técnicos' in html
    assert '## Metodología' in html
    assert '### Casos de prueba' in html
    assert '## Conclusión' in html

