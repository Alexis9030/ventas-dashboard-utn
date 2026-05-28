import pandas as pd
import matplotlib.pyplot as plt

# Leer archivo CSV
df = pd.read_csv('datos/ventas.csv')

# Crear columna total
df['total'] = df['cantidad'] * df['precio']

# Mostrar ventas totales
ventas_totales = df['total'].sum()

print("Ventas totales:", ventas_totales)

# Ventas por producto
ventas_producto = df.groupby('producto')['cantidad'].sum()

print("\nProductos vendidos:")
print(ventas_producto)

# Crear gráfico
ventas_producto.plot(kind='bar')

plt.title('Ventas por Producto')
plt.xlabel('Producto')
plt.ylabel('Cantidad Vendida')

# Guardar gráfico
plt.savefig('resultados/grafico_ventas.png')

print("\nGráfico generado correctamente.")