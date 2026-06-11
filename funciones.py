import random

titulos = []
tipos = []
plataformas = []
precios = []
stocks = []
categorias = []
estados = []

tipos_validos = ["Película", "Videojuego"]
categorias_validas = ["Acción", "Aventura", "Deportes", "Estrategia", "Terror", "Ciencia Ficción", "Infantil", "Otro"]
estados_validos = ["Disponible", "Alquilado", "Reservado", "Discontinuado"]

titulos_azar = ["Super Mario Bros Wonder", "The Legend of Zelda", "Jurassic Park", "Star Wars"]
plataformas_azar = ["PlayStation 5", "Xbox Series X", "Nintendo Switch", "PC", "Blu-ray", "DVD"]

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
def buscar_producto(titulo_buscado):
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
def cargar_categoria():
    i = 0
    while i < len(categorias_validas):
        print(str(i + 1) + ". " + categorias_validas[i])
        i = i + 1

    opcion = int(input("Seleccione categoría: "))

    while opcion < 1 or opcion > len(categorias_validas):
        print("Categoría inválida.")
        opcion = int(input("Seleccione categoría: "))

    return categorias_validas[opcion - 1]

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

# Autor principal: Valentina Marfany
def registrar_manual():
    titulo = input("Ingrese título del producto: ")

    while titulo == "":
        print("El título no puede quedar vacío.")
        titulo = input("Ingrese título del producto: ")

    tipo = cargar_tipo()

    plataforma = input("Ingrese plataforma o formato: ")
    while plataforma == "":
        print("La plataforma o formato no puede quedar vacío.")
        plataforma = input("Ingrese plataforma o formato: ")

    precio = float(input("Ingrese precio de alquiler o venta: "))
    while precio < 0:
        print("El precio no puede ser negativo.")
        precio = float(input("Ingrese precio de alquiler o venta: "))

    stock = int(input("Ingrese cantidad disponible en stock: "))
    while stock < 0:
        print("El stock debe ser positivo o cero.")
        stock = int(input("Ingrese cantidad disponible en stock: "))

    categoria = cargar_categoria()
    estado = cargar_estado()

    titulos.append(titulo)
    tipos.append(tipo)
    plataformas.append(plataforma)
    precios.append(precio)
    stocks.append(stock)
    categorias.append(categoria)
    estados.append(estado)

    print("Producto registrado correctamente.")

# Autor principal: Valentina Marfany
def registrar_automatico():
    titulo = random.choice(titulos_azar)
    tipo = random.choice(tipos_validos)
    plataforma = random.choice(plataformas_azar)
    precio = round(random.uniform(2500.50, 45999.99), 2)
    stock = random.randint(0, 50)
    categoria = random.choice(categorias_validas)
    estado = random.choice(estados_validos)

    titulos.append(titulo)
    tipos.append(tipo)
    plataformas.append(plataforma)
    precios.append(precio)
    stocks.append(stock)
    categorias.append(categoria)
    estados.append(estado)

    print("Producto generado automáticamente.")

# Autor principal: Agustina Maquieira
def registrar_producto():
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
            registrar_manual()
        else:
            registrar_automatico()

        i = i + 1

# Autor principal: Ainara Salvatierra
def eliminar_producto():
    if len(titulos) == 0:
        print("No hay productos cargados.")
    else:
        titulo = input("Ingrese el título del producto a eliminar: ")
        pos = buscar_producto(titulo)

        if pos == len(titulos):
            print("Producto no encontrado.")
        else:
            if estados[pos] == "Discontinuado" and stocks[pos] == 0:
                confirmacion = input("Confirma eliminación? S/N: ")

                if confirmacion == "S" or confirmacion == "s":
                    titulos.pop(pos)
                    tipos.pop(pos)
                    plataformas.pop(pos)
                    precios.pop(pos)
                    stocks.pop(pos)
                    categorias.pop(pos)
                    estados.pop(pos)
                    print("Producto eliminado.")
                else:
                    print("Eliminación cancelada.")
            else:
                print("Solo se puede eliminar si está Discontinuado y con stock cero.")

# Autor principal: Valentina Rodriguez
def modificar_producto():
    if len(titulos) == 0:
        print("No hay productos cargados.")
    else:
        titulo = input("Ingrese el título del producto a modificar: ")
        pos = buscar_producto(titulo)

        if pos == len(titulos):
            print("Producto no encontrado.")
        else:
            opcion = "0"

            while opcion != "8":
                print("Producto seleccionado:", titulos[pos])
                print("1. Modificar título")
                print("2. Modificar tipo")
                print("3. Modificar plataforma/formato")
                print("4. Modificar precio")
                print("5. Modificar stock")
                print("6. Modificar categoría")
                print("7. Modificar estado")
                print("8. Volver al menú")

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
                    nuevo = input("Nueva plataforma/formato: ")
                    while nuevo == "":
                        print("No puede quedar vacío.")
                        nuevo = input("Nueva plataforma/formato: ")
                    plataformas[pos] = nuevo

                elif opcion == "4":
                    nuevo = float(input("Nuevo precio: "))
                    while nuevo < 0:
                        print("El precio no puede ser negativo.")
                        nuevo = float(input("Nuevo precio: "))
                    precios[pos] = nuevo

                elif opcion == "5":
                    nuevo = int(input("Nuevo stock: "))
                    while nuevo < 0:
                        print("El stock debe ser positivo o cero.")
                        nuevo = int(input("Nuevo stock: "))
                    stocks[pos] = nuevo

                elif opcion == "6":
                    categorias[pos] = cargar_categoria()

                elif opcion == "7":
                    estados[pos] = cargar_estado()

                elif opcion == "8":
                    print("Volviendo al menú...")

                else:
                    print("Opción inválida.")

# Autor principal: Ainara Salvatierra
def ordenar_por_stock_y_titulo():
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

                aux = precios[i]
                precios[i] = precios[j]
                precios[j] = aux

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

# Autor principal: Agustina Maquieira
def informe_general():
    if len(titulos) == 0:
        print("No hay productos cargados.")
    else:
        ordenar_por_stock_y_titulo()

        print("=" * 80)
        print("INFORME GENERAL DE PRODUCTOS")
        print("=" * 80)

        i = 0
        while i < len(titulos):
            print("Título:", titulos[i])
            print("Tipo:", tipos[i])
            print("Plataforma/Formato:", plataformas[i])
            print("Precio:", precios[i])
            print("Stock:", stocks[i])
            print("Categoría:", categorias[i])
            print("Estado:", estados[i])
            print("-" * 80)
            i = i + 1