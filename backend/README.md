# Backend Service

## Overview
FastAPI service for the AI Job Application Agent.

## Setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Key Packages
- FastAPI for APIs
- SQLAlchemy + Alembic for persistence
- Celery + Redis for background jobs
