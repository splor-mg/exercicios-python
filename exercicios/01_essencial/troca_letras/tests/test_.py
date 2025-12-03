from troca_letras.main import resposta
import inspect
import pytest

def test_not_none():
    assert resposta("batatinha") is not None, "Esperado valor diferente de 'None'"

def test_type():
    assert type(resposta("batatinha")) == str, "Esperado uma string"

def test_parameters():
    assert len(inspect.getfullargspec(resposta).args) == 1, "Assinatura da função deverá receber um parâmetro"

def test_options_resposta():
    assert resposta('batatinha') == 'aatatinhb' , f"Esperado valor 'aatatinhb'"
    assert resposta('a' ) == 'a' , f"Esperado valor 'a'"
    assert resposta('ab') == 'ba', f"Esperado valor 'ba'"