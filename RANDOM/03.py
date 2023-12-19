# precios del coto 18/12/2023
# aclaraciones:
# el papel higiencio es *4 y el precio por metro es de $90
# , el dulce de leche es por 5 kilos
# 
precios = {
    'atun':1043,
    'harina':800,
    'leche':600,
    'dulce de leche':3100,
    'carne picada':1500,
    'pollo': 5000,
    'suprema':3800,
    'pechuga':2900,
    'papas noisette':3100,
    'papel higienico':1200,
    'detergente': 1300,
    'shampoo':5000,
    'jabon':300,
    'té': 700,
    'pure de tomate': 600,
    'fideos':995,
}
# detergente, papel higienico ¿comprar en mayorista de esos productos?
print('Hola Yas, esta es la lista de precios de coto:\nfecha: 18/12')
for i in precios.items():
    print(i)
# Inicializar el diccionario para almacenar la cantidad de cada producto
cantidades = {}
# Solicitar al usuario la cantidad de cada producto
for producto in precios:
    print('-'*50)
    if producto == 'pollo':
        print('poner cantidad de pollos')
    elif producto ==  'suprema':
        print('poner kilos, es sin piel ni hueso')
    elif producto == 'pechuga':
        print('poner kilos, es medio pollo')  
    elif producto == 'dulce de leche':
        print('el tarrito de 5 kilos')
    elif producto == 'shampoo':
        print('puse uno de $5000.-')
    elif producto == 'papel higienico':
        print('es el rollo de 4, campanita')              
    cantidad = int(input(f'¿Cuántos {producto} quieres comprar? '))
    cantidades[producto] = cantidad
# Calcular el total
total = sum(precios[producto] * cantidades[producto] for producto in precios)
# Mostrar el total
print(f'\nTotal a pagar: ${total}')



