import streamlit as st
from datetime import datetime, timedelta
from views import View
import time

class AbrirAgendaUI:
    def main():
        data = st.text_input("Informe a data no formato dd/mm/aaaa", datetime.now().strftime("%d/%m/%Y"))
        hora_inicio = st.text_input("Informe o horário inicial no formato HH:MM", datetime.now().strftime("%H:%M"))
        hora_final = st.text_input("Informe o horário final no formato HH:MM", datetime.now().strftime("%H:%M"))
        intervalo = st.text_input("Informe o intervalo entre horários (min)", 30)

        if st.button("Abrir Agenda"):
            try:
                i = 0
                while True:
                    i += 1

                    hora_livre = datetime.strptime(data + " " + hora_inicio, "%d/%m/%Y %H:%M")
                    hora_livre = hora_livre + timedelta(minutes=int(intervalo)) * i
                    
                    if hora_livre > datetime.strptime(data + " " + hora_final, "%d/%m/%Y %H:%M"):
                        break
                    View.horario_inserir(hora_livre, False, None, None, st.session_state["usuario_id"])

                st.success("Horários inseridos com sucesso")
            except ValueError as erro:
                st.error(erro)
                
            time.sleep(2)
            st.rerun()