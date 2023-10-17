import csv

def crearCSVEmpleados(lista, nombreCSV):
    with open('data/' + nombreCSV, mode='w', newline='', encoding='utf-8') as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow(["ID", "Nombre", "Cargo", "Edad", "ReteFuente", "Salario"])
        for empleado in lista:
            writer.writerow([empleado["id"], empleado["nombre"], empleado["cargo"], empleado["edad"], empleado["retefuente"], empleado["salario"]])
