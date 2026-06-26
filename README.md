📊 Smart Expense Tracker API
A simple backend API built with FastAPI + SQLite to track and manage personal expenses.
🚀 Features
Add expenses (title, amount, category)
View all expenses
Get total spending
Stores data using SQLite database
🏗️ Tech Stack
Python
FastAPI
SQLite
Uvicorn
📁 Project Structure
Plain text
expense-tracker/
│
├── main.py
├── tracker.py
├── database.py
├── expenses.db
├── requirements.txt
└── README.md
⚙️ How to Run
Install dependencies
Bash
pip install -r requirements.txt
Start server
Bash
uvicorn main:app --reload
🌐 API Endpoints
➕ Add Expense

POST /expense?title=Food&amount=100&category=Groceries
📋 Get All Expenses

GET /expenses
💰 Total Spending

GET /total
🧠 System Flow
Plain text
User → FastAPI → Logic Layer → SQLite → Response
🚀 Future Improvements
Add date tracking
Add charts/analytics
AI expense categorization
User authentication
