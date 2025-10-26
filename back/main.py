from flask import Flask
from routes.empresas import bp as empresa_bp
from routes.login import bp as login_bp
from routes.problems import bp as problemns_bp
from routes.researcher import bp as researcher_bp
from config import Config
from database import db
   
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Inicializa o módulo de conexão com o banco de dados
    db.init_app(app)

    # Registro das Blueprints (Rotas)
    app.register_blueprint(researcher_bp)
    app.register_blueprint(empresa_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(problemns_bp)
    
    # ... adicione outras rotas aqui
    
    return app
  
if __name__ == "__main__":
    # conn = psycopg2.connect(database="Eureka",
    #                     host="localhost",
    #                     user="root",
    #                     password="1234",
    #                     port="db_port")

    app = create_app()
    app.run(debug=True)