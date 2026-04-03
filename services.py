from db import execute_query
def create_user(name, role):
    execute_query(
        "INSERT INTO users (name, role) VALUES (%s, %s)",
        (name, role)
    )
def get_user(user_id):
    result = execute_query(
        "SELECT * FROM users WHERE id=%s",
        (user_id,),
        fetch=True
    )
    return result[0] if result else None
def create_transaction(data):
    query = """
    INSERT INTO transactions (amount, type, category, date, notes, user_id)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    values = (
        data["amount"],
        data["type"],
        data.get("category"),
        data.get("date"),
        data.get("notes"),
        data.get("user_id")
    )
    execute_query(query, values)
def get_transactions():
    return execute_query("SELECT * FROM transactions", fetch=True)
def update_transaction(id, data):
    execute_query(
        "UPDATE transactions SET amount=%s, category=%s WHERE id=%s",
        (data.get("amount"), data.get("category"), id)
    )
def delete_transaction(id):
    execute_query("DELETE FROM transactions WHERE id=%s", (id,))
def filter_transactions(type=None, category=None, date=None):
    query = "SELECT * FROM transactions WHERE 1=1"
    values = []
    if type:
        query += " AND type=%s"
        values.append(type)
    if category:
        query += " AND category=%s"
        values.append(category)
    if date:
        query += " AND date=%s"
        values.append(date)

    return execute_query(query, tuple(values), fetch=True)
def get_summary():
    income = execute_query(
        "SELECT SUM(amount) AS total FROM transactions WHERE type='income'",
        fetch=True
    )[0]["total"] or 0
    expense = execute_query(
        "SELECT SUM(amount) AS total FROM transactions WHERE type='expense'",
        fetch=True
    )[0]["total"] or 0
    return {
        "total_income": income,
        "total_expense": expense,
        "balance": income - expense
    }