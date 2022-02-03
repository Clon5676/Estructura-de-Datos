import cProfile

debit = []
credit = []

def operaciones():
    totDeb=0
    for i in range(len(debit)):
        totDeb += debit[i]
    print ("\nCompras Totales: ",totDeb)    
    totCre=0
    for i in range(len(credit)):
        totCre += credit[i]
    print ("Pagos Totales: ",totCre)   
    resultat = saldo(totCre,totDeb)
    print("El saldo es de :", resultat)
    prom = promedio(totDeb, len(debit))
    print("El promedio de precios de items es de: ", prom)
    print("El producto mas caro es: ", max(debit))
    conteo()
    print("Los creditos son: ",credit)
    print("Los debitos son: ",debit)

def Question():
    respuesta = str(input("Cual es su respuesta? Si/No "))
    return respuesta.upper()

def quitar(n):
    print("---------------------\nNumero ", credit[n-1] ," Quitado\n---------------------")
    credit.pop(n-1)
    
def creditos():
    respuesta =Question()
    if respuesta.upper() == "SI":
        sigCre = int(input("Ingrese valor de nuevo pago: "))
        credit.append(sigCre)
    elif respuesta.upper()== "NO":
        return 0
    else:
        print("\n\nPorfavor ponga una respuesta valida\n\n")

def debitos():
    respuesta = Question()
    if respuesta == "SI":
        sigDeb = int(input("Ingrese valor de nuevo item: "))
        debit.append(sigDeb)
    elif respuesta== "NO":
        return 0
    else:
        print("\n\nPorfavor ponga una respuesta valida\n\n")

def saldo(cred,  deb):
    return cred-deb

def promedio (debitos, tam):
    return debitos/tam

def conteo():
    numDeb =len(debit)
    numCre = len(credit)
    print("Hay", numDeb,"Debitos")
    print("Hay", numCre,"Creditos")

def programa():
    debit = []
    credit = []
    siguiente = True
    fin= False
    prochain = 0
    elimNum = 2
    ingrDeb = int(input("Ingrese el precio del primer item de compra: "))
    debit.append(ingrDeb)
    while not fin:
        if prochain == 0:
            while siguiente :
                print("Desea poner otro item?")
                resul = debitos()
                if resul == 0:
                    siguiente = False
            siguiente = True
            ingrCre = int(input("\nIngrese el primer pago: "))
            credit.append(ingrCre)
            while siguiente :
                print("Desea poner otro pago?")
                resul = creditos()
                if resul == 0:
                    siguiente = False
        operaciones()
        while elimNum < 4:
            quitar(elimNum)
            elimNum += 1
            prochain += 1
            break
        if elimNum >=4:
            fin = True
            operaciones()
programa()
cProfile.run("programa")