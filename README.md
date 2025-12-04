**Expense Tracker Web App**

A simple Python Flask web application to track your expenses and budgets.
Designed to help users manage their monthly budgets, track expenses, and get alerts when budgets are almost full.

**Features**

1) Add monthly budgets for multiple categories (Food, Transport, Entertainment, etc.)
2) Add expenses under each category
3) Select the month for budgets and expenses
4) Monthly report showing total spent per category
5) Alerts when a category is running low (10% remaining) or exceeded
6) Simple, clean UI with one-page forms and reports
7) Runs in Docker for easy setup

**Folder Structure**
expense_tracker/

├── app.py

├── requirements.txt

├── Dockerfile

├── README.md

└── templates/

    ├── base.html
    
    ├── index.html
    
    ├── add_budget.html
    
    ├── add_expense.html
    
    └── report.html


**Setup Instructions (Locally)**

**Clone the repo**

git clone <your-github-repo-link>
cd expense_tracker


**Create a virtual environment** 

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows


**Install dependencies**

pip install -r requirements.txt


**Run the application**

python app.py


Open the web app
Go to: http://localhost:5000

**Using the App**

**Add Budget**

* Click Add Budget in the navigation bar

* Enter category, amount, and month (YYYY-MM)

* Click Save Budget

**Add Expense**

* Click Add Expense

* Choose category, amount, description, and month

* Click Add Expense

* Alerts will appear if you are near or over the budget

**View Reports**

* Click Monthly Report

* Select the month you want to view

* Table shows total spent per category, budget, and remaining amount

**Docker Setup** 

Build Docker image

docker build -t expense-tracker .


Run Docker container

docker run -p 5000:5000 expense-tracker


Open browser
http://localhost:5000

**Testing & Validation**

Add budgets and expenses for multiple months and categories

Check that totals are correct in reports

Verify that alerts appear when 10% budget remains or budget is exceeded


Check that expenses and reports are correctly displayed for older months

**Technologies Used**

* Python 3.x

* Flask

* SQLAlchemy (SQLite)

* HTML/CSS (Jinja2 templates)

* Docker (optional for deployment)



