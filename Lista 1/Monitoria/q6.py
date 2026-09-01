class Ingresso:
    @staticmethod
    def simular_lucro(
        preco_inicial: float = 5.0,
        qtd_inicial: int = 120,
        custo_fixo: float = 200.0,
        passo_preco: float = 0.5,
        passo_qtd: int = 26,
        iteracoes: int = 9
    ) -> tuple[float, float, int]:
        
        preco = preco_inicial
        quantidade = qtd_inicial
        lucro_max = 0.0
        preco_max = 0.0
        qtd_max = 0

        for _ in range(iteracoes):
            lucro = (quantidade * preco) - custo_fixo
            print("preço ingresso = {:.2f}, quantidade = {}, lucro = {:.2f}".format(preco, quantidade, lucro))

            if lucro > lucro_max:
                lucro_max = lucro
                preco_max = preco
                qtd_max = quantidade

            preco -= passo_preco
            quantidade += passo_qtd

        print("\nLucro Maximo = {:.2f}".format(lucro_max))
        print("Preço ingresso = {:.2f}".format(preco_max))
        print("Quantidade vendida = {}".format(qtd_max))

        return lucro_max, preco_max, qtd_max


if __name__ == "__main__":
    Ingresso.simular_lucro()