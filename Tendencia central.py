#Diana Laura Jimenez Caro
import statistics
from statistics import mean
from statistics import mode, multimode
   
datos=[]
valores= int (input("¿Cuantos valores desea ingresar?: "))
for i in range(valores):
    valor= float(input("Ingresa valor: "))
    datos.append(valor)

print(datos)
datos.sort()

print("La mediana es: ")
print(statistics.median(datos))

print("La media o promedio es:")
print(mean(datos))

print("La moda es: ")
print(statistics.multimode(datos))