from bson.objectid import ObjectId
from registro import Comida, Cliente, Venda
from database import colecao_comidas, colecao_clientes, colecao_vendas

# Funções CRUD e Função de Realizar Venda
def adicionar_comida(comida):
    colecao_comidas.insert_one({'nome': comida.nome, 'preco': comida.preco})

def listar_comidas():
    comidas = colecao_comidas.find()
    for comida in comidas:
        print(f"Nome: {comida['nome']}, Preço: {comida['preco']}")

def atualizar_comida(nome, novo_nome, novo_preco):
    colecao_comidas.update_one({'nome': nome}, {'$set': {'nome': novo_nome, 'preco': novo_preco}})

def remover_comida(nome):
    colecao_comidas.delete_one({'nome': nome})

def adicionar_cliente(cliente):
    colecao_clientes.insert_one({'nome': cliente.nome, 'cpf': cliente.cpf})

def listar_clientes():
    clientes = colecao_clientes.find()
    for cliente in clientes:
        nome = cliente.get('nome', 'N/A')
        cpf = cliente.get('cpf', 'N/A')
        print(f"Nome: {nome}, CPF: {cpf}")

def atualizar_cliente(cpf, novo_nome, novo_cpf):
    colecao_clientes.update_one({'cpf': cpf}, {'$set': {'nome': novo_nome, 'cpf': novo_cpf}})

def remover_cliente(cpf):
    colecao_clientes.delete_one({'cpf': cpf})

def realizar_venda(cliente_cpf, comida_nome, quantidade):
    venda = Venda(cliente_cpf, comida_nome, quantidade)
    colecao_vendas.insert_one({'cliente_cpf': venda.cliente_cpf, 'comida_nome': venda.comida_nome, 'quantidade': venda.quantidade})
    print(f"Venda realizada: Cliente CPF: {cliente_cpf}, Comida nome: {comida_nome}, Quantidade: {quantidade}")

# Menus de Navegação
def menu_inicial():
    print("\nMenu Inicial:")
    print("1. Gerenciar Alimentos")
    print("2. Gerenciar Clientes")
    print("3. Realizar Venda")
    print("4. Sair")
    escolha = input("Escolha uma opção: ")
    return escolha

def menu_gerenciar_alimentos():
    print("\nGerenciar Alimentos:")
    print("1. Adicionar Comida")
    print("2. Listar Comidas")
    print("3. Atualizar Comida")
    print("4. Remover Comida")
    print("5. Voltar")
    escolha = input("Escolha uma opção: ")
    return escolha

def menu_gerenciar_clientes():
    print("\nGerenciar Clientes:")
    print("1. Adicionar Cliente")
    print("2. Listar Clientes")
    print("3. Atualizar Cliente")
    print("4. Remover Cliente")
    print("5. Voltar")
    escolha = input("Escolha uma opção: ")
    return escolha

def main():
    while True:
        escolha = menu_inicial()
        
        if escolha == '1':
            while True:
                escolha_alimentos = menu_gerenciar_alimentos()
                
                if escolha_alimentos == '1':
                    nome = input("Nome da comida: ")
                    preco = float(input("Preço da comida: "))
                    adicionar_comida(Comida(nome, preco))
                elif escolha_alimentos == '2':
                    listar_comidas()
                elif escolha_alimentos == '3':
                    nome = input("Nome da comida a ser atualizada: ")
                    novo_nome = input("Novo nome da comida: ")
                    novo_preco = float(input("Novo preço da comida: "))
                    atualizar_comida(nome, novo_nome, novo_preco)
                elif escolha_alimentos == '4':
                    nome = input("Nome da comida a ser removida: ")
                    remover_comida(nome)
                elif escolha_alimentos == '5':
                    break
                else:
                    print("Opção inválida!")
        
        elif escolha == '2':
            while True:
                escolha_clientes = menu_gerenciar_clientes()
                
                if escolha_clientes == '1':
                    nome = input("Nome do cliente: ")
                    cpf = input("CPF do cliente: ")
                    adicionar_cliente(Cliente(nome, cpf))
                elif escolha_clientes == '2':
                    listar_clientes()
                elif escolha_clientes == '3':
                    cpf = input("CPF do cliente a ser atualizado: ")
                    novo_nome = input("Novo nome do cliente: ")
                    novo_cpf = input("Novo CPF do cliente: ")
                    atualizar_cliente(cpf, novo_nome, novo_cpf)
                elif escolha_clientes == '4':
                    cpf = input("CPF do cliente a ser removido: ")
                    remover_cliente(cpf)
                elif escolha_clientes == '5':
                    break
                else:
                    print("Opção inválida!")
        
        elif escolha == '3':
            cliente_cpf = input("CPF do cliente: ")
            comida_nome = input("Nome da comida: ")
            quantidade = int(input("Quantidade: "))
            realizar_venda(cliente_cpf, comida_nome, quantidade)
        
        elif escolha == '4':
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
