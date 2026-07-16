print("          WELCOME TO EXPENSE INSIGHTS")
#input functions
def get_user_lifestyle_profile():

    print("          ENTER USER PROFILE\n")
    profile={}
    profile["name"]=input("Enter your name:")
    profile["age"]=int(input("Enter your age:"))

    print("\nOccupation")
    print("1. Student")
    print("2. Working Professional")

    occupation=int(input("Enter your choice:"))

    if occupation==1:
        profile["occupation"]="Student"
    else:
        profile["occupation"]="Working Professional"

    profile["income"]=float(input("\nEnter your monthly income or allowance: ₹"))

    print("\nWhere do you live?")
    print("1. Hostel")
    print("2. PG")
    print("3. With Parents")
    print("4. Rented House")

    living=int(input("Enter your choice:"))

    if living==1:
        profile["living"]="Hostel"

    elif living==2:
        profile["living"]="PG"

    elif living==3:
        profile["living"]="Parents"

    else:
        profile["living"]="Rent"

    vehicle=input("\nDo you own a vehicle? (yes/no): ")

    if vehicle.lower()=="yes":
        profile["vehicle"]=True
    else:
        profile["vehicle"]=False

    travel=input("Do you travel daily? (yes/no): ")

    if travel.lower()=="yes":
        profile["travel"]=True
    else:
        profile["travel"]=False

    print("\nSavings Goal")
    print("1. Low")
    print("2. Medium")
    print("3. High")

    goal=int(input("Choose (1-3):"))

    if goal==1:
        profile["goal"]="Low"

    elif goal==2:
        profile["goal"]="Medium"

    else:
        profile["goal"]="High"

    return profile

#main budget profile function

def calculate_budget(profile):

    income=profile["income"]

    budget={}

    #default settings in %
    
    food=30
    travel=10
    shopping=15
    entertainment=10
    emergency=10
    savings=25

    #lifestyle changes options and changes acc to that

    if profile["living"]=="Parents":
        food=20
        savings+=10

    if profile["vehicle"]:
        travel=18
        shopping=12

    if profile["goal"]=="High":
        savings+=10
        entertainment-=5
        shopping-=5

    elif profile["goal"]=="Low":
        savings-=10
        entertainment+=5
        shopping+=5

    # calculations

    budget["Food"]=income*food/100
    budget["Travel"]=income*travel/100
    budget["Shopping"]=income*shopping/100
    budget["Entertainment"]=income*entertainment/100
    budget["Emergency"]=income*emergency/100
    budget["Savings"]=income*savings/100

    return budget

# display function

def display_budget(budget):

    print("\n          RECOMMENDED BUDGET\n")

    for category,amount in budget.items():

        print(f"{category:<18} ₹{amount:.2f}")

    print()

#changes

def edit_budget(budget):

    while True:

        choice=input("Do you want to edit any category? (yes/no): ")

        if choice.lower()=="no":
            break

        category=input("Enter Category Name: ").title()

        if category in budget:

            amount=float(input("Enter new amount: ₹"))

            budget[category]=amount

            print("\nBudget Updated Successfully!\n")

            display_budget(budget)

        else:

            print("Invalid Category!")

    return budget
   
# user expense function 

from datetime import datetime

def add_expense(expenses):

    print("\n          ADD EXPENSE\n")

    while True:

        print("\nExpense Categories")

        print("1. Food")
        print("2. Travel")
        print("3. Shopping")
        print("4. Entertainment")
        print("5. Emergency")

        choice=int(input("\nChoose Category:"))

        if choice==1:
            category="Food"

        elif choice==2:
            category="Travel"

        elif choice==3:
            category="Shopping"

        elif choice==4:
            category="Entertainment"

        elif choice==5:
            category="Emergency"

        else:
            print("Invalid Choice!")
            continue

        amount=float(input("Enter Amount (₹):"))

        description=input("Description:")

        expense={

            "category":category,
            "amount":amount,
            "description":description,

        }

        expenses.append(expense)

        print("\nExpense Added Successfully!")

        again=input("\nDo you want to add another expense? (yes/no): ")

        if again.lower()=="no":
            break


#edit        

def view_expenses(expenses):

    print("\n          ALL EXPENSES\n")

    if len(expenses)==0:

        print("No Expenses Added Yet!")

        return

    total=0

    for expense in expenses:

        print("\n")

        print("Category    :",expense["category"])

        print("Amount      : ₹",expense["amount"])

        print("Description :",expense["description"])

        total+=expense["amount"]

    print("\n")

    print("Total Expenses : ₹",total)    

#search

def search_expense(expenses):

    category=input("\nEnter Category to Search: ").title()

    found=False

    print()

    for expense in expenses:

        if expense["category"]==category:

            print("\n")

            print("Category    :",expense["category"])

            print("Amount      : ₹",expense["amount"])

            print("Description :",expense["description"])

            found=True

    if not found:

       print("No Expense Found!")

#delete


def delete_expense(expenses):

    category=input("\nEnter Category to Delete: ").title()

    found=False

    for expense in expenses:

        if expense["category"]==category:

            expenses.remove(expense)

            print("\nExpense Deleted Successfully!")

            found=True

            break

    if not found:

        print("No Expense Found!")

#BUDGET ANALYSIS FN

def budget_analysis(budget,expenses):

    print("\n          BUDGET ANALYSIS")
    print("\n")

    categories=[
        "Food",
        "Travel",
        "Shopping",
        "Entertainment",
        "Emergency"
    ]

    spent={}

    #Initialize spending
    for category in categories:
        spent[category]=0

    #Calculate spending
    for expense in expenses:

        category=expense["category"]

        if category in spent:

            spent[category]+=expense["amount"]

    print(f"{'Category':<18}{'Budget':<12}{'Spent':<12}{'Remaining':<15}{'Status'}")

    for category in categories:

        budget_amount=budget[category]

        spent_amount=spent[category]

        remaining=budget_amount-spent_amount

        #Difference Percentage
        if budget_amount > 0:
          difference_percentage = abs((remaining / budget_amount) * 100)
        else:
         difference_percentage = 100.0 if spent_amount > 0 else 0.0

        if spent_amount>budget_amount:

            status=f"Over by {difference_percentage:.1f}%"

        elif spent_amount==budget_amount:

            status="Perfect"

        else:

            status=f"Under by {difference_percentage:.1f}%"

        print(f"{category:<18}₹{budget_amount:<11.2f}₹{spent_amount:<11.2f}₹{remaining:<14.2f}{status}")


def saving_status(profile,expenses,budget):

    print("\n          SAVINGS STATUS")

    income=profile["income"]

    total_expense=0

    for expense in expenses:

        total_expense+=expense["amount"]

    total_savings=income-total_expense

    expected_savings=budget["Savings"]

    savings_percentage=(total_savings/income)*100

    print(f"Income             : ₹{income:.2f}")
    print(f"Total Expenses     : ₹{total_expense:.2f}")
    print(f"Total Savings      : ₹{total_savings:.2f}")
    print(f"Expected Savings   : ₹{expected_savings:.2f}")
    print(f"Savings Percentage : {savings_percentage:.1f}%")

    print()

    if total_savings>expected_savings:

        print("Status : Excellent!")
        print("You saved more than your target.")

    elif total_savings==expected_savings:

        print("Status : Great!")
        print("You achieved your savings goal.")

    elif total_savings>=expected_savings*0.8:

        print("Status : Good")
        print("You were very close to your savings goal.")

    else:

        print("Status : Needs Improvement")
        print("Try reducing unnecessary expenses next month.")

def financial_score(profile,expenses,budget):

    print("\n          FINANCIAL HEALTH SCORE")
    print("\n")

    income=profile["income"]

    total_expense=0

    for expense in expenses:

        total_expense+=expense["amount"]

    total_savings=income-total_expense

    score=100
    if total_savings<budget["Savings"]:

        score-=20

    categories=[
        "Food",
        "Travel",
        "Shopping",
        "Entertainment",
        "Emergency"
    ]

    spent={}

    for category in categories:

        spent[category]=0

    for expense in expenses:

        category=expense["category"]

        if category in spent:

            spent[category]+=expense["amount"]

    for category in categories:

        if spent[category]>budget[category]:

            score-=10

    #score

    if score<0:

        score=0

    #rating in stars

    if score>=90:

        stars="★★★★★"

        rating="Excellent"

    elif score>=75:

        stars="★★★★☆"

        rating="Very Good"

    elif score>=60:

        stars="★★★☆☆"

        rating="Good"

    elif score>=40:

        stars="★★☆☆☆"

        rating="Average"

    else:

        stars="★☆☆☆☆"

        rating="Needs Improvement"

    print(f"Score : {score}/100")

    print(stars)

def suggestions(profile,expenses,budget):

    print("\n          SUGGESTIONS")
    print("\n")

    categories=[
        "Food",
        "Travel",
        "Shopping",
        "Entertainment",
        "Emergency"
    ]

    spent={}

    for category in categories:

        spent[category]=0

    for expense in expenses:

        category=expense["category"]

        if category in spent:

            spent[category]+=expense["amount"]

    for category in categories:

        budget_amount=budget[category]

        spent_amount=spent[category]

        difference=spent_amount-budget_amount

        percentage=(difference/budget_amount)*100

        if spent_amount>budget_amount:

            print(f"\n{category}")

            print(f"You exceeded your budget by ₹{difference:.2f}")

            print(f"({percentage:.1f}% over budget)")

            if category=="Food":

                print("Suggestion : Reduce outside food and food delivery.")

            elif category=="Travel":

                print("Suggestion : Try public transport or carpooling.")

            elif category=="Shopping":

                print("Suggestion : Avoid unnecessary purchases.")

            elif category=="Entertainment":

                print("Suggestion : Reduce entertainment expenses slightly.")

            elif category=="Emergency":

                print("Suggestion : Plan emergency expenses more carefully.")

        else:

            remaining=budget_amount-spent_amount

            percentage=(remaining/budget_amount)*100

            print(f"\n{category}")

            print("Great! You stayed within budget.")

            print(f"Remaining Budget : ₹{remaining:.2f}")

            print(f"({percentage:.1f}% budget still available)")

#MAIN FN

print("\n")
print("          EXPENSE INSIGHTS")
print("\n  Lifestyle-Based Budget Planner")
print("\n")

profile=get_user_lifestyle_profile()

budget=calculate_budget(profile)

display_budget(budget)

budget=edit_budget(budget)

expenses=[]

#Expense Menu
while True:

    print("\nExpense Menu")
    print("\n")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expense")
    print("4. Delete Expense")
    print("5. Generate Monthly Report")

    option=input("Enter your choice: ")

    if option=="1":

        add_expense(expenses)

    elif option=="2":

        view_expenses(expenses)

    elif option=="3":

        search_expense(expenses)

    elif option=="4":

        delete_expense(expenses)

    elif option=="5":

        print("\nGenerating Monthly Report\n")

        break

    else:

        print("Invalid Choice!")

budget_analysis(budget,expenses)
saving_status(profile,expenses,budget)
score=financial_score(profile,expenses,budget)
suggestions(profile,expenses,budget)

print("\nThank you for using Expense Insights!")
print("Every expense tells a story. Make yours a smart one!")
