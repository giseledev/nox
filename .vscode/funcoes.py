import math


def potencia(base, expoente):
    """Calcula base elevada a expoente."""
    if not isinstance(base, (int, float)) or isinstance(base, bool):
        raise ValueError("POTENCIA exige uma base numerica.")
    if not isinstance(expoente, (int, float)) or isinstance(expoente, bool):
        raise ValueError("POTENCIA exige um expoente numerico.")
    try:
        resultado = base ** expoente
    except (OverflowError, ZeroDivisionError, ValueError) as erro:
        raise ValueError(f"Nao foi possivel calcular POTENCIA: {erro}.") from erro
    if isinstance(resultado, complex):
        raise ValueError("POTENCIA nao aceita resultado complexo nesta linguagem.")
    return resultado


def raiz(numero):
    """Calcula a raiz quadrada de um numero real nao negativo."""
    if not isinstance(numero, (int, float)) or isinstance(numero, bool):
        raise ValueError("RAIZ exige um numero real.")
    if numero < 0:
        raise ValueError("RAIZ nao aceita numeros negativos.")
    return math.sqrt(numero)


def _fmt(numero):
    if math.isclose(numero, round(numero), abs_tol=1e-12):
        return str(int(round(numero)))
    return f"{numero:.10g}"


def montar_etapas(a, b, c):
    """Retorna explicacoes do calculo e as raizes reais encontradas."""
    for nome, valor in (("a", a), ("b", b), ("c", c)):
        if not isinstance(valor, (int, float)) or isinstance(valor, bool):
            raise ValueError(f"O coeficiente '{nome}' deve ser numerico.")

    if a == 0:
        raise ValueError(
            "Nao e uma equacao do segundo grau: o coeficiente 'a' nao pode ser zero."
        )

    b2 = b ** 2
    quatro_ac = 4 * a * c
    delta = b2 - quatro_ac
    etapas = [
        f"Equacao: {a}x^2 + ({b})x + ({c}) = 0",
        "Etapa 1 - Formula do discriminante: delta = b^2 - 4*a*c. O delta mostra quantas raizes reais a equacao tem.",
        f"Etapa 2 - Substituicao: aqui a = {a}, b = {b} e c = {c}. Trocando na formula: delta = ({b})^2 - 4*({a})*({c})",
        f"Etapa 3 - Calculo: primeiro o quadrado e o produto, depois a subtracao: delta = {_fmt(b2)} - {_fmt(quatro_ac)} = {_fmt(delta)}",
    ]

    if delta < 0:
        etapas.append(
            "Etapa 4 - Como delta < 0, nao existe raiz quadrada real de numero negativo. "
            "A equacao nao possui raizes reais (a parabola nao toca o eixo x)."
        )
        return etapas, []

    raiz_delta = math.sqrt(delta)
    denominador = 2 * a
    numerador_mais = -b + raiz_delta
    numerador_menos = -b - raiz_delta
    x1 = numerador_mais / denominador
    x2 = numerador_menos / denominador
    
    if delta == 0:
        situacao = "Como delta = 0, as duas raizes sao iguais"
    else:
        situacao = "Como delta > 0, existem duas raizes reais diferentes"

    etapas.extend([
        f"Etapa 4 - Formula resolutiva: x = (-b +/- raiz(delta)) / (2*a). {situacao}: o sinal de + gera x1 e o sinal de - gera x2.",
        f"Etapa 5 - Substituicao de x1: usando o sinal +, x1 = (-({b}) + raiz({_fmt(delta)})) / (2*({a}))",
        f"Etapa 6 - Calculo de x1: x1 = ({_fmt(-b)} + {_fmt(raiz_delta)}) / {_fmt(denominador)} = {_fmt(x1)}",
        f"Etapa 7 - Substituicao de x2: usando o sinal -, x2 = (-({b}) - raiz({_fmt(delta)})) / (2*({a}))",
        f"Etapa 8 - Calculo de x2: x2 = ({_fmt(-b)} - {_fmt(raiz_delta)}) / {_fmt(denominador)} = {_fmt(x2)}",
    ])
    if delta == 0:
        etapas.append(f"Conclusao: raiz dupla x1 = x2 = {_fmt(x1)}. A parabola apenas encosta no eixo x.")
    else:
        etapas.append(f"Conclusao: x1 = {_fmt(x1)} e x2 = {_fmt(x2)}. Sao os pontos onde a parabola corta o eixo x.")
    return etapas, [x1, x2]


def bhaskara(a, b, c):
    """Resolve a equacao e exibe o desenvolvimento matematico."""
    etapas, raizes = montar_etapas(a, b, c)
    print("\nDesenvolvimento da equacao do segundo grau:")
    for etapa in etapas:
        print(etapa)
    return raizes


FUNCOES = {
    "POTENCIA": (2, potencia),
    "RAIZ": (1, raiz),
    "BHASKARA": (3, bhaskara),
}
