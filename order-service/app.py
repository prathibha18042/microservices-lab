from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os
import uvicorn

# Database setup
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://orderuser:orderpass@order-db:5432/orders')
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Database model
class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    product_id = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    total_price = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

# Create tables
Base.metadata.create_all(bind=engine)

# FastAPI app - MUST BE DEFINED BEFORE ROUTES
app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic model for request
class OrderCreate(BaseModel):
    user_id: int
    product_id: int
    quantity: int
    total_price: float

# Routes

@app.get("/health")
def health():
    try:
        # Test database connection with proper text() wrapper
        db = SessionLocal()
        db.execute(text("SELECT 1"))
        db.close()
        return {
            "status": "healthy",
            "service": "order-service",
            "database": "connected",
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        return {
            "status": "unhealthy",
            "service": "order-service",
            "database": "disconnected",
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }

@app.get("/api/orders")
def get_orders():
    db = SessionLocal()
    try:
        orders = db.query(Order).all()
        return [
            {
                "id": o.id,
                "user_id": o.user_id,
                "product_id": o.product_id,
                "quantity": o.quantity,
                "total_price": o.total_price,
                "created_at": o.created_at.isoformat()
            }
            for o in orders
        ]
    finally:
        db.close()

@app.post("/api/orders")
def create_order(order: OrderCreate):
    db = SessionLocal()
    try:
        new_order = Order(**order.dict())
        db.add(new_order)
        db.commit()
        db.refresh(new_order)
        return {
            "id": new_order.id,
            "user_id": new_order.user_id,
            "product_id": new_order.product_id,
            "quantity": new_order.quantity,
            "total_price": new_order.total_price,
            "created_at": new_order.created_at.isoformat()
        }
    finally:
        db.close()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8003)