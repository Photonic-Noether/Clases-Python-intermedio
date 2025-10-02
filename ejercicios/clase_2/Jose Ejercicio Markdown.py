import markdown

Primer_texto = """
# ¡Hello World!
## ¿Cómo estamos?
*Empezamos*
Esto es un texto en formato **Markdown**
"""


html = markdown.markdown(Primer_texto) # Convertivos el texto de Markdown a HTML
print(html)