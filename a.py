productos = {"8475HD" : {"marca" : "HP","pantalla": 15.6,"ram": "8GB","disco": "DD","GBdeDD": "1T","procesador": "Intel Core i5","video": "Nvidia GTX1050"} ,
             "2175HD": {"marca": "Dell","pantalla": 14,"ram": "4GB","disco": "SSD","GBdeDD": "412GB","procesador": "Intel Core i5","video": "Nvidia GTX1050"},
             "GF75HD": {"marca": "MSI", "pantalla": 15.6,"ram": "12GB","disco": "DD","GBdeDD": "1T","procesador": "Intel Core i7","video": "Nvidia GTX1050"}
}

stock = {"8475HD" : {"precio": 38799000, "stock": 20},
        "2175HD": {"precio": 421025, "stock": 14},
        "GF75HD": {"precio": 54545, "stock": 26}
}

def stock_marca(marca): 
    stock_total = 0
    encontrados = False
    for modelo in productos:
         variable = productos[modelo]
         if variable["marca"].lower() == marca:
              stock_total += stock[modelo]["stock"]
              encontrados = True
              if encontrados:
                   print(f"El stock disponible para esa marca es de: {stock_total}")
              else: 
                   print("no se encontro stock de ese producto, Ingrese otro")
        
def busqueda_precio(p_min, p_max):
    lista_modelos = []
    for modelo in productos:
        precio = stock[modelo]["precio"]
        if p_min <= precio <= p_max:
            marca = productos[modelo]["marca"]
            lista_modelos.append(f"{marca}--{modelo}")
    if lista_modelos:
                print(f"Los noteboocks disponibles en los rangos de precio solicitado son: {lista_modelos}")
    else: 
        print("No se encontraron noteboocks dentro del rango solicitado")
        return lista_modelos

def eliminar_producto(modelo):
    if modelo in productos:
        productos.pop(modelo)
        stock.pop(modelo)
        return True
    else:
        return False
    

while True:
    print("\n*** Menu Principal***")
    print("1: Stock de Marca")
    print("2: Busqueda por precio")
    print("3: Eliminar producto")
    print("4: Salir")


    opcion = int(input("Seleccione una opcion de nuestro menu: "))
    if opcion == 1:
        marca = input("ingrese la marca la cual quiere consultar: ").lower()
        stock_marca(marca)

    elif opcion == 2:
        while True: 
            try:
                p_min = int(input("ingrese el rango minimo del precio: "))
                p_max = int(input("ingrese el rango maximo del precio: "))
                busqueda_precio(p_min, p_max)
                break
            except ValueError:
                print("debe ingresar valores numericos")

    elif opcion == 3: 
        while True:
            modelo = input("ingrese el modelo que quiere eliminar: ")
            resultado = eliminar_producto(modelo)
            if resultado:
                print("El producto fue eliminado con exito")
            else: 
                print("El modelo que menciono no existe") 

            continuar = input("Desea eliminar otro producto (si/no)").lower()
            if continuar != "si":
                break
    elif opcion == 4:
            print("El programa fue finalizado, muchas gracias por usar nuestro servicio")
            break
    else:
        print("Seleccione una opcion valida de nuestro sistema")
