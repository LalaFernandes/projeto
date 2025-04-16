# numero = input("Insira os números separados por espaços: ")
# listaNumeros = numero.split()
# print(listaNumeros)
# print(listaNumeros[0])


matriz = [[0, 1, 2], [3, 4, 5], [6, 7 ,8]]
print(matriz[0][2])
print('0 1 2')
print('3 4 5')
print('6 7 8')

print(matriz)

for linha in matriz:
    for valor_coluna in linha:
        if (linha - valor_coluna == 0):
            print("diagona principal")
        print("linha", linha, "coluna", valor_coluna)
        
