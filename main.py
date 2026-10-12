from utills.arquivos import titulo,salvar_json

titulo('Taskflow')
print('''[1] - Adicionar tarefa
[2] - Listar tarefas
[3] - Buscar tarefa
[4] - Editar tarefa
[5] - Concluir tarefa
[6] - Excluir tarefa
[7] - Ver extatísticas
[0] - Sair''')

opcao = int(input('Digite a opção desejada: '))

if opcao == 1:
    from services.tarefas import adicionar_tarefa
    adicionar_tarefa()
