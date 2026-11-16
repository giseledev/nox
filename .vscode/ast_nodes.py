from dataclasses import dataclass

class ASTNode:
    pass

@dataclass
class Number(ASTNode):
    value: object

@dataclass
class BinOp(ASTNode):
    left: ASTNode
    op: object
    right: ASTNode

@dataclass
class UnaryOp(ASTNode):
    op: object
    right: ASTNode

@dataclass
class FunctionCall(ASTNode):
    name: str
    args: list

@dataclass
class Var(ASTNode):
    value: object

@dataclass
class Assignment(ASTNode):
    left: Var
    value: ASTNode

@dataclass
class Texto(ASTNode):
    value: str
