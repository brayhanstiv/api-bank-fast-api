import uuid
from pydantic import BaseModel, Field
from app.models.debt_model import DebtSchema
from decimal import Decimal

class VendorSchema(BaseModel):
  id:str = Field(default_factory=uuid.uuid4,alias="_id")
  name: str = Field(...)

  class Config:
    schema_extra = {
      "example":{
        "_id":"066de609-b04a-4b30-b46c-32537c7f1f6e",
        "name":"Test",
      }
    }

class VendorDetail(BaseModel):
  code: str = Field(...)
  name: str = Field(...)
  debts: list[str] = Field(...)

  class Config:
    schema_extra = {
      "example":{
        "code":"ZXC123",
        "name":"Test",
        "current_debt":50000.40,
        "debts": [
            "066de609-b04a-4b30-b46c-32537c7f1f6y",
        ]
      }
    }