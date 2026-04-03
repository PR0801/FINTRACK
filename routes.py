from flask import request, jsonify
from app import app
from services import *
@app.route("/")
def home():
    return "Finance System Backend Running"
@app.route("/users", methods=["POST"])
def create_user_api():
    data = request.json
    if not data.get("name") or not data.get("role"):
        return jsonify({"error": "Name & role required"}), 400
    if data["role"] not in ["admin", "analyst", "viewer"]:
        return jsonify({"error": "Invalid role"}), 400
    create_user(data["name"], data["role"])
    return jsonify({"message": "User created"})
@app.route("/transactions", methods=["POST"])
def create():
    data = request.json
    if not data.get("amount"):
        return jsonify({"error": "Amount required"}), 400
    if data.get("type") not in ["income", "expense"]:
        return jsonify({"error": "Invalid type"}), 400
    user = get_user(data.get("user_id"))
    if not user:
        return jsonify({"error": "Invalid user"}), 400
    if user["role"] != "admin":
        return jsonify({"error": "Only admin can create"}), 403
    create_transaction(data)
    return jsonify({"message": "Transaction created"})
@app.route("/transactions", methods=["GET"])
def get_all():
    user_id = request.args.get("user_id")
    user = get_user(user_id)
    if not user:
        return jsonify({"error": "Invalid user"}), 400
    return jsonify(get_transactions())
@app.route("/transactions/<int:id>", methods=["PUT"])
def update(id):
    data = request.json
    user = get_user(data.get("user_id"))
    if not user:
        return jsonify({"error": "Invalid user"}), 400
    if user["role"] != "admin":
        return jsonify({"error": "Only admin can update"}), 403
    update_transaction(id, data)
    return jsonify({"message": "Updated"})
@app.route("/transactions/<int:id>", methods=["DELETE"])
def delete(id):
    data = request.json
    user = get_user(data.get("user_id"))
    if not user:
        return jsonify({"error": "Invalid user"}), 400
    if user["role"] != "admin":
        return jsonify({"error": "Only admin can delete"}), 40
    delete_transaction(id)
    return jsonify({"message": "Deleted"})
@app.route("/transactions/filter", methods=["GET"])
def filter_data():
    user_id = request.args.get("user_id")
    user = get_user(user_id)
    if not user:
        return jsonify({"error": "Invalid user"}), 400
    if user["role"] not in ["admin", "analyst"]:
        return jsonify({"error": "Access denied"}), 403
    type_ = request.args.get("type")
    category = request.args.get("category")
    date = request.args.get("date")
    return jsonify(filter_transactions(type_, category, date))
@app.route("/summary", methods=["GET"])
def summary():
    user_id = request.args.get("user_id")
    user = get_user(user_id)
    if not user:
        return jsonify({"error": "Invalid user"}), 400
    return jsonify(get_summary())