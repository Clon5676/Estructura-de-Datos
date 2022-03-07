from main import *
# # # languages = [{'name' : 'JavaScript'}, {'name' : 'Python'}, {'name' : 'Ruby'}]
# # # print(ordenes)
# # for r in ordenes:
# #     print( ' Orden: '.join([str(x) for x in r] ) ) 

import csv, json

# nodo = inventario.headval
# while nodo is not None:
#     print (len(nodo.dataval))
#     nodo = nodo.nextval
invDict = {"PRODUCTO":[],"PRECIO":[],"INVENTARIO":[]};
nodo = inventario.headval.nextval
while nodo is not None:
    # print(len(nodo.dataval))
    for i in range(0, len(nodo.dataval)):
        # invDict[list(nodo)[i]]
    # print (nodo.dataval)
        invDict[list(invDict)[i]].append(nodo.dataval[i])
        # print(list(nodo.dataval)[i])
    nodo = nodo.nextval

print(invDict)
# def inventarioJson():
# invDict = {"PRODUCTO":[],"PRECIO":[],"INVENTARIO":[]};
# for j in range(1, inventario.rows()):
#     for i in range(0,4):
        #print(ordenes[j][i])
        # ordenesDict[list(ordenesDict)[i]].append(ordenes[j][i])
# return(ordenesDict)