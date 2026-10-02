numero = int(input("Introduce un número: "))
es_par = (numero % 2 == 0)

print(f"¿El número {numero} es par? -> {es_par}")
print(f"¿El número {numero} es impar? -> {numero % 2 != 0}")