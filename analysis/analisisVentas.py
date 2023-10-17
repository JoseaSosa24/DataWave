import pandas as pd

from helpers.crearCSVVentas import crearCSV
from data.ventas import ventas

#1. Crear un CSV con los datos de las ventas
crearCSVVentas(ventas,'ventas.csv')

"#2 Cargo la fuente de datos y con pandos PANDAS creo un DATAFRAME"
ventasDataFrame=pd.read_csv('data/ventas.csv')

#3.Explorar los datos

#4.Filtrar y ordenar (limpiar)