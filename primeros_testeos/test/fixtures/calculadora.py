import random
import pytest

@pytest.fixture()
def numero_impar():
    def fabrica_numeros():
        while True:
            aleatorio = random.randint(1,100)
            if aleatorio % 2 != 0:
                return aleatorio
    return fabrica_numeros