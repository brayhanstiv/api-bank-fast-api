from datetime import datetime
import uuid
from pydantic import BaseModel, Field
from decimal import Decimal

class PaymentHistorySchema(BaseModel):
    id:str = Field(default_factory=uuid.uuid4,alias="_id")
    value: Decimal = Field(...)
    debt_id: str =Field(...)
    date: datetime = Field(...)

    class Config:
        schema_extra = {
            "example":{
                "_id":"066de609-b04a-4b30-b46c-32537c7f1f6m",
                "value": 5000.4,
                "debt_id":"066de609-b04a-4b30-b46c-32537c7f1f6p",
                "date":datetime.now()
            }
        }