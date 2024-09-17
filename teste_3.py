import json

with open('dados.json') as f:
    dados = json.load(f)

faturamentos = [dia['valor'] for dia in dados if dia['valor'] > 0]

menor_valor = min(faturamentos)
maior_valor = max(faturamentos)
media_mensal = sum(faturamentos) / len(faturamentos)
dias_acima_da_media = len([valor for valor in faturamentos if valor > media_mensal])

print(menor_valor)
print(maior_valor)
print(dias_acima_da_media)
