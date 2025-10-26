CREATE DATABASE IF NOT EXISTS Eureka;

USE Eureka;

CREATE TABLE IF NOT EXISTS Researcher (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    title VARCHAR(100),
    institution VARCHAR(100),
    location VARCHAR(100),
    -- expertise: string[]
    achievements VARCHAR(100),
    image VARCHAR(100),
    email VARCHAR(100),
    linkedin VARCHAR(100),
    solutionsCount INTEGER,
    successRate INTEGER
);

CREATE TABLE IF NOT EXISTS Company (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    location VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS Problems (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    id_company VARCHAR(100),
    companyLogo VARCHAR(100),
    -- category: ["Tecnologia Novel", "Melhoria de Processo"],
    -- partnershipModel: ["Pesquisa Patrocinada", "Co-desenvolvimento"],
    budget VARCHAR(100),
    deadline TIMESTAMP,
    description TEXT,
    status VARCHAR,
    CONSTRAINT fk_id_company
        FOREIGN KEY (id_company)
        REFERENCES Company (id)
);