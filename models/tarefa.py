from models.database import Database

class Tarefa:
    def __init__(self, titulo_tarefa, data_conclusao=None):
        self.titulo_tarefa = titulo_tarefa
        self.data_conclusao = data_conclusao

    def salvar_tarefa(self):
        with Database('./data/tarefas.sqlite3') as db:
            db.execute(
                'INSERT INTO tarefas (titulo_tarefa, data_conclusao) VALUES (?, ?);',
                (self.titulo_tarefa, self.data_conclusao)
            )
    
    @staticmethod
    def obter_tarefas():
        with Database('./data/tarefas.sqlite3') as db:
            resultados = db.fetchall('SELECT titulo_tarefa, data_conclusao FROM tarefas;')
            tarefas = [Tarefa(titulo, data) for titulo, data in resultados]
            return tarefas
    