from expression import Expression

class Polynome(Expression):
    """Polynome represente par une liste de coefficients [a0, a1, a2, ...]."""

    # Votre code ici (remplacer le "pass" par votre implementation)
    def __init__(self, liste_coef):
        self.liste_coef = liste_coef


    def evaluer(self, x: float) -> float:
        valeur_numerique = 0

        for i, element in enumerate(self.liste_coef):
            valeur_numerique += element*(x**i)

        return valeur_numerique


    def deriver(self) -> "Expression":
        expr_derivee = []

        for i, element in enumerate(self.liste_coef):
            if i > 0:
                expr_derivee.append(element*i)

        return Polynome(expr_derivee)


    def __str__(self) -> str:
        expr_lisible = ""
        premier = True

        for i, element in enumerate(self.liste_coef):
            if element == 0:
                continue

            element_valeur_absolue = abs(element)

            # Construction du terme
            if i == 0:
                terme = f"{element_valeur_absolue}"
            elif i == 1:
                if element_valeur_absolue == 1:
                    terme = "x" 
                else:
                    terme = f"{element_valeur_absolue}x"
            else:
                if element_valeur_absolue == 1:
                    terme = f"x^{i}"
                else:
                    terme = f"{element_valeur_absolue}x^{i}"


            if premier:
                if element < 0:
                    expr_lisible += f"-{terme}"
                else:
                    expr_lisible += f"{terme}"
                premier = False

            else:
                if element < 0:
                    expr_lisible += f" - {terme}"
                else:
                    expr_lisible += f" + {terme}"

        return expr_lisible