import streamlit as st
import time
from controllers.load_usurarios import load_usuarios

dados = []


st.title("Demonios à venda")

if "email" not in st.session_state:
   st.session_state.email = None

if "nome" not in st.session_state:
   st.session_state.nome = None

def login():
   usuarios = load_usuarios()

   email = st.text_input("Email", placeholder="email")
   senha = st.text_input("Senha", placeholder="Senha", type="password")
   login = st.button("Login")

   if login:
      for user in usuarios:
        if user["email"] == email and user ["senha"] == senha:
            st.session_state.email = user["email"]
            st.session_state.nome = user["nome"]
            st.success("Login efetuado com sucesso!")
            time.sleep(3)
            st.rerun()
        else:
         st.error("Email e Senha inválidos.")

def logout():
   if st.button("Terminei o Ritual"):
      st.session_state.clear()
      st.success("Finalizando o ritual")
      time.sleep(3)

@st.dialog("Formulário de Cadastro do Demonio")

def cadastrar_demonio():
   nome_demonio = st.text_input("Nome do Demonio", placeholder= "Nome do Demonio")
   email_demonio = st.text_input("Email do Demonio", placeholder= "Email do Demonio")
   cpf_demonio = st.text_input("CPF do Demonio", placeholder= "CPF do Demonio")
   dataNasc_demonio = st.date_input("Data de Nascimento do Demonio")
   telefone_demonio = st.text_input("Numero do Demonho", placeholder= "Numero do Demonho")

btn_cadastrar = st.button("Cadastrar")


def main_page():
   tabs = st.tabs(["Dashboard", "Cadastro", "Logout"])
   nome = st.session_state.nome

   with tabs[0]:
     st.subheader("Dashboard")
     st.write(f"**Usuário logado:** {nome}")

   with tabs[1]:
     st.subheader("Cadastro")
     if st.button("Abrir formulário de cadastro"):
        cadastrar_demonio()

   with tabs[2]:
     st.subheader("Logout")
     logout()
      
if st.session_state.email:
   main_page()
    
else:
   login()


# if "contador" not in st.session_state:
#     st.session_state.contador = 0

# if st.button("Adicionar"):
#     st.session_state.contador += 1 

# if st.button("Diminuir"):
#     if st.session_state.contador > 0:
#      st.session_state.contador -= 1 

# st.write(st.session_state)