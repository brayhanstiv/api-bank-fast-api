from app.config.db_connection import vendor_collection,debt_collection, payment_history_collection
from app.models.vendor_model import VendorSchema, VendorDetail
from app.models.debt_model import DebtSchema, DebtDetail, UpdateDebtSchema
from app.models.payment_history import PaymentHistorySchema
from decimal import Decimal
from bson.decimal128 import Decimal128
from fastapi.encoders import jsonable_encoder
from datetime import datetime

def get_vendors():
    vendors = []
    cursor = vendor_collection.find()
    for document in cursor:
        vendors.append(VendorSchema(**document))
    return vendors

def get_vendor_by_id(id:str):
    document = vendor_collection.find_one(id)
    if document is not None:
        return VendorDetail(**document)
    return None

def get_debts():
    debts = []
    cursor = debt_collection.find()
    for document in cursor:
        debts.append(DebtSchema(**document))
    return debts

def get_debt_by_id(id:str):
    document = debt_collection.find_one(id)
    if document is not None:
        return DebtDetail(**document)
    return None

def make_payment(debt_id:str, value:UpdateDebtSchema):
    debt: DebtSchema = DebtSchema(**debt_collection.find_one(debt_id))
    if debt is None: return None
    current_value = debt.value
    if value.value > current_value:
        raise Exception("Debes menos de lo que vas a pagar")
    update_result = debt_collection.update_one({"_id":debt_id},{"$set": {
        "value":Decimal128(str(current_value-value.value))
    }})
    if update_result.modified_count == 0:
        raise Exception("Usuario no encontrado")
    debt_detail = DebtDetail(**debt_collection.find_one(debt_id))
    new_record = PaymentHistorySchema(value=debt.value,debt_id=debt.id,date=datetime.now())
    create_payment_record(new_record)
    return debt_detail

def get_payment_records():
    records = []
    cursor = payment_history_collection.find()
    for document in cursor:
        records.append(PaymentHistorySchema(**document))
    return records

def create_payment_record(payment_record:PaymentHistorySchema):
    record = jsonable_encoder(payment_record)
    print(payment_record)
    new_record = payment_history_collection.insert_one(record)
    return PaymentHistorySchema(**payment_history_collection.find_one(new_record.inserted_id))
