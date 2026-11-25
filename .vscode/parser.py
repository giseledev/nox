from tokens import TipoToken
from ast_nodes import Number, BinOp, UnaryOp, FunctionCall, Var, Assignment, Texto

class ErroSintatico(Exception):
    pass

class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def _current(self):
        return self.tokens[self.pos]

    def _advance(self):
        token = self._current()
        if token.tipo != TipoToken.EOF:
            self.pos += 1
        return token

    def _expect(self, tipo):
        token = self._current()
        if token.tipo != tipo:
            raise ErroSintatico(f'Erro de sintaxe na posicao {token.posicao}: era esperado {tipo.name}, mas foi encontrado {token.tipo.name}.')
        return self._advance()

    def parse(self):
        node = self._parse_expression()
        self._expect(TipoToken.EOF)
        return node

    def parse_compare(self):
        node = self._parse_aritmetica()
        while self._current().tipo in (TipoToken.MAIOR, TipoToken.MENOR, TipoToken.MAIOR_IGUAL, TipoToken.MENOR_IGUAL, TipoToken.COMPARACAO):
            op = self._current()
            self._advance()
            right = self._parse_aritmetica()
            node = BinOp(node, op, right)
        return node

    def _parse_expression(self):
        if self._current().tipo == TipoToken.IDENTIFICADOR:
            nome = self._advance().valor
            if self._current().tipo == TipoToken.ATRIBUICAO:
                self._advance()
                var = self._parse_expression()
                node = Assignment(Var(nome), var)
                return node
            self.pos -= 1
        return self.parse_compare()

    def _parse_aritmetica(self):
        node = self._parse_term()
        while self._current().tipo in (TipoToken.SOMA, TipoToken.SUBTRACAO):
            op = self._advance()
            right = self._parse_term()
            node = BinOp(node, op, right)
        return node

    def _parse_term(self):
        node = self._parse_potencia()
        while self._current().tipo in (TipoToken.MULTIPLICACAO, TipoToken.DIVISAO):
            op = self._advance()
            right = self._parse_potencia()
            node = BinOp(node, op, right)
        return node

    def _parse_potencia(self):
        node = self._parse_factor()
        if self._current().tipo == TipoToken.POTENCIA:
            op = self._advance()
            if self._current().tipo == TipoToken.EOF:
                raise ErroSintatico(f'Erro de sintaxe na posicao {self._current().posicao}: potencia espera 2 operandos mas recebeu apenas 1')
            right = self._parse_potencia()
            return BinOp(node, op, right)
        return node

    def _parse_factor(self):
        token = self._current()
        if token.tipo == TipoToken.SUBTRACAO:
            op = self._advance()
            right = self._parse_factor()
            return UnaryOp(op, right)
        if token.tipo == TipoToken.NUMERO:
            self._advance()
            return Number(token.valor)
        if token.tipo == TipoToken.TEXTO:
            self._advance()
            return Texto(token.valor)
        if token.tipo == TipoToken.IDENTIFICADOR:
            nome = self._advance().valor
            if self._current().tipo == TipoToken.ABRE_PARENTESES:
                self._advance()
                args = []
                if self._current().tipo != TipoToken.FECHA_PARENTESES:
                    args.append(self._parse_expression())
                    while self._current().tipo == TipoToken.VIRGULA:
                        self._advance()
                        args.append(self._parse_expression())
                self._expect(TipoToken.FECHA_PARENTESES)
                return FunctionCall(nome, args)
            return Var(nome)
        if token.tipo == TipoToken.ABRE_PARENTESES:
            self._advance()
            node = self._parse_expression()
            self._expect(TipoToken.FECHA_PARENTESES)
            return node
        raise ErroSintatico(f'Erro de sintaxe na posicao {token.posicao}: token inesperado: {token.tipo.name}.')
