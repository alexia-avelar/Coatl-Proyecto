from boleto_logic import BoletoLogic
from compradetallada_view import deleteCompra
from prettytable import PrettyTable

logic = BoletoLogic()


def viewAllBoletos():
    boletosObjList = logic.getAllBoletos()
    table = PrettyTable()
    table.field_names = [
        "Id",
        "Tipo",
        "Fecha",
        "Hora",
        "IdCompra",
        "Sala",
        "Película",
    ]

    for boleto in boletosObjList:
        table.add_row(
            [
                boleto["idboleto"],
                boleto["tipo"],
                boleto["fecha"],
                boleto["hora"],
                boleto["compradetallada_idcompra"],
                boleto["sala_idsala"],
                boleto["peliculas_idpeliculas"],
            ]
        )
    print(table)


def addBoleto():
    print("Agregue una nueva reserva (boleto)")
    tipo = input("Tipo: ")
    fecha = input("Fecha: ")
    hora = input("Hora: ")
    compradetallada_idcompra = input("Id de compra ")
    sala_idsala = input("Id de sala ")
    peliculas_idpeliculas = input("Id de pelicula: ")

    logic.createBoletoObj(
        tipo, fecha, hora, compradetallada_idcompra, sala_idsala, peliculas_idpeliculas
    )
    logic.insertBoleto(
        tipo, fecha, hora, compradetallada_idcompra, sala_idsala, peliculas_idpeliculas
    )
    print("Reserva (boleto) realizada exitosamente")


def deleteBoleto():
    logic.deleteBoletoById(id)