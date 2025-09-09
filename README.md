# TradePost API

A backend API for a smart item bartering platform, built with FastAPI. This project allows users to register, log in, and post items they wish to trade, creating a foundation for a full-featured trading application.

---

## Features Implemented

- [x] User Registration with password hashing
- [x] User Login with JWT Token Authentication
- [x] OAuth2 Password Flow for secure login
- [x] Protected endpoints to require authentication
- [x] Relational database schema with Users and Items
- [x] Alembic database migrations for safe schema changes
- [x] Pydantic schemas for data validation and serialization

---

## Technology Stack

- **Framework:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Database Migrations:** Alembic
- **Data Validation:** Pydantic
- **Authentication:** JWT Tokens, Passlib (for hashing), python-jose
- **Server:** Uvicorn
- **Containerization:** Docker (for PostgreSQL)

---

## Setup and Installation

Follow these steps to get the project running locally.

### 1. Clone the Repository

```bash
git clone [https://github.com/diegorbb/tradepost-api.git](https://github.com/diegorbb/tradepost-api.git)
cd tradepost-api
```

### 2. Create and Activate a Virtual Environment

It's highly recommended to use a virtual environment to manage project dependencies.

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install all the required Python packages from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 4. Set Up the Database with Docker

This project uses a PostgreSQL database. The easiest way to run it locally is with Docker. Make sure you have Docker Desktop installed and running.

```bash
# This command will download the official Postgres image and run it in a container.
# It maps port 5433 on your machine to port 5432 in the container.
docker run --name tradepost-db -e POSTGRES_PASSWORD=1234 -p 5433:5432 -d postgres
```
After running this, use a database client like DBeaver or pgAdmin to connect to the server and create a new, empty database named `tradepost-db`.

### 5. Configure Environment Variables

The application requires environment variables for database credentials and security keys. A `.env.example` file is provided in the repository.

First, create a copy of the example file.

```bash
# For Windows (PowerShell) or macOS/Linux
cp .env.example .env

# For Windows (Command Prompt)
copy .env.example .env
```
Next, open the new `.env` file and generate a secret key. You can generate one using Python:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```
Paste the generated key as the value for `SECRET_KEY` in your `.env` file.

### 6. Run Database Migrations

With the database running and the `.env` file configured, apply all database schema changes using Alembic.

```bash
alembic upgrade head
```

### 7. Run the Application

Finally, run the FastAPI development server.

```bash
uvicorn app.main:app --reload
```
The API will now be available at `http://127.0.0.1:8000`.

---

## API Documentation

Once the server is running, interactive API documentation (provided by Swagger UI) is available at:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

This interface allows you to interact with all the API endpoints, handle authentication, and see real-time responses.