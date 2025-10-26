import uuid
from flask import Blueprint, request, jsonify
from models.problems import create_problem # Importa a função do modelo

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

        if not data or not data.get('title'):
            return jsonify({
                "status": "error",
                "message": "Dados incompletos"
            }), 400
        
        problem = create_problem(data)
        # problems = {
        #     "id": str(uuid.uuid1()),
        #     "name": data.get('name'),
        #     "area": data.get('area')
        # }

        return jsonify({
            "status": "sucess",
            "problems": data}), 201
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Erro interno: {str(e)}"
        }), 500