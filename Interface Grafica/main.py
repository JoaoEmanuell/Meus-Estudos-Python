import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        layout = [#layout da pagina
            [sg.Text('Nome', size = (5,0)),sg.Input(size = (50,0), key = 'nome')], #cada lista dessa é uma linha da janela
            [sg.Text('Idade', size = (5,0)),sg.Input(size = (3,0), key = 'idade')],
            [sg.Text('Quais provedores de e-mail serão aceitos? ')],
            [sg.Checkbox('Gmail', key = 'gmail'), sg.Checkbox('Outlook', key = 'outlook'), sg.Checkbox('Yahoo', key = 'yahoo')], #Checkbox cria uma caixa para você clicar
            [sg.Button('Enviar dados')]
        ]
        
        janela = sg.Window('Dados do Usuário').layout(layout) #sg.Window, cria uma janela com o nome especificado, .layout() passa o layout da janela
        
        self.button, self.values = janela.Read() #isso aqui servirar para extrair os dados da janela para o codigo
        
    def Iniciar(self):
        print(self.values)

tela = TelaPython()#var tela 

tela.Iniciar()#inicia a tela