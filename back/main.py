from flask import Flask, request
# import psycopg2
import json
import uuid

app = Flask(__name__)

@app.post("/cadastro/researchers")
def add_researchers():
    try:
        if request.method == 'POST':
            researcher = {
                "name": request.form['name'],
                "age": request.form['age'],
                "id": str(uuid.uuid1()),
                "area": request.form['area'],
                "years_experience": request.form['years_experience']
            }

        # Obter uma string formatada em JSON
        return json.dumps(researcher)
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
        return json.dumps(empresa)
    except e:
        return "Error: {e}"

@app.post("/cadastro/problems")
def cadastro_problems():
    try:
        if request.method == 'POST':
            problems = {
                "name": request.form['name'],
                "id": str(uuid.uuid1()),
                "area": request.form['area']
            }

        # Obter uma string formatada em JSON
        return json.dumps(problems)
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
        return json.dumps(vaga)
    except e:
        return "Error: {e}"

@app.post("/login")
def login():
    try:
        if request.method == 'POST':
            login = {
                "name": request.form['name'],
                "password": request.form['password']
            }

            return json.dumps(login)     
    except e:
        return "Error: {e}"
  
if __name__ == "__main__":
    # conn = psycopg2.connect(database="Eureka",
    #                     host="localhost",
    #                     user="root",
    #                     password="1234",
    #                     port="db_port")

    app.run(debug=True)