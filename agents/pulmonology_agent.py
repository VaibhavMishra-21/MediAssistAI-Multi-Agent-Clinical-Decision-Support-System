from services.gemini_service import ask_gemini


class PulmonologyAgent:

    def analyze(
        self,
        symptoms
    ):

        prompt = f"""
        You are a pulmonology specialist.

        Analyze:

        {symptoms}

        Educational use only.
        """

        return ask_gemini(prompt)
