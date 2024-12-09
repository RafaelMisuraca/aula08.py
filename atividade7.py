vendas_trimestrais = [
    [50, 55, 60],  
    [40, 45, 50],  
    [60, 65, 70],  
    [30, 35, 40]   
]


media_trimestral = [sum(trimestre) / len(trimestre) for trimestre in vendas_trimestrais]


somas_trimestrais = [sum(trimestre) for trimestre in vendas_trimestrais]
maior_soma = max(somas_trimestrais)
indice_maior_soma = somas_trimestrais.index(maior_soma)


menor_soma = min(somas_trimestrais)
indice_menor_soma = somas_trimestrais.index(menor_soma)


total_vendas_ano = sum(somas_trimestrais)


print(f"Média de vendas por trimestre: {media_trimestral}")
print(f"Trimestre com a maior soma de vendas: Trimestre {indice_maior_soma + 1} com {maior_soma} unidades")
print(f"Trimestre com a menor soma de vendas: Trimestre {indice_menor_soma + 1} com {menor_soma} unidades")
print(f"Total de vendas no ano: {total_vendas_ano} unidades")
