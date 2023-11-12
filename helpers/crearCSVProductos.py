import csv
from .generarPDF import generar_pdf

def crearCSVProductos(lista, nombreCSV):

    with open('data/'+nombreCSV,mode='w',newline='',encoding='utf-8') as archivo_csv:
        writer=csv.writer(archivo_csv)
        writer.writerow(['Id_producto','Nombre','Precio_unitario', 'iva'])
        writer.writerows(lista)

        generar_pdf(['Id_producto','Nombre','Precio_unitario', 'iva'],lista, "productos.pdf", "../data")