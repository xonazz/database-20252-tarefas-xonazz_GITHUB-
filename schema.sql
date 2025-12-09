CREATE TABLE projetos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    lider VARCHAR(100)
);

CREATE TABLE atividades (
    id SERIAL PRIMARY KEY,
    projeto_id INT REFERENCES projetos(id),
    descricao VARCHAR(200)
);
