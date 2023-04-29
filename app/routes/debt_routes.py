from fastapi import APIRouter
from app.repository import repository

debt_routes = APIRouter(prefix='/debt', tags=['Debts'])


@debt_routes.get('/')
def get_debts_by_vendor():
  return repository.get_debts()

@debt_routes.get('/{id}')
def get_debt_by_id(id:str):
  return repository.get_debt_by_id(id)