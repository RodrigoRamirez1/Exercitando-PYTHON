class PrimeiraClasse:
    def imprimir_mensagem(self, nome): # Criando um método 
        print(f"Olá {nome}, seja bem vindo!")

objeto1 = PrimeiraClasse() # Instanciando um objeto do tipo PrimeiraClasse 
objeto1.imprimir_mensagem('João') # Invocando o método

##################################

class Calculadora:
    def somar(self, n1, n2):
        return n1 + n2

    def subtrair(self, n1, n2):
        return n1 - n2

    def multiplicar(self, n1, n2):
        return n1 * n2

    def dividir(self, n1, n2):
        return n1 / n2

    def dividir_resto(self, n1, n2):
        return n1 % n2

calc = Calculadora()

print('Soma:', calc.somar(4, 3))
print('Subtração:', calc.subtrair(13, 7))
print('Multiplicação:', calc.multiplicar(2, 4))
print('Divisão:', calc.dividir(16, 5))
print('Resto da divisão:', calc.dividir_resto(7, 3))
