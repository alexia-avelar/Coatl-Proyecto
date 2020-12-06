from peliculas_view import viewAllPeliculas, addPelicula, updatePelicula, deletePelicula
from compradetallada_view import addCompra, viewAllCompras, updateCompra, deleteCompra
from boleto_view import addBoleto, viewAllBoletos, deleteBoleto
from sucursal_view import (
    viewAllSucursales,
    addSucursal,
    updateSucursal,
    deleteSucursal,
)
from asiento_view import (
    viewAllAsientos,
    addAsiento,
    updateAsiento,
    deleteAsiento,
)
from sala_view import (
    viewAllSalas,
    addSala,
    updateSala,
    deleteSala,
)


def goToSucursalesSubMenu():
    while True:
        print("Menú Sucursal")
        print("0 - Regresar al menú principal: ")
        print("1 - Ver Sucursales: ")
        print("2 - Agregar Sucursal: ")
        print("3 - Actualizar Sucursal: ")
        print("4 - Borrar Sucursal: ")
        optionSucursal = int(input("Seleccione una opción: "))

        if optionSucursal == 0:
            print("Regresando a menú principal...")
            break
        elif optionSucursal == 1:
            viewAllSucursales()
        elif optionSucursal == 2:
            addSucursal()
        elif optionSucursal == 3:
            updateSucursal()
        elif optionSucursal == 4:
            deleteSucursal()


def goToAsientosSubMenu():
    while True:
        print("Asientos")
        print("Menu: ")
        print("0 - Regresar al menú principal: ")
        print("1 - Ver Asientos: ")
        print("2 - Agregar Asiento: ")
        print("3 - Actualizar Asiento: ")
        print("4 - Eliminar Asiento: ")
        optionAsiento = int(input("Seleccione una opción: "))

        if optionAsiento == 0:
            print("Regresando a menú principal...")
            break
        elif optionAsiento == 1:
            viewAllAsientos()
        elif optionAsiento == 2:
            addAsiento()
        elif optionAsiento == 3:
            updateAsiento()
        elif optionAsiento == 4:
            deleteAsiento()


def goToSalaSubMenu():
    while True:
        print("Menú Sala")
        print("0 - Regresar al menú principal: ")
        print("1 - Ver Salas: ")
        print("2 - Agregar Sala: ")
        print("3 - Actualizar Sala: ")
        print("4 - Eliminar Sala: ")
        optionSala = int(input("Seleccione una opción: "))

        if optionSala == 0:
            print("Regresando a menú principal...")
            break
        elif optionSala == 1:
            viewAllSalas()
        elif optionSala == 2:
            addSala()
        elif optionSala == 3:
            updateSala()
        elif optionSala == 4:
            deleteSala()


def goToPeliculasSubMenu():
    while True:
        print("Menú Películas")
        print("0 - Regresar a menú principal: ")
        print("1 - Ver Peliculas: ")
        print("2 - Agregar Pelicula: ")
        print("3 - Actualizar Pelicula: ")
        print("4 - Eliminar Pelicula: ")
        optionPelicula = int(input("Seleccione una opción: "))

        if optionPelicula == 0:
            print("Regresando a menú principal...")
            break
        elif optionPelicula == 1:
            viewAllPeliculas()
        elif optionPelicula == 2:
            addPelicula()
        elif optionPelicula == 3:
            updatePelicula()
        elif optionPelicula == 4:
            deletePelicula()


def goToBoletoSubMenu():
    while True:
        print("Menú Boletos: ")
        print("0 - Regresar a menú principal: ")
        print("1 - Ver reservas (boletos): ")
        print("2 - Crear reserva (boleto): ")
        optionBoleto = int(input("Seleccione una opción: "))

        if optionBoleto == 0:
            print("Regresando a menú principal...")
            break
        elif optionBoleto == 1:
            viewAllBoletos()
        elif optionBoleto == 2:
            addBoleto()


def goToCompraDetalladaSubMenu():
    while True:
        print("Menú Compra Detallada: ")
        print("0 - Regresar a menú principal: ")
        print("1 - Ver todas las compras: ")
        print("2 - Crear compra: ")
        print("3 - Actualizar una compra: ")
        print("4 - Eliminar una compra: ")
        optionCompra = int(input("Seleccione una opción: "))

        if optionCompra == 0:
            print("Regresando a menú principal...")
            break
        elif optionCompra == 1:
            viewAllCompras()
        elif optionCompra == 2:
            addCompra()
        elif optionCompra == 3:
            updateCompra()
        elif optionCompra == 4:
            deleteCompra()
            deleteBoleto()


while True:
    print("Bienvenid@ a la app cine")
    print("Menú: ")
    print("0 - Salir de la app: ")
    print("1 - Usuario: ")
    print("2 - Sucursales: ")
    print("3 - Peliculas: ")
    print("4 - Salas: ")
    print("5 - Asientos: ")
    print("6 - Boletos: ")
    print("7 - Detalle de compra: ")
    option = int(input("Seleccione una opción: "))

    if option == 0:
        print("Saliste de la aplicación")
        break
    elif option == 1:
        pass
    elif option == 2:
        goToSucursalesSubMenu()
    elif option == 3:
        goToPeliculasSubMenu()
    elif option == 4:
        goToSalaSubMenu()
    elif option == 5:
        goToAsientosSubMenu()
    elif option == 6:
        goToBoletoSubMenu()
    elif option == 7:
        goToCompraDetalladaSubMenu()
