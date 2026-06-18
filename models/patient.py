from pydantic import BaseModel


class Patient(BaseModel):

    name: str

    age: int

    gender: str

    symptoms: str
