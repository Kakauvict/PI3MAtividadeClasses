class Tarefa:
    tarefas = []

    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao
        self.concluido = False
        Tarefa.tarefas.append(self)

    def __str__(self):
        return f'{self.titulo} | {self.descricao}'

    @classmethod
    def listarTarefas(cls):
        for tarefa in cls.tarefas:
            print(tarefa)


tarefa_01 = Tarefa('Corrigir Provas', 'Corrigir provas 01')
tarefa_02 = Tarefa('Estudar Python', 'Estudar Orientação a objetos')

Tarefa.listarTarefas()

# Atividade 1
print('Quantidade de tarefas:', len(Tarefa.tarefas))


# Atividade 2
class Pessoa:

    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'{self.nome} | {self.idade} | {self.profissao}'

    def aniversario(self):
        self.idade += 1


pessoa1 = Pessoa('Kauany', 17, 'Estudante')

print(pessoa1)

pessoa1.aniversario()

print(pessoa1)