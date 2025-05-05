inventario=[]

def pedir_numero_positivo(prompt):
    while(True):
        try:
            numero = float(input(prompt))
            if numero > 0:
                return numero
            else:
                print("El numero no es positivo")
        except ValueError:
            print("El numero es invalido")

def menu_principal():
    print("1. Agregar productos")
    print("2. Consultar productos")
    print("3. Actualizar precios")
    print("4. Eliminar productos")
    print("5. Inventario total")
    print("6. Salir")
    opcion = input('Elige lo que deseas realizar:    ')
    if opcion == '1':
        agregar_producto()
        menu_principal()
    elif opcion == '2':
        consultar_productos()
        menu_principal()
    elif opcion == '3':
        actualizar_precios()
        menu_principal()
    elif opcion == '4':
        eliminar_productos()
        menu_principal()
    elif opcion == '5':
        calcular_valor_total_iventario()
        menu_principal()
    elif opcion == "6":
        SystemExit
    else:
        print('Numero Invalido')
        print('-----------------------------------------------')
        menu_principal()

def agregar_producto():
    producto = obtener_producto()
    inventario.append(producto)

def obtener_producto():
    nombre_producto = input("Producto:    ")
    precio = pedir_numero_positivo("Precio:  ")

    producto = {
        'Nombre':nombre_producto,
        'Precio':precio
    }
    
    return producto

def consultar_productos():
    print(inventario)
    

def actualizar_precios():
    producto_actualizar = obtener_producto()

    for i, producto in enumerate(inventario):
        if producto['Nombre'] == producto_actualizar['Nombre']:
            inventario[i] = producto_actualizar

def eliminar_productos():
    nombre_producto=input("Producto a eliminar: ")
    for producto in inventario:
        if producto['Nombre'] == nombre_producto:
            inventario.remove(producto)

def calcular_valor_total_iventario():
    calculadora = 0
    for producto in inventario:
        calculadora = calculadora + producto['Precio']  
    print (calculadora)

menu_principal()
    