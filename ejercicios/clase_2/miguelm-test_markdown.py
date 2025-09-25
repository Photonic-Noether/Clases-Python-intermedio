import pytest
from xml.etree import ElementTree as ET
from miguelm_markdown import convertir_markdown

@pytest.fixture
def texto_markdown():
    return """
[[TOC]]

# Introducción
## Objetivos
### Detalles
# Conclusión
"""
def test_conversion_html(texto_markdown):
    html = convertir_markdown(texto_markdown)

    # Verifica que se genera una lista <ul> con enlaces
    assert "<ul>" in html
    assert "</ul>" in html

    # Verifica que los enlaces apuntan a los IDs correctos
    assert 'href="#introducción"' in html
    assert 'href="#objetivos"' in html
    assert 'href="#detalles"' in html
    assert 'href="#conclusión"' in html

    # Verifica que los textos de los enlaces están presentes (sin forzar casing)
    assert ">introducción<" in html.lower()
    assert ">objetivos<" in html.lower()
    assert ">detalles<" in html.lower()
    assert ">conclusión<" in html.lower()
