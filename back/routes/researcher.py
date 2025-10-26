import uuid
from flask import Blueprint, request, jsonify
#from models.researcher import create_researcher # Importa a função do modelo

# Cria um Blueprint (um mini-aplicativo)
bp = Blueprint('researchers', __name__, url_prefix='/cadastro/researchers')

'''
    Endpoint para cadastro de pesquisadores
'''
@bp.route("/", methods=['POST'])
def add_researcher():
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