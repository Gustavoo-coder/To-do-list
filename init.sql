CREATE TABLE IF NOT EXISTS usuario (
    id_usuario SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    senha_hash TEXT NOT NULL
);


CREATE TABLE IF NOT EXISTS tarefa (
    id_tarefa SERIAL PRIMARY KEY,
    nome_tarefa VARCHAR(100) NOT NULL,
    descricao_tarefa TEXT,
    status_tarefa VARCHAR(20),
    id_usuario INTEGER REFERENCES usuario(id_usuario),
    CONSTRAINT validar_status CHECK (status_tarefa IN ('A fazer', 'Em andamento', 'Concluido'))
);