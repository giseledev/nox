NOX - LINGUAGEM MATEMATICA PARA EQUACOES DO SEGUNDO GRAU

OBJETIVO
A NOX e focada em operacoes aritmeticas e na resolucao explicada de equacoes do segundo grau.

FUNCOES DISPONIVEIS

POTENCIA(base, expoente)
Calcula uma potencia. Exemplo: POTENCIA(3, 2) -> 9.

RAIZ(numero)
Calcula a raiz quadrada real. O argumento deve ser nao negativo.
Exemplo: RAIZ(25) -> 5.

BHASKARA(a, b, c)
Resolve a equacao ax^2 + bx + c = 0, apresenta as etapas do calculo do delta e das raizes e retorna os dois resultados reais.
O coeficiente a nao pode ser zero.
Se delta for negativo, a NOX informa que nao existem raizes reais.

Exemplo:
BHASKARA(1, -3, 2)

Resultado matematico:
x1 = 2; x2 = 1

A funcao tambem trata:
- delta igual a zero: apresenta a raiz dupla;
- delta menor que zero: informa que nao ha raizes reais;
- a igual a zero: gera erro controlado, pois a expressao deixa de ser de segundo grau.

OPERADORES
+ soma
- subtracao e sinal negativo
* multiplicacao
/ divisao
** potencia
( ) agrupamento
= atribuicao

A divisao por zero e identificada pela linguagem antes da operacao. A NOX mostra um erro proprio, em vez da excecao ZeroDivisionError do Python.

ETAPAS MOSTRADAS NA EXECUCAO
Ao executar uma expressao, a NOX apresenta:
1. Tokens reconhecidos;
2. Arvore Sintatica Abstrata (AST);
3. Resultado da analise semantica;
4. Codigo intermediario TAC;
5. Execucao e, em BHASKARA, o desenvolvimento matematico passo a passo;
6. Resultado final.

Exemplo de chamada:
BHASKARA(1, -3, 2)

A funcao explica a substituicao de a, b e c no discriminante, calcula delta, verifica a existencia de raizes reais, substitui os valores na formula resolutiva e apresenta x1 e x2.

ARQUIVOS
 tokens.py       Tipos de tokens.
 ast_nodes.py    Nos da AST.
 lexer.py        Analise lexica.
 parser.py       Analise sintatica e precedencia.
 semantic.py     Validacao de variaveis, tipos e chamadas.
 funcoes.py      POTENCIA, RAIZ e BHASKARA.
 interpreter.py  Execucao da AST.
 tac.py          Geracao de codigo intermediario.
 main.py         Interface interativa e exibicao das etapas.
 tests.py        Testes da linguagem.

COMO EXECUTAR
No terminal, dentro da pasta do projeto:
  python main.py

Para sair do modo interativo, digite sair ou exit.

NOTA SOBRE TOKENS
Os tokens aritmeticos ja existentes (+, -, *, /, **, parenteses e atribuicao) sao suficientes para o foco matematico. Os tokens de comparacao permanecem por compatibilidade com o parser; nao impedem o uso especializado da linguagem.


APRESENTACAO DA RESOLUCAO

A funcao BHASKARA mostra a conta em portugues, usando o nome "raiz quadrada" por extenso junto do simbolo matematico. A explicacao foi resumida para mostrar somente a formula, a substituicao dos coeficientes, o valor do discriminante e as raizes.

Exemplo de apresentacao:

Resolucao da equacao:
Equacao: 1x² + (-3)x + (2) = 0
Discriminante: Δ = b² - 4ac
Substituindo: Δ = (-3)² - 4 × (1) × (2)
Calculando: Δ = 9 - 8 = 1
Formula resolutiva: x = (-b ± √Δ) / (2a)
Raiz quadrada do discriminante: √Δ = √1 = 1
Primeira raiz: x₁ = (3 + 1) / 2 = 2
Segunda raiz: x₂ = (3 - 1) / 2 = 1
Resultado: x₁ = 2 e x₂ = 1.


FATORIAL(numero)

Calcula o fatorial de um numero inteiro nao negativo e mostra o
desenvolvimento da multiplicacao.

Exemplo:

FATORIAL(5)

Desenvolvimento:

5! = 5 × 4 × 3 × 2 × 1 = 120

Resultado:

120

O fatorial de zero e definido como 1:

FATORIAL(0) -> 1