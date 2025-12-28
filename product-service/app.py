from datetime import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Product Service")

products_db = {
    1: {"id": 1, "name": "Laptop", "price": 1000},
    2: {"id": 2, "name": "Phone", "price": 500},
    3: {"id": 3, "name": "Tablet", "price": 300}
}

class Product(BaseModel):
    name: str
    price: float

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "product-service"}

@app.get("/api/products")
def get_products():
    return {"products": list(products_db.values()), "source": "product-microservice"}

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

@app.route('/health', methods=['GET'])
def health():
    try:
        # Check database connection
        from sqlalchemy import text
        db.session.execute(text('SELECT 1'))
        return jsonify({
            "status": "healthy",
            "service": "order-service",
            "database": "connected",
            "timestamp": datetime.now().isoformat()
        }), 200
    except Exception as e:
        return jsonify({
            "status": "unhealthy",
            "service": "order-service",
            "database": "disconnected",
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }), 503

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)