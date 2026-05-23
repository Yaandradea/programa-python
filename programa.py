# Nombre del estudiante: Yeni Alexandra Andrade Arias
# Grupo: 703 
# Programa: Ingeniería de Sistemas 
# Código fuente: Autoría propia 
# Matriz de productos
productos = [
    ["Hamburguesa", "Comida", 25000],
    ["Gaseosa", "Bebida", 5000],
    ["Pizza", "Comida", 30000],
    ["Helado", "Postre", 8000],
    ["Perro Caliente", "Comida", 18000],
    ["Jugo Natural", "Bebida", 12000]
]

# Promoción
categoria_objetivo = "Comida"
precio_umbral = 20000


# Función para calcular precio final
def calcular_precio_final(categoria, precio_base):

    if categoria == categoria_objetivo and precio_base > precio_umbral:

        precio_final = precio_base - (precio_base * 0.15)
        descuento = "Sí aplica 15% de descuento"

    else:

        precio_final = precio_base
        descuento = "No aplica descuento"

    return precio_final, descuento


# Variables
continuar = "si"
total_compra = 0

# Lista para guardar compras
factura = []


while continuar == "si":

    print("\n========= MENÚ DEL RESTAURANTE =========")
    print("Promoción:")
    print("Los productos de categoría COMIDA")
    print("que tengan un precio mayor a $20.000")
    print("reciben un descuento del 15%")
    print("========================================")

    # Mostrar productos
    for i in range(len(productos)):

        print(i + 1, "-", productos[i][0],
              "- $", productos[i][2])

    print("========================================")

    # Escoger producto
    opcion = int(input("Digite el número del producto que desea comprar: "))

    # Validar opción
    if opcion >= 1 and opcion <= len(productos):

        producto = productos[opcion - 1]

        nombre = producto[0]
        categoria = producto[1]
        precio_base = producto[2]

        # Calcular precio final
        precio_final, descuento = calcular_precio_final(categoria, precio_base)

        # Guardar compra
        factura.append([nombre, precio_base, descuento, precio_final])

        # Sumar total
        total_compra = total_compra + precio_final

        print("\nProducto agregado correctamente")

    else:

        print("Opción no válida")

    # Preguntar si desea continuar
    continuar = input("\n¿Desea comprar otro producto? (si/no): ")


# Mostrar factura final
print("\n============= FACTURA FINAL =============")

for compra in factura:

    print("\nProducto:", compra[0])
    print("Precio base: $", compra[1])
    print("Descuento:", compra[2])
    print("Precio final: $", compra[3])
    print("-----------------------------------------")

print("\nTOTAL DE LA COMPRA: $", total_compra)
print("=========================================")