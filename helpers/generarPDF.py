import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

directorio_actual = os.getcwd()
def generar_pdf(encabezado, datos, nombre_pdf="output.pdf", ruta_pdf=None):
    # Si no se especifica la ruta del PDF, usar la ruta del directorio actual
    if ruta_pdf is None:
        ruta_pdf = nombre_pdf
    else: 
        ruta_pdf = os.path.join(ruta_pdf, nombre_pdf)

    ruta_completa_pdf = os.path.join(os.path.dirname(os.path.abspath(__file__)), ruta_pdf)

    # Crear un documento PDF
    pdf_doc = SimpleDocTemplate(ruta_completa_pdf, pagesize=letter)
    
    # Configurar los estilos para la tabla
    styles = getSampleStyleSheet()
    style_table = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])

    # Añadir el encabezado y los datos a la tabla
    datos_tabla = [encabezado] + datos
    tabla = Table(datos_tabla)
    tabla.setStyle(style_table)

    # Crear la lista de elementos (story) y agregar la tabla al PDF
    story = [tabla]
    pdf_doc.build(story)

# Ejemplo de uso









