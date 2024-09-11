from fastapi import FastAPI

import routes

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the API task collection"}

app.include_router(routes.router)
