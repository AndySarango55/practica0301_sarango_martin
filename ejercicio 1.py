import datetime


def fibonacci(numero):
    if (numero == 0):
        return 0
    elif (numero == 1):
        return 1
    else:
        return (fibonacci(numero-2)+fibonacci(numero-1))
inicio = datetime.datetime.now()
numero = int(input("Introduce el valor del numero:\n "))
print("La secuencia es:")
for numero in range(0, numero):
  print(fibonacci(numero))

fin = datetime.datetime.now()
print("el tiempo de ejecucion es de :", fin - inicio)


def fibonacci_iter(n):
    a = 1
    b = 1
    if n == 1:
        print('0')
    elif n == 2:
        print('0', '1')
    else:
        print('0')
        print(a)
        print(b)
        for i in range(n - 3):
            total = a + b
            b = a
            a = total
            print(total)

inicio2 = datetime.datetime.now()
fibonacci_iter(8)
fin = datetime.datetime.now()
print("el tiempo de ejecucion es de :", fin - inicio)

