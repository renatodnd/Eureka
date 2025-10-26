import uuid
from flask import Blueprint, request, jsonify
#from models.researcher import create_researcher # Importa a função do modelo

# Cria um Blueprint (um mini-aplicativo)
bp = Blueprint('login', __name__, url_prefix='/login')

'''
    Endpoint para realização do login
'''
@bp.route("/", methods=['POST'])
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
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Erro interno: {str(e)}"
        }), 500