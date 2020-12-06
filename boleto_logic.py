from dx_logic import Logic
from boleto_obj import BoletoObj


class BoletoLogic(Logic):
    def __init__(self):
        super().__init__()
        self.tableName = "boleto"

    def getAllBoletos(self):
        boletoList = super().getAllRows(self.tableName)
        boletoObjList = []
        for element in boletoList:
            boletoObjList.append(element)
        return boletoObjList

    def createBoletoObj(
        self,
        tipo,
        fecha,
        hora,
        compradetallada_idcompra,
        sala_idsala,
        peliculas_idpeliculas,
    ):
        boletoDict = dict(
            tipo=tipo,
            fecha=fecha,
            hora=hora,
            compradetallada_idcompra=compradetallada_idcompra,
            sala_idsala=sala_idsala,
            peliculas_idpeliculas=peliculas_idpeliculas,
        )
        return boletoDict

    def insertBoleto(
        self,
        tipo,
        fecha,
        hora,
        compradetallada_idcompra,
        sala_idsala,
        peliculas_idpeliculas,
    ):
        database = self.database
        sql = (
            f"INSERT INTO `dbcine`.`boleto`(`idboleto`,`tipo`,`fecha`,`hora`, `compradetallada_idcompra`, `sala_idsala`, `peliculas_idpeliculas`) "
            + f"VALUES(0,'{tipo}','{fecha}','{hora}',{compradetallada_idcompra},{sala_idsala},{peliculas_idpeliculas});"
        )
        row = database.executeNonQueryRows(sql)
        return row

    def updateBoletoById(
        self,
        idboleto,
        tipo,
        fecha,
        hora,
        compradetallada_idcompra,
        sala_idsala,
        peliculas_idpeliculas,
    ):
        database = self.database
        sql = (
            "UPDATE `dbcine`.`boleto` "
            + f"SET `tipo` = '{tipo}', `fecha` = '{fecha}', `hora` = '{hora}', `compradetallada_idcompra` = {compradetallada_idcompra},`sala_idsala` = {sala_idsala}, `peliculas_idpeliculas` = {peliculas_idpeliculas} "
            + f"WHERE `idboleto` = {idboleto};"
        )
        row = database.executeNonQueryRows(sql)
        return row

    def getBoletoById(self, idboleto):
        database = self.database
        sql = "SELECT * FROM `dbcine`.`boleto` " + f"where idboleto ={idboleto};"
        boletoDict = database.executeQueryOneRow(sql)
        return boletoDict

    def deleteBoletoById(self, idcompra):
        database = self.database
        sql = (
            "DELETE FROM `dbcine`.`boleto` "
            + f"WHERE compradetallada_idcompra = {idcompra};"
        )
        row = database.executeNonQueryRows(sql)
        return row
