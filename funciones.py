import random

tipos_validos = ["Película", "Videojuego"]
categorias_validas = ["Acción", "Aventura", "Deportes", "Estrategia", "Terror", "Ciencia Ficción", "Infantil", "Otro"]
estados_validos = ["Disponible", "Alquilado", "Reservado", "Discontinuado"]

# Plataformas separadas por tipo de producto, para que no quede una película asignada a una plataforma de Videojuego (o viceversa)
plataformas_peliculas = ["Blu-ray", "DVD"]
plataformas_videojuegos = ["PlayStation 5", "Xbox Series X", "Nintendo Switch", "PC"]

titulos_azar = ["Super Mario Bros Wonder", "The Legend of Zelda", "Jurassic Park", "Star Wars", "Call of Duty", "Resident Evil", "Final Fantasy VII", "Hogwarts Legacy", "Ace Attorney", "Mazze Runner: Correr o Morir", "Avengers: Endgame", "Harry Potter y la Piedra Filosofal", "Los Juegos del Hambre", "El Señor de los Anillos"]

# Autor principal: Agustina Maquieira
def mostrar_menu():
    print("=" * 50)
    print("SISTEMA DE GESTIÓN: RETROPIXEL STORE")
    print("1. Registrar producto (Alta)")
    print("2. Eliminar producto (Baja)")
    print("3. Modificar producto (Modificación)")
    print("4. Informe General – Visualización de los datos")
    print("5. Salir")
    print("=" * 50)


# Autor principal: Valentina Marfany
def buscar_producto(titulo_buscado, titulos):
    i = 0
    while i < len(titulos) and titulos[i].lower() != titulo_buscado.lower():
        i = i + 1
    return i


# Autor principal: Valentina Rodriguez
def cargar_tipo():
    print("Tipo de contenido:")
    print("1. Película")
    print("2. Videojuego")
    opcion = input("Seleccione una opción: ")

    while opcion != "1" and opcion != "2":
        print("Opción inválida.")
        opcion = input("Seleccione 1 o 2: ")

    if opcion == "1":
        tipo = "Película"
    else:
        tipo = "Videojuego"

    return tipo


# Autor principal: Valentina Rodriguez
# Reemplaza al input libre de plataforma: ahora se elige de una lista
# que depende del tipo de producto (Película o Videojuego), para que
# no se pueda asignar, por ejemplo, "Nintendo Switch" a una Película.
def cargar_plataforma(tipo):

    if tipo == "Película":
        plataformas_validas = plataformas_peliculas
    else:
        plataformas_validas = plataformas_videojuegos

    print("Plataformas disponibles:")
    i = 0
    while i < len(plataformas_validas):
        print(str(i + 1) + ". " + plataformas_validas[i])
        i = i + 1

    print(str(len(plataformas_validas) + 1) + ". Agregar nueva plataforma")

    opcion = int(input("Seleccione una opción: "))

    while opcion < 1 or opcion > len(plataformas_validas) + 1:
        print("Opción inválida.")
        opcion = int(input("Seleccione una opción: "))

    if opcion == len(plataformas_validas) + 1:
        nueva = input("Ingrese el nombre de la nueva plataforma: ")
        while nueva == "":
            print("La plataforma no puede quedar vacía.")
            nueva = input("Ingrese el nombre de la nueva plataforma: ")

        plataformas_validas.append(nueva)
        print("Plataforma agregada correctamente.")
        return nueva

    return plataformas_validas[opcion - 1]


# Autor principal: Valentina Rodriguez
# Reemplaza a cargar_categoria(): ahora permite elegir varios géneros
# para un mismo producto (por ejemplo: Aventura y Acción a la vez).
def cargar_categorias():

    categorias_elegidas = []
    opcion = -1

    while opcion != 0 or len(categorias_elegidas) == 0:

        print("Categorías disponibles:")
        i = 0
        while i < len(categorias_validas):
            print(str(i + 1) + ". " + categorias_validas[i])
            i = i + 1

        print("0. Terminar selección de categorías")

        opcion = int(input("Seleccione una categoría: "))

        while opcion < 0 or opcion > len(categorias_validas):
            print("Opción inválida.")
            opcion = int(input("Seleccione una categoría: "))

        if opcion != 0:
            categoria_elegida = categorias_validas[opcion - 1]

            j = 0
            while j < len(categorias_elegidas) and categorias_elegidas[j] != categoria_elegida:
                j = j + 1

            if j == len(categorias_elegidas):
                categorias_elegidas.append(categoria_elegida)
                print("Categoría agregada:", categoria_elegida)
            else:
                print("Ya seleccionó esta categoría.")
        else:
            if len(categorias_elegidas) == 0:
                print("Debe seleccionar al menos una categoría.")

    return categorias_elegidas


# Autor principal: Ainara Salvatierra
def cargar_estado():
    i = 0
    while i < len(estados_validos):
        print(str(i + 1) + ". " + estados_validos[i])
        i = i + 1

    opcion = int(input("Seleccione estado: "))

    while opcion < 1 or opcion > len(estados_validos):
        print("Estado inválido.")
        opcion = int(input("Seleccione estado: "))

    return estados_validos[opcion - 1]


# Autor principal: Ainara Salvatierra
# Reemplaza al input único de precio: ahora se pregunta la modalidad
# (Alquiler, Venta o Venta y Alquiler) y se piden los precios que correspondan.
def cargar_modalidad_y_precios():

    print("Modalidad de comercialización:")
    print("1. Alquiler")
    print("2. Venta")
    print("3. Venta y Alquiler")

    opcion = input("Seleccione una opción: ")

    while opcion != "1" and opcion != "2" and opcion != "3":
        print("Opción inválida.")
        opcion = input("Seleccione 1, 2 o 3: ")

    if opcion == "1":
        modalidad = "Alquiler"

        precio_alquiler = float(input("Ingrese precio de alquiler: "))
        while precio_alquiler < 0:
            print("El precio no puede ser negativo.")
            precio_alquiler = float(input("Ingrese precio de alquiler: "))

        precio_venta = None

    elif opcion == "2":
        modalidad = "Venta"

        precio_venta = float(input("Ingrese precio de venta: "))
        while precio_venta < 0:
            print("El precio no puede ser negativo.")
            precio_venta = float(input("Ingrese precio de venta: "))

        precio_alquiler = None

    else:
        modalidad = "Venta y Alquiler"

        precio_alquiler = float(input("Ingrese precio de alquiler: "))
        while precio_alquiler < 0:
            print("El precio no puede ser negativo.")
            precio_alquiler = float(input("Ingrese precio de alquiler: "))

        precio_venta = float(input("Ingrese precio de venta: "))
        while precio_venta < 0:
            print("El precio no puede ser negativo.")
            precio_venta = float(input("Ingrese precio de venta: "))

    return modalidad, precio_alquiler, precio_venta


# Autor principal: Valentina Marfany
def registrar_manual(titulos, tipos, plataformas, modalidades, precios_alquiler, precios_venta, stocks, categorias, estados):
    titulo = input("Ingrese título del producto: ")

    while titulo == "":
        print("El título no puede quedar vacío.")
        titulo = input("Ingrese título del producto: ")

    tipo = cargar_tipo()

    plataforma = cargar_plataforma(tipo)

    modalidad, precio_alquiler, precio_venta = cargar_modalidad_y_precios()

    stock = int(input("Ingrese cantidad disponible en stock: "))
    while stock < 0:
        print("El stock debe ser positivo o cero.")
        stock = int(input("Ingrese cantidad disponible en stock: "))

    categoria = cargar_categorias()
    estado = "Disponible"

    titulos.append(titulo)
    tipos.append(tipo)
    plataformas.append(plataforma)
    modalidades.append(modalidad)
    precios_alquiler.append(precio_alquiler)
    precios_venta.append(precio_venta)
    stocks.append(stock)
    categorias.append(categoria)
    estados.append(estado)

    print("Producto registrado correctamente.")


# Autor principal: Valentina Marfany
def registrar_automatico(titulos, tipos, plataformas, modalidades, precios_alquiler, precios_venta, stocks, categorias, estados):
    titulo = random.choice(titulos_azar)
    tipo = random.choice(tipos_validos)

    if tipo == "Película":
        plataforma = random.choice(plataformas_peliculas)
    else:
        plataforma = random.choice(plataformas_videojuegos)

    modalidad = random.choice(["Alquiler", "Venta", "Venta y Alquiler"])

    if modalidad == "Alquiler":
        precio_alquiler = round(random.uniform(2500.50, 15000.00), 2)
        precio_venta = None
    elif modalidad == "Venta":
        precio_alquiler = None
        precio_venta = round(random.uniform(15000.00, 45999.99), 2)
    else:
        precio_alquiler = round(random.uniform(2500.50, 15000.00), 2)
        precio_venta = round(random.uniform(15000.00, 45999.99), 2)

    stock = random.randint(0, 50)

    cantidad_generos = random.randint(1, 3)
    categoria = []
    while len(categoria) < cantidad_generos:
        genero_random = random.choice(categorias_validas)

        j = 0
        while j < len(categoria) and categoria[j] != genero_random:
            j = j + 1

        if j == len(categoria):
            categoria.append(genero_random)

    estado = "Disponible"

    titulos.append(titulo)
    tipos.append(tipo)
    plataformas.append(plataforma)
    modalidades.append(modalidad)
    precios_alquiler.append(precio_alquiler)
    precios_venta.append(precio_venta)
    stocks.append(stock)
    categorias.append(categoria)
    estados.append(estado)

    print("Producto generado automáticamente.")


# Autor principal: Agustina Maquieira
def registrar_producto(titulos, tipos, plataformas, modalidades, precios_alquiler, precios_venta, stocks, categorias, estados):
    cantidad = int(input("¿Cuántos productos desea registrar?: "))

    while cantidad <= 0:
        print("Debe registrar al menos un producto.")
        cantidad = int(input("¿Cuántos productos desea registrar?: "))

    i = 0
    while i < cantidad:
        print("Producto", i + 1)
        print("1. Carga manual")
        print("2. Carga automática")
        opcion = input("Seleccione una opción: ")

        while opcion != "1" and opcion != "2":
            print("Opción inválida.")
            opcion = input("Seleccione 1 o 2: ")

        if opcion == "1":
            registrar_manual(titulos, tipos, plataformas, modalidades, precios_alquiler, precios_venta, stocks, categorias, estados)
        else:
            registrar_automatico(titulos, tipos, plataformas, modalidades, precios_alquiler, precios_venta, stocks, categorias, estados)

        i = i + 1


# Autor principal: Ainara Salvatierra
def eliminar_producto(titulos, tipos, plataformas, modalidades, precios_alquiler, precios_venta, stocks, categorias, estados):
    if len(titulos) == 0:
        print("No hay productos cargados.")
    else:
        titulo = input("Ingrese el título del producto a eliminar: ")
        pos = buscar_producto(titulo, titulos)

        if pos == len(titulos):
            print("Producto no encontrado.")
        else:
            if estados[pos] == "Discontinuado" and stocks[pos] == 0:
                confirmacion = input("Confirma eliminación? S/N: ")

                if confirmacion == "S" or confirmacion == "s":
                    titulos.pop(pos)
                    tipos.pop(pos)
                    plataformas.pop(pos)
                    modalidades.pop(pos)
                    precios_alquiler.pop(pos)
                    precios_venta.pop(pos)
                    stocks.pop(pos)
                    categorias.pop(pos)
                    estados.pop(pos)
                    print("Producto eliminado.")
                else:
                    print("Eliminación cancelada.")
            else:
                print("Solo se puede eliminar si está Discontinuado y con stock cero.")


# Autor principal: Agustina Maquieira
# Actualiza el stock de un producto sumando o restando unidades, en lugar de tener que reescribir el número entero.
def actualizar_stock_rapido(pos, stocks):
    print("Stock actual:", stocks[pos])
    signo = input("Ingrese + para sumar o - para restar: ")

    while signo != "+" and signo != "-":
        print("Opción inválida.")
        signo = input("Ingrese + para sumar o - para restar: ")

    cantidad = int(input("Ingrese la cantidad: "))
    while cantidad < 0:
        print("La cantidad no puede ser negativa.")
        cantidad = int(input("Ingrese la cantidad: "))

    if signo == "+":
        stocks[pos] = stocks[pos] + cantidad
    else:
        nuevo_stock = stocks[pos] - cantidad
        while nuevo_stock < 0:
            print("No puede restar más unidades que el stock actual.")
            cantidad = int(input("Ingrese la cantidad: "))
            nuevo_stock = stocks[pos] - cantidad
        stocks[pos] = nuevo_stock

    print("Stock actualizado. Nuevo stock:", stocks[pos])


# Autor principal: Ainara Salvatierra
# Elimina de una sola vez todos los productos que están discontinuados y con stock cero, sin tener que hacerlo uno por uno.
def eliminar_en_lote(titulos, tipos, plataformas, modalidades, precios_alquiler, precios_venta, stocks, categorias, estados):
    if len(titulos) == 0:
        print("No hay productos cargados.")
    else:
        confirmacion = input("¿Confirma eliminar todos los productos Discontinuados con stock 0? S/N: ")

        if confirmacion == "S" or confirmacion == "s":
            cantidad_eliminados = 0

            # Se recorre de atrás hacia adelante para que el .pop() no
            # desordene las posiciones de los productos que faltan revisar
            i = len(titulos) - 1
            while i >= 0:
                if estados[i] == "Discontinuado" and stocks[i] == 0:
                    titulos.pop(i)
                    tipos.pop(i)
                    plataformas.pop(i)
                    modalidades.pop(i)
                    precios_alquiler.pop(i)
                    precios_venta.pop(i)
                    stocks.pop(i)
                    categorias.pop(i)
                    estados.pop(i)
                    cantidad_eliminados = cantidad_eliminados + 1
                i = i - 1

            print("Productos eliminados en lote:", cantidad_eliminados)
        else:
            print("Eliminación en lote cancelada.")


# Autor principal: Valentina Rodriguez
def modificar_producto(titulos, tipos, plataformas, modalidades, precios_alquiler, precios_venta, stocks, categorias, estados):
    if len(titulos) == 0:
        print("No hay productos cargados.")
    else:
        titulo = input("Ingrese el título del producto a modificar: ")
        pos = buscar_producto(titulo, titulos)

        if pos == len(titulos):
            print("Producto no encontrado.")
        else:
            opcion = "0"

            while opcion != "10":
                print("Producto seleccionado:", titulos[pos])
                print("1. Modificar título")
                print("2. Modificar tipo")
                print("3. Modificar plataforma/formato")
                print("4. Modificar modalidad y precios")
                print("5. Modificar stock (reemplazar valor)")
                print("6. Modificar categorías")
                print("7. Modificar estado")
                print("8. Actualizar stock rápido (sumar/restar)")
                print("9. Eliminar en lote (Discontinuados con stock 0)")
                print("10. Volver al menú")

                opcion = input("Seleccione una opción: ")

                if opcion == "1":
                    nuevo = input("Nuevo título: ")
                    while nuevo == "":
                        print("El título no puede quedar vacío.")
                        nuevo = input("Nuevo título: ")
                    titulos[pos] = nuevo

                elif opcion == "2":
                    tipos[pos] = cargar_tipo()

                elif opcion == "3":
                    plataformas[pos] = cargar_plataforma(tipos[pos])

                elif opcion == "4":
                    modalidad, precio_alquiler, precio_venta = cargar_modalidad_y_precios()
                    modalidades[pos] = modalidad
                    precios_alquiler[pos] = precio_alquiler
                    precios_venta[pos] = precio_venta

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
                    actualizar_stock_rapido(pos, stocks)

                elif opcion == "9":
                    eliminar_en_lote(titulos, tipos, plataformas, modalidades, precios_alquiler, precios_venta, stocks, categorias, estados)
                    # Como eliminar_en_lote puede haber borrado el producto que se
                    # estaba modificando, se vuelve a buscar su posición actual
                    if pos < len(titulos) and titulos[pos].lower() == titulo.lower():
                        pass
                    else:
                        pos = buscar_producto(titulo, titulos)
                        if pos == len(titulos):
                            print("El producto que estaba modificando fue eliminado en el lote.")
                            opcion = "10"

                elif opcion == "10":
                    print("Volviendo al menú...")

                else:
                    print("Opción inválida.")


# Autor principal: Ainara Salvatierra
# Ordenamiento manual de mayor a menor stock; si hay igualdad de stock,
# ordena alfabéticamente por título.
def ordenar_por_stock_y_titulo(titulos, tipos, plataformas, modalidades, precios_alquiler, precios_venta, stocks, categorias, estados):
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

                aux = modalidades[i]
                modalidades[i] = modalidades[j]
                modalidades[j] = aux

                aux = precios_alquiler[i]
                precios_alquiler[i] = precios_alquiler[j]
                precios_alquiler[j] = aux

                aux = precios_venta[i]
                precios_venta[i] = precios_venta[j]
                precios_venta[j] = aux

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


# Autor principal: Valentina Rodriguez
# Ordenamiento manual por precio (alquiler o venta, a elección del usuario),
# de menor a mayor o de mayor a menor según lo que se pida.
def ordenar_por_precio(titulos, tipos, plataformas, modalidades, precios_alquiler, precios_venta, stocks, categorias, estados, precio_elegido, orden_elegido):

    if precio_elegido == "1":
        precios_a_usar = precios_alquiler
    else:
        precios_a_usar = precios_venta

    i = 0
    while i < len(titulos) - 1:
        j = i + 1
        while j < len(titulos):

            cambiar = False
            precio_i = precios_a_usar[i]
            precio_j = precios_a_usar[j]

            # Los productos sin precio en esa modalidad (None) se dejan siempre al final
            if precio_i == None and precio_j != None:
                cambiar = True
            elif precio_i != None and precio_j != None:
                if orden_elegido == "1" and precio_j < precio_i:
                    cambiar = True
                elif orden_elegido == "2" and precio_j > precio_i:
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

                aux = modalidades[i]
                modalidades[i] = modalidades[j]
                modalidades[j] = aux

                aux = precios_alquiler[i]
                precios_alquiler[i] = precios_alquiler[j]
                precios_alquiler[j] = aux

                aux = precios_venta[i]
                precios_venta[i] = precios_venta[j]
                precios_venta[j] = aux

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


# Autor principal: Valentina Marfany
# Convierte la lista de géneros de un producto en un texto legible,
# por ejemplo: ["Aventura", "Acción"] -> "Aventura, Acción"
def texto_de_categorias(lista_categorias_producto):
    texto = ""
    j = 0
    while j < len(lista_categorias_producto):
        texto = texto + lista_categorias_producto[j]
        if j < len(lista_categorias_producto) - 1:
            texto = texto + ", "
        j = j + 1
    return texto


# Autor principal: Ainara Salvatierra
# Arma el texto de precio según la modalidad del producto.
def texto_de_precio(modalidad, precio_alquiler, precio_venta):
    if modalidad == "Venta y Alquiler":
        texto = "Alquiler $" + str(precio_alquiler) + " / Venta $" + str(precio_venta)
    elif modalidad == "Alquiler":
        texto = "$" + str(precio_alquiler)
    else:
        texto = "$" + str(precio_venta)
    return texto


# Autor principal: Ainara Salvatierra
# Calcula la suma de (precio_venta * stock) de todos los productos que
# tengan precio de venta cargado (modalidad Venta o Venta y Alquiler).
def calcular_valor_total_inventario(precios_venta, stocks, modalidades):
    total = 0.0
    i = 0
    while i < len(precios_venta):
        if modalidades[i] == "Venta" or modalidades[i] == "Venta y Alquiler":
            total = total + (precios_venta[i] * stocks[i])
        i = i + 1
    return round(total, 2)


# Autor principal: Valentina Marfany
# Cuenta cuántos productos hay de cada tipo (Película / Videojuego).
def calcular_cantidad_por_tipo(tipos):
    cantidad_peliculas = 0
    cantidad_videojuegos = 0

    i = 0
    while i < len(tipos):
        if tipos[i] == "Película":
            cantidad_peliculas = cantidad_peliculas + 1
        else:
            cantidad_videojuegos = cantidad_videojuegos + 1
        i = i + 1

    return cantidad_peliculas, cantidad_videojuegos


# Autor principal: Agustina Maquieira
def informe_general(titulos, tipos, plataformas, modalidades, precios_alquiler, precios_venta, stocks, categorias, estados):
    if len(titulos) == 0:
        print("No hay productos cargados.")
    else:
        print("¿Cómo desea ordenar el informe?")
        print("1. Por stock (de mayor a menor)")
        print("2. Por precio")
        opcion_orden = input("Seleccione una opción: ")

        while opcion_orden != "1" and opcion_orden != "2":
            print("Opción inválida.")
            opcion_orden = input("Seleccione 1 o 2: ")

        if opcion_orden == "1":
            ordenar_por_stock_y_titulo(titulos, tipos, plataformas, modalidades, precios_alquiler, precios_venta, stocks, categorias, estados)
        else:
            print("¿Sobre qué precio desea ordenar?")
            print("1. Precio de alquiler")
            print("2. Precio de venta")
            precio_elegido = input("Seleccione una opción: ")

            while precio_elegido != "1" and precio_elegido != "2":
                print("Opción inválida.")
                precio_elegido = input("Seleccione 1 o 2: ")

            print("¿Cómo desea ordenar?")
            print("1. Menor a mayor")
            print("2. Mayor a menor")
            orden_elegido = input("Seleccione una opción: ")

            while orden_elegido != "1" and orden_elegido != "2":
                print("Opción inválida.")
                orden_elegido = input("Seleccione 1 o 2: ")

            ordenar_por_precio(titulos, tipos, plataformas, modalidades, precios_alquiler, precios_venta, stocks, categorias, estados, precio_elegido, orden_elegido)

        print("=" * 80)
        print("INFORME GENERAL DE PRODUCTOS")
        print("=" * 80)

        i = 0
        while i < len(titulos):
            print("Título:", titulos[i])
            print("Tipo:", tipos[i])
            print("Plataforma/Formato:", plataformas[i])
            print("Modalidad:", modalidades[i])
            print("Precio:", texto_de_precio(modalidades[i], precios_alquiler[i], precios_venta[i]))
            print("Stock:", stocks[i])
            print("Categoría:", texto_de_categorias(categorias[i]))
            print("Estado:", estados[i])
            print("-" * 80)
            i = i + 1

        cantidad_peliculas, cantidad_videojuegos = calcular_cantidad_por_tipo(tipos)
        valor_total = calcular_valor_total_inventario(precios_venta, stocks, modalidades)

        print("=" * 80)
        print("RESUMEN GENERAL")
        print("Cantidad de Películas:", cantidad_peliculas)
        print("Cantidad de Videojuegos:", cantidad_videojuegos)
        print("Valor total del inventario (según precio de venta): $" + str(valor_total))
        print("=" * 80)
