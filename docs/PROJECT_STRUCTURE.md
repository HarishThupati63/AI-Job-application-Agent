# Project Structure

```
AI-Job-application-Agent/
├── README.md
├── backend/
│   ├── README.md
│   ├── requirements.txt
│   ├── app/
│   │   ├── main.py
│   │   ├── api/
│   │   │   └── routes.py
│   │   ├── core/
│   │   │   └── config.py
│   │   ├── models/
│   │   │   └── __init__.py
│   │   ├── schemas/
│   │   │   └── __init__.py
│   │   └── services/
│   │       └── __init__.py
│   └── tests/
├── frontend/
│   ├── README.md
│   └── src/
└── docs/
    ├── PROJECT_STRUCTURE.md
    └── REQUIREMENTS.md
```

## Notes
- `backend/` contains FastAPI service scaffolding and dependency definitions.
- `frontend/` is ready for a React/TypeScript dashboard bootstrap.
- `docs/` stores project requirements and architecture documentation.
