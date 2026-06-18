from services.gemini_service import ask_gemini


class NeurologyAgent:

    def analyze(
        self,
        symptoms
    ):

        prompt = f"""
        You are a neurology specialist.

        Analyze:

        {symptoms}

        Educational use only.
        """

        return ask_gemini(prompt)
