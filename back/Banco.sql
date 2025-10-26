CREATE DATABASE IF NOT EXISTS Eureka;

USE Eureka;

CREATE TABLE IF NOT EXISTS Researcher (
    id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    title VARCHAR(150) NOT NULL,
    institution VARCHAR(200) NOT NULL,
    location VARCHAR(150),
    expertise TEXT[],
    achievements TEXT,
    image VARCHAR(500),
    email VARCHAR(255) UNIQUE, -- Adicionado UNIQUE e aumentado
    linkedin VARCHAR(500), -- Aumentado para URLs completas
    solutions_count INTEGER DEFAULT 0 CHECK (solutions_count >= 0),
    success_rate DECIMAL(5,2) DEFAULT 0.00 CHECK (success_rate >= 0 AND success_rate <= 100),
    is_verified BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,

    -- Constraints
    CONSTRAINT valid_email CHECK (email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$')
);

CREATE TABLE IF NOT EXISTS Company (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    location VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS Problems (
    id SERIAL PRIMARY KEY,
    title VARCHAR(500) NOT NULL,
    id_company INTEGER NOT NULL,
    company_logo VARCHAR(500),
    category TEXT[], -- Array de strings para categorias
    partnership_model TEXT[], -- Array de strings para modelos de parceria
    budget VARCHAR(100),
    deadline VARCHAR(100),
    description TEXT,
    status VARCHAR(7) CHECK (status IN ('Aberto', 'Fechado')) DEFAULT 'Aberto',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_id_company
        FOREIGN KEY (id_company) REFERENCES Company (id)
);

CREATE TABLE research_projects (
    id SERIAL PRIMARY KEY,
    id_research INTEGER NOT NULL,
    timestamp VARCHAR(100),
    content TEXT,
    problem VARCHAR(500) NOT NULL,
    company VARCHAR(255) NOT NULL,
    technologies TEXT[], -- Array de strings para as tecnologias
    category VARCHAR(100) NOT NULL,
    progress INTEGER CHECK (progress >= 0 AND progress <= 100),
    current_stage INTEGER,
    total_stages INTEGER,
    stages TEXT[], -- Array de strings para os estágios
    likes INTEGER DEFAULT 0,
    comments INTEGER DEFAULT 0,
    shares INTEGER DEFAULT 0,
    is_liked BOOLEAN DEFAULT FALSE,
    image VARCHAR(500),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_id_researcher
        FOREIGN KEY (id_research) REFERENCES Researcher (id)
);