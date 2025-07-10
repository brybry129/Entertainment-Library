from fastapi import FastAPI

# Import routes
from app.routes import media, auth_routes

app = FastAPI()

# Register routes
app.include_router(auth_routes.router)
app.include_router(media.router)

@app.get("/")
def read_root():
    return {"message": "pong"}
