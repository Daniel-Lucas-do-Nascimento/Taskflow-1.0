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

while True:
    try:
        opcao = int(input('Digite a opção desejada: '))
        if opcao < 0 or opcao > 7:
            print('Opção inválida. Digite novamente.')
        else:
            break
    except ValueError:
        print('Opção inválida. Digite um número inteiro.')

if opcao == 1:
    from services.tarefas import adicionar_tarefa
    adicionar_tarefa()
elif opcao == 2:
    from services.tarefas import listar_tarefas
    listar_tarefas()
elif opcao == 3:
    from services.tarefas import buscar_tarefa
    buscar_tarefa()
