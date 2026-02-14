# Project Structure

```
AI-Job-application-Agent/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── api/
│   │   │   ├── routes.py
│   │   │   ├── auth.py
│   │   │   ├── profile.py
│   │   │   ├── jobs.py
│   │   │   ├── applications.py
│   │   │   └── tracking.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   ├── security.py
│   │   │   └── logging.py
│   │   ├── db/
│   │   │   ├── session.py
│   │   │   └── base.py
│   │   ├── models/
│   │   │   ├── user.py
│   │   │   ├── resume.py
│   │   │   ├── job_posting.py
│   │   │   ├── application.py
│   │   │   └── feedback.py
│   │   ├── schemas/
│   │   │   ├── profile.py
│   │   │   ├── jobs.py
│   │   │   └── applications.py
│   │   ├── services/
│   │   │   ├── resume_parser.py
│   │   │   ├── job_connectors/
│   │   │   │   ├── linkedin.py
│   │   │   │   ├── indeed.py
│   │   │   │   └── common.py
│   │   │   ├── matcher.py
│   │   │   ├── cover_letter_generator.py
│   │   │   └── apply_executor.py
│   │   ├── workers/
│   │   │   ├── celery_app.py
│   │   │   └── tasks.py
│   │   └── utils/
│   │       ├── browser_automation.py
│   │       └── validators.py
│   └── tests/
├── frontend/
│   └── src/
│       ├── pages/
│       ├── components/
│       ├── services/api.ts
│       └── store/
└── docs/
    ├── REQUIREMENTS.md
    ├── PROJECT_STRUCTURE.md
    ├── API_CONTRACT.md
    └── CONNECTORS.md
```
