from soma_dois.main import resposta
import inspect
import pytest

def test_not_none():
    assert resposta([1,2,3]) is not None, "Esperado valor diferente de 'None'"

def test_type():
    assert type(resposta([1,2,3])) == int, "Esperado um inteiro"

def test_parameters():
    assert len(inspect.getfullargspec(resposta).args) == 1, "Assinatura da função deverá receber um parâmetro"

def test_options_resposta():
    assert resposta([1,2,3]) == 3 , f"Esperado valor 3"
    assert resposta([100,200,400]) == 300, f"Esperado valor 300"
    assert resposta([1]) == 1, f"Esperado valor 1"