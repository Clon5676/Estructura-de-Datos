
def abv75 ():
    print("Su Resultado es: O")
def gradeA ():
    print("Su Resultado es: A")
def gradeB ():
    print("Su Resultado es: B")
def gradeC ():
    print("Su Resultado es: C")
def blw40 ():
    print("Su Resultado es: D")

def determineGrade(nota):
    if 75 <= nota <= 100:
        salir =True
        abv75()
        return salir
    elif 60 <= nota <= 75:
        salir =True
        gradeA()
        return salir 
    elif 50 <= nota <= 59:
        salir =True
        gradeB()
        return salir
    elif 40 <= nota <= 49:
        salir =True
        gradeC()
        return salir 
    elif 0 <= nota <= 40:
        salir =True
        blw40()
        return salir
    else:
        print("Introduzca un numero valido")
        
        
salir =False

while (not salir):
    note= int(input("Qual es su nota? "))
    salir = determineGrade(note)