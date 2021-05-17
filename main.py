from typing import Optional

from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


users = [{"user_id": 1, "name": "Khushal Bhalsod", "email": "bhalsodkhushalce@gmail.com", "mobile": "9924952829"},
         {"user_id": 2, "name": "Dinesh Rathod", "email": "dinesh@gmail.com", "mobile": "8965896584"}]


@app.get("/", response_class=HTMLResponse)
def get_index(request: Request):
    # return {"page": "Home"}
    return templates.TemplateResponse("home.html", {"request": request, "id": "100"})


@app.get("/users")
def get_home():
    return {"users": users}


@app.get("/users/{user_id}")
def read_item(user_id: int, q: Optional[str] = None):
    response = users[user_id-1]
    return {"users": response, "user_id": user_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
