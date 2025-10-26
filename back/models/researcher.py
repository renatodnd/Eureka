# models/researcher.py
import uuid
import psycopg2
from database.db import get_db

def create_researcher(data):
    """
    Insere um novo pesquisador no banco de dados com base na estrutura da tabela Researcher.
    
    Args:
        data (dict): Dicionário contendo os dados do pesquisador.
                     Esperado: name, title, institution, email, expertise (lista de strings).
                     
    Returns:
        dict: O objeto pesquisador recém-criado, incluindo o ID.
        
    Raises:
        Exception: Em caso de falha na inserção no banco de dados.
    """
    conn = get_db()
    cursor = conn.cursor()
    
    # 1. Preparar os dados
    researcher_id = str(uuid.uuid4())
    
    # O psycopg2 mapeia automaticamente listas/tuplas Python para o tipo array do PostgreSQL (TEXT[])
    expertise_list = data.get('expertise', []) 
    
    # Mapeamento dos dados que podem ser opcionais
    achievements = data.get('achievements')
    image = data.get('image')
    linkedin = data.get('linkedin')
    location = data.get('location')

    # 2. Comando SQL de Inserção
    sql = """
    INSERT INTO researcher (
        id, name, title, institution, location, expertise, achievements, image, email, linkedin
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    RETURNING id, name, title, institution, location, expertise, email; -- Retorna um subconjunto de dados
    """
    
    try:
        # 3. Execução da Query
        cursor.execute(sql, (
            researcher_id,
            data['name'],
            data['title'],
            data['institution'],
            location,
            expertise_list, # Passando a lista Python que será convertida para TEXT[]
            achievements,
            image,
            data['email'],
            linkedin,
        ))
        
        # 4. Confirmação e Retorno
        conn.commit()
        
        # O RETURNING retorna os dados inseridos
        inserted_data = cursor.fetchone() 
        
        # Constrói o dicionário de resposta
        researcher = {
            "id": inserted_data[0],
            "name": inserted_data[1],
            "title": inserted_data[2],
            "institution": inserted_data[3],
            "location": inserted_data[4],
            "expertise": inserted_data[5], # O psycopg2 converte o array TEXT[] de volta para lista Python
            "email": inserted_data[6]
        }
        
        return researcher
        
    except psycopg2.IntegrityError as e:
        # Lida com erros de violação de constraints (ex: email duplicado, formato inválido)
        conn.rollback()
        # Você pode inspecionar o código de erro do PostgreSQL para dar uma mensagem mais específica
        if 'unique constraint "researcher_email_key"' in str(e):
             raise Exception("E-mail já cadastrado.")
        
        raise Exception(f"Erro de integridade do BD: {e.diag.message_primary}")
        
    except psycopg2.Error as e:
        # Lida com outros erros de BD
        conn.rollback()
        raise Exception(f"Erro ao inserir pesquisador no BD: {str(e)}")
        
    finally:
        cursor.close()

def get_researcher_by_id(researcher_id):
    """
    Busca um pequisador pelo ID.
    
    Args:
        researcher_id (str): UUID do pesquisador
        
    Returns:
        dict: Dados do pesquisador ou None se não encontrado
    """
    conn = get_db()
    cursor = conn.cursor()
    
    sql = """
    SELECT id, name, title, institution, location, expertise,
           email
    FROM researcher 
    WHERE id = %s
    """
    
    try:
        cursor.execute(sql, (researcher_id,))
        result = cursor.fetchone()
        
        if result:
            return {
                "id": result[0],
                "name": result[1],
                "title": result[2],
                "institution": result[3],
                "location": result[4],
                "expertise": result[5], # O psycopg2 converte o array TEXT[] de volta para lista Python
                "email": result[6]
            }
        return None
        
    except psycopg2.Error as e:
        raise Exception(f"Erro ao buscar pesquisador: {str(e)}")
    finally:
        cursor.close()