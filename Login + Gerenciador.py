import PySimpleGUI as sg

def criar_janela_login():
    layout_login = [
        [sg.Text('Usuário')],
        [sg.Input(key='usuario')],
        [sg.Text('Senha')],
        [sg.Input(key='senha', password_char='*')],
        [sg.Button('Login'), sg.Button('Sair')],
        [sg.Text('', key='mensagem')]
    ]

    return sg.Window('Login', layout=layout_login, finalize=True)

def criar_janela_todolist():
    sg.theme('DarkBlue4')
    layout_todolist = [
        [sg.Frame('Tarefas', layout=[[sg.Checkbox(''), sg.Input('')]], key='container')],
        [sg.Button('Nova Tarefa'), sg.Button('Resetar')]
    ]

    return sg.Window('Todo List', layout=layout_todolist, finalize=True)

janela_login = criar_janela_login()
janela_todolist = None

while True:
    window, event, values = sg.read_all_windows()

    if window == sg.WIN_CLOSED:
        break

    if window == janela_login:
        if event == sg.WIN_CLOSED or event == 'Sair':
            break
        elif event == 'Login':                #Criado um login: Nome:Thiago senha:12345
            senha_correta = '12345'
            usuario_correto = 'Thiago'
            usuario = values['usuario']
            senha = values['senha']
            if senha == senha_correta and usuario == usuario_correto:
                janela_login['mensagem'].update('Login efetuado com sucesso!')
                janela_todolist = criar_janela_todolist()
                janela_login.hide()
            else:
                janela_login['mensagem'].update('Senha ou usuário incorreto')

    elif window == janela_todolist:
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Nova Tarefa':
            janela_todolist.extend_layout(janela_todolist['container'], [[sg.Checkbox(''), sg.Input('')]])
        elif event == 'Resetar':
            janela_todolist.close()
            janela_todolist = criar_janela_todolist()

janela_login.close()
if janela_todolist:
    janela_todolist.close()