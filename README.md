# Expense Insight

A Python-based personal finance management application that helps users plan, track, and analyze their monthly expenses — generating a personalized budget, evaluating spending behavior, and delivering actionable financial insights.

--

## Table of Contents

- [About the Project](#about-the-project)
- [Problem Statement](#problem-statement)
- [Objectives](#objectives)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

---

## About the Project

Expense Insight is designed to promote financial awareness, encourage disciplined spending habits, and help users achieve their savings goals through a structured budgeting process. It generates a personalized budget based on the user's income and lifestyle preferences, records expenses across multiple categories, and evaluates overall spending behavior.

## Problem Statement

Many individuals struggle to manage their finances effectively due to the absence of proper budgeting and expense-tracking practices. Overspending, inadequate savings, and poor financial planning often result from a lack of visibility into spending patterns.

Expense Insight addresses this by providing a simple yet effective budgeting framework that lets users compare actual spending against a recommended budget and receive meaningful feedback on their financial performance.

## Objectives

- Create a personalized budgeting system based on lifestyle and income
- Track expenses across different spending categories
- Analyze spending patterns and identify overspending
- Encourage better savings habits
- Provide financial performance evaluation through a scoring system
- Generate recommendations for improving financial management

## Key Features

### 1. Lifestyle-Based User Profiling
Collects user information such as monthly income/allowance, lifestyle preferences, travel habits, and savings priorities to generate a customized budget allocation.

### 2. Automated Budget Recommendation
Distributes a recommended budget across:
- Food
- Travel
- Shopping
- Entertainment
- Emergency Fund
- Savings

### 3. Budget Modification
Users can review and adjust the recommended budget before tracking begins, giving flexibility within a structured framework.

### 4. Expense Management System
- Add expenses
- View recorded expenses
- Search expenses by category
- Delete expenses

*All expense records are stored using Python data structures during program execution.*

### 5. Budget Analysis Module
Compares recommended budgets against actual expenditure per category, identifying whether the user stayed within, matched, or exceeded budget — and calculates percentage deviation.

### 6. Savings Analysis
Calculates total income, total expenditure, total savings, expected savings, and savings percentage, then classifies performance into predefined levels.

### 7. Financial Health Score
A 0–100 score based on savings target achievement, budget adherence, and overspending behavior, paired with a qualitative rating.

### 8. Achievement System
Rewards positive financial behavior based on budget compliance, savings performance, financial discipline, and overall score.

### 9. Personalized Recommendation Engine
Suggests category-specific actions when overspending is detected, e.g.:
- Reducing unnecessary shopping expenses
- Limiting food delivery expenditure
- Using cost-effective transportation alternatives
- Increasing emergency fund allocation

## Tech Stack

- Language: Python 3.13
- Data Storage: In-memory (Python data structures) — *no persistent storage between runs*
- Libraries: *(add any used, e.g. none / standard library only)*

## Usage

Follow the on-screen prompts to:
1. Enter your income and lifestyle preferences
2. Review and modify your recommended budget
3. Add and manage expenses
4. View your monthly report that include savings analysis, and financial health score

## Roadmap

-  Add persistent storage (e.g., SQLite or JSON file)
-  Add data visualization (charts for spending trends)
-  Export monthly reports to PDF/CSV
-  Add multi-user support

