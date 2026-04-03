#FINTRACK

##Finance Tracker Backend (Flask + MySQL)

## Overview

This project is a Python-based backend system for managing financial records. It allows users to create, manage, and analyze transactions such as income and expenses.

## Tech Stack

* Python (Flask)
* MySQL
* mysql-connector-python

## Features

* Create, Read, Update, Delete (CRUD) transactions
* Filter transactions by type, category, and date
* Financial summary (total income, expense, balance)
* User management with roles (Admin, Analyst, Viewer)
* Role-based access control
* Input validation and error handling

## API Endpoints

### User

* POST /users → Create user

### Transactions

* POST /transactions → Create transaction
* GET /transactions → Get all transactions
* PUT /transactions/<id> → Update transaction
* DELETE /transactions/<id> → Delete transaction
* GET /transactions/filter → Filter transactions

### Analytics

* GET /summary → Get financial summary

## Setup Instructions

1. Install dependencies:
   pip install -r requirements.txt

2. Create MySQL database:
   CREATE DATABASE FINTRACK;

3. Create tables:
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

4. Update database credentials in db.py

5. Run the application:
   python app.py

## Assumptions

* Authentication is simplified (user_id passed in request)
* Dates are stored as strings
* Roles are predefined (admin, analyst, viewer)

## Testing

Use Postman to test all endpoints.

## Author

Pratyush Raunak
