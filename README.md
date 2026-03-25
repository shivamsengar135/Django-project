# Shivam Ice-Cream Website (Django)

A full-stack Django website with:
- Home, About, Services, and Contact pages
- Register/Login/Logout authentication
- Search functionality for products and pages
- Contact form submissions stored in backend database
- Admin panel for managing data

## Tech Stack
- Python
- Django
- Bootstrap 5
- SQLite (default)
- Gunicorn + WhiteNoise (deployment)

## Project Structure
```text
Hello/
  Hello/            # project settings, urls, wsgi
  home/             # app (views, models, urls)
  templates/        # HTML templates
  static/           # static assets
  manage.py
```

## Local Setup
1. Create and activate virtual environment
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run migrations
```bash
python manage.py migrate
```

4. Start server
```bash
python manage.py runserver
```

Visit: `http://127.0.0.1:8000/`

## Admin Access
Create superuser:
```bash
python manage.py createsuperuser
```
Then open: `http://127.0.0.1:8000/admin/`

## Deployment (Render)
- Build command:
```bash
pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
```
- Start command:
```bash
gunicorn Hello.wsgi:application
```

## Environment Variables (Recommended)
- `SECRET_KEY`
- `DEBUG`
- `ALLOWED_HOSTS`
- `DATABASE_URL` (for PostgreSQL in production)

## Notes
- `db.sqlite3` is for local development.
- For production, use PostgreSQL and set `DATABASE_URL`.
