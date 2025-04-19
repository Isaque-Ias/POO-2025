def iniciais(nome):
    nome = nome.split(" ")
    lista_iniciais = list(map(lambda x: x[0], nome))
    iniciais_finais = ""
    for letra in lista_iniciais:
        iniciais_finais += f"{letra.upper()}. "
    return iniciais_finais[:-1]