from fastapi import APIRouter

router = APIRouter(prefix="/profile", tags=["profile"])


@router.get("/ping")
def ping_profile() -> dict[str, str]:
    return {"service": "profile", "status": "ok"}
