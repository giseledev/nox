from tokens import TipoToken
from ast_nodes import Number, BinOp, UnaryOp, FunctionCall, Var, Assignment, Texto
from funcoes import FUNCOES

class ErroExecucao(Exception):
    pass

class Interpreter:

    def __init__(self):
        self.memoria = {}

    def avaliar(self, node):
        if isinstance(node, Number):
            return node.value
        if isinstance(node, Texto):
            return node.value
        if isinstance(node, Var):
            if node.value not in self.memoria:
                raise ErroExecucao(f"Erro: variavel '{node.value}' nao foi definida.")
            return self.memoria[node.value]
        if isinstance(node, Assignment):
            valor = self.avaliar(node.value)
            self.memoria[node.left.value] = valor
            return valor
        if isinstance(node, UnaryOp):
            valor = self.avaliar(node.right)
            if node.op.tipo == TipoToken.SUBTRACAO:
                return -valor
            raise ErroExecucao('Erro: operador unario desconhecido.')
        if isinstance(node, BinOp):
            esquerda = self.avaliar(node.left)
            direita = self.avaliar(node.right)
            if node.op.tipo == TipoToken.SOMA:
                return esquerda + direita
            if node.op.tipo == TipoToken.SUBTRACAO:
                return esquerda - direita
            if node.op.tipo == TipoToken.MULTIPLICACAO:
                return esquerda * direita
            if node.op.tipo == TipoToken.DIVISAO:
                if direita == 0:
                    raise ErroExecucao('Erro: divisao por zero nao e permitida.')
                return esquerda / direita
            if node.op.tipo == TipoToken.POTENCIA:
                return esquerda ** direita
            if node.op.tipo == TipoToken.MAIOR:
                return esquerda > direita
            if node.op.tipo == TipoToken.MENOR:
                return esquerda < direita
            if node.op.tipo == TipoToken.MAIOR_IGUAL:
                return esquerda >= direita
            if node.op.tipo == TipoToken.MENOR_IGUAL:
                return esquerda <= direita
            if node.op.tipo == TipoToken.COMPARACAO:
                return esquerda == direita
            raise ErroExecucao('Erro: operador binario desconhecido.')
        if isinstance(node, FunctionCall):
            nome = node.name.upper()
            if nome not in FUNCOES:
                raise ErroExecucao(f"Erro: funcao '{node.name}' nao existe.")
            quantidade, funcao = FUNCOES[nome]
            argumentos = [self.avaliar(argumento) for argumento in node.args]
            recebida = len(argumentos)
            if quantidade is not None and recebida != quantidade:
                raise ErroExecucao(f"Erro: funcao '{node.name}' esperava {quantidade} argumentos, mas recebeu {recebida}.")
            try:
                return funcao(*argumentos)
            except (ValueError, TypeError) as erro:
                raise ErroExecucao(str(erro)) from erro
        raise ErroExecucao(f'Erro: no desconhecido {type(node).__name__}.')
