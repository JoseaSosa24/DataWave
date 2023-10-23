import pandas as pd
from helpers.crearCSVEmpleados import crearCSVEmpleados
from data.empleado import Empleado  # Importa la lista de empleados o utiliza la generación de empleados desde tu clase Empleado
empleados = Empleado()
lista = empleados.generar_empleado(2000)
# 1. Crear un CSV con los datos de los empleados
crearCSVEmpleados(lista, 'empleados.csv')

# 2. Cargar la fuente de datos y crear un DataFrame con pandas
empleadosDataFrame = pd.read_csv('data/empleados.csv')
print(empleadosDataFrame)

# 3. Explorar los datos (puedes realizar operaciones de análisis y filtrado aquí)



# 4. Filtrar y ordenar (limpiar) según tus necesidades
