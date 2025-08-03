from model.models import Contato, ContatoDAO
import json
from datetime import datetime
import os

current_folder = os.path.dirname(os.path.abspath(__file__))

class View:
    classmethod
    def inserir(cls, nome, email, fone, ano, mes, dia):
        contato = Contato(0, nome, email, fone, datetime(ano, mes, dia))
        
        ContatoDAO.inserir(contato)

    @classmethod
    def listar(cls):
        return ContatoDAO.listar()

    @classmethod
    def listar_id(cls, id):
        return ContatoDAO.listar_id(id)

    @classmethod
    def excluir(cls, id):
        ContatoDAO.excluir_id(id)

    @classmethod
    def atualizar(cls):
        cls.excluir()
        cls.inserir()

    @classmethod
    def pesquisar(cls, iniciais):
        for contato in ContatoDAO.listar().items():
            nome = contato.nome
            iniciais_sep = list(map(lambda x: x[0], nome.split(" ")))

            texto = ""
            for inicial in iniciais_sep:
                texto = texto + inicial + ". "
            texto = texto[:-1]
            
            if texto == iniciais:
                return contato

    @classmethod
    def aniversariantes(cls, mes):
        contatos = []
        for contato in ContatoDAO.listar().items():
            if contato.get_nascimento().month == mes:
                contatos.append(contato[1])
        return contatos

    @classmethod
    def salvar(cls):
        json_dict = {}
        for contato in ContatoDAO.listar().items():
            json_dict[contato[0]] = contato[1].__dict__
            json_dict[contato[0]]["nascimento"] = [contato[1].nascimento.year, contato[1].nascimento.month, contato[1].nascimento.day]
            
        with open(current_folder + "\\contato.json", "w") as file:
            json.dump(json_dict, file)