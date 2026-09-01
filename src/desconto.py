
from abc import ABC, abstractmethod

class Desconto(ABC):
    @abstractmethod
    def calcular(self, valor):
        pass
class DescontoNormal(Desconto):
    def calcular(self, valor):
        return valor * 0.1  # 10% de desconto

class DescontoVIP(Desconto):
    def calcular(self, valor):
        return valor * 0.2  # 20% de desconto

class DescontoPremium(Desconto):
    def calcular(self, valor):
        return valor * 0.3  # 30% de desconto


def main():
    valor = 100  # Valor original do produto

    desconto_normal = DescontoNormal()
    desconto_vip = DescontoVIP()
    desconto_premium = DescontoPremium()

    print(f"Desconto Normal: {desconto_normal.calcular(valor):.2f}")
    print(f"Desconto VIP: {desconto_vip.calcular(valor):.2f}")
    print(f"Desconto Premium: {desconto_premium.calcular(valor):.2f}")

if __name__ == "__main__":
    main()