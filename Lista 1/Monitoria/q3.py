"""
Formulas:
    arranjo:
        n! / (n - p)!
    combinacao:
        n! / ((n - r)! * (r!))

"""

from q2 import Fatorial

class Combinatoria:
    @staticmethod
    def arranjo(n: int, p: int) -> float:
        return Fatorial().iterativo(n) / Fatorial().iterativo(n - p)
    @staticmethod
    def combinacao(n: int, r: int) -> float:
        return Fatorial().iterativo(n) / (Fatorial().iterativo(n - r) *
                                          Fatorial().iterativo(r))

if __name__ == "__main__":
    n, p, r = map(int, input('Informe n, p e r: ').split())
    print('Arranjo: ', Combinatoria().arranjo(n, p))
    print('Combinatoria: ', Combinatoria().combinacao(n, r))