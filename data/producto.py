import random
productos = []
for _ in range(3000):
    
    productoId=random.randint(0,500000)
    nombreProducto=random.choice(['Camisa', 'Pantalon', 'Sudadera', 'Chompa','Blue Jean'])
    costoUnitario = random.randint(150000, 600000)
    iva = 0.19
    orden = [productoId, nombreProducto, costoUnitario, iva]
    productos.append(orden)