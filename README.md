# AI Career Copilot

A production-minded Django 5 career intelligence workspace for resume analysis, skill-gap discovery, personalized learning roadmaps, interview practice, and progress analytics.

## Stack

- Python 3.10+ and Django 5
- SQLite for local development
- Bootstrap 5.3, Chart.js, HTML5, CSS3, ES6+
- PyMuPDF for local PDF text extraction
- Pure-Python local NLP utilities with TF-IDF vectors, cosine similarity, keyword matching, and rule-based generation
- WhiteNoise for static assets in deployment

## Run locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
python manage.py makemigrations accounts resume_analysis roadmap interview
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py runserver
```

Open `http://127.0.0.1:8000/` and create an account. No API key, network connection, or external AI provider is required. Resume matching, scoring, roadmaps, interview feedback, career writing, recommendations, and chat run locally from uploaded data and database records.

## Architecture

Each domain is isolated in its own Django app. `resume_analysis` owns PDF/DOCX parsing, score breakdowns, and analysis history. `skill_gap` owns role taxonomies and readiness scoring. `roadmap` persists generated tasks and completion state. `interview` contains practice history and local answer evaluation. `career_tools` owns TF-IDF job matching, application tracking, project recommendations, template-based career writing, and local career chat. `dashboard` composes persisted activity into Chart.js-friendly context. Shared local NLP utilities live in `ai_service.py`. Shared presentation lives in `templates/` and `static/`.

## Deployment

The included `Procfile` works with Render or Heroku using Gunicorn. Configure `SECRET_KEY`, `DEBUG=False`, and `ALLOWED_HOSTS` in the platform environment. Run migrations and `collectstatic` during release/build setup. User-uploaded PDFs and profile images require persistent media storage in production.
