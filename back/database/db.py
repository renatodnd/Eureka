# database/db.py
import psycopg2
from flask import current_app, g # 'g' é para armazenar dados por requisição

def get_db():
    """
    Cria uma nova conexão com o banco de dados se ainda não houver uma
    para a requisição atual.
    """
    if 'db_conn' not in g:
        g.db_conn = psycopg2.connect(
            database=current_app.config['POSTGRES_DB'],
            user=current_app.config['POSTGRES_USER'],
            password=current_app.config['POSTGRES_PASSWORD'],
            host=current_app.config['POSTGRES_HOST'],
            port=current_app.config['POSTGRES_PORT']
        )
    return g.db_conn

def close_db(e=None):
    """Fecha a conexão com o banco de dados ao final da requisição."""
    db_conn = g.pop('db_conn', None)

    if db_conn is not None:
        db_conn.close()

def init_app(app):
    """Registra as funções de fechamento de conexão no Flask."""
    app.teardown_appcontext(close_db)
    # Você também pode adicionar aqui a função para criar tabelas:
    # app.cli.add_command(init_db_command)