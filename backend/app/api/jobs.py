from fastapi import APIRouter

router = APIRouter(prefix="/jobs", tags=["jobs"])


@router.get("/ping")
def ping_jobs() -> dict[str, str]:
    return {"service": "jobs", "status": "ok"}
