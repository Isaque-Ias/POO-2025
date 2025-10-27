import streamlit as st
from views import View
import pandas as pd

class PerfilClienteUI:
    def main():
        st.header("Meu Perfil")

        tab1, tab2 = st.tabs(["Meus Dados", "Serviços"])
        with tab1: PerfilClienteUI.dados()
        with tab2: PerfilClienteUI.servicos()

    def dados():
        op = View.cliente_listar_id(st.session_state["usuario_id"])
        nome = st.text_input("Informe o novo nome", op.get_nome())
        email = st.text_input("Informe o novo e-mail", op.get_email())
        fone = st.text_input("Informe o novo fone", op.get_fone())
        senha = st.text_input("Informe a nova senha", op.get_senha(),
        type="password")

        if st.button("Atualizar"):
            try:
                id = op.get_id()
                View.cliente_atualizar(id, nome, email, fone, senha)
                st.success("Cliente atualizado com sucesso")
            except ValueError as erro:
                st.error(erro)

    def servicos():
        horarios = View.horario_servicos_agendados(st.session_state["usuario_id"])

        if len (horarios) == 0: st.write("Nenhum horário cadastrado")
        else:
            dic = []
            for obj in horarios:
                servico = View.servico_listar_id(obj.get_id_servico())
                profissional = View.profissional_listar_id(obj.get_id_profissional())
                if servico != None: servico = servico.get_descricao()
                if profissional != None: profissional = profissional.get_nome()
                dic.append({"id" : obj.get_id(),
                            "data" : obj.get_data(),
                            "confirmado" : obj.get_confirmado(),
                            "serviço" : servico,
                            "profissional" : profissional})

            df = pd.DataFrame(dic)
            st.dataframe(df)