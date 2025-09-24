import markdown
from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor
from xml.etree.ElementTree import Element


class GeneradorIndice(Treeprocessor):
    """
    Procesador de árbol que busca encabezados en el documento HTML
    generado por Markdown y construye una lista con enlaces internos.
    Inserta el índice donde aparezca la etiqueta [[TOC]].
    """

    def run(self, root):
        # Crear lista <ul> para el índice
        indice = Element("ul")

        for elemento in root.iter():
            if elemento.tag in ["h1", "h2", "h3"]:
                texto = "".join(elemento.itertext())
                nivel = int(elemento.tag[1])
                ancla = texto.lower().replace(" ", "-")

                # Asignar ID al encabezado para el enlace
                elemento.set("id", ancla)

                # Crear entrada en el índice
                li = Element("li")
                li.set("style", f"margin-left:{(nivel - 1) * 20}px")
                enlace = Element("a", href=f"#{ancla}")
                enlace.text = texto
                li.append(enlace)
                indice.append(li)

        # Reemplazar la etiqueta [[TOC]] por el índice generado
        for i, hijo in enumerate(root):
            if hijo.tag == "p" and hijo.text and "[[TOC]]" in hijo.text:
                root.remove(hijo)
                root.insert(i, indice)
                break


class ExtensionIndice(Extension):
    """
    Extensión que registra el procesador de índice en Markdown.
    """

    def extendMarkdown(self, md):
        md.treeprocessors.register(GeneradorIndice(md), "generador_indice", priority=15)


def convertir_markdown(texto_md):
    """
    Convierte texto Markdown en HTML con índice automático.
    Requiere que el texto contenga [[TOC]] donde se desea insertar el índice.
    """
    md = markdown.Markdown(extensions=[ExtensionIndice()])
    return md.convert(texto_md)


# Ejemplo de uso
if __name__ == "__main__":
    texto = """
[[TOC]]

# Introducción
## Objetivos
### Detalles
# Conclusión
"""
    html = convertir_markdown(texto)
    print(html)
