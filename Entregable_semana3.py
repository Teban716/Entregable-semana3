inventario=[]

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
    elif opcion == '2':
        print(inventario)
        menu_principal
    elif opcion == '3':
        actualizar_precios()
    elif opcion == '4':
        eliminar_productos()
    elif opcion == '5':
        inventario()
    elif opcion == "6":
        SystemExit
    else:
        print('Numero Invalido')
        print('-----------------------------------------------')

def agregar_producto():
    producto = input("Producto a agregar:    ")
    precio = float (input("Precio del producto:  "))
    inventario.append(producto,precio)
    pedir_otro_producto

def pedir_otro_producto():
    añadir_producto=input("¿Deseas agregar otro producto? ")
    if pedir_otro_producto==("si"):
        añadir_producto
    elif pedir_otro_producto == ("no"):
        menu_principal
    else: 
        print("Respuesta invalida, escribir si o no")
        pedir_otro_producto()    

def actualizar_precios():
    input("")

def eliminar_productos():
    input("")

def calcular_valor_total_iventario():
    print("")

menu_principal()
    