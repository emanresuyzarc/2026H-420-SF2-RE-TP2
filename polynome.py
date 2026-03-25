from expression import Expression


class Polynome(Expression):
    """Polynome represente par une liste de coefficients [a0, a1, a2, ...]."""

    # Votre code ici (remplacer le "pass" par votre implementation)
    def __init__(self, liste_coef):
        self.liste_coef = liste_coef


    def evaluer(self, x: float) -> float:
        """Retourne la valeur numerique de l'expression pour x."""


    def deriver(self) -> "Expression":
        expr_derivee = []
        i = 0
        for element in self.liste_coef:
            expr_derivee.append(element*i)
            i += 1

        return Polynome(expr_derivee)


    def __str__(self) -> str:
        expr_lisible = []
        i = 0

        for element in self.liste_coef:
            if i == 0:
                terme = element

            elif i == 1:
                terme = f"{element}x"

            else:
                terme = f"{element}x^{i}"

        expr_lisible.append(terme)

        return " + ".join(expr_lisible)
                