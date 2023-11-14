import pandas as pd
#import matplotlib.pyplot as plt

from helpers.crearCSVVentas import crearCSVVentas
from helpers.crearTablaHTML import crearTabla
#from helpers.crearGraficaVentas import graficar
from helpers.crearGrafica import graficar

from data.ventas import ventas

# 1. Crear un CSV con los datos de las ventas
crearCSVVentas(ventas, 'ventas.csv')

"#2 Cargo la fuente de datos y con pandos PANDAS creo un DATAFRAME"
ventasDataFrame = pd.read_csv('data/ventas.csv')
crearTabla(ventasDataFrame, 'tablaventas')

# print(ventasDataFrame)

# 3.Explorar los datos
# examen1 = ventasDataFrame.head()
# examen2 = ventasDataFrame.tail()
# examen3 = ventasDataFrame.head(20)
# examen4 = ventasDataFrame.info()
# examen5 = ventasDataFrame.describe()
# examen6 = ventasDataFrame.tail(50)

# 4.Filtrar y ordenar (limpiar)

filtroUno = ventasDataFrame.query("(Costo>500000)")
totalVentas = filtroUno[['NumeroOrden', 'Costo']]
# print(totalVentas)

filtroDos = ventasDataFrame.query("(Costo>100000) and (Costo<250000)")
totalVentas2 = filtroDos[['NumeroOrden', 'Costo']]
# print(totalVentas2)


# 6. Presentar y explorar los datos
ventasAltas = ventasDataFrame.nlargest(5, "Costo")
ventasBajas = ventasDataFrame.nsmallest(5, "Costo")
#print(ventasBajas)


# graficando un dataframe con MATPLOTLIB
graficar(ventasAltas, 
"figuras/barrasventasAltas.png",
"NumeroOrden","Costo",
"Numero de orden",
"Costo",
"Ventas más altas en el último mes",
45)
""" graficar(ventasBajas,
"figuras/barrasventasBajas.png",
"NumeroOrden",
"Costo",
"Numero de orden",
"Costo",
"Ventas más bajas en el último mes",
45, 45) """

