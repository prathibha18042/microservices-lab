from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="E-Commerce Monolith")

# In-memory databases
users_db = {
    1: {"id": 1, "username": "john", "email": "john@example.com"},
    2: {"id": 2, "username": "jane", "email": "jane@example.com"}
}

products_db = {
    1: {"id": 1, "name": "Laptop", "price": 1000},
    2: {"id": 2, "name": "Phone", "price": 500},
    3: {"id": 3, "name": "Tablet", "price": 300}
}

orders_db = {}
order_counter = 1

# Models
class User(BaseModel):
    username: str
    email: str

class Product(BaseModel):
    name: str
    price: float

class Order(BaseModel):
    user_id: int
    product_ids: List[int]

# USER ENDPOINTS
@app.get("/")
def root():
    return {"message": "E-Commerce Monolith", "status": "running"}

@app.get("/api/users")
def get_users():
    return {"users": list(users_db.values())}

@app.get("/api/users/{user_id}")
def get_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]

@app.post("/api/users")
def create_user(user: User):
    user_id = max(users_db.keys()) + 1
    new_user = {"id": user_id, "username": user.username, "email": user.email}
    users_db[user_id] = new_user
    return new_user

# PRODUCT ENDPOINTS
@app.get("/api/products")
def get_products():
    return {"products": list(products_db.values())}

@app.get("/api/products/{product_id}")
def get_product(product_id: int):
    if product_id not in products_db:
        raise HTTPException(status_code=404, detail="Product not found")
    return products_db[product_id]

@app.post("/api/products")
def create_product(product: Product):
    product_id = max(products_db.keys()) + 1
    new_product = {"id": product_id, "name": product.name, "price": product.price}
    products_db[product_id] = new_product
    return new_product

# ORDER ENDPOINTS
@app.post("/api/orders")
def create_order(order: Order):
    global order_counter
    
    if order.user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    total = 0
    products = []
    for pid in order.product_ids:
        if pid not in products_db:
            raise HTTPException(status_code=404, detail=f"Product {pid} not found")
        products.append(products_db[pid])
        total += products_db[pid]["price"]
    
    new_order = {
        "order_id": order_counter,
        "user": users_db[order.user_id],
        "products": products,
        "total": total
    }
    orders_db[order_counter] = new_order
    order_counter += 1
    
    return new_order

@app.get("/api/orders")
def get_orders():
    return {"orders": list(orders_db.values())}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
