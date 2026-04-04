# FINTRACK
# FINTRACK – Finance Tracker Backend (Flask + MySQL)

## 📌 Overview

FINTRACK is a Python-based backend system designed to manage and analyze financial records. It provides RESTful APIs to handle income and expense tracking, generate summaries, and enforce role-based access control.

This project focuses on clean backend architecture, proper data handling, and logical business implementation.

---

## ⚙️ Tech Stack

* **Backend Framework:** Flask
* **Database:** MySQL
* **Connector:** mysql-connector-python
* **Testing Tool:** Postman

---

## 🚀 Features

### 🔹 Financial Records Management

* Create, Read, Update, Delete (CRUD) transactions
* Track income and expenses
* Categorize transactions
* Store date and notes

### 🔹 Filtering & Search

* Filter by:

  * Type (income/expense)
  * Category
  * Date

### 🔹 Analytics & Summary

* Total Income
* Total Expense
* Current Balance (Income − Expense)

### 🔹 User & Role Management

* Admin → Full access (CRUD)
* Analyst → View + Filter
* Viewer → Read-only access

### 🔹 Validation & Error Handling

* Input validation
* Proper error messages
* Role-based access restrictions

---

## 🏗️ Project Structure

```
finance_app/
├── app.py          # Entry point
├── db.py           # Database connection
├── routes.py       # API endpoints
├── services.py     # Business logic
├── requirements.txt
```

👉 The project follows a **layered architecture**:

* Routes → Handle HTTP requests
* Services → Handle business logic
* DB → Handles database operations

---

## 📡 API Endpoints

### 👤 User

* `POST /users` → Create user

---

### 💰 Transactions

* `POST /transactions` → Create transaction
* `GET /transactions` → Get all transactions
* `PUT /transactions/<id>` → Update transaction
* `DELETE /transactions/<id>` → Delete transaction
* `GET /transactions/filter` → Filter transactions

---

### 📊 Analytics

* `GET /summary` → Get financial summary

---

## 🧪 Example Requests

### ➤ Create User

```json
POST /users
{
  "name": "AdminUser",
  "role": "admin"
}
```

---

### ➤ Create Transaction

```json
POST /transactions
{
  "amount": 5000,
  "type": "income",
  "category": "salary",
  "date": "2026-04-03",
  "user_id": 1
}
```

---

### ➤ Get Transactions

```
GET /transactions?user_id=1
```

---

### ➤ Filter Transactions

```
GET /transactions/filter?type=income&user_id=2
```

---

### ➤ Get Summary

```
GET /summary?user_id=1
```

---

## 🗄️ Database Setup

```sql
CREATE DATABASE FINTRACK;
USE FINTRACK;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    role VARCHAR(20)
);

CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    amount FLOAT NOT NULL,
    type VARCHAR(10),
    category VARCHAR(50),
    date VARCHAR(20),
    notes VARCHAR(200),
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

---

## ⚙️ Setup Instructions

1. Clone the repository
2. Install dependencies:

```
pip install -r requirements.txt
```

3. Configure MySQL credentials in `db.py`

4. Run the server:

```
python app.py
```

5. Test APIs using Postman

---

## 🧠 Design Approach

The application follows a modular and layered architecture where:

* Routes handle incoming API requests
* Services encapsulate business logic
* Database layer manages persistence

This ensures clean code, maintainability, and separation of concerns.

---

## ⚠️ Assumptions

* Authentication is simplified using `user_id`
* Dates are stored as strings
* Roles are predefined (admin, analyst, viewer)

---

## 🧪 Testing

All endpoints are tested using Postman.
Role-based access is verified for different user types.

---
## 📡 API Documentation

### Base URL

http://127.0.0.1:5000/

---

## 👤 Create User

**POST /users**

Request:

```json
{
  "name": "AdminUser",
  "role": "admin"
}
```

Response:

```json
{
  "message": "User created"
}
```

---

## 💰 Create Transaction

**POST /transactions**

Request:

```json
{
  "amount": 5000,
  "type": "income",
  "category": "salary",
  "date": "2026-04-03",
  "user_id": 1
}
```

Response:

```json
{
  "message": "Transaction created"
}
```

---

## 📖 Get Transactions

**GET /transactions?user_id=1**

Response:

```json
[
  {
    "id": 1,
    "amount": 5000,
    "type": "income",
    "category": "salary"
  }
]
```

---

## 🔍 Filter Transactions

**GET /transactions/filter?type=income&user_id=2**

Response:

```json
[
  {
    "id": 1,
    "amount": 5000,
    "type": "income"
  }
]
```

---

## 📊 Get Summary

**GET /summary?user_id=1**

Response:

```json
{
  "total_income": 5000,
  "total_expense": 0,
  "balance": 5000
}
```

---

## ⚠️ Error Responses

```json
{ "error": "Invalid user" }
{ "error": "Only admin can create" }
{ "error": "Access denied" }
```

---

## 📌 Status Codes

* 200 → Success
* 400 → Bad Request
* 403 → Forbidden
* 500 → Server Error

## 👨‍💻 Author

**Pratyush Raunak**

---

## 📌 Note

This project is developed as part of a backend assessment to demonstrate Python development skills, API design, and system architecture.
