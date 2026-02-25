# -Elias-Final-Project-Building-FastAPI-Task-Management-System

# FastAPI Task Management System

A simple backend API to manage tasks. 
Data is stored in `tasks.txt` using the JSON Lines format.

# How to Run
1. Create a virtual environment: `python -m venv venv`
2. Activate it: `.\venv\Scripts\activate` (Windows)
3. Install FastAPI: `pip install fastapi uvicorn`
4. Run the server: `uvicorn main:app --reload`
5. Visit: `http://127.0.0.1:8000/docs`
