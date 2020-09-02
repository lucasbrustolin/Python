import PySimpleGUI as sg  

# -------------------------------------------------------------------------------------
#                                       EXEMPLO 1
#
# Description: InterfaceGUI  os metodos read(), readline() e readlines()
# -------------------------------------------------------------------------------------
class TelaPython:
    def __init__(self):
        #   Layout 
        layout = [
            [sg.Text('Nome', size=(5,0)),sg.Input(size=(20,0),key='nome')],
            [sg.Text('Idade',size=(5,0)),sg.Input(size=(20,0),key='idade')],
            [sg.Text('Quais provedores de e-mail são aceitos?')],
            [sg.Checkbox('Gmail', key='gmail'), sg.Checkbox('Outlook', key='outlook'), sg.Checkbox('Yahoo', key='yahoo')],
            [sg.Button('Enviar Dados')]
        ]
        #   Janela
        janela = sg.Window("Interface GUI - Python").layout(layout)
        #   Extrair os dados da tela 
        self.button, self.values = janela.Read()

    def Iniciar(self):
        nome            = self.values['nome']
        idade           = self.values['idade']
        aceita_gmail    = self.values['gmail']
        aceita_outlook  = self.values['outlook']
        aceita_yahoo    = self.values['yahoo']

        print("Nome"    , nome)
        print("Idade"   , idade)
        print("Gmail"   , aceita_gmail)
        print("Outlook" , aceita_outlook)
        print("Yahoo"   , aceita_yahoo)
        print("\n") # exemplo 2 de passar variavel ao print
        print(f"Nome:           {nome}")
        print(f"Idade:          {idade}")
        print(f"Aceita Gmail:   {aceita_gmail}")
        print(f"Aceita Outlook: {aceita_outlook}")
        print(f"Aceita Yahoo:   {aceita_yahoo}")

        #print(self.values)


tela = TelaPython()
tela.Iniciar()


