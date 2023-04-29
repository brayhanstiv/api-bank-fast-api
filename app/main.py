from fastapi import FastAPI
from app.routes.debt_routes import debt_routes
from app.routes.vendor_routes import vendor_routes
from app.routes.payment_routes import payment_routes

app = FastAPI()
app.include_router(debt_routes, prefix='/api')
app.include_router(vendor_routes, prefix='/api')
app.include_router(payment_routes, prefix='/api')

@app.get('/')
def initial_get():
  return "hola"