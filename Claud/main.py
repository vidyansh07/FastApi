# from fastapi import FastAPI 
# from pydantic import BaseModel
# app = FastAPI()

# class UserIn(BaseModel):
#     id : str
#     name : str
#     email : str
#     age : int | None=  None
    
# class UserOut(BaseModel):
#     name : str
#     email : str

# @app.post("/user/", response_model=UserOut)
# async def create_user(user: UserIn):
#     return user




"""Data Validation and Type Hints"""

from fastapi import FastAPI, Query, Path
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    name: str = Field(..., min_length=1, max_length=50)
    price: float = Field(..., gt=0)
    description: str | None = Field(None, max_length=1000)

@app.get("/items/{item_id}")
async def read_item(
    item_id: int = Path(..., ge=1),
    q: str | None = Query(None, min_length=3, max_length=50)
):
    return {"item_id": item_id, "q": q}

@app.post("/items/")
async def create_item(item: Item):
    return item