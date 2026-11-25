from ast_nodes import Number, Texto, BinOp, UnaryOp, Var, Assignment, FunctionCall

class TAC:

    def __init__(self):
        self.codigo = []
        self.contador = 0

    def temporario(self):
        self.contador += 1
        return f't{self.contador}'

    def gerar(self, node):
        if isinstance(node, Number):
            return str(node.value)
        if isinstance(node, Texto):
            return f'"{node.value}"'
        if isinstance(node, Var):
            return node.value
        if isinstance(node, Assignment):
            valor = self.gerar(node.value)
            self.codigo.append(f'{node.left.value} = {valor}')
            return node.left.value
        if isinstance(node, UnaryOp):
            valor = self.gerar(node.right)
            temporario = self.temporario()
            self.codigo.append(f'{temporario} = {node.op.valor}{valor}')
            return temporario
        if isinstance(node, BinOp):
            esquerda = self.gerar(node.left)
            direita = self.gerar(node.right)
            temporario = self.temporario()
            self.codigo.append(f'{temporario} = {esquerda} {node.op.valor} {direita}')
            return temporario
        if isinstance(node, FunctionCall):
            argumentos = [self.gerar(argumento) for argumento in node.args]
            temporario = self.temporario()
            self.codigo.append(f"{temporario} = {node.name}({', '.join(argumentos)})")
            return temporario
