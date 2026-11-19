# Spendly – Personal Expense Tracker

Spendly is a personal expense tracking web application built using Python and Django. It helps users manage their daily expenses, track spending, and understand their spending habits.

## Features

- Add new expenses
- View all expenses
- Edit and delete expenses
- Filter expenses by category, date, and title
- View monthly expense summaries
- View category-wise expense breakdown
- Interactive dashboard with a donut chart

## Technologies Used

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite
- **Tools:** VS Code, Git, GitHub

## Expense Categories

- Food
- Transport
- Shopping
- Bills
- Entertainment
- Other

## Project Structure

```text
personal_expense_tracker/
│
├── config/
├── expenses/
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
├── templates/
│   └── expenses/
│       └── index.html
├── manage.py
├── requirements.txt
└── .gitignore
```

## Installation and Setup

**1. Clone the repository**

```bash
git clone https://github.com/gopikamr666-byte/personal-expense-tracker.git
```

**2. Open the project folder**

```bash
cd personal-expense-tracker
```

**3. Create a virtual environment**

```bash
python -m venv venv
```

**4. Activate the virtual environment**

```bash
venv\Scripts\activate
```

**5. Install dependencies**

```bash
pip install -r requirements.txt
```

**6. Apply migrations**

```bash
python manage.py migrate
```

**7. Run the development server**

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Author

**Gopika M R**

GitHub: https://github.com/gopikamr666-byte