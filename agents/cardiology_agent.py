from services.gemini_service import ask_gemini


class CardiologyAgent:

    def analyze(
        self,
        symptoms
    ):

        prompt = f"""
        You are a cardiology specialist.

        Analyze these symptoms:

        {symptoms}

        Give possible cardiac observations.

        Educational use only.
        """

        return ask_gemini(prompt)
