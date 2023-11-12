import csv
from .generarPDF import generar_pdf


def crearCSVVentas(lista, nombreCSV):

    with open('data/'+nombreCSV,mode='w',newline='',encoding='utf-8') as archivo_csv:
        writer=csv.writer(archivo_csv)
        writer.writerow(['NumeroOrden','Cliente','Costo'])
        writer.writerows(lista)

        generar_pdf(['NumeroOrden','Cliente','Costo'],lista, "ventas.pdf", "../data")
    
    