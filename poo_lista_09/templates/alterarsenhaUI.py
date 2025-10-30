import streamlit as st
from views import View

class AlterarSenhaUI:
    def main():
        st.header("Alterar Senha")

        op = View.cliente_listar_id(st.session_state["usuario_id"])
        senha = st.text_input("Informe a nova senha", "", type="password")
        senha2 = st.text_input("Repita a senha", "", type="password")

        if st.button("Alterar"):
            if senha == senha2:
                id = op.get_id()
                View.cliente_atualizar(id, op.get_nome(), op.get_email(), op.get_fone(), senha, op.get_idade())
                st.success("Senha alterada com sucesso")
            else:
                st.warning("Senhas diferentes")