import json
def titulo(texto):
    print('=' * 40)
    print(texto.center(40))
    print('=' * 40)

def salvar_json(dados,arq):
    with open('utills.tarefas.json', 'w') as arq:json.dump(dados,arq)

