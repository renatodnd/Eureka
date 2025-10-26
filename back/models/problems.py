# models/problem.py
import uuid
import psycopg2
from database.db import get_db

def create_problem(data):
    """
    Insere um novo problema no banco de dados com base na estrutura da tabela Problems.
    
    Args:
        data (dict): Dicionário contendo os dados do problema.
                     Campos obrigatórios: title, id_company
                     Campos opcionais: company_logo, category, partnership_model, 
                                     budget, deadline, description, status
                     
    Returns:
        dict: O objeto problema recém-criado, incluindo o ID.
        
    Raises:
        Exception: Em caso de falha na inserção no banco de dados.
    """
    conn = get_db()
    cursor = conn.cursor()
    
    # 1. Preparar os dados
    problem_id = str(uuid.uuid4())
    
    # Converter listas para arrays PostgreSQL
    category_list = data.get('category', [])
    partnership_model_list = data.get('partnership_model', [])
    
    # Valores padrão para campos opcionais
    company_logo = data.get('company_logo')
    budget = data.get('budget')
    deadline = data.get('deadline')
    description = data.get('description')
    status = data.get('status', 'Aberto')  # Default para 'Aberto'
    
    # 2. Comando SQL de Inserção
    sql = """
    INSERT INTO Problems (
        id, title, id_company, company_logo, category, partnership_model, 
        budget, deadline, description, status
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    RETURNING id, title, id_company, company_logo, category, partnership_model, 
              budget, deadline, description, status, created_at;
    """
    
    try:
        # 3. Execução da Query
        cursor.execute(sql, (
            problem_id,
            data['title'],
            data['id_company'],
            company_logo,
            category_list,  # Será convertido para TEXT[]
            partnership_model_list,  # Será convertido para TEXT[]
            budget,
            deadline,
            description,
            status,
        ))
        
        # 4. Confirmação e Retorno
        conn.commit()
        
        # O RETURNING retorna os dados inseridos
        inserted_data = cursor.fetchone() 
        
        # Constrói o dicionário de resposta
        problem = {
            "id": inserted_data[0],
            "title": inserted_data[1],
            "id_company": inserted_data[2],
            "company_logo": inserted_data[3],
            "category": inserted_data[4],  # Array convertido para lista Python
            "partnership_model": inserted_data[5],  # Array convertido para lista Python
            "budget": inserted_data[6],
            "deadline": inserted_data[7],
            "description": inserted_data[8],
            "status": inserted_data[9],
            "created_at": inserted_data[10]
        }
        
        return problem
        
    except psycopg2.IntegrityError as e:
        # Lida com erros de violação de constraints (ex: foreign key, check constraint)
        conn.rollback()
        
        # Verifica se é erro de foreign key (company não existe)
        if 'foreign key constraint "fk_id_company"' in str(e):
            raise Exception("Empresa não encontrada.")
        
        # Verifica se é erro de check constraint (status inválido)
        elif 'check constraint' in str(e) and 'status' in str(e):
            raise Exception("Status inválido. Use apenas 'Aberto' ou 'Fechado'.")
        
        raise Exception(f"Erro de integridade do BD: {str(e)}")
        
    except psycopg2.Error as e:
        # Lida com outros erros de BD
        conn.rollback()
        raise Exception(f"Erro ao inserir problema no BD: {str(e)}")
        
    finally:
        cursor.close()


def get_problem_by_id(problem_id):
    """
    Busca um problema pelo ID.
    
    Args:
        problem_id (str): UUID do problema
        
    Returns:
        dict: Dados do problema ou None se não encontrado
    """
    conn = get_db()
    cursor = conn.cursor()
    
    sql = """
    SELECT id, title, id_company, company_logo, category, partnership_model,
           budget, deadline, description, status, created_at
    FROM Problems 
    WHERE id = %s
    """
    
    try:
        cursor.execute(sql, (problem_id,))
        result = cursor.fetchone()
        
        if result:
            return {
                "id": result[0],
                "title": result[1],
                "id_company": result[2],
                "company_logo": result[3],
                "category": result[4],
                "partnership_model": result[5],
                "budget": result[6],
                "deadline": result[7],
                "description": result[8],
                "status": result[9],
                "created_at": result[10]
            }
        return None
        
    except psycopg2.Error as e:
        raise Exception(f"Erro ao buscar problema: {str(e)}")
    finally:
        cursor.close()

def update_problem_status(problem_id, new_status):
    """
    Atualiza o status de um problema.
    
    Args:
        problem_id (str): UUID do problema
        new_status (str): Novo status ('Aberto' ou 'Fechado')
        
    Returns:
        bool: True se atualizado com sucesso
    """
    conn = get_db()
    cursor = conn.cursor()
    
    sql = "UPDATE Problems SET status = %s WHERE id = %s"
    
    try:
        cursor.execute(sql, (new_status, problem_id))
        conn.commit()
        return cursor.rowcount > 0
        
    except psycopg2.Error as e:
        conn.rollback()
        raise Exception(f"Erro ao atualizar status do problema: {str(e)}")
    finally:
        cursor.close()