CREATE DATABASE IF NOT EXISTS Eureka;

USE Eureka;

CREATE TABLE IF NOT EXISTS Researcher (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    title VARCHAR(100),
    institution VARCHAR(100),
    location VARCHAR(100),
    expertise: string[]
    achievements VARCHAR(100),
    image VARCHAR(100),
    email VARCHAR(100),
    linkedin VARCHAR(100),
    solutionsCount INTEGER,
    successRate INTEGER
);

CREATE TABLE IF NOT EXISTS Empresa (
    id SERIAL PRIMARY KEY,
    
);

CREATE TABLE IF NOT EXISTS Problems (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    company VARCHAR(100),
    companyLogo VARCHAR(100),
    category: ["Tecnologia Novel", "Melhoria de Processo"],
    partnershipModel: ["Pesquisa Patrocinada", "Co-desenvolvimento"],
    budget VARCHAR(100),
    deadline TIMESTAMP,
    description TEXT,
    status VARCHAR
    
);

CREATE TABLE IF NOT EXISTS Vaga (
    id SERIAL PRIMARY KEY,
    
);