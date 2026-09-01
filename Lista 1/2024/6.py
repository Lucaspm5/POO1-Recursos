preco, quantidade, lucro, lucroMax, PrecoMax, QuantidadeMax = 5., 120, 400., 0., 0., 0
for i in range(9):
    print('preço ingresso = {:.2f}, quantidade = {}, lucro = {:.2f}'.format(preco, quantidade, lucro))
    preco -= 0.5
    quantidade += 26
    lucro = float((quantidade * preco) - 200)
    if lucro > lucroMax:
        lucroMax = lucro
        PrecoMax = preco
        QuantidadeMax = quantidade
print()
print('Lucro Maximo = {:.2f}'.format(lucroMax))
print('Preço ingresso = {:.2f}'.format(PrecoMax))
print('Quantidade vendida = {}'.format(QuantidadeMax))
        