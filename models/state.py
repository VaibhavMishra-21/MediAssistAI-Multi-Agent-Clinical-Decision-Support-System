from typing import TypedDict


class MedicalState(TypedDict):

    patient_info: str

    symptoms: str

    cardiology_result: str

    pulmonology_result: str

    neurology_result: str

    psychology_result: str

    risk_level: str

    final_report: str
