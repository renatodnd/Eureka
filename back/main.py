from flask import Flask, request
# import psycopg2
import json
import uuid

app = Flask(__name__)

@app.post("/cadastro/pesquisadores")
def cadastro_pesquisadores():
    try:
        if request.method == 'POST':
            pesquisador = {
                "name": request.form['name'],
                "age": request.form['age'],
                "id": str(uuid.uuid1()),
                "area": request.form['area'],
                "years_experience": request.form['years_experience']
            }

        # Obter uma string formatada em JSON
        pesquisador_JSON = json.dumps(pesquisador)
        return pesquisador_JSON
    except e:
        return "Error: {e}"

@app.post("/cadastro/empresas")
def cadastro_empresas():
    try:
        if request.method == 'POST':
            empresa = {
                "name": request.form['name'],
                "id": str(uuid.uuid1()),
                "area": request.form['area']
            }

        # Obter uma string formatada em JSON
        empresa_JSON = json.dumps(empresa)
        return empresa_JSON
    except e:
        return "Error: {e}"

@app.post("/cadastro/projetos")
def cadastro_projetos():
    try:
        if request.method == 'POST':
            projeto = {
                "name": request.form['name'],
                "id": str(uuid.uuid1()),
                "area": request.form['area']
            }

        # Obter uma string formatada em JSON
        projeto_JSON = json.dumps(projeto)
        return projeto_JSON
    except e:
        return "Error: {e}"

@app.post("/cadastro/vagas")
def cadastro_vagas():
    try:
        if request.method == 'POST':
            vaga = {
                "name": request.form['name'],
                "id": str(uuid.uuid1()),
                "area": request.form['area']
            }

        # Obter uma string formatada em JSON
        vaga_JSON = json.dumps(vaga)
        return vaga_JSON
    except e:
        return "Error: {e}"

@app.route("/")
def home():
    return "Hello, World!"

    
if __name__ == "__main__":
    # conn = psycopg2.connect(database="db_name",
    #                     host="db_host",
    #                     user="db_user",
    #                     password="db_pass",
    #                     port="db_port")

    app.run(debug=True)