from services.gemini_service import ask_gemini


class SupervisorAgent:

    def generate_final_report(
        self,
        cardiology,
        pulmonology,
        neurology,
        psychology,
        risk
    ):

        prompt = f"""
        You are a senior medical review specialist.

        Risk Level:
        {risk}

        Cardiology Findings:
        {cardiology}

        Pulmonology Findings:
        {pulmonology}

        Neurology Findings:
        {neurology}

        Psychology Findings:
        {psychology}

        Create a structured educational report:

        1. Summary
        2. Major Concerns
        3. Recommended Specialist
        4. Suggested Next Steps

        Educational use only.
        """

        return ask_gemini(prompt)
