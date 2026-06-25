from funciones import (mostrar_menu, registrar_producto, eliminar_producto, modificar_producto, informe_general, informe_matricial)

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
    
    while opcion != "6":
        mostrar_menu()

        opcion = input("Elegi una opcion: ")

        if opcion == "1":
            registrar_producto(titulos, tipos, plataformas, precios_venta,
                               precios_alquiler, stocks, categorias, estados)

        elif opcion == "2":
            eliminar_producto(titulos, tipos, plataformas, precios_venta,
                              precios_alquiler, stocks, categorias, estados)

        elif opcion == "3":
            modificar_producto(titulos, tipos, plataformas, precios_venta,
                               precios_alquiler, stocks, categorias, estados)

        elif opcion == "4":
            informe_general(titulos, tipos, plataformas, precios_venta,
                            precios_alquiler, stocks, categorias, estados)

        elif opcion == "5":
            informe_matricial(tipos, categorias)

        elif opcion == "6":
            print("\nGracias por usar RetroPixel Store! Nos vemos pronto.")

        else:
            print("Opcion invalida. Ingrese un numero del 1 al 6.")


main()