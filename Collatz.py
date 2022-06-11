rojo = '\033[0;31m'
blanco = '\033[0;m'
print(rojo, '*' * 80, blanco)
print(' Conjetura de Collatz')
print(rojo, '*' * 80, blanco)


def numero_par(numero):
    resultado = numero // 2

    return resultado


def numero_impar(n):
    resultado = 3 * n + 1
    return resultado


def promedio(total, cantidad):
    resultado = total / cantidad

    return resultado


def funcion_principal():
    may = 0
    contador = 0
    acumulador = 0
    n = int(input(' Ingrese numero:'))
    print(' Orbita n =', n)
    print(' valores calculados incluyendo al', n, 'y al 1 son:')

    while n != 0:
        print(rojo, '|', blanco, n, end=' ')
        acumulador += n
        contador += 1
        if n == 1:
            break
        if n % 2 == 0:
            n = numero_par(n)

        else:
            n = numero_impar(n)

        if n > may:
            may = n

    final = promedio(acumulador, contador)
    print()
    print(' La longitud de la orbita es:', contador)
    print(' El promedio total de num es:', round(final, 1))
    print(' Mayor de los números en esa órbita:', may)
    print(rojo, '*' * 80, blanco)


funcion_principal()
