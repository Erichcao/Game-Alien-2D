
from abc import ABC, abstractmethod

class Desconto(ABC):
    @abstractmethod
    def calcular(self, valor):
        pass

class IDesconto:
    def calcular(self, valor):
        raise NotImplementedError
class ICupom:
    def aplicar_cupom(self, codigo):
        raise NotImplementedError
class IVIP:
    def validar_usuario_vip(self, usuario):
        raise NotImplementedError


class DescontoNormal(IDesconto):
    def calcular(self, valor):
        return valor * 0.1  # 10% de desconto


class DescontoVIP(IDesconto, ICupom, IVIP):
    def calcular(self, valor):
        return valor * 0.2  # 20% de desconto
    def aplicar_cupom(self, codigo):
        return True
    def validar_usuario_vip(self, usuario):
        return usuario == "vip"

class DescontoPremium(Desconto):
    def calcular(self, valor):
        return valor * 0.3  # 30% de desconto
    
def aplicar_desconto(desconto: Desconto, valor: float)-> float:
    return desconto.calcular(valor)

def aplicar_cupom(cupom: ICupom, codigo: str) -> bool:
    return cupom.aplicar_cupom(codigo)

if __name__ == "__main__":
    valor = 100  # Valor original do produto

    normal = DescontoNormal()
    vip = DescontoVIP()

print("Desconto Normal:", aplicar_desconto(normal, valor))
print("Desconto VIP:", aplicar_desconto(vip, valor))

print("Cupom VIP:", aplicar_cupom("DESC10"))


