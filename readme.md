# Partner API (FastAPI + PostgreSQL)

A simple REST API that connects a web application to a PostgreSQL database using FastAPI and SQLAlchemy. It supports API key authentication and basic CRUD operations for partner data.

---

## Tech Stack

- FastAPI (API framework)
- Uvicorn (ASGI server)
- PostgreSQL (database)
- SQLAlchemy (ORM)
- Psycopg2 (PostgreSQL driver)
- Python-dotenv (environment variables)

---

## Project Structure

partner-api/
.env
main.py
database.py
models.py
auth.py
routers/
  -partners.py

---

## Setup Instructions

### 1. Clone and navigate
git clone <url of this redo>
cd partner-api

### 2. Create virtual environment
python -m venv venv
venv\Scripts\activate
### 3. Install dependencies
pip install fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv python-jose[cryptography]

### Database Setup (PostgreSQL):
CREATE DATABASE partner_db;

CREATE USER api_user WITH PASSWORD 'securepass123';

GRANT ALL PRIVILEGES ON DATABASE partner_db TO api_user;
GRANT ALL ON SCHEMA public TO api_user;
ALTER SCHEMA public OWNER TO api_user;

(you can manually change the owndership of the partner_db via... find your database at pgadmin find schemas >> public >> right click >> Properties >> owner: find "api_user")

### Environment Variables
at your dotENV:
DATABASE_URL=postgresql://api_user:securepass123@localhost:5432/partner_db

### Run Test 
uvicorn main:app --reload

### Access docs at:
http://localhost:8000/docs

| Method | Endpoint           | Description        |
| ------ | ------------------ | ------------------ |
| GET    | /api/partners      | Get all partners   |
| GET    | /api/partners/{id} | Get partner by ID  |
| POST   | /api/partners      | Create new partner |

## Note: 
At if you don't wanna look up your API key. you can disable the line "current_partner = Depends(verify_api_key)" to disable the API auth process in http://localhost:8000/docs so that you can user GET without restrictions