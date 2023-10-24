from flask import Flask, request

app = Flask(__name__)

stores = [{"name": "My Store", 
           "items": [{"name": "Chair", "price": 15.99}] }]

# Endpoint: http://127.0.0.1:5000/store
@app.get("/store")
def get_stores():
    return {"stores": stores}

# Endpoint: http://127.0.0.1:5000/store
@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201