import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        layout = [#layout da pagina
            [sg.Text('Nome'),sg.Input()], #cada lista dessa é uma linha da janela
            [sg.Text('Idade'),sg.Input()],
            [sg.Button('Enviar dados')]
        ]
        
        janela = sg.Window('Dados do Usuário').layout(layout) #sg.Window, cria uma janela com o nome especificado, .layout() passa o layout da janela
        
        self.button, self.values = janela.Read() #isso aqui servirar para extrair os dados da janela para o codigo
        
    def Iniciar(self):
        print(self.values)

tela = TelaPython()#var tela 

tela.Iniciar()#inicia a tela