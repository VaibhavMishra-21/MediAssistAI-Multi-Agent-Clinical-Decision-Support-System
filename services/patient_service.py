class PatientService:

    @staticmethod
    def build_patient_context(
        name,
        age,
        gender,
        symptoms
    ):

        return f"""
        Patient Name: {name}

        Age: {age}

        Gender: {gender}

        Symptoms: {symptoms}
        """
