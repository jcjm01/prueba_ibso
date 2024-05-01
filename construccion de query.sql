1.	Construcción de query en SQL
Instrucciones: Con el diagrama de base de datos compartido, crea un query para obtener la información de ventas del cliente, incluyendo los siguientes campos: 
	# de ticket
	Fecha
	Monto (DCANT) con y sin IVA
	Vendedor
	Cliente
	Productos comprados (SKU)
	Descripción
	Cantidad (unidades)
	Almacén que vendió
	Precio de lista
	Talla
	Color
	Temporada




SELECT FDOC.DNUM AS ticket,FDOC.DFECHA AS fecha,FDOC.DCANT AS monto_sin_iva,(FDOC.DCANT + FDOC.DIVA) AS monto_con_iva,FDOC.DPAR1 AS vendedor,FCLI.CLINOM AS cliente,FAXINV.ICODE AS producto_SKU,FINV.IDESC AS descripcion_producto,FAXINV.AICANTF AS cantidad_unidades,FAXINV.AIALMACEN AS almacen,FINV.ILISTA3 AS precio_lista,FINV.IFAM3 AS talla,FINV.IFAM4 AS color,FINV.IFAM5 AS temporada
FROM FDOC INNER JOIN FCLI ON FDOC.CLUICOD = FCLI.CLUICOD INNER JOIN FAXINV ON FDOC.DNUM = FAXINV.FMOV INNER JOIN FINV ON FAXINV.ICODE = FINV.ICODE WHERE FDOC.DESFACT = 'Venta' ORDER BY FDOC.DFECHA DESC;
