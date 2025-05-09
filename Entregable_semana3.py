inventario=[]

def pedir_numero_positivo(prompt):
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

def agregar_producto():
    producto = obtener_producto()
    inventario.append(producto)

def obtener_producto():
    nombre_producto = input("Producto:")
    precio = pedir_numero_positivo("Precio:  $")
    cantidad_disponible = (pedir_numero_entero_positivo("Cantidad Disponible:   "))
    
    producto = {
            'Nombre':nombre_producto,
            'Precio':precio,
            'Cantidad Disponible':(cantidad_disponible)
    }
    
    return producto

def consultar_productos():
    if len(inventario) == 0:
        print("El inventario esta vacio")
    else:
        print(f"CONSULTAR PRODUCTOS \n${inventario}")
    
def actualizar_precios():
    producto_actualizar = obtener_producto()
    if len(inventario) == 0:
        print("El inventario esta vacio")
    else:
        for i, producto in enumerate(inventario):
            if producto['Nombre'] == producto_actualizar['Nombre']:
                inventario[i] = producto_actualizar

def eliminar_productos():
    nombre_producto=input("Producto a eliminar: ")
    for producto in inventario:
        if producto['Nombre'] == nombre_producto:
            inventario.remove(producto)

def calcular_valor_total_iventario():
    multiplicacion = lambda p, c : p * c
    total = 0
    for i in inventario:
      sum = multiplicacion(i['Precio'],i['Cantidad Disponible'])
      total += sum
    print(f"\VALOR TOTAL DEL INVENTARIO \n${total}")
    #SIN LAMBDA
    # calculadora = 0
    # for producto in inventario:
    #     calculadora = calculadora + ((producto['Precio'])*(producto['Cantidad Disponible']))  
    # print(f"VALOR TOTAL DEL INVENTARIO \n${calculadora}")
    # print(total)
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
        opcion = input('Elige lo que deseas realizar:    ')
        print('-----------------------------------------------')
        if opcion == '1':
            agregar_producto()
            print('-----------------------------------------------')
            print("PRODUCTO AGREGADO")
        elif opcion == '2':
            print('-----------------------------------------------')
            print("INVENTARIO")
            consultar_productos()
        elif opcion == '3':
            actualizar_precios()
            print('-----------------------------------------------')
            print("PRECIO ACTUALIZADO")
        elif opcion == '4':
            eliminar_productos()
            print('-----------------------------------------------')
            print("PRODUCTO ELIMINADO")
        elif opcion == '5':
            calcular_valor_total_iventario()
        elif opcion == "6":
            break
        else:
            print('Numero Invalido')
        
visualizar_menu_principal()
    