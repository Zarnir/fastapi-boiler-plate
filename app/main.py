from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.middleware.cors import CORSMiddleware

from settings import settings
from development import development_settings

app = FastAPI(
    title=settings.API_PREFIX,
    version=settings.API_VERSION,
    description="API Description",
    contact={"name": "Your Name", "email": "your_email@example.com"},
)

# CORS Configuration
origins = [
    "http://localhost:3000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Routes
@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}


# Error Handling
@app.exception_handler(Exception)
def handle_exception(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"message": "Internal Server Error"})


# Development Settings
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
