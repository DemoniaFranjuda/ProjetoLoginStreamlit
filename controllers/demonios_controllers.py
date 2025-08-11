import json
import os

demonios = "data/demonios.json"

def load_demonios():
    if os.path.exists(demonios):
        with open(demonios, "r", encoding="utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return []
    
def select_todos_demonios():
    demonios = load_demonios()

    for demonio in demonios:
        return demonio
    
def select_demonio_por_email(email):
    demonios = load_demonios()

    for demonio in demonios:
       if demonio["email_demonio"] == email:
        return True
    else:
        return False
    
def select_demonio_por_cpf(cpf):
    demonios = load_demonios()

    for demonio in demonios:
       if demonio["cpf_demonio"] == cpf:
        return True
    else:
        return False


