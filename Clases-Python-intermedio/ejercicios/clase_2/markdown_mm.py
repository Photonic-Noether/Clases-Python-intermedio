from markdown import Markdown
from markdown.treeprocessors import Treeprocessor
from markdown.extensions import Extension
from xml.etree.ElementTree import Element
from dataclasses import dataclass
from typing import List

@dataclass
class Encabezado:
    """
    Representa un encabezado Markdown con su nivel y texto.
    """
    nivel: int
    texto: str


class TocTreeProcessor(Treeprocessor):
    """
    Procesador que genera un índice de encabezados Markdown.
    """

    def run(self, root: Element) -> Element:
        encabezados: List[Encabezado] = []

        for elem in root.iter():
            if elem.tag in ["h1", "h2", "h3", "h4", "h5", "h6"]:
                nivel = int(elem.tag[1])
                texto = elem.text or ""
                encabezados.append(Encabezado(nivel=nivel, texto=texto))

        toc = Element("div", {"class": "toc"})
        for encabezado in encabezados:
            item = Element("p", {"class": f"nivel-{encabezado.nivel}"})
            item.text = f"{'#' * encabezado.nivel} {encabezado.texto}"
            toc.append(item)

        root.insert(0, toc)
        return root


class TocExtension(Extension):
    """
    Extensión Markdown que agrega un índice al inicio del documento HTML.
    """

    def extendMarkdown(self, md: Markdown) -> None:
        md.treeprocessors.register(TocTreeProcessor(md), "toc_tree", priority=5)


if __name__ == "__main__":
    texto_md = """
# Bienvenida
## Objetivos
Texto normal
### Detalles
## Metodología
"""

    md = Markdown(extensions=[TocExtension()])
    html = md.convert(texto_md)
    print(html)
