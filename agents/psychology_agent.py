from services.gemini_service import ask_gemini


class PsychologyAgent:

    def analyze(self, symptoms):

        prompt = f"""
        You are a psychology specialist.

        Analyze the following symptoms:

        {symptoms}

        Identify possible psychological or behavioral factors.

        Educational use only.
        """

        return ask_gemini(prompt)
