Expenses = [] 
while True:
    options = input("Choose an option:add/view/quit/delete/edit/search:") 
    if options == "add":
        description = input("Enter description:")
        amount = float(input("Enter amount:"))
        category = input("Enter category:")
        Expenses.append({"description": description, "amount": amount, "category": category})
    elif options == "delete":
        delete_expense = input("Enter description to delete:")
        for expense in Expenses:
            if delete_expense == expense['description']:
                    Expenses.remove(expense)
                    break
    elif options == "search":
        search_expense = input("Enter description to search:")
        found = False
        for expense in Expenses:
            if search_expense == expense['description']:
                found = True
                print(f"Found: {expense['description']}: ${expense['amount']} ({expense['category']})")
                break
            else:
                if not found:
                    print("Expense not found")
               
    elif options == "edit":
        new_expense = input("Enter description to edit first:")
        for expense in Expenses:
            if expense['description'] == new_expense:
                edit_expense = input("Enter field(description,amount,category) to edit:")
                if edit_expense == 'description':
                    new_description = input("Enter new description:")
                    expense['description'] = new_description
                elif edit_expense == 'amount':
                    new_amount = float(input("Enter new amount:"))
                    expense['amount'] = new_amount
                elif edit_expense == 'category':
                    new_category = input("Enter new category:")
                    expense['category'] = new_category
    elif options == "view":
        if not Expenses:
            print("No expenses recorded.")
        else:
            for expense in Expenses:
                print(f"{expense['description']}: ${expense['amount']} ({expense['category']})")
    elif options == "quit":
        print("Exiting program")
        print("Description     | Amount | Category")
        print("-"*40)
        for expense in Expenses:
            print(f"{expense['description']:<15} | ${expense['amount']:7.2f} | {expense['category']:10}")
        total_expense = sum(expense['amount'] for expense in Expenses)
        print(f"Total Expenses: ${total_expense:.2f}")  
        total_category = {}
        for expense in Expenses:
            category = expense['category']
            amount = expense['amount']
            if category not in total_category:
                total_category[category] = amount
            else:
                total_category[category] += amount 
        for category, total in total_category.items():
            print(f"{category}: ${total:.2f}")
 
        break
        
    else:
        print("Invalid option")

    
    
    


