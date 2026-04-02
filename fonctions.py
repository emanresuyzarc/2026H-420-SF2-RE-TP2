from expression import Expression
from operations import Multiplication
from polynome import Polynome
import math


class Sin(Expression):

    def __init__(self, u: Expression):
        self.u = u

    def evaluer(self, x: float) -> float:
        return math.sin(self.u.evaluer(x))

    def deriver(self) -> Expression:
        return Multiplication(Cos(self.u), self.u.deriver())

    def __str__(self) -> str:
        return f"sin({self.u})"


class Cos(Expression):

    def __init__(self, u: Expression):
        self.u = u

    def evaluer(self, x: float) -> float:
        return math.cos(self.u.evaluer(x))

    def deriver(self) -> Expression:
        return Multiplication(Multiplication(Polynome([-1]), Sin(self.u)), self.u.deriver())

    def __str__(self) -> str:
        return f"cos({self.u})"


class Exp(Expression):

    def __init__(self, u: Expression):
        self.u = u

    def evaluer(self, x: float) -> float:
        return math.exp(self.u.evaluer(x))

    def deriver(self) -> "Expression":
        return Multiplication(Exp(self.u), self.u.deriver())

    def __str__(self) -> str:
        return f"e^({self.u})"
