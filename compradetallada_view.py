from compradetallada_logic import CompraDetLogic
from prettytable import PrettyTable

logic = CompraDetLogic()


def viewAllCompras():
    comprasObjList = logic.getAllCompras()
    table = PrettyTable()
    table.field_names = [
        "Id",
        "Tipo",
        "Precios unitarios",
        "Cantidad",
        "Monto total",
        "Estado",
    ]

    for compras in comprasObjList:
        table.add_row(
            [
                compras["idcompra"],
                compras["tipo"],
                compras["precios_unitarios"],
                compras["cantidad"],
                compras["monto_total"],
                compras["estado"],
            ]
        )
    print(table)


def addCompra():
    print("Agregue una nueva compra")
    tipo = input("Tipo:")
    precios_unitarios = input("Precios unitarios:")
    cantidad = input("Cantidad:")
    monto_total = input("Monto total: ")
    estado = input("Estado de compra: ")

    logic.createCompraObj(tipo, precios_unitarios, cantidad, monto_total, estado)
    logic.insertCompra(tipo, precios_unitarios, cantidad, monto_total, estado)
    print("Compra registrada con éxito")


# def viewComprasById():
#     comprasObjList = logic.getCompraById()
#     table = PrettyTable()
#     table.field_names = [
#         "idcompra",
#         "tipo",
#         "precios_unitarios",
#         "cantidad",
#         "monto_total",
#         "estado",
#     ]

#     for compras in comprasObjList:
#         table.add_row(
#             [
#                 compras.idcompra,
#                 compras.tipo,
#                 compras.precios_unitarios,
#                 compras.cantidad,
#                 compras.monto_total,
#                 compras.estado,
#             ]
#         )
#     print(table)


def updateCompra():
    print("Actualice la compra")
    idcompra = int(input("Id de compra a actualizar: "))
    oldCompra = logic.getCompraById(idcompra)

    update = int(input("¿Actualizar estado? Si - 1  No - 0 "))
    if update == 1:
        print(f"Estado anterior: {oldCompra['estado']}")
        estado = input("Ingrese el nuevo estado: ")
    else:
        estado = oldCompra["estado"]

    compra = logic.updateCompraById(idcompra, estado)
    print("El estado de la compra ha sido actualizado")


def deleteCompra():
    print("Eliminar compra")
    idcompra = int(input("Id de la pelicula a eliminar: "))
    logic.deleteCompraById(idcompra)
    print("Compra eliminada con éxito")