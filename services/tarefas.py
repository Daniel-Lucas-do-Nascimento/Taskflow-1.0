def adicionar_tarefa():
    from utills.arquivos import gerar_id,salvar_json,ler_json,validar_titulo,validar_prazo, validar_prioridade
    dados2 = ler_json()
    titulo = validar_titulo()
    descricao = input('Digite a descrição da tarefa: ')
    prioridade = validar_prioridade()
    prazo = validar_prazo()   
    dados = {'id': gerar_id(),
            'titulo' : titulo,
            'descricao' : descricao,
            'prioridade' : prioridade,
            'prazo' : prazo,
            'status' : 'pendente'}
    dados2.append(dados)
    salvar_json(dados2)

def listar_tarefas():
    from utills.arquivos import ler_json,escrever_tarefa
    dados = ler_json()
    for tarefa in dados:
        escrever_tarefa(tarefa)
        

def buscar_tarefa():
    from utills.arquivos import ler_json,escrever_tarefa
    dados = ler_json()
    verificador = False
    while True:
        try:
          busca_id = int(input('Digite o ID da tarefa que desefa buscar: ')) 
          break
        except ValueError:
            print('ID inválido. Digite um número inteiro.')
    for tarefas in dados:
        if tarefas['id'] == busca_id:
            escrever_tarefa(tarefas)
            verificador = True
            break
    if verificador == False:
        print('Tarefa não encontrada.')
           