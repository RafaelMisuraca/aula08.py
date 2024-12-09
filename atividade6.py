numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = len(list(filter(lambda x: x % 2 == 0, numeros)))

impares = len(list(filter(lambda x: x % 2 != 0, numeros)))

print(f'Pares: {pares}')
print(f'Ímpares: {impares}')
