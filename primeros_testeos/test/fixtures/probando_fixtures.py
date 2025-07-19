import pytest

@pytest.fixture
def nombre():
    return "Facundo"

@pytest.fixture
def apellido():
    return "Perez"

@pytest.fixture
def ine():
    return 1234