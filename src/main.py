from fastapi import FastAPI, HTTPException
from .models import ItemPayload

app = FastAPI()

# This is a dictionary that will hold our grocery list items.
grocery_list: dict[int, ItemPayload] = {}

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI Grocery List Web App"}

@app.post("/items/{item_name}/{quantity}")
def add_item(item_name: str, quantity: int) -> dict[str, ItemPayload]:
    '''Route to add an item to the grocery list.
    '''

    # Validate the quantity
    if quantity <= 0:
        raise HTTPException(status_code=400, detail="Quantity must be greater than 0")

    # Get all item names
    items_ids: dict[str, int] = {
        item.item_name: item.item_id if item.item_id is not None else 0
        for item in grocery_list.values()
    }

    if item_name in items_ids.keys():
        # If item already exists, we'll just add the quantity.
        # get index of item_name in item_ids, which is the item_id
        item_id: int = items_ids[item_name]
        grocery_list[item_id].quantity += quantity
    else:
        # Otherwise, create a new item.
        # generate an ID for the item based on the highest ID in the grocery_list
        item_id = max(grocery_list.keys()) + 1 if grocery_list else 0
        grocery_list[item_id] = ItemPayload(
            item_id=item_id, item_name=item_name, quantity=quantity
        )

    return {"item": grocery_list[item_id]}


@app.get("/items/{item_id}")
def list_item(item_id: int) -> dict[str, ItemPayload]:
    '''Route to list a specific item by ID
    '''
    if item_id not in grocery_list:
        raise HTTPException(status_code=404, detail="Item not found.")
    return {"item": grocery_list[item_id]}


@app.get("/items")
def list_items() -> dict[str, dict[int, ItemPayload]]:
    '''Route to list all items
    '''
    return {"items": grocery_list}


@app.delete("/items/{item_id}")
def delete_item(item_id: int) -> dict[str, str]:
    '''Route to delete a specific item by ID
    '''
    if item_id not in grocery_list:
        raise HTTPException(status_code=404, detail="Item not found.")
    del grocery_list[item_id]
    return {"result": "Item deleted."}


@app.delete("/items/{item_id}/{quantity}")
def remove_quantity(item_id: int, quantity: int) -> dict[str, str]:
    '''Route to remove some quantity of a specific item by ID
    '''
    if item_id not in grocery_list:
        raise HTTPException(status_code=404, detail="Item not found.")
    # if quantity to be removed is higher or equal to item's quantity, delete the item
    if grocery_list[item_id].quantity <= quantity:
        del grocery_list[item_id]
        return {"result": "Item deleted."}
    else:
        grocery_list[item_id].quantity -= quantity
    return {"result": f"{quantity} items removed."}