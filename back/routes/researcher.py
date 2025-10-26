import uuid
from flask import Blueprint, request, jsonify
from models.researcher import create_researcher # Importa a função do modelo

# Cria um Blueprint (um mini-aplicativo)
bp = Blueprint('researchers', __name__, url_prefix='/cadastro/researchers')

'''
    Endpoint para cadastro de pesquisadores
'''
@bp.route("/", methods=['POST'])
def add_researcher():
    try:
        data = request.get_json()

        # Validação básica de entrada
        if not data or not data.get('name'):
            return jsonify({
                "status": "error",
                "message": "Dados incompletos"
            }), 400

        # Chama a função do modelo que interage com o BD
        researcher = create_researcher(data)

        return jsonify({
            "status": "sucess",
            "researcher": data}), 201
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Erro interno: {str(e)}"
        }), 500