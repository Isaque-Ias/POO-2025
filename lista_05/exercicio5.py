def formatar_nome(nome):
    nome = nome.split(" ")
    nome_formatado = ""
    for nome_parte in nome:
        nome_formatado += nome_parte.capitalize() + " "
    return nome_formatado[:-1]