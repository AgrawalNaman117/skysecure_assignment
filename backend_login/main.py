from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from config import settings

app = FastAPI()

# Add session middleware (important for login tracking)
app.add_middleware(
    SessionMiddleware,
    secret_key=settings.SESSION_SECRET
)

@app.get("/")
def home():
    return {"message": "Backend running"}