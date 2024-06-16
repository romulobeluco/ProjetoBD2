
class Comida:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Venda:
    def __init__(self, cliente_cpf, comida_nome, quantidade):
        self.cliente_cpf = cliente_cpf
        self.comida_nome = comida_nome
        self.quantidade = quantidade
