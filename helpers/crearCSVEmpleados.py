import csv
from .generarPDF import generar_pdf

def crearCSVEmpleados(lista, nombreCSV):
    datos_empleados = []
    for empleado in lista:
       
        datos_empleados.append([
            empleado["id"],
            empleado["nombre"],
            empleado["apellido"],
            empleado["cargo"],
            empleado["edad"],
            empleado["retefuente"],
            empleado["salario"]
        ])
    generar_pdf(["ID", "Nombre", "Apellido", "Cargo", "Edad", "ReteFuente", "Salario"],datos_empleados, "empleados.pdf", "../data")
    with open('data/' + nombreCSV, mode='w', newline='', encoding='utf-8') as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow(["ID", "Nombre", "Apellido", "Cargo", "Edad", "ReteFuente", "Salario"])
        for empleado in lista:
            writer.writerow([empleado["id"], empleado["nombre"],empleado["apellido"], empleado["cargo"], empleado["edad"], empleado["retefuente"], empleado["salario"]])
        
   
    
