
def fibonacci(numero):
    if (numero == 0):
        return 0
    elif (numero == 1):
        return 1
    else:
        return (fibonacci(numero-2)+fibonacci(numero-1))
numero = int(input("Introduce el valor del numero:\n "))
print("La secuencia es:")
for numero in range(0, numero):
  print(fibonacci(numero))
