from fastapi import FastAPI

from app.api.routes import router as api_router

app = FastAPI(title="AI Job Application Agent")

app.include_router(api_router)


@app.get("/")
def read_root() -> dict[str, str]:
    return {"status": "ok"}
