class bola():
    def __init__(self, cor, circ, mat):
        self.cor  = cor
        self.circ = circ
        self.mat  = mat

    def escrever(self):
        print(f"A cor da bola é {self.cor}")
        print(f"A circuferencia da bola é {self.circ}")
        print(f"O material da bola é {self.mat}")

p1 = bola('Branco', 10, "Plastico")

p1.escrever()
