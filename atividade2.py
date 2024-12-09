produtos = {
    1: {'nome': 'Produto A', 'preço': 20.5, 'quantidade': 10},
    2: {'nome': 'Produto B', 'preço': 35.0, 'quantidade': 5},
    3: {'nome': 'Produto C', 'preço': 12.0, 'quantidade': 20}
}

def adicionar_produto(id_produto, nome, preço, quantidade):
    if id_produto in produtos:
        print("Produto já existe.")
    else:
        produtos[id_produto] = {'nome': nome, 'preço': preço, 'quantidade': quantidade}
        print(f"Produto {nome} adicionado com sucesso!")

def remover_produto(id_produto):
    if id_produto in produtos:
        del produtos[id_produto]
        print(f"Produto {id_produto} removido com sucesso!")
    else:
        print("Produto não encontrado.")

def atualizar_produto(id_produto, nome=None, preço=None, quantidade=None):
    if id_produto in produtos:
        if nome:
            produtos[id_produto]['nome'] = nome
        if preço is not None:
            produtos[id_produto]['preço'] = preço
        if quantidade is not None:
            produtos[id_produto]['quantidade'] = quantidade
        print(f"Produto {id_produto} atualizado com sucesso!")
    else:
        print("Produto não encontrado.")

def exibir_produtos():
    for id_produto, info in produtos.items():
        print(f"ID: {id_produto}, Nome: {info['nome']}, Preço: R${info['preço']:.2f}, Quantidade: {info['quantidade']}")

exibir_produtos()  

adicionar_produto(4, 'Produto D', 25.0, 15)

atualizar_produto(2, preço=37.0, quantidade=7)

remover_produto(3)

exibir_produtos()