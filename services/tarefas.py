def adicionar_tarefa():
    from utills.arquivos import gerar_id,salvar_json,ler_json
    dados2 = ler_json()
    dados = {'id': gerar_id(),
             'titulo' : input('Digite o título da tarefa: '),
             'descricao' : input('Digite a descrição da tarefa: '),
             'prioridade' : input('Digite a prioridade da tarefa: '),
             'prazo' : input('Data limite: '),
             'status' : 'pendente'}
    dados2.append(dados)
    salvar_json(dados2)
