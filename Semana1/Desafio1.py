#Trabajas en una empresa X donde sus vendedores cobran comisiones del 6% de
#sus ventas totales y el departamento comercial te solicita que ayudes a los
#vendedores a calcular sus comisiones creando un programa que les pregunte su
#nombre y cuánto han vendido en éste mes.
#Tu programa le va a responder con una frase que incluya su nombre y el monto
#que le corresponde por las comisiones

vendedor = input('Cual es tu nombre? ')
monto = float(input('Ingresa el monto de ventas realizadas... '))
comision = (monto * 0.06)
print('Al señor/a ', vendedor, ' le corresponden un total de $', comision, ' de comisiones.')
