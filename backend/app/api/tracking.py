from fastapi import APIRouter

router = APIRouter(prefix="/tracking", tags=["tracking"])


@router.get("/ping")
def ping_tracking() -> dict[str, str]:
    return {"service": "tracking", "status": "ok"}
