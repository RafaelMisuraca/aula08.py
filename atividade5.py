vendas = {
    'produto_a': 50,
    'produto_b': 75,
    'produto_c': 75,
    'produto_d': 30,
}

max_vendas = max(vendas.values())


produtos_mais_vendidos = [produto for produto, quantidade in vendas.items() if quantidade == max_vendas]


print("Produto(s) mais vendido(s):", produtos_mais_vendidos)
