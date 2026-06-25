import random

tipos_validos = ["Pelicula", "Videojuego"]
categorias_validas = ["Accion", "Aventura", "Deportes", "Estrategia", "Terror", "Ciencia Ficcion", "Infantil", "Otro"]
estados_validos = ["Disponible", "Alquilado", "Reservado", "Discontinuado"]

titulos_azar = ["Super Mario Bros Wonder", "The Legend of Zelda", "Jurassic Park", "Star Wars", "Call of Duty", "Resident Evil", "Final Fantasy VII", "Hogwarts Legacy", "Ace Attorney", "Maze Runner: Correr o Morir", "Avengers: Endgame", "Harry Potter y la Piedra Filosofal", "Los Juegos del Hambre", "El Senor de los Anillos"]
plataformas_azar = ["PlayStation 5", "Xbox Series X", "Nintendo Switch", "PC", "Blu-ray", "DVD"]

# Autor principal: Agustina Maquieira
def ajustar_texto(texto, ancho):
    while len(texto) < ancho:

        texto = texto + " "
    return texto

# Autor principal: Agustina Maquieira
def mostrar_menu():
    print("=" * 50)
    print("SISTEMA DE GESTION: RETROPIXEL STORE")
    print("1. Registrar producto (Alta)")
    print("2. Eliminar producto (Baja)")
    print("3. Modificar producto (Modificacion)")
    print("4. Informe General - Visualizacion de los datos")
    print("5. Informe Matricial - Categoria x Tipo de contenido")
    print("6. Salir")
    print("=" * 50)

# Autor principal: Valentina Rodriguez
def cargar_tipo():
    print("Tipo de contenido:")
    print("1. Pelicula")
    print("2. Videojuego")
    opcion = input("Seleccione una opcion: ")

    while opcion != "1" and opcion != "2":

        print("Opcion invalida.")
        opcion = input("Seleccione 1 o 2: ")

    if opcion == "1":
        tipo = "Pelicula"
    else:
        tipo = "Videojuego"

    return tipo

# Autor principal: Valentina Rodriguez
def cargar_categorias():
    categorias_producto = []

    seguir = "S"

    while seguir == "S" or seguir == "s":

        i = 0
        while i < len(categorias_validas):
            print(str(i + 1) + ". " + categorias_validas[i])
            i = i + 1

        opcion = int(input("Seleccione categoria: "))

        while opcion < 1 or opcion > len(categorias_validas):

            print("Categoria invalida.")
            opcion = int(input("Seleccione categoria: "))

        categoria_elegida = categorias_validas[opcion - 1]

        if categoria_elegida in categorias_producto:

            print("Esa categoria ya fue agregada a este producto.")
        else:
            categorias_producto.append(categoria_elegida)

        seguir = input("Desea agregar otra categoria? S/N: ")

        while seguir != "S" and seguir != "s" and seguir != "N" and seguir != "n":

            print("Opcion invalida.")
            seguir = input("Desea agregar otra categoria? S/N: ")

    return categorias_producto

# Autor principal: Ainara Salvatierra
def cargar_estado():
    i = 0
    while i < len(estados_validos):
        print(str(i + 1) + ". " + estados_validos[i])
        i = i + 1

    opcion = int(input("Seleccione estado: "))

    while opcion < 1 or opcion > len(estados_validos):

        print("Estado invalido.")
        opcion = int(input("Seleccione estado: "))

    return estados_validos[opcion - 1]

# Autor principal: Valentina Marfany
def cargar_precios():
    precio_venta = 0.0
    precio_alquiler = 0.0

    tiene_venta = input("El producto tiene precio de venta? S/N: ")
    while tiene_venta != "S" and tiene_venta != "s" and tiene_venta != "N" and tiene_venta != "n":
        print("Opcion invalida.")
        tiene_venta = input("El producto tiene precio de venta? S/N: ")

    if tiene_venta == "S" or tiene_venta == "s":
        precio_venta = float(input("Ingrese precio de venta: "))
        while precio_venta < 0:

            print("El precio no puede ser negativo.")
            precio_venta = float(input("Ingrese precio de venta: "))

    tiene_alquiler = input("El producto tiene precio de alquiler? S/N: ")
    while tiene_alquiler != "S" and tiene_alquiler != "s" and tiene_alquiler != "N" and tiene_alquiler != "n":
        print("Opcion invalida.")
        tiene_alquiler = input("El producto tiene precio de alquiler? S/N: ")

    if tiene_alquiler == "S" or tiene_alquiler == "s":
        precio_alquiler = float(input("Ingrese precio de alquiler: "))
        while precio_alquiler < 0:
            print("El precio no puede ser negativo.")
            precio_alquiler = float(input("Ingrese precio de alquiler: "))

    while precio_venta == 0.0 and precio_alquiler == 0.0:

        print("El producto debe tener al menos un precio (venta o alquiler).")
        precio_venta = float(input("Ingrese precio de venta (0 si no aplica): "))
        while precio_venta < 0:
            print("El precio no puede ser negativo.")
            precio_venta = float(input("Ingrese precio de venta (0 si no aplica): "))
        precio_alquiler = float(input("Ingrese precio de alquiler (0 si no aplica): "))
        while precio_alquiler < 0:
            print("El precio no puede ser negativo.")
            precio_alquiler = float(input("Ingrese precio de alquiler (0 si no aplica): "))

    return precio_venta, precio_alquiler

# Autor principal: Valentina Marfany
def buscar_producto(titulo_buscado, titulos):
    i = 0

    while i < len(titulos) and titulos[i].lower() != titulo_buscado.lower():

        i = i + 1

    return i

# Autor principal: Ainara Salvatierra
def ordenar_por_stock_y_titulo(titulos, tipos, plataformas, precios_venta,
                                precios_alquiler, stocks, categorias, estados):
    i = 0
    while i < len(titulos) - 1:

        j = i + 1
        while j < len(titulos):

            cambiar = False

            if stocks[j] > stocks[i]:

                cambiar = True
            elif stocks[j] == stocks[i] and titulos[j].lower() < titulos[i].lower():

                cambiar = True

            if cambiar == True:

                aux = titulos[i]
                titulos[i] = titulos[j]
                titulos[j] = aux

                aux = tipos[i]
                tipos[i] = tipos[j]
                tipos[j] = aux

                aux = plataformas[i]
                plataformas[i] = plataformas[j]
                plataformas[j] = aux

                aux = precios_venta[i]
                precios_venta[i] = precios_venta[j]
                precios_venta[j] = aux

                aux = precios_alquiler[i]
                precios_alquiler[i] = precios_alquiler[j]
                precios_alquiler[j] = aux

                aux = stocks[i]
                stocks[i] = stocks[j]
                stocks[j] = aux

                aux = categorias[i]
                categorias[i] = categorias[j]
                categorias[j] = aux

                aux = estados[i]
                estados[i] = estados[j]
                estados[j] = aux

            j = j + 1
        i = i + 1

# Autor Principal: Agustina Maquieira
def construir_matriz_categoria_tipo(tipos, categorias):

    matriz = [
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
    ]

    i = 0
    while i < len(tipos):

        columna = 0
        while columna < len(tipos_validos) and tipos_validos[columna] != tipos[i]:
            columna = columna + 1

        j = 0
        while j < len(categorias[i]):

            fila = 0
            while fila < len(categorias_validas) and categorias_validas[fila] != categorias[i][j]:
                fila = fila + 1

            matriz[fila][columna] = matriz[fila][columna] + 1

            j = j + 1
        i = i + 1

    return matriz

# Autor principal: Valentina Marfany
def registrar_manual(titulos, tipos, plataformas, precios_venta,
                     precios_alquiler, stocks, categorias, estados):
    titulo = input("Ingrese titulo del producto: ")
    while titulo == "":

        print("El titulo no puede quedar vacio.")
        titulo = input("Ingrese titulo del producto: ")

    tipo = cargar_tipo()

    plataforma = input("Ingrese plataforma o formato: ")
    while plataforma == "":
        print("La plataforma o formato no puede quedar vacio.")
        plataforma = input("Ingrese plataforma o formato: ")

    precio_venta, precio_alquiler = cargar_precios()

    stock = int(input("Ingrese cantidad disponible en stock: "))
    while stock < 0:

        print("El stock debe ser positivo o cero.")
        stock = int(input("Ingrese cantidad disponible en stock: "))

    categorias_producto = cargar_categorias()

    estado = "Disponible"

    titulos.append(titulo)
    tipos.append(tipo)
    plataformas.append(plataforma)
    precios_venta.append(precio_venta)
    precios_alquiler.append(precio_alquiler)
    stocks.append(stock)
    categorias.append(categorias_producto)
    estados.append(estado)

    print("Producto registrado correctamente.")

# Autor principal: Valentina Marfany
def registrar_automatico(titulos, tipos, plataformas, precios_venta,
                          precios_alquiler, stocks, categorias, estados):
    titulo = random.choice(titulos_azar)

    tipo = random.choice(tipos_validos)
    plataforma = random.choice(plataformas_azar)

    precio_venta = round(random.uniform(2500.50, 45999.99), 2)
    precio_alquiler = round(random.uniform(500.50, 8999.99), 2)

    incluye_venta = random.choice([True, False])
    incluye_alquiler = random.choice([True, False])

    if incluye_venta == False and incluye_alquiler == False:
        incluye_venta = True

    if incluye_venta == False:
        precio_venta = 0.0
    if incluye_alquiler == False:
        precio_alquiler = 0.0

    stock = random.randint(0, 50)

    cantidad_categorias = random.randint(1, 3)
    categorias_producto = []
    while len(categorias_producto) < cantidad_categorias:
        categoria_azar = random.choice(categorias_validas)
        if categoria_azar not in categorias_producto:
            categorias_producto.append(categoria_azar)

    estado = "Disponible"

    titulos.append(titulo)
    tipos.append(tipo)
    plataformas.append(plataforma)
    precios_venta.append(precio_venta)
    precios_alquiler.append(precio_alquiler)
    stocks.append(stock)
    categorias.append(categorias_producto)
    estados.append(estado)

    print("Producto generado automaticamente.")

# Autor principal: Agustina Maquieira
def registrar_producto(titulos, tipos, plataformas, precios_venta,
                        precios_alquiler, stocks, categorias, estados):
    cantidad = int(input("Cuantos productos desea registrar?: "))
    while cantidad < 1:

        print("Debe registrar al menos 1 producto.")
        cantidad = int(input("Cuantos productos desea registrar?: "))

    i = 0
    while i < cantidad:

        print("Producto", i + 1)

        print("1. Carga manual")
        print("2. Carga automatica")
        opcion = input("Seleccione una opcion: ")

        while opcion != "1" and opcion != "2":
            print("Opcion invalida.")
            opcion = input("Seleccione 1 o 2: ")

        if opcion == "1":
            registrar_manual(titulos, tipos, plataformas, precios_venta,
                             precios_alquiler, stocks, categorias, estados)
        else:
            registrar_automatico(titulos, tipos, plataformas, precios_venta,
                                  precios_alquiler, stocks, categorias, estados)

        i = i + 1

# Autor principal: Ainara Salvatierra
def eliminar_producto(titulos, tipos, plataformas, precios_venta,
                      precios_alquiler, stocks, categorias, estados):
    if len(titulos) == 0:

        print("No hay productos cargados.")
    else:
        titulo = input("Ingrese el titulo del producto a eliminar: ")
        pos = buscar_producto(titulo, titulos)

        if pos == len(titulos):

            print("Producto no encontrado.")
        else:
            if estados[pos] == "Discontinuado" and stocks[pos] == 0:

                confirmacion = input("Confirma eliminacion? S/N: ")

                while (confirmacion != "S" and confirmacion != "s"
                       and confirmacion != "N" and confirmacion != "n"):
                    print("Opcion invalida.")
                    confirmacion = input("Confirma eliminacion? S/N: ")

                if confirmacion == "S" or confirmacion == "s":
                    titulos.pop(pos)
                    tipos.pop(pos)
                    plataformas.pop(pos)
                    precios_venta.pop(pos)
                    precios_alquiler.pop(pos)
                    stocks.pop(pos)
                    categorias.pop(pos)
                    estados.pop(pos)

                    print("Producto eliminado.")
                else:
                    print("Eliminacion cancelada.")
            else:
                print("Solo se puede eliminar si esta Discontinuado y con stock cero.")

# Autor principal: Valentina Rodriguez
def modificar_producto(titulos, tipos, plataformas, precios_venta,
                        precios_alquiler, stocks, categorias, estados):
    if len(titulos) == 0:
        print("No hay productos cargados.")
    else:
        titulo = input("Ingrese el titulo del producto a modificar: ")
        pos = buscar_producto(titulo, titulos)

        if pos == len(titulos):
            print("Producto no encontrado.")
        else:
            opcion = "0"

            while opcion != "9":

                print("Producto seleccionado:", titulos[pos])
                print("1. Modificar titulo")
                print("2. Modificar tipo")
                print("3. Modificar plataforma/formato")
                print("4. Modificar precio de venta y/o alquiler")
                print("5. Modificar stock")
                print("6. Modificar categorias")
                print("7. Modificar estado")
                print("8. Ver categorias actuales")
                print("9. Volver al menu")

                opcion = input("Seleccione una opcion: ")

                if opcion == "1":
                    nuevo = input("Nuevo titulo: ")
                    while nuevo == "":
                        print("El titulo no puede quedar vacio.")
                        nuevo = input("Nuevo titulo: ")
                    titulos[pos] = nuevo

                elif opcion == "2":
                    tipos[pos] = cargar_tipo()

                elif opcion == "3":
                    nuevo = input("Nueva plataforma/formato: ")
                    while nuevo == "":
                        print("No puede quedar vacio.")
                        nuevo = input("Nueva plataforma/formato: ")
                    plataformas[pos] = nuevo

                elif opcion == "4":
                    nuevo_venta, nuevo_alquiler = cargar_precios()
                    precios_venta[pos] = nuevo_venta
                    precios_alquiler[pos] = nuevo_alquiler

                elif opcion == "5":
                    nuevo = int(input("Nuevo stock: "))
                    while nuevo < 0:
                        print("El stock debe ser positivo o cero.")
                        nuevo = int(input("Nuevo stock: "))
                    stocks[pos] = nuevo

                elif opcion == "6":
                    categorias[pos] = cargar_categorias()

                elif opcion == "7":
                    estados[pos] = cargar_estado()

                elif opcion == "8":
                    print("Categorias actuales:", categorias[pos])

                elif opcion == "9":
                    print("Volviendo al menu...")

                else:
                    print("Opcion invalida.")

# Autor principal: Agustina Maquieira
def informe_general(titulos, tipos, plataformas, precios_venta,
                    precios_alquiler, stocks, categorias, estados):
    if len(titulos) == 0:
        print("No hay productos cargados.")
    else:
        ordenar_por_stock_y_titulo(titulos, tipos, plataformas, precios_venta,
                                   precios_alquiler, stocks, categorias, estados)

        print("=" * 80)
        print("INFORME GENERAL DE PRODUCTOS")
        print("=" * 80)

        i = 0
        while i < len(titulos):

            print("Titulo:", titulos[i])
            print("Tipo:", tipos[i])
            print("Plataforma/Formato:", plataformas[i])
            print("Precio de venta:", precios_venta[i])
            print("Precio de alquiler:", precios_alquiler[i])
            print("Stock:", stocks[i])

            print("Categorias:", end=" ")

            j = 0
            while j < len(categorias[i]):

                if j < len(categorias[i]) - 1:
                    print(categorias[i][j], end=", ")

                else:
                    print(categorias[i][j])

                j = j + 1

            print("Estado:", estados[i])
            print("-" * 80)
            i = i + 1

# Autor principal: Valentina Rodriguez y Ainara Salvatierra
def informe_matricial(tipos, categorias):
    if len(tipos) == 0:
        print("No hay productos cargados.")
    else:
        matriz = construir_matriz_categoria_tipo(tipos, categorias)

        print("=" * 80)
        print("INFORME MATRICIAL - CANTIDAD DE PRODUCTOS POR CATEGORIA Y TIPO")
        print("=" * 80)

        encabezado = ajustar_texto("Categoria", 20)

        c = 0
        while c < len(tipos_validos):
            encabezado = encabezado + ajustar_texto(tipos_validos[c], 15)

            c = c + 1
        print(encabezado)
        print("-" * 80)

        f = 0
        while f < len(matriz):

            fila_texto = ajustar_texto(categorias_validas[f], 20)

            c = 0
            while c < len(matriz[f]):

                fila_texto = fila_texto + ajustar_texto(str(matriz[f][c]), 15)

                c = c + 1
            print(fila_texto)
            f = f + 1

        print("-" * 80)