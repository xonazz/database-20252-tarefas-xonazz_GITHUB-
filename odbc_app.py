import pyodbc

conn = pyodbc.connect(
    "DRIVER={PostgreSQL Unicode};"
    "SERVER=localhost;"
    "PORT=5432;"
    "DATABASE=AtividadesBD;"
    "UID=admin;"
    "PWD=1234;"
)

cursor = conn.cursor()

# Inserir atividade
cursor.execute("""
    INSERT INTO atividades (projeto_id, descricao)
    VALUES (1, 'Nova atividade via ODBC')
""")

# Atualizar líder
cursor.execute("""
    UPDATE projetos
    SET lider = 'Novo Líder'
    WHERE id = 1
""")

# Listar projetos e atividades
cursor.execute("""
    SELECT p.nome, p.lider, a.descricao
    FROM projetos p
    JOIN atividades a ON p.id = a.projeto_id
""")

for row in cursor.fetchall():
    print(row)

conn.commit()
conn.close()
