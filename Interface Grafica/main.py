import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        layout = [#layout da pagina
            [sg.Text('Nome', size = (5,0)),sg.Input(size = (50,0), key = 'nome')], #cada lista dessa é uma linha da janela
            [sg.Text('Idade', size = (5,0)),sg.Input(size = (3,0), key = 'idade')],
            [sg.Text('Quais provedores de e-mail serão aceitos? ')],
            [sg.Checkbox('Gmail', key = 'gmail'), sg.Checkbox('Outlook', key = 'outlook'), sg.Checkbox('Yahoo', key = 'yahoo')], #Checkbox cria uma caixa para você clicar
            [sg.Text('Aceita cartão')],
            [sg.Radio('Sim', 'cartoes', key = 'cartao_sim'), sg.Radio('Não', 'cartoes', key = 'cartao_não')],
            [sg.Button('Enviar dados')]
        ]
        
        janela = sg.Window('Dados do Usuário').layout(layout) #sg.Window, cria uma janela com o nome especificado, .layout() passa o layout da janela
        
        self.button, self.values = janela.Read() #isso aqui servirar para extrair os dados da janela para o codigo
        
    def Iniciar(self):
        nome = self.values['nome'] # recebe o item que possue a key nome, do dicionario valores
        idade = self.values['idade']
        gmail = self.values['gmail']
        outlook = self.values['outlook']
        yahoo = self.values['yahoo']
        cartao_sim = self.values['cartao_sim']
        cartao_nao = self.values['cartao_não']
        print(f'nome: {nome}')
        print(f'idade: {idade}')
        print(f'aceita gmail: {gmail}')
        print(f'aceita outlook: {outlook}')
        print(f'aceita yahoo: {yahoo}')
        print(f'aceita cartao, sim: {cartao_sim}')
        print(f'aceita cartao, não: {cartao_nao}')
tela = TelaPython()#var tela 

tela.Iniciar()#inicia a tela