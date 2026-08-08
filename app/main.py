from fastapi import FastAPI

from app.api.routes import urls

app = FastAPI(
    title="URL Shortener",
    description="A production-style URL shortener API",
    version="0.1.0",
)

app.include_router(urls.router)


@app.get("/")
def read_root():
    return {"message": "URL Shortener API is running"}
