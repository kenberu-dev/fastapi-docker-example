from fastapi import FastAPI, Depends
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username: str
    is_active: bool = True
    
users = [
    User(username="山田", is_active=True),
    User(username="鈴木", is_active=False),
    User(username="高橋", is_active=True)
]

def get_active_users():
    active_users = [user for user in users if user.is_active]
    print("=== アクティブなユーザーを取得 ===")
    return active_users

@app.get("/active")
async def list_active_users(active_users: list[User] = Depends(get_active_users)):
    print("=== 【依存】してデータを取得 ===")
    return active_users