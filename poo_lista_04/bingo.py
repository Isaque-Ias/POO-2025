from random import randint

class Bingo:
    def __init__(self, n_bolas):
        self.__n_bolas = n_bolas
        self.__bolas = [valor + 1 for valor in range(self.__n_bolas)]
        self.__bolas_sorteadas = []
    
    def sortear(self):
        if len(self.__bolas) == 0:
            return -1
        numero = randint(0, len(self.__bolas) - 1)
        bola = self.__bolas[numero]
        self.__bolas_sorteadas.append(bola)
        self.__bolas.pop(numero)
        return bola

    def sorteados(self):
        return self.__bolas_sorteadas

class BingoUI:
    @staticmethod
    def main():
        while True:
            interacao = BingoUI.menu()

            if interacao == 4:
                break

    def menu():
        print("1 - Iniciar novo jogo\n2 - Sortear um número\n3 - Verificar números sorteados\n4 - Sair")
        interacao = int(input())

        if interacao == 1:
            BingoUI.iniciar_jogo()
        elif interacao == 2:
            BingoUI.sortear(BingoUI.jogo)
        elif interacao == 3:
            BingoUI.sorteados(BingoUI.jogo)
        
        return interacao

    @staticmethod
    def iniciar_jogo():
        BingoUI.jogo = Bingo(10)
        print("Jogo iniciado.")

    @staticmethod
    def sortear(bingo):
        print("Número sorteado: ", bingo.sortear())

    @staticmethod
    def sorteados(bingo):
        print("Números sorteados: ", *bingo.sorteados())

BingoUI.main()