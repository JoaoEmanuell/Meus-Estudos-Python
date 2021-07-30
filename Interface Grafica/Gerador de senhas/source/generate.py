from random import randint

class generate:

    #Gerador
    def listas(self):
        self.Minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.Maisculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P','Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.Numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.Especiais = ['"', '!', '@', '#', '$', '%', '&', '*', '(', ')', '-', '=', ',','{', '[', ']', '}', ';', '?', '~', '^', '/', '+', '.']

    def geração(self):
        try:
            limite = round(abs(float(str(self.tamanho).replace(',', '.'))))
        except ValueError:
            print("Erro, o valor informado não pode ser aceito, por favor insira um numero valido")
        else:
    #bloco com todas as opções marcadas
            if self.minusculas and self.numeros and self.especiais and self.maisculas:
                generate.aleatorio_4(self.Maisculas, self.Minusculas, self.Numeros, self.Especiais, limite)
    #bloco das letras maisculas
            elif self.maisculas:
                #sub bloco letras minusculas
                if self.maisculas and self.minusculas:
                    if self.maisculas and self.minusculas and self.numeros:
                        generate.aleatorio_3(self.Maisculas, self.Minusculas, self.Numeros, limite)
                    elif self.maisculas and self.minusculas and self.especiais:
                        generate.aleatorio_3(self.Especiais, self.Maisculas, self.Minusculas, limite)
                    else:
                        generate.aleatorio_2(self.Maisculas, self.Minusculas, limite)
                #sub bloco numeros
                elif self.maisculas and self.numeros:
                    if self.maisculas and self.especiais and self.numeros == True:
                        generate.aleatorio_3(self.Especiais, self.Maisculas, self.Numeros, limite)
                    else:
                        generate.aleatorio_2(self.Maisculas, self.Numeros, limite)
                elif self.maisculas and self.especiais:
                    generate.aleatorio_2(self.Maisculas, self.Especiais, limite)
                else:
                    generate.aleatorio_1(self.Maisculas, limite)
    #bloco das letras minusculas
            elif self.minusculas:
                #sub bloco numeros
                if self.minusculas and self.numeros:
                    if self.minusculas and self.numeros and self.especiais:
                        generate.aleatorio_3(self.Minusculas, self.Numeros, self.Especiais, limite)
                    else:
                        generate.aleatorio_2(self.Minusculas, self.Numeros, limite)
                #sub bloco especiais
                elif self.minusculas and self.especiais:
                    generate.aleatorio_2(self.Minusculas, self.Especiais, limite)
                else:
                    generate.aleatorio_1(self.Minusculas, limite)
    #bloco dos numeros
            elif self.numeros:
                if self.numeros and self.especiais:
                    generate.aleatorio_2(self.Numeros, self.Especiais, limite)
                else:
                    generate.aleatorio_1(self.Numeros, limite)
    #bloco dos especiais
            elif self.especiais:
                generate.aleatorio_1(self.Especiais, limite)
    #Função de aleatoridade
    def aleatorio_1(lista, limite):
        l = 0
        while l != limite:
                car = lista[randint(0, (len(lista) - 1))]
                print(f"{car}", end='')
                l += 1

    def aleatorio_2(lista1, lista2, limite):
        l = 0
        while l != limite:
            lista = randint(1 , 2)
            if lista == 1:
                car = lista1[randint(0, (len(lista1) - 1))]
            elif lista == 2:
                car = lista2[randint(0, (len(lista2) - 1))]
            print(f"{car}", end='')
            l += 1

    def aleatorio_3(lista1, lista2, lista3, limite):
        l = 0
        while l != limite:
            lista = randint(1 , 3)
            if lista == 1:
                car = lista1[randint(0, (len(lista1) - 1))]
            elif lista == 2:
                car = lista2[randint(0, (len(lista2) - 1))]
            elif lista == 3:
                car = lista3[randint(0, (len(lista3) - 1))]
            print(f"{car}", end='')
            l += 1

    def aleatorio_4(lista1, lista2, lista3, lista4, limite):
        l = 0
        while l != limite:
            lista = randint(1 , 4)
            if lista == 1:
                car = lista1[randint(0, (len(lista1) - 1))]
            elif lista == 2:
                car = lista2[randint(0, (len(lista2) - 1))]
            elif lista == 3:
                car = lista3[randint(0, (len(lista3) - 1))]
            elif lista == 4:
                car = lista4[randint(0, (len(lista4) - 1))]
            print(f"{car}", end='')
            l += 1