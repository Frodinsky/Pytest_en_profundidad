class Calculadora:


    def sumar(self, a: int, b: int) -> int:
        return a+b

    @classmethod
    def resta(cls, a: int, b: int) -> int:
        return a - b

    @staticmethod
    def multiplicacion(a: int, b: int) -> int:
        return a * b

    @staticmethod
    def division(a: int, b: int) -> float:
        return a / b

