# models/empresas.py
import uuid
import psycopg2
from database.db import get_db


def create_empresas(data):
    """
    Insere uma nova empresa no banco de dados com base na estrutura da tabela empresa.
    
    Args:
        data (dict): Dicionário contendo os dados da empresa.
                     Campos obrigatórios: name, location
                     
    Returns:
        dict: O objeto problema recém-criado, incluindo o ID.
        
    Raises:
        Exception: Em caso de falha na inserção no banco de dados.
    """
    conn = get_db()
    cursor = conn.cursor()
    
    # 1. Preparar os dados
    company_id = str(uuid.uuid4())

    # 2. Comando SQL de Inserção
    sql = """
    INSERT INTO company (
        id, name, location
    )
    VALUES (%s, %s, %s)
    RETURNING id, name, location; -- Retorna um subconjunto de dados
    """
    
    try:
        # 3. Execução da Query
        cursor.execute(sql, (
            company_id,
            data['name'],
            data['location']
        ))
        
        # 4. Confirmação e Retorno
        conn.commit()
        
        # O RETURNING retorna os dados inseridos
        inserted_data = cursor.fetchone() 
        
        # Constrói o dicionário de resposta
        company = {
            "id": inserted_data[0],
            "name": inserted_data[1],
            "location": inserted_data[2]
        }
        
        return company
        
    except psycopg2.IntegrityError as e:
        # Lida com erros de violação de constraints (ex: email duplicado, formato inválido)
        conn.rollback()
        # Você pode inspecionar o código de erro do PostgreSQL para dar uma mensagem mais específica
        if 'unique constraint "company_email_key"' in str(e):
             raise Exception("E-mail já cadastrado.")
        
        raise Exception(f"Erro de integridade do BD: {e.diag.message_primary}")
        
    except psycopg2.Error as e:
        # Lida com outros erros de BD
        conn.rollback()
        raise Exception(f"Erro ao inserir pesquisador no BD: {str(e)}")
        
    finally:
        cursor.close()