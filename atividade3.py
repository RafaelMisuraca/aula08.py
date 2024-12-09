cores = {"azul", "amarelo", "vermelho", "roxo", "laranja", "preto", "branco", "cinza", "rosa", "marrom"}

def cores_com_mais_de_quatro_letras(cores):
    return {cor for cor in cores if len(cor) > 4}

cores_filtradas = cores_com_mais_de_quatro_letras(cores)

print(cores_filtradas)
