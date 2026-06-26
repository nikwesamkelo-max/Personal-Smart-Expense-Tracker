from fastapi import FastAPI
from database import init_db
from tracker import create_expense, list_expenses, total_spent

app = FastAPI()

init_db()


@app.get("/")
def home():
    return {"message": "Smart Expense Tracker API is running 🚀"}


@app.post("/expense")
def add(title: str, amount: float, category: str):

    return create_expense(title, amount, category)


@app.get("/expenses")
def get_all():

    return list_expenses()


@app.get("/total")
def total():

    return total_spent()
