import json
from datetime import datetime as dt


class expense:

    def __init__(self, amount=0, description="", name="", date=None):
        self.description = description
        self.rate = amount
        # date ah user input panra date ah set panum, illa na default ah current date ah set panum
        self.date = dt.now().strftime("%d-%m-%Y") if not date else date
        self.data = f"{name}.json"  # json file create panum, athula expenses store panum

    def __str__(self):   # ithu object a panama nama define panra string ah return panum
        return f"Expense(rate={self.rate}, description='{self.description}')"

    def file(self):
        try:
            with open(self.data, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def add_expense(self):

        data = self.file()
        found = False

        for i in data:
            if i["Date"] == self.date:
                found = True
                break

        if not found:
            i = {
                "Date": self.date,
                "Expense": [],
                "Total_expense": 0
            }
            data.append(i)

        i["Expense"].append({
            "Expense": self.description,
            "Rate": self.rate
        })

        i["Total_expense"] = sum(
            j["Rate"] for j in i["Expense"]
        )

        data.sort(
            key=lambda x: dt.strptime(x["Date"], "%d-%m-%Y")
        )

        with open(self.data, "w") as f:
            json.dump(data, f, indent=4)

        print("Expense added successfully!")
        print("Total expense:", i["Total_expense"])


# Main program
print("Welcome to the Expense Tracker!")
name = input("Enter your name: ").capitalize()
print("""
        1.today's expense
        2.custom date expense
        3.exit
        """)
choice=input("Enter a choice..").lower()
if choice=="exit":
    exit()
elif choice.isdigit():
    choice=int(choice)      

match choice:
    case 1:
        
        while True:

            description = input("Enter the expense or ( type 'exit' to quit): ")
            if description.lower() == "exit":
                break
            try:
                amount = int(input("Enter the amount of the expense: "))
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
                continue
            exp = expense(amount, description, name)
            exp.add_expense()
    case 2:
        date = input("Enter the date (dd-mm-yyyy): ")
        while True:
            description = input("Enter the expense or ( type 'exit' to quit): ")
            if description.lower() == "exit":
                break
            try:
                amount = int(input("Enter the amount of the expense: "))
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
                continue

            exp = expense(amount, description, name, date)
            exp.add_expense()
    case 3:
        print("Thank you for using the application")
        exit()
    case _:
        print("Invalid choice")
