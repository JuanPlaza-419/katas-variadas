import pytest
from Sumador.calculadora import sumatoria

def test_suma_tres_numeros():
    assert sumatoria("1, 2, 3") == 6

def test_un_solo_numero():
    assert sumatoria("1") == 1

def test_string_vacio_retorna_cero():
    assert sumatoria("") == 0

def test_saltos_de_linea_multiples():
    assert sumatoria("1\n2\n3") == 6

def test_mezcla_comas_y_saltos_linea():
    assert sumatoria("1\n2,3\n4") == 10

def test_muchos_saltos_seguidos():
    assert sumatoria("1\n\n\n\n2") == 3