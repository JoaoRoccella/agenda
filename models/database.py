from sqlite3 import Connection, connect

class Database:
    def __init__(self, db_name: str):
        self.connection: Connection = connect(db_name)
        self.cursor = self.connection.cursor()

    def execute(self, query: str, params: tuple = ()):
        self.cursor.execute(query, params)
        self.connection.commit()
        return self.cursor

    def fetchall(self, query: str, params: tuple = ()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()
    
    def close(self):
        self.connection.close()

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

# Extensão: qwtel.sqlite-viewer

# try:
#     db = Database('./data/tarefas.sqlite3')
#     db.execute('''
#     CREATE TABLE IF NOT EXISTS tarefas (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         titulo_tarefa TEXT NOT NULL,
#         data_conclusao TEXT);
#     ''')
#     db.execute('INSERT INTO tarefas (titulo_tarefa, data_conclusao) VALUES (?, ?);', ('Estudar Python', '2024-06-30'))
# except Exception as e:
#     print(f"Erro ao criar tabela: {e}")
# finally:
#     db.close()
