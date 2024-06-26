from fastapi import FastAPI
from app.api.v1.router import api_router  # Import the centralized router from the v1 API

app = FastAPI(title="backend_amp_core", version="1.0", description="A secure, scalable Python-based web application")

# Include the API routers
app.include_router(api_router, prefix="/api/v1")  # Prefix all the routes defined in api_router with `/api/v1`

@app.get("/")
async def root():
    return {"message": "Welcome to backend_amp_core API!"}