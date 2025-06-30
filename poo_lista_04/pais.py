class Pais:
    def __init__(self, id, nome, populacao, area):
        self.__id = id
        self.nome = nome
        self.populacao = populacao
        self.area = area

    def get_id(self):
        return self.__id

    def densidade(self):
        return self.populacao / self.area

    def __str__(self):
        return f"ID: {self.__id}\nnome: {self.nome}\npopulação: {self.populacao}\nárea: {self.area}"

class PaisUI:
    paises = []

    @staticmethod
    def main():
        while True:
            interacao = PaisUI.menu()

            if interacao == 7:
                break

    def menu():
        print("1 - Inserir Pais\n2 - Listar Paises\n3 - Excluir Paises\n4 - Atualizar Paises\n5 - Pais mais populoso\n6 - Pais mais povoado\n7 - Sair")
        interacao = int(input())

        if interacao == 1:
            PaisUI.inserir()
        elif interacao == 2:
            PaisUI.listar()
        elif interacao == 3:
            PaisUI.excluir()
        elif interacao == 4:
            PaisUI.atualizar()
        elif interacao == 5:
            PaisUI.populoso()
        elif interacao == 6:
            PaisUI.povoado()
        
        return interacao

    @staticmethod
    def inserir():
        id = input("informe o ID: ")
        nome = input("informe o nome: ")
        populacao = int(input("informe a população: "))
        area = int(input("informe a área: "))
        
        pais = Pais(id, nome, populacao, area)

        PaisUI.paises.append(pais)

    @staticmethod
    def listar():
        print("Paises: ")
        for pais in PaisUI.paises:
            print(pais)

    @staticmethod
    def excluir():
        valor_id = input("Informe o ID do Pais: ")
        for pais in PaisUI.paises:
            if pais.get_id() == valor_id:
                PaisUI.paises.remove(pais)

    @staticmethod
    def atualizar():
        PaisUI.excluir()
        PaisUI.inserir()

    @staticmethod
    def populoso():
        populoso = 0
        for pais in PaisUI.paises:
            if populoso == 0:
                populoso = pais
            if pais.populacao > populoso.populacao:
                populoso = pais
        print(populoso)
        
    @staticmethod
    def povoado():
        povoado = 0
        for pais in PaisUI.paises:
            if povoado == 0:
                povoado = pais
            if pais.densidade() > povoado.densidade():
                povoado = pais
        print(povoado)

PaisUI.main()