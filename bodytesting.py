from typing import Optional, List, Set

from fastapi import FastAPI, Query, Body
from pydantic import BaseModel, Field

class Image(BaseModel):
    url: str
    name: str

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = set()
    image: Optional[Image] = None


class User(BaseModel):
    username: str
    full_name: Optional[str] = None

class Ornament(BaseModel):
    item_name: str
    item_prize: int

app = FastAPI()

@app.get("/items/")
async def read_items(q: Optional[str] = Query(None, min_length=3, max_length=50, regex="^fixedquery$")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.get("/items/required")
async def read_items(q: Optional[str] = Query(..., min_length=3, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.get("/items/multiplequeryparams")
async def read_items(q: Optional[List[str]] = Query(None, title="Query String", description="Query string for items to search")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.get("/items/alias")
async def read_items_alias(q: Optional[str] = Query(None, alias="item-query")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.get("/items/deprecated")
async def read_items_deprecated(q: Optional[str] = Query(None, deprecated=True)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: Optional[str] = None):
    result ={"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result

@app.put("/items/update/{item_id}")
async def update_item(item_id: int, item: Item, user: User):
    results = {"item_id": item_id, "item": item, "user": user}
    return results

@app.post("/ornaments/list")
async def get_ornaments(ornament: Ornament = Body(..., embed=True)):
    return ornament

class Bike(BaseModel):
    name: str = Field(None, title="Name of the bike", max_length=10)
    fuel_type: str = Field(None, description="Fuel type petrol or diesel")

@app.get("/bike/info")
async def get_bike(bike: Bike):
    return bike