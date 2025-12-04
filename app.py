# app.py
from flask import Flask, render_template, request, redirect, flash
from datetime import datetime
from models import db, Budget, Expense
import os

app = Flask(__name__)
app.secret_key = "simple-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///expenses.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# Create DB if not exists
with app.app_context():
    db.create_all()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add-budget", methods=["GET", "POST"])
def add_budget():
    if request.method == "POST":
        category = request.form["category"]
        amount = float(request.form["amount"])
        month = request.form["month"]

        new_budget = Budget(category=category, amount=amount, month=month)
        db.session.add(new_budget)
        db.session.commit()

        flash(f"Budget for {category} added successfully!", "success")
        return redirect("/")

    return render_template("add_budget.html")


@app.route("/add-expense", methods=["GET", "POST"])
def add_expense():
    budgets = Budget.query.all()

    if request.method == "POST":
        category = request.form["category"]
        amount = float(request.form["amount"])
        desc = request.form["description"]
        month = request.form["month"]   # <-- USE SELECTED MONTH

        today = datetime.today()

        new_expense = Expense(
            category=category,
            amount=amount,
            description=desc,
            month=month,  # <-- SAVE CORRECT MONTH
            date=today
        )
        db.session.add(new_expense)
        db.session.commit()

        # Check alerts
        budget = Budget.query.filter_by(category=category, month=month).first()

        if budget:
            spent = db.session.query(db.func.sum(Expense.amount))\
                .filter_by(category=category, month=month).scalar() or 0

            remaining = budget.amount - spent

            if remaining <= budget.amount * 0.10:
                flash(f"⚠ Only 10% budget left for {category}!")

            if remaining < 0:
                flash(f"🚨 Budget exceeded for {category}!")

        flash("Expense added successfully.")
        return redirect("/add-expense")

    return render_template("add_expense.html", budgets=budgets)



@app.route("/report")
def report():
    # If user selected a month, use that
    selected_month = request.args.get("month")

    # else use current month
    if selected_month:
        month = selected_month
    else:
        month = datetime.today().strftime("%Y-%m")

    budgets = Budget.query.filter_by(month=month).all()
    expenses = Expense.query.filter_by(month=month).all()

    total_spent = sum(e.amount for e in expenses)

    spend_by_category = {}
    for e in expenses:
        spend_by_category.setdefault(e.category, 0)
        spend_by_category[e.category] += e.amount

    return render_template(
        "report.html",
        month=month,
        total_spent=total_spent,
        budgets=budgets,
        spend_by_category=spend_by_category
    )



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

