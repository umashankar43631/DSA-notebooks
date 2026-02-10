from fastapi import FastAPI
from functools import wraps


app = FastAPI()
authenticated = False

@app.get("/")
def read_root():
    return {"Hello": "World"}


def login_required(func):
    def wrapper(*args, **kwargs):
        # Simulate authentication check
        # authenticated = True  # Change this as needed for testing
        if not authenticated:
            return {"error": "Authentication required"}
        return func(*args, **kwargs)
    return wrapper

# somecode - fetch data from db - takes time for connection 
# meanwhile i can able to run other code this is possible with async await (parallel processing)

@app.get("/items/{item_id}")
@login_required
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.post("/items/")
def create_item(name: str):
    return {"name": name, "message": "Item created successfully"}



if __name__ == "__main__":
    import uvicorn
    # k8s, azure web apps
    uvicorn.run(app, host="0.0.0.0", port=8000)