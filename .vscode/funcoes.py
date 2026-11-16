import math

def potencia(base, expoente):
    if not isinstance(base, (int, float)) or isinstance(base, bool):
        raise ValueError('POTENCIA exige uma base numerica.')
    if not isinstance(expoente, (int, float)) or isinstance(expoente, bool):
        raise ValueError('POTENCIA exige um expoente numerico.')
    try:
        resultado = base ** expoente
    except (OverflowError, ZeroDivisionError, ValueError) as erro:
        raise ValueError(f'Nao foi possivel calcular POTENCIA: {erro}.') from erro
    if isinstance(resultado, complex):
        raise ValueError('POTENCIA nao aceita resultado complexo nesta linguagem.')
    return resultado

def raiz(numero):
    if not isinstance(numero, (int, float)) or isinstance(numero, bool):
        raise ValueError('RAIZ exige um numero real.')
    if numero < 0:
        raise ValueError('RAIZ nao aceita numeros negativos.')
    return math.sqrt(numero)

def _fmt(numero):
    if math.isclose(numero, round(numero), abs_tol=1e-12):
        return str(int(round(numero)))
    return f'{numero:.10g}'

def montar_etapas(a, b, c):
    for nome, valor in (('a', a), ('b', b), ('c', c)):
        if not isinstance(valor, (int, float)) or isinstance(valor, bool):
            raise ValueError(f"O coeficiente '{nome}' deve ser numerico.")
    if a == 0:
        raise ValueError("Nao e uma equacao do segundo grau: o coeficiente 'a' nao pode ser zero.")
    b2 = b ** 2
    quatro_ac = 4 * a * c
    delta = b2 - quatro_ac
    etapas = [f'Equacao: {a}x² + ({b})x + ({c}) = 0', 'Discriminante: Δ = b² - 4ac', f'Substituindo: Δ = ({b})² - 4 × ({a}) × ({c})', f'Calculando: Δ = {_fmt(b2)} - {_fmt(quatro_ac)} = {_fmt(delta)}']
    if delta < 0:
        etapas.append('Como Δ é menor que zero, nao existem raizes reais.')
        return (etapas, [])
    raiz_delta = math.sqrt(delta)
    denominador = 2 * a
    x1 = (-b + raiz_delta) / denominador
    x2 = (-b - raiz_delta) / denominador
    etapas.extend(['Formula resolutiva: x = (-b ± √Δ) / (2a)', f'Raiz quadrada do discriminante: √Δ = √{_fmt(delta)} = {_fmt(raiz_delta)}', f'Primeira raiz: x₁ = ({_fmt(-b)} + {_fmt(raiz_delta)}) / {_fmt(denominador)} = {_fmt(x1)}', f'Segunda raiz: x₂ = ({_fmt(-b)} - {_fmt(raiz_delta)}) / {_fmt(denominador)} = {_fmt(x2)}'])
    if delta == 0:
        etapas.append(f'Resultado: raiz dupla x₁ = x₂ = {_fmt(x1)}.')
    else:
        etapas.append(f'Resultado: x₁ = {_fmt(x1)} e x₂ = {_fmt(x2)}.')
    return (etapas, [x1, x2])

def bhaskara(a, b, c):
    etapas, raizes = montar_etapas(a, b, c)
    print('\nResolucao da equacao:')
    for etapa in etapas:
        print(etapa)
    return raizes
FUNCOES = {'POTENCIA': (2, potencia), 'RAIZ': (1, raiz), 'BHASKARA': (3, bhaskara)}
