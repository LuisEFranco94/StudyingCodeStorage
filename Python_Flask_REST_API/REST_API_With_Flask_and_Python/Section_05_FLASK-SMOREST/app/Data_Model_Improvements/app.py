from flask import Flask, request
from flask_smorest import abort
from db import stores, items
import uuid

app = Flask(__name__)

# New get_stores
@app.get("/store")
def get_stores():
    return {"stores": list(stores.values())}

# New create_store
@app.post("/store")
def create_store():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex
    store = {**store_data, "id": store_id}
    stores[store_id] = store

    return store

# New create_item
@app.post("/item")
def create_item():
    item_data = request.get_json()
    if item_data["store_id"] not in stores:
        return {"message": "Store not found"}, 404

    item_id = uuid.uuid4().hex
    item = {**item_data, "id": item_id}
    items[item_id] = item

    return item

# Get store by id
@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        # Here you might also want to add the items in this store
        # We'll do that later on in the course
        return stores[store_id]
    except KeyError:
        abort(404, message="Store not found.")


@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        abort(404, message="Item not found.")


@app.get("/item")
def get_all_items():
    return {"items": list(items.values())}



