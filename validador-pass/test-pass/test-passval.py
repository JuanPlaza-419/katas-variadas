import sys
from pathlib import Path

ruta_padre = str(Path(__file__).parent.parent)
sys.path.append(ruta_padre)

import pytest
from validador import validar_password

def test_error_longitud():
    """Falla por ser corta (aunque tenga todo lo demás)"""
    res = validar_password("a1!")
    assert "La contraseña es demasiado corta" in res["errors"]

def test_error_numero():
    """Falla por no tener números"""
    res = validar_password("SoloLetras!")
    assert "Debe contener al menos un número" in res["errors"]

def test_error_letra():
    """Falla por no tener letras (solo números y símbolos)"""
    res = validar_password("12345678!!!")
    assert "Debe contener al menos una letra" in res["errors"]

def test_error_minuscula():
    res = validar_password("SOLO_MAYUSCULAS_123!")
    assert "Debe contener al menos una letra minúscula" in res["errors"]

def test_error_mayuscula():
    res = validar_password("solo_minusculas_123!")
    assert "Debe contener al menos una letra mayúscula" in res["errors"]

def test_error_especial():
    """Falla por no tener caracteres especiales"""
    res = validar_password("Password123")
    assert "Debe contener al menos un carácter especial" in res["errors"]

def test_password_correcta():
    """Pasa todas las reglas"""
    res = validar_password("Mortadelo67!")
    assert res["isValid"] is True
    assert len(res["errors"]) == 0