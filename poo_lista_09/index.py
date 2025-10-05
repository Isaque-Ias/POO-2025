from templates.manterclienteUI import ManterClienteUI
from templates.manterservicoUI import ManterServicoUI
from templates.manterhorarioUI import ManterHorarioUI
from templates.
from templates.abrircontaUI import AbrirContaUI
from templates.loginUI import LoginUI
from templates.perfilclienteUI import PerfilClienteUI
import streamlit as st
from views import View

class IndexUI:
    def menu_admin():
        op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes", "Cadastro de Serviços", "Cadastro de Horários"])
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Serviços": ManterServicoUI.main()
        if op == "Cadastro de Horários": ManterHorarioUI.main()
        
    def sidebar():
        IndexUI.menu_admin()

    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
        if op == "Entrar no Sistema": LoginUI.main()
        if op == "Abrir Conta": AbrirContaUI.main()

    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ["Meus Dados"])
        if op == "Meus Dados": PerfilClienteUI.main()

    def menu_admin():
        op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes", "Cadastro de Serviços", "Cadastro de Horários", "Cadastro de Profissionais"])
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Serviços": ManterServicoUI.main()
        if op == "Cadastro de Horários": ManterHorarioUI.main()
        if op == "Cadastro de Profissionais": ManterProfissionalUI.main()

    def main():
        View.cliente_criar_admin()
        IndexUI.sidebar()


IndexUI.main()