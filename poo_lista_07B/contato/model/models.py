import json
from datetime import datetime
import os

current_folder = os.path.dirname(os.path.abspath(__file__))

class Contato:
    def __init__(self, id, nome, email, fone, nascimento):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
        self.set_nascimento(nascimento)

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_fone(self):
        return self.__fone

    def set_fone(self, fone):
        self.__fone = fone

    def get_nascimento(self):
        return self.__nascimento

    def set_nascimento(self, nascimento):
        self.__nascimento = nascimento

    def __str__(self):
        return f"ID: {self.__id}\nnome: {self.__nome}\nemail: {self.__email}\nfone: {self.__fone}\nnascimento: {self.__nascimento}"
    
class ContatoDAO:
    __contatos = {}
    __id_atual = 0

    @classmethod
    def inserir(cls, obj):
        obj.set_id(cls.__id_atual)
        cls.__contatos[cls.__id_atual] = obj
        
        cls.__id_atual += 1

    @classmethod
    def listar(cls):
        return cls.__contatos

    @classmethod
    def listar_id(cls, id):
        return cls.__contatos.get(id)

    @classmethod
    def excluir_id(cls, id):
        if cls.__contatos.get(id):
            cls.__contatos.pop(id)

    @classmethod
    def abrir(cls):
        with open(current_folder + "\\contato.json", "r") as file:
            json_dict = json.load(file)

        cls.__contatos = {}
        for contato in json_dict.items():
            cls.__contatos[contato[0]] = Contato(contato[1]["id"], contato[1]["nome"], contato[1]["email"], contato[1]["fone"], datetime(contato[1]["nascimento"][0], contato[1]["nascimento"][1], contato[1]["nascimento"][2]))