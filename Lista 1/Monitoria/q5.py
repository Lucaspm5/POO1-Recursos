#padrão 32 bits (womp womp)

class Numero:
    @staticmethod
    def transformBinario(n: int) -> str:
        return "".join(str((n >> i) & 1) for i in range(31, -1, -1))
    
if __name__ == "__main__":
    n = int(input('Informe um numero: '))
    print(Numero.transformBinario(n))