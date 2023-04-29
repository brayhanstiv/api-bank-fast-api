from fastapi import APIRouter
from app.models.debt_model import UpdateDebtSchema
from app.repository import repository

payment_routes = APIRouter(prefix='/payment', tags=['Payments'])

@payment_routes.post('/{debt_id}')
def pay_debt(debt_id: str, payment:UpdateDebtSchema):
  return repository.make_payment(debt_id,payment)

@payment_routes.get('/records/')
def get_payment_records():
  return repository.get_payment_records()