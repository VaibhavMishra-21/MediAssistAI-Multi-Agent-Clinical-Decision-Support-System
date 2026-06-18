class RiskAgent:

    def evaluate(
        self,
        symptoms
    ):

        symptoms = symptoms.lower()

        score = 0

        if "chest pain" in symptoms:
            score += 5

        if "shortness of breath" in symptoms:
            score += 5

        if "dizziness" in symptoms:
            score += 3

        if "fever" in symptoms:
            score += 2

        if score >= 8:
            return "HIGH"

        elif score >= 4:
            return "MEDIUM"

        return "LOW"
