from fastapi import FastAPI
from faker import Faker

app = FastAPI(title="Mock Server")
fake = Faker(locale="zh_CN")

@app.get("/api/user/info")
def user_info():
    return {
        "code": 0,
        "data": {
            "uid": fake.random_int(1000, 9999),
            "username": fake.user_name(),
            "phone": fake.phone_number()
        }
    }

@app.post("/api/order/create")
def create_order():
    return {"code": 0, "order_id": fake.uuid4()}