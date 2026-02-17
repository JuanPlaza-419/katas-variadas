import pytest
from calculadora import sumatoria

def test_suma_tres_numeros():
    assert sumatoria("1, 2, 3") == 6

def test_suma_dos_numeros():
    assert sumatoria("1, 2") == 3

def test_un_solo_numero():
    assert sumatoria("1") == 1

def test_string_vacio_retorna_cero():
    assert sumatoria("") == 0