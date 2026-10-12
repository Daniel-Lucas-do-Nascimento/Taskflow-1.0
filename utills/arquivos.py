import json
def titulo(texto):
    print('=' * 40)
    print(texto.center(40))
    print('=' * 40)

def ler_json():
    with open('dados/tarefas.json' , 'r') as arq:
        return json.load(arq)

def salvar_json(dados):
    with open('dados/tarefas.json', 'w') as arq:
        json.dump(dados,arq, indent = 4,ensure_ascii = False)

def gerar_id():
    dados = ler_json()
    maiorid = 0
    if len(dados) > 0:
        for cont in dados:
            if cont['id'] > maiorid:
                maiorid = cont['id']
        return maiorid + 1
    else:
        return 1

