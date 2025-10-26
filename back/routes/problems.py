import uuid
from flask import Blueprint, request, jsonify
#from models.researcher import create_researcher # Importa a função do modelo

# Cria um Blueprint (um mini-aplicativo)
bp = Blueprint('problemns', __name__, url_prefix='/cadastro/problemns')

# '''
#     Endpoint para cadastro de vagas
# '''
# @bp.route("/cadastro/vagas", methods=['POST'])
# def cadastro_vagas():
#     try:
#         data = request.get_json()

#         vaga = {
#             "id": str(uuid.uuid1()),
#             "name": data.get('name'),
#             "area": data.get('area')
#         }

#         return jsonify({
#             "status": "sucess",
#             "vaga": vaga}), 201
#     except Exception as e:
#         return jsonify({
#             "status": "error",
#             "message": f"Erro interno: {str(e)}"
#         }), 500
    

'''
    Endpoint para cadastro de um problema
'''
@bp.route("/", methods=['POST'])
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
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Erro interno: {str(e)}"
        }), 500