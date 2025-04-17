# -*- coding: utf-8 -*-
"""AluraStoreLatam.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tx_U6e0FobcIXhuDMzs2U324GAtoTyGT

### Importación de datos
"""

import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_1%20.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_4.csv"

tienda = pd.read_csv(url)
tienda2 = pd.read_csv(url2)
tienda3 = pd.read_csv(url3)
tienda4 = pd.read_csv(url4)

tienda2.head()

# Analisis exploratorio
print(tienda.shape)
print(tienda2.shape)
print(tienda3.shape)
print(tienda4.shape)

print(tienda.info())
print(tienda2.info())
print(tienda3.info())
print(tienda4.info())

print(tienda.isnull().sum())
print(tienda2.isnull().sum())
print(tienda3.isnull().sum())
print(tienda4.isnull().sum())

#corregir tipo de dato
conversiones = {
    "Precio": int,
    "Costo de envío": int,
    "Fecha de Compra" : "datetime"
}

def corregir_tipos(df, conversiones):
    for columna, tipo in conversiones.items():
        if columna in df.columns:
            if tipo == "datetime":
                df[columna] = pd.to_datetime(df[columna], format="%d/%m/%Y")
            else:
                df[columna] = df[columna].astype(tipo)
    return df


tiendas = [tienda, tienda2, tienda3, tienda4]
tiendas_corregidas = [corregir_tipos(df, conversiones) for df in tiendas]

tienda.head()

"""#1. Análisis de facturación


"""

# suma de ventas por tienda
ventas_tienda1 = tienda["Precio"].sum()
ventas_tienda2 = tienda2["Precio"].sum()
ventas_tienda3 = tienda3["Precio"].sum()
ventas_tienda4 = tienda4["Precio"].sum()


ingresos = {
    "Tienda 1": ventas_tienda1,
    "Tienda 2": ventas_tienda2,
    "Tienda 3": ventas_tienda3,
    "Tienda 4": ventas_tienda4
}

for tien, ingre in ingresos.items():
    print(f"{tien}: ${ingre:,.2f}")

#grafica de ventas por tienda
tiendas = list(ingresos.keys())
ingresos = list(ingresos.values())

plt.bar(tiendas, ingresos)
plt.xlabel("Tiendas")
plt.ylabel("Ingresos")
plt.title("Ingresos por Tienda")
plt.show()

# Pie chart
plt.figure(figsize=(6, 6))
plt.pie(ingresos, labels=tiendas, autopct='%1.1f%%', startangle=140)
plt.title("Ingresos por Tienda\n")
plt.axis("equal")
plt.show()

# Line plot
plt.figure(figsize=(8, 5))
plt.plot(tiendas, ingresos, marker='o', linestyle='-', color='teal')
plt.title("Ingresos por Tienda")
plt.xlabel("Tiendas")
plt.ylabel("Ingresos")
plt.grid(True)
plt.tight_layout()
plt.show()

"""# 2. Ventas por categoría"""

# Agrupar y suma de total de categorias
#Tienda1
categorias_tienda1 = tienda["Categoría del Producto"].value_counts().reset_index()
categorias_tienda1.columns = ["Categoría del Producto", "Cantidad"]
# Tienda 2
categorias_tienda2 = tienda2["Categoría del Producto"].value_counts().reset_index()
categorias_tienda2.columns = ["Categoría del Producto", "Cantidad"]
# Tienda 3
categorias_tienda3 = tienda3["Categoría del Producto"].value_counts().reset_index()
categorias_tienda3.columns = ["Categoría del Producto", "Cantidad"]
# Tienda 4
categorias_tienda4 = tienda4["Categoría del Producto"].value_counts().reset_index()
categorias_tienda4.columns = ["Categoría del Producto", "Cantidad"]

print("Ventas tienda 1 por Categoría\n",categorias_tienda1, "\n")
print("Ventas tienda 2 por Categoría\n",categorias_tienda2, "\n")
print("Ventas tienda 3 por Categoría\n",categorias_tienda3, "\n")
print("Ventas tienda 4 por Categoría\n",categorias_tienda4, "\n")

def graficas_por_categoria(ventas_por_categoria, nom_tienda, tipo="barra"):
    plt.figure(figsize=(10, 6))

    if tipo == "barra":
        plt.bar(ventas_por_categoria["Categoría del Producto"], ventas_por_categoria["Cantidad"], color='skyblue')
        plt.title(f"Ventas por Categoría en {nom_tienda}", fontweight='bold')
        plt.xlabel("Categoría del Producto")
        plt.ylabel("Cantidad")
        plt.xticks(rotation=45)

    elif tipo == "pastel":
        plt.pie(
            ventas_por_categoria["Cantidad"],
            labels=ventas_por_categoria["Categoría del Producto"],
            autopct="%1.1f%%",
            startangle=140
        )
        plt.title(f"Ventas por Categoría en {nom_tienda}", fontweight='bold')
        plt.axis("equal")

    elif tipo == "linea":
        plt.plot(
            ventas_por_categoria["Categoría del Producto"],
            ventas_por_categoria["Cantidad"],
            marker='o', linestyle='-', color='green'
        )
        plt.title(f"Ventas por Categoría en {nom_tienda}", fontweight='bold')
        plt.xlabel("Categoría del Producto")
        plt.ylabel("Cantidad")
        plt.xticks(rotation=45)
        plt.grid(True)

    else:
        print("Tipo de gráfico no soportado. Usa 'barra', 'pastel' o 'linea'.")

    plt.tight_layout()
    plt.show()

# Barras
graficas_por_categoria(categorias_tienda1, "Tienda 1", tipo="barra")
graficas_por_categoria(categorias_tienda2, "Tienda 2", tipo="barra")
graficas_por_categoria(categorias_tienda3, "Tienda 3", tipo="barra")
graficas_por_categoria(categorias_tienda4, "Tienda 4", tipo="barra")

# Pastel
graficas_por_categoria(categorias_tienda1, "Tienda 1", tipo="pastel")
graficas_por_categoria(categorias_tienda2, "Tienda 2", tipo="pastel")
graficas_por_categoria(categorias_tienda3, "Tienda 3", tipo="pastel")
graficas_por_categoria(categorias_tienda4, "Tienda 4", tipo="pastel")

# Línea
graficas_por_categoria(categorias_tienda1, "Tienda 1", tipo="linea")
graficas_por_categoria(categorias_tienda2, "Tienda 2", tipo="linea")
graficas_por_categoria(categorias_tienda3, "Tienda 3", tipo="linea")
graficas_por_categoria(categorias_tienda4, "Tienda 4", tipo="linea")

"""# 3. Calificación promedio de la tienda

"""

calificacion_tienda1 = tienda["Calificación"].mean()
calificacion_tienda2 = tienda2["Calificación"].mean()
calificacion_tienda3 = tienda3["Calificación"].mean()
calificacion_tienda4 = tienda4["Calificación"].mean()

print(f"Calificación promedio Tienda 1: {calificacion_tienda1:.2f}")
print(f"Calificación promedio Tienda 2: {calificacion_tienda2:.2f}")
print(f"Calificación promedio Tienda 3: {calificacion_tienda3:.2f}")
print(f"Calificación promedio Tienda 4: {calificacion_tienda4:.2f}")

nombres_tiendas = ["Tienda 1", "Tienda 2", "Tienda 3", "Tienda 4"]
calificaciones = [
    calificacion_tienda1,
    calificacion_tienda2,
    calificacion_tienda3,
    calificacion_tienda4
]

plt.figure(figsize=(8, 5))
plt.bar(nombres_tiendas, calificaciones, color='mediumseagreen')
plt.title("Calificación Promedio por Tienda", fontsize=14)
plt.xlabel("Tienda")
plt.ylabel("Calificación Promedio")
plt.ylim(0, 5)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

plt.figure(figsize=(8, 5))
plt.scatter(nombres_tiendas, calificaciones, color='royalblue', s=100)
plt.title("Calificación Promedio por Tienda", fontsize=14)
plt.xlabel("Tienda")
plt.ylabel("Calificación Promedio")
plt.ylim(0, 5)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

plt.figure(figsize=(6, 6))
plt.pie(calificaciones, labels=nombres_tiendas, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title("Calificación Promedio por Tienda\n", fontsize=14)
plt.axis('equal')
plt.show()

"""# 4. Productos más y menos vendidos"""

dict_tiendas = {
    "Tienda 1": tienda,
    "Tienda 2": tienda2,
    "Tienda 3": tienda3,
    "Tienda 4": tienda4
}

# Función para recorrer todos los productos por tienda
for nombre, df in dict_tiendas.items():
    # Asegurarse de que la columna exista
    if "Producto" not in df.columns:
        print(f"{nombre} no tiene la columna 'Producto'")
        continue

    # Contar las ventas por producto
    ventas = df["Producto"].value_counts()

    # Obtener más y menos vendido
    producto_mas = ventas.idxmax()
    cantidad_mas = ventas.max()
    producto_menos = ventas.idxmin()
    cantidad_menos = ventas.min()

    print(f"{nombre}")
    print(f"Más vendido: {producto_mas} ({cantidad_mas} ventas)")
    print(f"Menos vendido: {producto_menos} ({cantidad_menos} venta(s))\n")

    # Graficar el top 5
    top5 = ventas.head(5)
    plt.figure(figsize=(8, 5))
    top5.plot(kind="bar", color="mediumturquoise")
    plt.title(f"Top 5 Productos Más Vendidos - {nombre}")
    plt.xlabel("Producto")
    plt.ylabel("Cantidad Vendida")
    plt.xticks(rotation=45)
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.show()
    print("\n")

     # Gráfico de líneas
    plt.figure(figsize=(8, 5))
    plt.plot(top5.index, top5.values, marker='o', linestyle='-', color='cornflowerblue')
    plt.title(f"Top 5 Productos Más Vendidos (Líneas) - {nombre}")
    plt.xlabel("Producto")
    plt.ylabel("Cantidad Vendida")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    print("\n")

     # Gráfico de pastel
    plt.figure(figsize=(6, 6))
    plt.pie(top5.values, labels=top5.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Set3.colors)
    plt.title(f"Top 5 Productos Más Vendidos (Pie) - {nombre}")
    plt.axis('equal')
    plt.tight_layout()
    plt.show()
    print("\n")

"""# 5. Envío promedio por tienda"""

costo_envio_promedio = {}

for nombre, df in dict_tiendas.items():
    promedio = df["Costo de envío"].mean()
    costo_envio_promedio[nombre] = promedio
    print(f"{nombre}: Costo de envío promedio = ${promedio:.2f}")

# Graficar los costos promedio
plt.figure(figsize=(8, 5))

nombres_tiendas = list(costo_envio_promedio.keys())
valores = list(costo_envio_promedio.values())
barras = plt.bar(nombres_tiendas, valores, color='salmon')

for barra in barras:
    altura = barra.get_height()
    plt.text(
        barra.get_x() + barra.get_width()/2,
        altura + 0.5,
        f"${altura:.2f}",
        ha='center', va='bottom', fontsize=10, fontweight='bold'
    )

plt.title("Costo de Envío Promedio por Tienda")
plt.ylabel("Costo Promedio ($)")
plt.xlabel("Tienda")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# Gráfico de líneas
plt.figure(figsize=(8, 5))
plt.plot(nombres_tiendas, valores, marker='o', linestyle='-', color='darkorange')
plt.title("Costo de Envío Promedio por Tienda")
plt.xlabel("Tienda")
plt.ylabel("Costo Promedio ($)")
plt.grid(True, linestyle='--', alpha=0.6)

for i, valor in enumerate(valores):
    plt.text(i, valor + 0.5, f"${valor:.2f}", ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.show()

# Gráfico de pastel
plt.figure(figsize=(6, 6))
plt.pie(valores, labels=nombres_tiendas, autopct=lambda p: f"${(p/100)*sum(valores):.2f}", startangle=140, colors=plt.cm.Pastel1.colors)
plt.title("Costos de Envío Promedio Por Tienda")
plt.axis('equal')
plt.tight_layout()
plt.show()

"""# **Informe Final - Análisis de Tiendas**

## **Introducción**

El propósito de este análisis es ayudar al Sr. Juan a decidir en qué tienda debería vender sus productos. Para tomar una decisión informada, se han evaluado diversos factores clave que influyen directamente en el rendimiento de cada tienda:

- Ingresos totales generados  
- Categorías de productos más y menos vendidas  
- Calificaciones promedio de los clientes  
- Productos más y menos vendidos  
- Costo de envío promedio  

A través de gráficos y estadísticas, hemos comparado el desempeño de las tiendas disponibles para identificar la que ofrece el mejor entorno para sus ventas.

---

## **Conclusión y Recomendación**

Después de considerar todos los factores evaluados, la mejor opción para que el Sr. Juan venda sus productos es **Tienda 1**. Esta recomendación se basa en las siguientes fortalezas:

- **Mayor ingreso total**, lo cual refleja un mercado activo y un alto potencial de ventas.  
- **Buena distribución en ventas por categoría**, lo cual permite una mayor exposición de diversos productos.  
- **Producto más vendido con buena rotación (60 unidades)**, que confirma la demanda.

Si bien **Tienda 3** tiene la mejor calificación promedio, y **Tienda 4** cuenta con el menor coste de envío, estos factores no compensan el hecho de que ambas tiendas presentan menores ingresos y una rotación ligeramente más baja en productos clave. Además, **Tienda 1** mantiene una calificación aceptable (**3.98**), dentro de un margen competitivo.

---

### ✅ **Recomendación final**  
El Sr. Juan debería vender en **Tienda 1**, donde encontrará:

- El mayor volumen de ventas  
- Una demanda amplia en varias categorías  
- Un historial financiero sólido
"""