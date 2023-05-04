from flask import Flask, request

stores = {}



app = Flask(__name__)


@app.get("/store")
def get_stores():
    return {"stores": list(stores.values())}

@app.post("/store")
def create_stores():
    request_data = request.get_json()
    new_store = {"name": request_data['name'], "items": [] }
    stores.append(new_store)
    return new_store, 201


@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    print(request_data)
    for store in stores:
        if store["name"] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)            
            return store, 201
    return {"message": "Store not found"}, 404
