from lexer import Lexer
from parser import Parser
from interpreter import Interpreter
from semantic import Semantica
from tac import TAC
from ast_nodes import Number, BinOp, UnaryOp, FunctionCall, Var, Assignment, Texto

def formatar_ast(node, nivel=0):
    espaco = '    ' * nivel
    if isinstance(node, Number):
        return f'Number({node.value})'
    if isinstance(node, Texto):
        return f'Texto("{node.value}")'
    if isinstance(node, Var):
        return f'Var({node.value})'
    if isinstance(node, BinOp):
        return f"BinOp(\n{espaco}    left={formatar_ast(node.left, nivel + 1)},\n{espaco}    op='{node.op.valor}',\n{espaco}    right={formatar_ast(node.right, nivel + 1)}\n{espaco})"
    if isinstance(node, UnaryOp):
        return f"UnaryOp(\n{espaco}    op='{node.op.valor}',\n{espaco}    right={formatar_ast(node.right, nivel + 1)}\n{espaco})"
    if isinstance(node, Assignment):
        return f'Assignment(\n{espaco}    left={formatar_ast(node.left, nivel + 1)},\n{espaco}    value={formatar_ast(node.value, nivel + 1)}\n{espaco})'
    if isinstance(node, FunctionCall):
        args = ', '.join((formatar_ast(arg, nivel + 1) for arg in node.args))
        return f"FunctionCall(\n{espaco}    name='{node.name}',\n{espaco}    args=[{args}]\n{espaco})"
    return f'<No desconhecido: {type(node).__name__}>'

def analisar_estrutura(codigo, semantico=None):
    semantico = semantico or Semantica()
    tokens = Lexer(codigo).tokenizar()
    arvore = Parser(tokens).parse()
    semantico.analisar(arvore)
    gerador = TAC()
    gerador.gerar(arvore)
    return (tokens, arvore, gerador.codigo)

def formatar_resultado(resultado):
    if isinstance(resultado, list):
        if not resultado:
            return 'Nao existem raizes reais.'
        if len(resultado) == 2:
            return f'x1 = {resultado[0]:.10g}; x2 = {resultado[1]:.10g}'
    return str(resultado)

def processar(linha, semantico, interpretador):
    tokens, arvore, codigo_tac = analisar_estrutura(linha, semantico)
    print('\nEtapa 1 - Simbolos reconhecidos:')
    print(' | '.join((f'{token.tipo.name}({token.valor})' for token in tokens)))
    print('\nEtapa 2 - Arvore da expressao:')
    print(formatar_ast(arvore))
    print('\nEtapa 3 - Verificacao da expressao:')
    print('Variaveis, tipos e argumentos estao corretos.')
    print('\nEtapa 4 - Passos intermediarios do calculo:')
    print('\n'.join(codigo_tac) if codigo_tac else '(nenhuma instrucao)')
    print('\nEtapa 5 - Resolucao:')
    resultado = interpretador.avaliar(arvore)
    print('\nResposta:')
    print(formatar_resultado(resultado))
    print()
    return resultado

def analisar_codigo(codigo, semantico=None, interpretador=None):
    semantico = semantico or Semantica()
    interpretador = interpretador or Interpreter()
    _, arvore, tac = analisar_estrutura(codigo, semantico)
    resultado = interpretador.avaliar(arvore)
    return (resultado, arvore, tac)

def executar(codigo, semantico=None, interpretador=None):
    resultado, _, _ = analisar_codigo(codigo, semantico, interpretador)
    return resultado

def repl():
    print('NOX - linguagem matematica para equacoes do segundo grau')
    print("Digite 'sair' para encerrar.\n")
    semantico = Semantica()
    interpretador = Interpreter()
    while True:
        codigo = input('>>> ').strip()
        if codigo.lower() in ('sair', 'exit'):
            print('Programa encerrado.')
            break
        if not codigo:
            continue
        try:
            processar(codigo, semantico, interpretador)
        except Exception as erro:
            print(f'{erro}\n')
if __name__ == '__main__':
    repl()
