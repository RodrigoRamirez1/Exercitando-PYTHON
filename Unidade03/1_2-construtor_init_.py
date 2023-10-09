# CONSTRUTOR DA CLASSE_INIT_()

class Televisao:
    def __init__(self):
        self.volume = 10

    def aumentar_volume(self):
        self.volume += 1

    def diminuir_volume(self):
        self.volume -= 1

tv = Televisao()

print("Volume ao ligar a tv = ", tv.volume)
tv.aumentar_volume()
print("Volume atual = ", tv.volume)

#### ATRIBUTOS PRIVADOS

class ContaCorrente:
    def __init__(self):
        self._saldo = 0

    def depositar(self, valor):
        self._saldo += valor

    def consultar_saldo(self):
        return self._saldo
    

conta = ContaCorrente()
valor = float(input('Depositar na conta R$' )) 
conta.depositar(valor)
print('Saldo conta R$', conta.consultar_saldo())
