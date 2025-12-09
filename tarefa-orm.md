# Tarefa – ODBC e ORM

## 🔗 Links dos scripts e programas

- Script Docker: ./docker-compose.yml  
- Programa com ODBC: ./odbc_app.py  
- Programa com ORM: ./orm_app.py  

---

## 🧩 Resumo sobre ODBC (em Python)

ODBC (Open Database Connectivity) é um padrão que permite que aplicações se conectem a bancos de dados usando drivers específicos.  
No Python, utilizamos a biblioteca **pyodbc**, que permite a comunicação com bancos de dados como PostgreSQL, MySQL e SQL Server através de uma string de conexão padronizada.

Vantagens:
- Independência de banco
- Alta compatibilidade
- Estabilidade

---

## 🧩 Resumo sobre ORM (em Python)

ORM (Object Relational Mapping) é uma técnica que permite mapear tabelas do banco para classes Python.  
Em vez de escrever SQL diretamente, trabalhamos com objetos.

Framework escolhido: **SQLAlchemy**

Vantagens:
- Menos código SQL manual
- Mais produtividade
- Código mais organizado e seguro

---

## 🗄️ Banco de Dados

Banco criado com:
- Docker
- PostgreSQL
- PgAdmin

Banco: **AtividadesBD**

---

## ✅ Comandos SQL implementados

### Com ODBC:
- Inserir atividade em projeto
- Atualizar líder de projeto
- Listar projetos e atividades

### Com ORM:
- Inserir atividade em projeto
- Atualizar líder de projeto
- Listar projetos e atividades
