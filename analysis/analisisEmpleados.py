import pandas as pd
from helpers.crearCSVEmpleados import crearCSVEmpleados
from data.empleados import empleados  # Importa la lista de empleados o utiliza la generación de empleados desde tu clase Empleado

# 1. Crear un CSV con los datos de los empleados
crearCSVEmpleados(empleados, 'empleados.csv')

# 2. Cargar la fuente de datos y crear un DataFrame con pandas
empleadosDataFrame = pd.read_csv('data/empleados.csv')

# 3. Explorar los datos (puedes realizar operaciones de análisis y filtrado aquí)

# 4. Filtrar y ordenar (limpiar) según tus necesidades
