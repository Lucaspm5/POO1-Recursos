from math import pi

print('Digite "sair" para encerrar o programa a qualquer momento')

leitura = lambda: input('Informe umas das seguintes formas (triangulo, circulo ou quadrado): ')

flag = 1

while flag:
    n = leitura().lower()
    if n == 'sair': break
    area = 0
    if n == 'triangulo':
        base, altura = map(int, input('Informe a base e a altura respectivamente: ').split())
        area = (base * altura) / 2.
    elif n == 'circulo':
        raio = int(input('informe o raio: '))
        area = pi * raio ** 2
    elif n == 'quadrado':
        lado = int(input('Informe a medida de um dos lados: '))
        area = lado ** 2
    area = float(area)
    print('Area do {}: {:.2f}'.format(n, area))