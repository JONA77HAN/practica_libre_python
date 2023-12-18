# loteria
numeros_ganadores = []
numero = ''

while numero != 00:
    numero = int(input('ingrese el numero ganador q sigue: '))
    numeros_ganadores.append(numero)

    #debe ser de otra forma usado el sort
    
    acomodados = numeros_ganadores.sort()
    print(acomodados)