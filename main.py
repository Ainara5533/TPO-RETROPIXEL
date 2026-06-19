from funciones import mostrar_menu, registrar_producto, eliminar_producto, modificar_producto, informe_general

titulos = []
tipos = []
plataformas = []
precios_venta = []
precios_alquiler = []
stocks = []
categorias = []
estados = []

def main():
    opcion = "0"
    while opcion != "5":
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_producto(titulos, tipos, plataformas, precios_venta, precios_alquiler, stocks, categorias, estados)
        elif opcion == "2":
            eliminar_producto(titulos, tipos, plataformas, precios_venta, precios_alquiler, stocks, categorias, estados)
        elif opcion == "3":
            modificar_producto(titulos, tipos, plataformas, precios_venta, precios_alquiler, stocks, categorias, estados)
        elif opcion == "4":
            informe_general(titulos, tipos, plataformas, precios_venta, precios_alquiler, stocks, categorias, estados)
        elif opcion == "5":
            print("Sistema finalizado.")
        else:
            print("Opción inválida.")

main()