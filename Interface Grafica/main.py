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
            [sg.Slider(range = (0, 100), default_value = 0, orientation = 'h', size = (15, 20), key = 'slider')] #Slider, range será o valor minimo e maximo que ele ira receber, default_value é o valor padrão, orientation = 'h' ou 'v', h = 'horizontal', v = 'vertical'
            [sg.Button('Enviar dados')],
            [sg.Output(size = (30,20))] #output, tudo que seria printado no console é enviado para essa aréa
        ]
        
        self.janela = sg.Window('Dados do Usuário').layout(layout) #sg.Window, cria uma janela com o nome especificado, .layout() passa o layout da janela
        
        
        
    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read() #isso aqui servirar para extrair os dados da janela para o codigo
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