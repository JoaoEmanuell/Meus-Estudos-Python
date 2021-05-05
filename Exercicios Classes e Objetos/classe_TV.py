"""
[Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.]
"""
class tv():
    def __init__(self, canal = 1, volume = 1):
        """[__init__]

        Args:
            canal (int, Numero do canal): [Informe o numero do canal]. Defaults to 1.
            volume (int, Numero do volume): [Informe o numero do volume]. Defaults to 1.
        """        
        if volume < 1:
            print("Desculpe, o volume informado está invalido")
        elif canal < 1:
            print("Desculpe o canal informado está invalido")
        else:
            self.canal = canal
            self.volume = volume
    
    def mudar_canal(self):
        novo_canal = int(input("Novo canal "))
        if novo_canal < 1 or novo_canal > 10000:
            return ("Desculpe mas o canal informado está invalido")
        else:
            return (f"O canal foi mudado com sucesso\nO novo canal é o canal {self.canal}\nAproveite o novo canal")

    def aumentar_volume(self):
        novo_volume = int(input("Quanto a porcentagem deseja aumentar do volume atual? "))
        volume_atual = self.volume
        volume_atual += novo_volume
        if volume_atual > 100 or novo_volume < 0:
            return ("Desculpe, volume invalido")
        else:
            self.volume += novo_volume
            return (f"Sucesso, o volume atual é {self.volume}")

    def diminuir_volume(self):
        novo_volume = int(input("Quanto a porcentagem deseja diminuir do volume atual? "))
        volume_atual = self.volume
        volume_atual -= novo_volume
        if volume_atual < 0:
            return ("Desculpe, volume invalido")
        else:
            self.volume -= novo_volume
            return (f"Sucesso, o volume atual é {self.volume}")

tv = tv(2, 50)

print(tv.aumentar_volume())