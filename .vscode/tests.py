from main import analisar_codigo
from interpreter import Interpreter, ErroExecucao
from semantic import Semantica, ErroSemantico
from funcoes import montar_etapas

def verificar(nome, codigo, esperado):
    resultado = analisar_codigo(codigo, Semantica(), Interpreter())[0]
    assert resultado == esperado, f'{nome}: esperado {esperado}, recebido {resultado}'
    print(f'[OK] {nome}: {resultado}')

def verificar_raizes(nome, codigo, esperado, tolerancia=1e-09):
    resultado = analisar_codigo(codigo, Semantica(), Interpreter())[0]
    assert len(resultado) == len(esperado), f'{nome}: numero de raizes incorreto: {resultado}'
    assert all((abs(a - b) <= tolerancia for a, b in zip(resultado, esperado))), f'{nome}: esperado {esperado}, recebido {resultado}'
    print(f'[OK] {nome}: {resultado}')
verificar('potencia', 'POTENCIA(3, 2)', 9)
verificar('raiz quadrada', 'RAIZ(25)', 5.0)
verificar_raizes('duas raizes reais', 'BHASKARA(1, -3, 2)', [2.0, 1.0])
verificar_raizes('raiz dupla', 'BHASKARA(1, -2, 1)', [1.0, 1.0])
verificar('delta negativo: sem raizes reais', 'BHASKARA(1, 2, 5)', [])
for nome, codigo, tipo in [
    ("a zero", "BHASKARA(0, 2, 1)", ErroExecucao),
    ("raiz de negativo", "RAIZ(-1)", ErroExecucao),
    ("aridade de BHASKARA", "BHASKARA(1, 2)", ErroSemantico),
    ("divisao por zero", "1 / 0", ErroExecucao),
    ("fatorial negativo", "FATORIAL(-3)", ErroExecucao),
    ("fatorial nao inteiro", "FATORIAL(2.5)", ErroExecucao),
    ("aridade de FATORIAL", "FATORIAL(5, 2)", ErroSemantico),
]:
    try:
        analisar_codigo(codigo, Semantica(), Interpreter())
    except tipo as erro:
        print(f"[OK ERRO] {nome}: {erro}")
    else:
        raise AssertionError(
            f"{nome}: era esperado {tipo.__name__}"
        )

    
saida = StringIO()

with redirect_stdout(saida):
    resultado_fatorial = analisar_codigo(
        "FATORIAL(5)",
        Semantica(),
        Interpreter(),
    )[0]

assert resultado_fatorial == 120
assert "5! = 5 × 4 × 3 × 2 × 1 = 120" in saida.getvalue()
print("[OK] fatorial: 5! = 120, com desenvolvimento")