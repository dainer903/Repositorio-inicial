# Productos, precios y cantidades iniciales
productos = [
    "Lay's", "Doritos", "Chochlitos", "Cheetos",
    "Mani", "Mani Moto", "Mani con Pasas", "Mani Mixto",
    "Gala", "Chocoramo", "Gansito", "Brownie",
    "Pepsi", "Manzana", "Colombiana", "Uva"
]

precios = [
    1000, 1500, 500, 900,
    500, 700, 600, 800,
    1000, 1800, 900, 2500,
    1500, 1500, 1500, 1500
]

cantidades = [
    5, 5, 5, 5,
    5, 5, 5, 5,
    5, 5, 5, 5,
    5, 5, 5, 4
]

ganancia_total = 0

def run():
    while True:
        print("\n--- Menú Máquina Expendedora ---")
        print("1. Retirar producto")
        print("2. Inventario")
        print("3. Informes")
        print("4. Configuración")
        print("5. Finalizar")
        opcion = input("Elija una opción: ")

        if opcion == "1":
            retirar_producto()
        elif opcion == "2":
            inventario()
        elif opcion == "3":
            informes()
        elif opcion == "4":
            configuracion()
        elif opcion == "5":
            print(f"Ganancia total recaudada: ${ganancia_total}")
            break
        else:
            print("Opción inválida.")

def mostrar_productos():
    print("\n--- Productos Disponibles ---")
    for i in range(len(productos)):
        fila, col = divmod(i, 4)
        print(f"{fila}{col}: {productos[i]} - ${precios[i]} (Stock: {cantidades[i]})")

def retirar_producto():
    global ganancia_total
    mostrar_productos()
    codigo = input("Ingrese código del producto (ej: 00, 01, 02): ")
    if len(codigo) == 2 and codigo.isdigit():
        fila, col = int(codigo[0]), int(codigo[1])
        indice = fila * 4 + col
        if 0 <= indice < len(productos):
            if cantidades[indice] > 0:
                print(f"Ha retirado {productos[indice]}")
                cantidades[indice] -= 1
                ganancia_total += precios[indice]
            else:
                print("Producto agotado.")
        else:
            print("Código inválido.")
    else:
        print("Código inválido.")

def inventario():
    while True:
        print("\n1. Añadir unidad a producto existente")
        print("2. Añadir nuevo producto")
        print("3. Mostrar inventario actual")
        print("4. Volver al menú principal")
        op = input("Seleccione una opción: ")

        if op == "1":
            mostrar_productos()
            codigo = input("Ingrese código: ")
            if len(codigo) == 2 and codigo.isdigit():
                fila, col = int(codigo[0]), int(codigo[1])
                indice = fila * 4 + col
                if 0 <= indice < len(productos):
                    cantidades[indice] += 1
                    print("Unidad añadida.")
                else:
                    print("Código inválido.")
            else:
                print("Código inválido.")
        elif op == "2":
            nombre = input("Nombre del nuevo producto: ")
            precio = int(input("Precio: "))
            cantidad = int(input("Cantidad inicial: "))
            productos.append(nombre)
            precios.append(precio)
            cantidades.append(cantidad)
            print(f"{nombre} añadido con éxito.")
        elif op == "3":
            mostrar_productos()
        elif op == "4":
            break
        else:
            print("Opción inválida.")

def informes():
    print(f"\nGanancia total: ${ganancia_total}")
    print("\nInforme de Ventas Detallado:")
    for i in range(len(productos)):
        vendidos = 5 - cantidades[i] if i != 15 else 4 - cantidades[i]
        if vendidos > 0:
            ganancia = vendidos * precios[i]
            print(f"{productos[i]} - Vendidos: {vendidos}, Ganancia: ${ganancia}")

def configuracion():
    print("\n--- Configuración ---")
    print("1. Restaurar valores de fábrica")
    op = input("Seleccione opción: ")
    if op == "1":
        restaurar_fabrica()

def restaurar_fabrica():
    global productos, precios, cantidades, ganancia_total
    productos = [
        "Lay's", "Doritos", "Chochlitos", "Cheetos",
        "Mani", "Mani Moto", "Mani con Pasas", "Mani Mixto",
        "Gala", "Chocoramo", "Gansito", "Brownie",
        "Pepsi", "Manzana", "Colombiana", "Uva"
    ]
    precios = [
        1000, 1500, 500, 900,
        500, 700, 600, 800,
        1000, 1800, 900, 2500,
        1500, 1500, 1500, 1500
    ]
    cantidades = [
        5, 5, 5, 5,
        5, 5, 5, 5,
        5, 5, 5, 5,
        5, 5, 5, 4
    ]
    ganancia_total = 0
    print("Máquina restaurada a valores de fábrica.")

# Iniciar programa
run()
