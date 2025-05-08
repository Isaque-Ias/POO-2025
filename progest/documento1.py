frase = input("Escreva uma frase: ")

nova_frase = ''.join([frase[i] for i in range(len(frase)) if i % 2 == 0])

print(nova_frase)
