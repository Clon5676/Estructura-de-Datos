from this import d
from flask import Flask, jsonify, request
from main import *
import json
app = Flask(__name__)
import shortuuid
def ordenesJson():
    #printOrdenes()
    ordenesDict = {"ID":[],"NOMBRE":[],"CANTIDAD":[], "ESTADO":[], "TOTAL":[]};
    #print('len(ordenes) ',len(ordenes))
    for j in range(1, len(ordenes)):
        for i in range(0,5):
            #print(ordenes[j][i])
            ordenesDict[list(ordenesDict)[i]].append(ordenes[j][i])
    return(ordenesDict)

def inventarioJson():
    invDict = {"PRODUCTO":[],"PRECIO":[],"INVENTARIO":[]};
    nodo = inventario.headval.nextval
    while nodo is not None:
        for i in range(0, len(nodo.dataval)):
            invDict[list(invDict)[i]].append(nodo.dataval[i])
        nodo = nodo.nextval
    return(invDict)
    
@app.route('/ordenes', methods=['GET'])
def imprimirOrdenes():
	return jsonify(ordenesJson())

# generar orden
@app.route('/ordenes/generar', methods=['PUT'])
def agregarOrden():
    idA = shortuuid.ShortUUID().random(length=10)
    orden = {'NOMBRE' : request.json['nombre'],'CANTIDAD' : request.json['cantidad'],}
    prodA = mayus(str(list(orden.values())[0]))
    totalA = int(list(orden.values())[1])
    productoInventario = inventario.listfind(prodA)
    if(productoInventario is not None):
        if(int(productoInventario[2])>=totalA):
            total = totalA * float(productoInventario[1])
            ordenes.append([j for j in [idA,prodA,totalA,"PENDIENTE",total]])
            # valorPrueba=int(productoInventario[2]) - totalA
            # #print(valorPrueba)
            inventario.listmodify(prodA,(int(productoInventario[2]) - totalA), 'Inventario')
            guardar()
            return jsonify({'message' : "Orden agregada exitosamente"})
        else:
            return jsonify({'message' : "El producto que desea comprar no cuenta con suficiente existencias, lo sentimos."})
    else:
        return jsonify({'message' : "El producto que desea comprar no existe"})
    # ordenes.append([j for j in [orden,"PENDIENTE",0]])
    
# realizar pago
@app.route('/ordenes/pagar', methods=['PUT'])
def pagar():
    orden = {'ID' : request.json['id'],'TARJETA' : request.json['tarjeta'],}
    idR = str(list(orden.values())[0])
    tarjeta = str(list(orden.values())[1])
    if(tarjeta != '1414'):# SIMULACION DE RESPUESTA DE VISANET
        return(jsonify({'message' : "El metodo de pago no ha sido aceptado."}))
    g = 0
    for k in range(0,len(ordenes)):
        if ordenes[k][0]== idR:
            ordenes[k][3]="PAGADA"
            g = 1
            guardar()
            return(jsonify({"message" :"Orden pagada con exito"}))
    if g==0:
        return(jsonify({"message" : "La orden no ha sido encontrada"}))

# anular orden
@app.route('/ordenes/anular', methods=['PUT'])
def anular():
    orden = {'ID' : request.json['id']}
    idR = str(list(orden.values())[0])
    g = 0
    for k in range(0,len(ordenes)):
        if ordenes[k][0]== idR:
            ordenes[k][3]="ANULADA"
            g = 1
            guardar()
            return(jsonify({"message" :"Orden anulada con exito"}))
    if g==0:
        return(jsonify({"message" : "La orden no ha sido encontrada"}))

# # eliminar ordenes, esta no sirve !
# @app.route('/ordenes/eliminar', methods=['PUT'])
# def eliminarAPi():
#     orden = {'ID' : request.json['id']}
#     idR = str(list(orden.values())[0])
#     ordenes = eliminar(idR)
#     # printOrdenes()
#     return(jsonify({"message" :"El producto ha sido eliminado"}))
#     # return(jsonify({"message" :"El producto no fue encontrado"}))  

@app.route('/inventario', methods=['GET'])
def inventarioimprimirAPI():
    return jsonify(inventarioJson())


@app.route('/inventario/agregar', methods=['PUT'])
def inventarioAgregrarAPI():
    orden = {'PRODUCTO' : request.json['producto'],'PRECIO' : request.json['precio'], 'INVENTARIO': request.json['inventario']}
    producto = mayus(str(list(orden.values())[0]))
    precio = float(list(orden.values())[1])
    inv = int(list(orden.values())[2])
    if(inventario.listfind(producto) is not None):
        return(jsonify({"message" : "Este producto ya existe en el inventario, por favor verifique"}))
    else:
        if(inventario.headval.nextval is None):
            inventario.agregar([producto, precio, inv])
        else:
            inventario.agregar([producto, precio, inv])
        return(jsonify({"message" : "Producto agregado con exito al inventario"}))

@app.route('/inventario/modificar', methods=['PUT'])
def inventarioModificar():
    orden = {'PRODUCTO' : request.json['producto'],'INVENTARIO' : request.json['inventario']}
    prodA = mayus(str(list(orden.values())[0]))
    inv = int(list(orden.values())[1])
    if(inv < 0):
        return jsonify({'message' : "No puede haber un inventario negativo"})
    productoInventario = inventario.listfind(prodA)
    if(productoInventario is not None):
        inventario.listmodify(prodA,inv, 'Inventario')
        guardar()
        return jsonify({'message' : "Nuevo inventario modificado exitosamente"})
    else:
        return jsonify({'message' : "El producto que desea modificar no existe"})

@app.route('/inventario/descuento', methods=['PUT'])
def inventarioDescuentos():
    orden = {'PRODUCTO' : request.json['producto'],'DESCUENTO' : request.json['descuento']}
    prodA = mayus(str(list(orden.values())[0]))
    descuento = float(list(orden.values())[1])
    if(descuento > 100):
        return jsonify({'message' : "El descuento debe ser un porcentaje"})
    productoInventario = inventario.listfind(prodA)
    if(productoInventario is not None):
        inventario.listmodify(prodA,float(productoInventario[1]) - (float(productoInventario[1]) * float(descuento)/100), 'Precio')
        guardar()
        return jsonify({'message' : "Descuento aplicado exitosamente"})
    else:
        return jsonify({'message' : "El producto que desea aplicar el descuento no existe"})


if __name__ == '__main__':
	app.run(debug=True)
