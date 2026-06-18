from pydantic import BaseModel


class Diagnosis(BaseModel):

    condition: str

    confidence: float

    recommendation: str
