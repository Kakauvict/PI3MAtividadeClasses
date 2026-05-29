class Tarefa:
    tarefas = []

    def __init__(self, titulo):
        self.titulo = titulo
        Tarefa.tarefas.append(self)

    def __str__(self):
        return self.titulo

    # Atividade 1
    @classmethod
    def quantidade_tarefas(cls):
        return len(cls.tarefas)


t1 = Tarefa("Estudar Python")
t2 = Tarefa("Fazer atividade")

print("Tarefas:")
for tarefa in Tarefa.tarefas:
    print(tarefa)

print("Quantidade:", Tarefa.quantidade_tarefas())


# Atividade 2
class Pessoa:

    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f"{self.nome} - {self.idade} anos - {self.profissao}"

    def aniversario(self):
        self.idade += 1


pessoa1 = Pessoa("Kauany", 17, "Estudante")

print("\nAntes do aniversário:")
print(pessoa1)

pessoa1.aniversario()

print("\nDepois do aniversário:")
print(pessoa1)