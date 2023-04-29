
from decimal import Decimal
import uuid
from pydantic import BaseModel, Field
from typing import Optional

class DebtSchema(BaseModel):
  id:str = Field(default_factory=uuid.uuid4,alias="_id")
  value: Decimal = Field(...)
  

  class Config:
    schema_extra ={
      "example":{
        "_id":"066de609-b04a-4b30-b46c-32537c7f1f6y",
        "value": 5000.4,
        
      }
    }

class UpdateDebtSchema(BaseModel):
  value: Optional[Decimal]

  class Config:
    schema_extra ={
      "example":{
        "value":50000.4
      }
    }

class DebtDetail(BaseModel):
  vendor_id: str = Field(...)
  value: Decimal = Field(...)

  class Config:
    schema_extra ={
      "example":{
        "vendor_id":"066de609-b04a-4b30-b46c-32537c7f2f6y",
        "value": 5000.4
      }
    }