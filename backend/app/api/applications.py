from fastapi import APIRouter

router = APIRouter(prefix="/applications", tags=["applications"])


@router.get("/ping")
def ping_applications() -> dict[str, str]:
    return {"service": "applications", "status": "ok"}
