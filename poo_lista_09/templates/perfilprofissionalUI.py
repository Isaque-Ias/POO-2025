import streamlit as st
from views import View
import time
import pandas as pd

class PerfilProfissionalUI:
    def main():
        st.header("Meu Perfil")

        tab1, tab2, tab3 = st.tabs(["Meus Dados", "Minha Agenda", "Confirmar Serviço"])
        with tab1: PerfilProfissionalUI.dados()
        with tab2: PerfilProfissionalUI.agenda()
        with tab3: PerfilProfissionalUI.servicos()

    def dados():
        op = View.profissional_listar_id(st.session_state["usuario_id"])
        nome = st.text_input("Informe o novo nome", op.get_nome())
        especialidade = st.text_input("Informe a nova especialidade", op.get_especialidade())
        conselho = st.text_input("Informe o novo conselho", op.get_conselho())
        email = st.text_input("Informe o novo e-mail", op.get_email())
        senha = st.text_input("Informe a nova senha", op.get_senha(),
        type="password")

        if st.button("Atualizar"):
            try:
                id = op.get_id()
                View.profissional_atualizar(id, nome, especialidade, conselho, email, senha)
                st.success("Profissional atualizado com sucesso")
            except ValueError as erro:
                st.error(erro)

    def agenda():
        horarios = View.profissional_listar_agenda(st.session_state["usuario_id"])

        if len (horarios) == 0: st.write("Nenhum horário cadastrado")
        else:
            dic = []
            for obj in horarios:
                cliente = View.cliente_listar_id(obj.get_id_cliente())
                servico = View.servico_listar_id(obj.get_id_servico())
                if cliente != None: cliente = cliente.get_nome()
                if servico != None: servico = servico.get_descricao()
                dic.append({"id" : obj.get_id(),
                            "data" : obj.get_data(),
                            "confirmado" : obj.get_confirmado(),
                            "cliente" : cliente,
                            "serviço" : servico,
                            "de_menor" : cliente.get_idade() < 18})

            df = pd.DataFrame(dic)
            st.dataframe(df)

    def servicos():
        horarios = View.horario_servicos_confirmar(st.session_state["usuario_id"])

        horario = st.selectbox("Informe o horário", horarios, index = None)

        if not horario == None:
            cliente = st.selectbox("Cliente", View.cliente_listar_id(horario.get_id_cliente()), disabled=True)

        if st.button("Confirmar"):
            id_horario = None

            if horario != None: id_horario = horario.get_id()
            
            View.horario_atualizar(id_horario, horario.get_data(), True, horario.get_id_cliente(), horario.get_id_servico(), horario.get_id_profissional())

            st.success("Serviço inserido com sucesso")
            time.sleep(2)
            st.rerun()