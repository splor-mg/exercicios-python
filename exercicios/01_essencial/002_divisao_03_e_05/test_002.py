from main import resposta
import inspect
import pytest

def test_not_none():
    assert resposta(1) is not None, "Esperado valor diferente de 'None'"

def test_type():
    assert type(resposta(1)) == str, "Esperado uma string"

def test_parameters():
    assert len(inspect.getfullargspec(resposta).args) == 1, "Assinatura da função deverá receber um parâmetro"

def test_options_resposta():
    assert resposta(3) == 'Fizz' , f"Esperado Fizz"
    assert resposta(5) == 'Buzz' , f"Esperado Buzz"
    assert resposta(15) == 'FizzBuzz' , f"Esperado FizzBuzz"