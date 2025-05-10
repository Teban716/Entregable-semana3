inventory = {
    "Panela": (5000, 5)
}

def pedir_numero_float_positivo(prompt):
    while(True):
        try:
            numero = float(input(prompt))
            if numero > 0:
                return numero
            else:
                print("\nEl numero no es positivo \n")
        except ValueError:
            print("\nEl numero es invalido \n")

def pedir_numero_entero_positivo(prompt):
    while(True):
        try:
            numero = int(input(prompt))
            if numero > 0:
                return numero
            else:
                print("\nEl numero no es positivo \n")
        except ValueError:
            print("\nEl numero es invalido \n")
    
def imprimir_fila(producto, precio, cantidad):
    print('{:<12}  {:<12}  {:<12}'.format(producto, precio, cantidad) )

def agregar_producto():
    producto = obtener_producto()
    if producto != None:
        inventory.update(producto)

def obtener_producto():
    nombre_producto = input("Producto:")
    if nombre_producto in inventory:
        print("||\nEl producto ya esta en el inventario||")
        return None

    precio = pedir_numero_float_positivo("Precio:  $")
    cantidad_disponible = (pedir_numero_entero_positivo("Cantidad Disponible:   "))
    print("PRODUCTO AGREGADO")
    return { nombre_producto: (precio, cantidad_disponible) }

def consultar_productos():
    if len(inventory) == 0:
        print("El inventario esta vacio")
    else:
        print("\n               INVENTARIO\n")
        imprimir_fila("PRODUCTO","PRECIO","CANTIDAD")
        print("_______________________________________________\n")
        for nombre, value in inventory.items():
            precio = value[0]
            cantidad = value[1]
            imprimir_fila(nombre,precio,cantidad)

def agregar_producto_actualizado():
    producto = actualizar_precios()
    if producto != None:
        inventory.update(producto)

def actualizar_precios():
    nombre_producto = input("Producto:")
    
    if nombre_producto not in inventory:
        print("\nEL PRODUCTO NO ESTA EN EL INVENTARIO")
        return
    
    precio = pedir_numero_float_positivo("Precio:  $")
    cantidad_disponible = (pedir_numero_entero_positivo("Cantidad Disponible:   "))
    
    if len(inventory) == 0:
        print("\nEL INVENTARIO ESTA VACIO")
        return
    
    inventory [nombre_producto] = (precio, cantidad_disponible)

def eliminar_productos():
    nombre_producto=input("Producto a eliminar: ")
    if nombre_producto not in inventory:
        print("\nEl producto no esta en el inventario")
        return
    del inventory[nombre_producto]
    print("\nPRODUCTO ELIMINADO")

def calcular_valor_total_iventario():
    multiplicacion = lambda p, c : p * c
    total = 0
    for _,j in inventory.items():
        p,c=j
        sum = multiplicacion(p,c)
        total += sum
    print(f"\nVALOR TOTAL DEL INVENTARIO \n${total:,}")

def visualizar_menu_principal():
    while True:
        print('-----------------------------------------------')
        print("1. Agregar productos")
        print("2. Consultar productos")
        print("3. Actualizar precios")
        print("4. Eliminar productos")
        print("5. Valor total del Inventario")
        print("6. Salir")
        print('-----------------------------------------------')
        opcion = input('Opcion:    ')
        print('-----------------------------------------------')
        if opcion == '1':
            agregar_producto()
            print('-----------------------------------------------')
        elif opcion == '2':
            print('-----------------------------------------------')
            consultar_productos()
        elif opcion == '3':
            actualizar_precios()
            print('-----------------------------------------------')
        elif opcion == '4':
            eliminar_productos()
            print('-----------------------------------------------')
        elif opcion == '5':
            calcular_valor_total_iventario()
        elif opcion == "6":
            break
        else:
            print('Numero Invalido')

visualizar_menu_principal()
