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








def fatorial(numero):
    if not isinstance(numero, (int, float)) or isinstance(numero, bool):
        raise ValueError("FATORIAL exige um numero inteiro nao negativo.")
    if numero < 0:
        raise ValueError("FATORIAL exige um numero inteiro nao negativo.")
    if isinstance(numero, float):
        if not math.isfinite(numero) or not numero.is_integer():
            raise ValueError("FATORIAL exige um numero inteiro nao negativo.")
    numero = int(numero)

    print("\nPasso a passo do fatorial:")
    print("Etapa 1 - Definicao: n! = produto de n por todos os inteiros positivos menores que ele.")
    if numero < 2:
        print(f"Etapa 2 - Caso especial: {numero}! vale 1 por definicao.")
        print(f"Conclusao: {numero}! = 1.")
        return 1

    fatores = list(range(numero, 0, -1))
    expansao = " × ".join(str(v) for v in fatores)
    print(f"Etapa 2 - Expansao: {numero}! = {expansao}")
    resultado = numero
    etapa = 3
    for valor in range(numero - 1, 1, -1):
        anterior = resultado
        resultado *= valor
        print(f"Etapa {etapa} - Multiplicando: {anterior} × {valor} = {resultado}")
        etapa += 1
    print(f"Conclusao: {numero}! = {expansao} = {resultado}.")
    return resultado









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
    etapas = [
        f"Equacao: {a}x² + ({b})x + ({c}) = 0",
        "Etapa 1 - Formula do discriminante: Δ = b² - 4 × a × c. O Δ mostra quantas raizes reais a equacao tem.",
        f"Etapa 2 - Substituicao: aqui a = {a}, b = {b} e c = {c}. Trocando na formula: Δ = ({b})² - 4 × ({a}) × ({c})",
        f"Etapa 3 - Calculo: primeiro o quadrado e o produto, depois a subtracao: Δ = {_fmt(b2)} - {_fmt(quatro_ac)} = {_fmt(delta)}",
    ]

    if delta < 0:
        etapas.append(
            "Etapa 4 - Como Δ < 0, nao existe raiz quadrada real de numero negativo. "
            "A equacao nao possui raizes reais (a parabola nao toca o eixo x)."
        )
        return etapas, []

    raiz_delta = math.sqrt(delta)
    denominador = 2 * a
    x1 = (-b + raiz_delta) / denominador
    x2 = (-b - raiz_delta) / denominador

    if delta == 0:
        situacao = "Como Δ = 0, as duas raizes sao iguais"
    else:
        situacao = "Como Δ > 0, existem duas raizes reais diferentes"

    etapas.extend([
        f"Etapa 4 - Formula resolutiva: x = (-b ± √Δ) / (2a). O ± quer dizer 'mais ou menos': fazemos a conta uma vez com + (x₁) e outra com - (x₂). {situacao}.",
        f"Etapa 5 - Substituicao de x₁: usando o sinal +, x₁ = (-({b}) + √{_fmt(delta)}) / (2 × ({a}))",
        f"Etapa 6 - Calculo de x₁: x₁ = ({_fmt(-b)} + {_fmt(raiz_delta)}) / {_fmt(denominador)} = {_fmt(x1)}",
        f"Etapa 7 - Substituicao de x₂: usando o sinal -, x₂ = (-({b}) - √{_fmt(delta)}) / (2 × ({a}))",
        f"Etapa 8 - Calculo de x₂: x₂ = ({_fmt(-b)} - {_fmt(raiz_delta)}) / {_fmt(denominador)} = {_fmt(x2)}",
    ])
    if delta == 0:
        etapas.append(f"Conclusao: raiz dupla x₁ = x₂ = {_fmt(x1)}. A parabola apenas encosta no eixo x.")
    else:
        etapas.append(f"Conclusao: x₁ = {_fmt(x1)} e x₂ = {_fmt(x2)}. Sao os pontos onde a parabola corta o eixo x.")
    return etapas, [x1, x2]


def bhaskara(a, b, c):
    etapas, raizes = montar_etapas(a, b, c)
    print('\nResolucao da equacao:')
    for etapa in etapas:
        print(etapa)
    return raizes


def grafico(a, b, c):
    for nome, valor in (('a', a), ('b', b), ('c', c)):
        if not isinstance(valor, (int, float)) or isinstance(valor, bool):
            raise ValueError(f"O coeficiente '{nome}' deve ser numerico.")
    if a == 0:
        raise ValueError("Nao e uma equacao do segundo grau: o coeficiente 'a' nao pode ser zero.")
    xv = -b / (2 * a)
    yv = a * xv ** 2 + b * xv + c
    delta = b ** 2 - 4 * a * c
    meia = 3.0
    raizes = []
    if delta >= 0:
        rd = math.sqrt(delta)
        raizes = [(-b + rd) / (2 * a), (-b - rd) / (2 * a)]
        meia = max(meia, 1.5 * abs(raizes[0] - xv))
    xmin = min(xv - meia, -1.0)
    xmax = max(xv + meia, 1.0)
    passos = 60
    pontos = []
    for i in range(passos + 1):
        x = xmin + (xmax - xmin) * i / passos
        pontos.append(f"{x:.4f},{a * x * x + b * x + c:.4f}")
    print("\nDados do grafico:")
    print(f"vertice = {_fmt(xv)}; {_fmt(yv)}")
    print("raizes = " + ("; ".join(_fmt(r) for r in raizes) if raizes else "nenhuma"))
    print("janela = " + f"{xmin:.4f}; {xmax:.4f}")
    print("pontos = " + " | ".join(pontos))
    return yv

FUNCOES = {
    "POTENCIA": (2, potencia),
    "RAIZ": (1, raiz),
    "BHASKARA": (3, bhaskara),
    "FATORIAL": (1, fatorial),
    "GRAFICO": (3, grafico),
}
