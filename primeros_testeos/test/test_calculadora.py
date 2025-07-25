from primeros_testeos.proyecto.main import Calculadora
import pytest

class TestCalculadora:

    @pytest.mark.parametrize(
        "nro1, nro2, expected", [
            (1, 5, 6),
            (10, 10, 20),
            (50, 1, 51)
        ]
    )

    def test_sumar(self, nro1,nro2,expected):
        calculadora = Calculadora()
        resultado = calculadora.sumar(nro1,nro2)
        assert resultado == expected

    def test_resta(self):
        resultado = Calculadora.resta(5, 4)
        assert  resultado == 1

    def test_division(self, nombre, apellido, ine):
        resultado = Calculadora.division(6,3)
        assert resultado == 2

    def test_impares(self, numero_impar):
        no1 = numero_impar()
        no2 = numero_impar()
        assert (no1 + no2) %2 == 0
