class Config:
    # Configurações do banco de dados PostgreSQL
    POSTGRES_DB = "Eureka"
    POSTGRES_USER = "root"
    POSTGRES_PASSWORD = "1234"
    POSTGRES_HOST = "localhost"
    POSTGRES_PORT = "5432" # Porta padrão do PostgreSQL é 5432, não "db_port"
    
    # Outras configurações (ex: chave secreta)
    SECRET_KEY = 'sua_chave_secreta_aqui'