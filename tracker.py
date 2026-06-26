from database import add_expense, get_all_expenses


def create_expense(title, amount, category):
    add_expense(title, amount, category)
    return {
        "message": "Expense added successfully",
        "data": {
            "title": title,
            "amount": amount,
            "category": category
        }
    }


def list_expenses():
    data = get_all_expenses()

    return {
        "total": len(data),
        "expenses": data
    }


def total_spent():
    data = get_all_expenses()

    total = sum([row[2] for row in data])

    return {
        "total_spent": total
    }
