"""
Calculo da Area:
    1. triangulo: 
        base * altura / 2
    2. quadrado: 
        lado * lado
    3. circulo: 
        pi * raio * raio
"""

from math import pi

class Area:
    @staticmethod
    def areadoObjeto(object: str) -> float | None:
        resposta = None
        match object:
            case 'triangulo':
                base, altura = map(float, input('Informe a base e a altura: ').split())
                resposta = base * altura / 2
            case 'quadrado':
                lado = float(input('Informe o lado: '))
                resposta = lado * lado
            case 'circulo':
                raio = float(input('Informe o raio: '))
                resposta = pi * raio * raio
        return resposta
    @staticmethod
    def menu():
        print('1. Triangulo')
        print('2. Quadrado')
        print('3. Circulo')
        print('Informe o nome do objeto a qual voce deseja verificar sua area (informe qualquer outra coisa para sair): ')

if __name__ == "__main__":
    while True:
        Area().menu()
        resposta = Area().areadoObjeto(input())
        if not resposta: 
            break
        print('Area: {:.2f}'.format(resposta))