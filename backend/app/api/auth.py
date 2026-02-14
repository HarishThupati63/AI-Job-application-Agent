from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["auth"])


@router.get("/ping")
def ping_auth() -> dict[str, str]:
    return {"service": "auth", "status": "ok"}
