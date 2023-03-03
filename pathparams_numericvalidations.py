from typing import Optional

from fastapi import FastAPI, Path, Query

app = FastAPI()

title_text = "The id of the item to get"

@app.get("/items/{item_id}")
async def read_items(
    q: str,
    item_id: int = Path(..., title=title_text, ge=1)
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

@app.get("/items/gtle/{item_id}")
async def read_items(
    q: str,
    item_id: int = Path(..., title=title_text, gt=0, le=1000)
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

@app.get("/items/floats/{item_id}")
async def read_items(
    q: str,
    item_id: int = Path(..., title=title_text, gt=0, le=1000),
    size: float = Query(..., gt=0, lt=10.5)
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

@app.get("/items/specificorder/{item_id}")
async def read_items_specificorder(
    *,
    item_id: int = Path(..., title=title_text),
    q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


