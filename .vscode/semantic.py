from ast_nodes import Number, Texto, BinOp, UnaryOp, Var, Assignment, FunctionCall

class ErroSemantico(Exception):
    pass

class Semantica:
    QUANTIDADE_ARGUMENTOS = {'POTENCIA': 2, 'RAIZ': 1, 'BHASKARA': 3}

    def __init__(self):
        self.variaveis = {}

    def analisar(self, node):
        if isinstance(node, Number):
            return 'numero'
        if isinstance(node, Texto):
            return 'texto'
        if isinstance(node, Var):
            if node.value not in self.variaveis:
                raise ErroSemantico(f"Erro semantico: variavel '{node.value}' nao declarada.")
            return self.variaveis[node.value]
        if isinstance(node, Assignment):
            nome = node.left.value
            tipo = self.analisar(node.value)
            if nome in self.variaveis and self.variaveis[nome] != tipo:
                raise ErroSemantico(f"Erro semantico: a variavel '{nome}' nao pode mudar de tipo.")
            self.variaveis[nome] = tipo
            return tipo
        if isinstance(node, UnaryOp):
            tipo = self.analisar(node.right)
            if tipo != 'numero':
                raise ErroSemantico('Erro semantico: o sinal unario exige um numero.')
            return 'numero'
        if isinstance(node, BinOp):
            esquerda = self.analisar(node.left)
            direita = self.analisar(node.right)
            if esquerda != 'numero' or direita != 'numero':
                raise ErroSemantico('Erro semantico: operadores aritmeticos exigem operandos numericos.')
            return 'numero'
        if isinstance(node, FunctionCall):
            nome = node.name.upper()
            if nome not in self.QUANTIDADE_ARGUMENTOS:
                raise ErroSemantico(f"Erro semantico: funcao '{node.name}' nao existe. Funcoes disponiveis: POTENCIA, RAIZ e BHASKARA.")
            esperada = self.QUANTIDADE_ARGUMENTOS[nome]
            recebida = len(node.args)
            if recebida != esperada:
                raise ErroSemantico(f"Erro: funcao '{node.name}' esperava {esperada} argumentos, mas recebeu {recebida}.")
            tipos = [self.analisar(argumento) for argumento in node.args]
            if any((tipo != 'numero' for tipo in tipos)):
                raise ErroSemantico(f"Erro semantico: funcao '{node.name}' exige argumentos numericos.")
            return 'solucao_equacao' if nome == 'BHASKARA' else 'numero'
        raise ErroSemantico(f'No semantico desconhecido: {type(node).__name__}.')
