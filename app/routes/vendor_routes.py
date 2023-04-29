from typing import List
from fastapi import APIRouter
from app.repository import repository

vendor_routes = APIRouter(prefix='/vendor', tags=['Vendors'])


@vendor_routes.get('/')
def get_all_vendors():
  vendors: List = repository.get_vendors()
  return vendors

@vendor_routes.get('/{id}')
def get_vendor_by_id(id:str):
  vendor = repository.get_vendor_by_id(id)
  return vendor