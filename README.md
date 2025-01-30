# FastAPI Customer Success API

## Overview
This is a simple FastAPI application that provides CRUD operations for managing items in a PostgreSQL database. The application includes RESTful endpoints and utilizes SQLAlchemy for database interactions.

---

## Project Structure
```
CS/
│-- main.py         # FastAPI application with API routes
│-- database.py     # Database configuration and models
│-- test_unit.py    # Unit tests for the API
│-- requirements.txt # Python dependencies
│-- README.md       # Project documentation
```

---

## Prerequisites
Ensure you have the following installed on your system:
- Python 3.10+
- PostgreSQL
- Virtual Environment (venv)

---

## Setup Instructions
### 1️⃣ Clone the Repository
```bash
git clone <repository-url>
cd CS
```

### 2️⃣ Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure PostgreSQL Database
Create a database in PostgreSQL:
```sql
CREATE DATABASE customer_success;
```
Update `DATABASE_URL` in `database.py`:
```python
DATABASE_URL = "postgresql://raviyadav:<your-password>@localhost/customer_success"
```

---

## Running the Application
Start the FastAPI server:
```bash
uvicorn main:app --reload
```
Access the API documentation:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## API Endpoints
| Method | Endpoint        | Description             |
|--------|----------------|-------------------------|
| POST   | /items/        | Create a new item       |
| GET    | /items/        | Retrieve all items      |
| GET    | /items/{id}    | Retrieve a specific item |
| PUT    | /items/{id}    | Update an item         |
| DELETE | /items/{id}    | Delete an item         |

---

## Running Unit Tests
Run the tests using `pytest`:
```bash
pytest test_unit.py
```

---

## Common Issues & Fixes
### 1️⃣ **ModuleNotFoundError: No module named 'sqlalchemy'**
Run:
```bash
pip install sqlalchemy
```

### 2️⃣ **ERROR: Address already in use**
Kill the running process:
```bash
lsof -i :8000  # Find process ID (PID)
kill -9 <PID>  # Kill process
```

### 3️⃣ **Cannot Connect to Database**
- Ensure PostgreSQL is running:
```bash
brew services start postgresql  # macOS
sudo service postgresql start   # Linux
```

---

## License
This project is licensed under the MIT License.

