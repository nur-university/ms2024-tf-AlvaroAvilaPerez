from pydantic import BaseModel

from domain.enums.plan import Plan


class ClientCreateModel(BaseModel):
    first_name: str
    last_name: str
    address: str
    plan: Plan
    age: int
    size: str
    weight: str