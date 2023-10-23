import csv

def crearCSVProductos(lista, nombreCSV):

    with open('data/'+nombreCSV,mode='w',newline='',encoding='utf-8') as archivo_csv:
        writer=csv.writer(archivo_csv)
        writer.writerow(['Id_producto','Nombre','Precio_unitario', 'iva'])
        writer.writerows(lista)