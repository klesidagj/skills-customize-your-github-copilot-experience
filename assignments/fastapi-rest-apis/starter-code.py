"""Starter code for the FastAPI REST API assignment."""

from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="Task Tracker API")


class Item(BaseModel):
    id: int
    name: str
    description: str
    is_active: bool = True


class ItemCreate(BaseModel):
    name: str
    description: str


items = [
    Item(id=1, name="Learn FastAPI", description="Build a simple REST API", is_active=True),
    Item(id=2, name="Add Validation", description="Use Pydantic models", is_active=True),
]


@app.get("/")
def root():
    return {"message": "Welcome to the Task Tracker API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/items")
def list_items(q: Optional[str] = None):
    # TODO: return the sample items, optionally filtering by the query string.
    return items


@app.get("/items/{item_id}")
def get_item(item_id: int):
    # TODO: find and return the matching item.
    raise HTTPException(status_code=404, detail="Item not found")


@app.post("/items", status_code=201)
def create_item(item: ItemCreate):
    # TODO: create a new item and add it to the in-memory list.
    return {"message": "Item created", "item": item}


@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: ItemCreate):
    # TODO: update the matching item.
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    # TODO: delete the matching item.
    raise HTTPException(status_code=404, detail="Item not found")