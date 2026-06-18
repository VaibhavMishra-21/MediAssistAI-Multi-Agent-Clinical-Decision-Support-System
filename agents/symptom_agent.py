class SymptomAgent:

    def analyze(
        self,
        symptoms
    ):

        symptoms = symptoms.lower()

        findings = []

        if "fever" in symptoms:
            findings.append(
                "Possible infection"
            )

        if "cough" in symptoms:
            findings.append(
                "Respiratory concern"
            )

        if "chest pain" in symptoms:
            findings.append(
                "Cardiac evaluation advised"
            )

        if "headache" in symptoms:
            findings.append(
                "Neurological evaluation advised"
            )

        return findings
