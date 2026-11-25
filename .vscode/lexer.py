from tokens import TipoToken, Token

class ErroLexico(Exception):
    pass
PALAVRAS_RESERVADAS = {}

class Lexer:

    def __init__(self, codigo):
        self.codigo = codigo
        self.pos = 0

    def _atual(self):
        if self.pos >= len(self.codigo):
            return '\x00'
        return self.codigo[self.pos]

    def _avancar(self):
        caractere = self._atual()
        self.pos += 1
        return caractere

    def _ler_numero(self):
        inicio = self.pos
        pontos = 0
        while self._atual().isdigit() or self._atual() == '.':
            if self._atual() == '.':
                pontos += 1
            if pontos > 1:
                raise ErroLexico(f'Numero invalido na posicao {self.pos}.')
            self._avancar()
        texto = self.codigo[inicio:self.pos]
        if '.' in texto:
            valor = float(texto)
        else:
            valor = int(texto)
        return Token(TipoToken.NUMERO, valor, inicio)

    def _ler_texto(self):
        inicio = self.pos
        self._avancar()
        inicio_texto = self.pos
        while self._atual() not in ('"', '\x00'):
            self._avancar()
        if self._atual() == '\x00':
            raise ErroLexico(f'Erro lexico na posicao {inicio}: texto sem aspas de fechamento.')
        texto = self.codigo[inicio_texto:self.pos]
        self._avancar()
        return Token(TipoToken.TEXTO, texto, inicio)

    def _ler_identificador(self):
        inicio = self.pos
        while self._atual().isalnum() or self._atual() == '_':
            self._avancar()
        texto = self.codigo[inicio:self.pos]
        tipo = PALAVRAS_RESERVADAS.get(texto)
        if tipo is not None:
            return Token(tipo, texto, inicio)
        return Token(TipoToken.IDENTIFICADOR, texto, inicio)

    def tokenizar(self):
        tokens = []
        operadores = {'+': TipoToken.SOMA, '-': TipoToken.SUBTRACAO, '*': TipoToken.MULTIPLICACAO, '/': TipoToken.DIVISAO, '(': TipoToken.ABRE_PARENTESES, ')': TipoToken.FECHA_PARENTESES, ',': TipoToken.VIRGULA, '=': TipoToken.ATRIBUICAO, '>': TipoToken.MAIOR, '<': TipoToken.MENOR}
        while self.pos < len(self.codigo):
            caractere = self._atual()
            if caractere.isspace():
                self._avancar()
                continue
            if caractere.isdigit():
                tokens.append(self._ler_numero())
                continue
            if caractere == '"':
                tokens.append(self._ler_texto())
                continue
            if caractere.isalpha() or caractere == '_':
                tokens.append(self._ler_identificador())
                continue
            inicio = self.pos
            dois = self.codigo[self.pos:self.pos + 2]
            if dois == '**':
                tokens.append(Token(TipoToken.POTENCIA, '**', inicio))
                self.pos += 2
                continue
            if dois == '>=':
                tokens.append(Token(TipoToken.MAIOR_IGUAL, '>=', inicio))
                self.pos += 2
                continue
            if dois == '<=':
                tokens.append(Token(TipoToken.MENOR_IGUAL, '<=', inicio))
                self.pos += 2
                continue
            if dois == '==':
                tokens.append(Token(TipoToken.COMPARACAO, '==', inicio))
                self.pos += 2
                continue
            if caractere in operadores:
                tokens.append(Token(operadores[caractere], caractere, inicio))
                self._avancar()
                continue
            raise ErroLexico(f"Erro lexico na posicao {self.pos}: simbolo '{caractere}' nao reconhecido.")
        tokens.append(Token(TipoToken.EOF, None, self.pos))
        return tokens
