from datetime import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="User Service")

users_db = {
    1: {"id": 1, "username": "john", "email": "john@example.com"},
    2: {"id": 2, "username": "jane", "email": "jane@example.com"}
}

class User(BaseModel):
    username: str
    email: str

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "user-service"}

@app.get("/api/users")
def get_users():
    return {"users": list(users_db.values()), "source": "user-microservice"}

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

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "healthy",
        "service": "user-service",
        "timestamp": datetime.now().isoformat()
    }), 200

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)