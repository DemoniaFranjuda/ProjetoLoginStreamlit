import streamlit as st
import re
from utils.validar_email import validar_email
from datetime import date
from controllers.demonios_controllers import select_demonio_por_cpf, select_demonio_por_email

@st.dialog("Formulário de Cadastro de Demonios", width=True)
def cadastrar_demonio():
  data_minima = date(1900, 1, 1)
  data_maxima = date.today()

  with st.form("Formulário de Cadastro"):
    nome_demonio = st.text_input("Nome do demonio", placeholder="Nome do demonio")
    email_demonio = st.text_input("Email do demonio", placeholder="Email do demonio")
    cpf_demonio = st.text_input(
      "CPF do demonio",
      placeholder="CPF do demonio",
      max_chars=11
    )
    dataNasc_demonio = st.date_input(
      "Data de Nascimento do demonio",
      value=data_maxima,
      min_value=data_minima,
      max_value=data_maxima
    )
    telefone_demonio = st.text_input(
      "Telefone do demonio",
      placeholder="Telefone do demonio",
      max_chars=11
    )

    cpf_demonio_numeros = re.sub(r"\D", "", cpf_demonio)
    telefone_demonio_numeros = re.sub(r"\D", "", telefone_demonio)
    email_isvalid = validar_email(email_demonio)

    colunas = st.columns(2)

    with colunas[0]:
      btn_cadastrar = st.form_submit_button("Cadastrar", use_container_width=True)

    with colunas[1]:
      btn_cancelar = st.form_submit_button("Cancelar", use_container_width=True)

    if btn_cadastrar:
      if not nome_demonio:
       return st.warning("Campo nome não pode estar vazio, seu capeta!")

      if not email_demonio:
       return st.warning("Campo email não pode estar vazio, demonio!")
      
      if not email_isvalid:
        return st.warning("Email inválido!")
    
      if not cpf_demonio:
        return st.warning("Campo CPF não pode estar vazio, djabo!")

      if len(cpf_demonio_numeros) != 11 or len(cpf_demonio_numeros) < 11:
        return st.warning("CPF inválido, fi do cão.")


      if not telefone_demonio:
        return st.warning("Campo numero não pode estar vazio, djabo!")

      if len(telefone_demonio_numeros) != 11 or len(telefone_demonio_numeros) < 11:
        return st.warning("CPF inválido, fi do cão.")

      

    if btn_cancelar:
      st.rerun()
