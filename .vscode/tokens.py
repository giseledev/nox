from enum import Enum, auto
from dataclasses import dataclass

class TipoToken(Enum):
    NUMERO = auto()
    IDENTIFICADOR = auto()
    TEXTO = auto()
    SOMA = auto()
    SUBTRACAO = auto()
    MULTIPLICACAO = auto()
    DIVISAO = auto()
    POTENCIA = auto()
    ABRE_PARENTESES = auto()
    FECHA_PARENTESES = auto()
    VIRGULA = auto()
    EOF = auto()
    ATRIBUICAO = auto()
    MAIOR = auto()
    MENOR = auto()
    MAIOR_IGUAL = auto()
    MENOR_IGUAL = auto()
    COMPARACAO = auto()

@dataclass
class Token:
    tipo: TipoToken
    valor: object = None
    posicao: int = 0
