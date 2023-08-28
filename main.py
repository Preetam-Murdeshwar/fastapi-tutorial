from fastapi import FastAPI
from pydantic import BaseModel
# from typing import Optional


app = FastAPI()


@app.get("/")
async def root():
    return {"Message": "Hello World"}


@app.post("/")
async def post():
    return {"Message": "I am post method"}


@app.put("/")
async def put():
    return {"Message": "I am put method"}


@app.get("/users")
async def get_all_user():
    return {"Message": "All Users List"}


@app.get("/users/me")
async def get_current_user():
    return {"Message": "I am Current User"}


# path parameters example
@app.get("/users/{user_id}")
async def get_user(user_id: str):
    return {"User ID": user_id}


# # query parameters example
# @app.get("/tiems")
# async def get_item_list(skip: int=0, limit: int=10):
#     return {"Skip": skip, "Limit": limit}
 

# @app.get("/items/{item_id}")
# async def get_item(item_id: str, q: str | None = None): # | None = None makes parameters optional works python > 3.10
#     if q:
#         return {"Item ID:": item_id, "q": q}
#     return {"Item ID:": item_id}


# request body
class Item(BaseModel):
    name: str
    description: str | None = None  # Optional[str] = None - Used if python < 3.10. This makes the parameter optional
    price: float
    tax: float | None = None # Makes the parameter optional


@app.post("/items")
async def create_item(item: Item):
    return item
 

