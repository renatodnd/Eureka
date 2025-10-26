from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from pydantic import BaseModel, Field, ValidationError
# import psycopg2
import os
import json
import uuid

app = Flask(__name__)

# Exemplo de string de conexão PostgreSQL
# FORMATO: postgresql://usuario:senha@host:porta/nome_do_banco
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@localhost:5432/meu_banco"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

'''
    Endpoint para cadastro de pesquisadores
'''
@app.post("/cadastro/researchers")
def add_researchers():
    try:
        data = request.get_json()

        researcher = {
            "id": str(uuid.uuid1()),
            "name": data.get('name'),
            "age": data.get('age'),
            "area": data.get('area'),
            "years_experience": data.get('years_experience')
        }

        return jsonify({
            "status": "sucess",
            "researcher": researcher}), 201
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Erro interno: {str(e)}"
        }), 500


'''
    Endpoint para cadastro de empresas
'''
@app.post("/cadastro/empresas")
def cadastro_empresas():
    try:
        data = request.get_json()

        empresa = {
            "id": str(uuid.uuid1()),
            "name": data.get('name'),
            "area": data.get('area')
        }

        return jsonify({
            "status": "sucess",
            "empresa": empresa}), 201
    except e:
        return jsonify({
            "status": "error",
            "message": f"Erro interno: {str(e)}"
        }), 500


'''
    Endpoint para cadastro de um problema
'''
@app.post("/cadastro/problems")
def cadastro_problems():
    try:
        data = request.get_json()

        problems = {
            "id": str(uuid.uuid1()),
            "name": data.get('name'),
            "area": data.get('area')
        }

        return jsonify({
            "status": "sucess",
            "problems": problems}), 201
    except e:
        return jsonify({
            "status": "error",
            "message": f"Erro interno: {str(e)}"
        }), 500


'''
    Endpoint para cadastro de vagas
'''
@app.post("/cadastro/vagas")
def cadastro_vagas():
    try:
        data = request.get_json()

        vaga = {
            "id": str(uuid.uuid1()),
            "name": data.get('name'),
            "area": data.get('area')
        }

        return jsonify({
            "status": "sucess",
            "vaga": vaga}), 201
    except e:
        return jsonify({
            "status": "error",
            "message": f"Erro interno: {str(e)}"
        }), 500

'''
    Endpoint para realização do login
'''
@app.post("/login")
def login():
    try:
        data = request.get_json()

        login = {
            "name": data.get('name'),
            "password": data.get('password')
        }

        return jsonify({
            "status": "sucess",
            "message": "Login realizado com sucesso"}), 201   
    except e:
        return jsonify({
            "status": "error",
            "message": f"Erro interno: {str(e)}"
        }), 500
  
if __name__ == "__main__":
    # conn = psycopg2.connect(database="Eureka",
    #                     host="localhost",
    #                     user="root",
    #                     password="1234",
    #                     port="db_port")

    app.run(debug=True)