import uuid
from flask import Blueprint, request, jsonify
from models.empresas import create_empresas # Importa a função do modelo

# Cria um Blueprint (um mini-aplicativo)
bp = Blueprint('empresas', __name__, url_prefix='/cadastro/empresas')

'''
    Endpoint para cadastro de empresas
'''
@bp.route("/", methods=['POST'])
def cadastro_empresas():
    try:
        data = request.get_json()

        # empresa = {
        #     "id": str(uuid.uuid1()),
        #     "name": data.get('name'),
        #     "area": data.get('area')
        # }

        problem = create_empresas(data)
        
        return jsonify({
            "status": "sucess",
            "empresa": data}), 201
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Erro interno: {str(e)}"
        }), 500