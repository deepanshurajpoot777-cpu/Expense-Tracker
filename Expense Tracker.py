expenses=[]

while True:
    print("=========EXPANSES TRACKER==========")
    print("1.Add Expenses")
    print("2.view Expenses")
    print("3.Total Expenses")
    print("4.Delete Expenses")
    print("5.Exit")

    choice=input("enter your choice")

    if choice=="1":
        exp=input("enter expenses name")
        ammt=int(input("enter Ammount"))
        expenses.append((exp,ammt))
        print("Expense added!")
    elif choice=="2":
        if len(expenses)==0:
            print("NO expense Found")
        else:
            for exp,ammt in expenses:
                print(exp,"-",ammt)
    elif choice=="3":
        total=0
        for exp,ammt in expenses:
            total=total+ammt
            print("Total Expenses=",total)
    elif choice=="4":
        exp=input("Enter expense name to delete")

        found=False
        for item in expenses:
            if item[0]==exp:
                expenses.remove(item)
                found=True
                print("Deleted")
                break
            if found==False:
                print("Expenses not found")
        
    elif choice=="5":
        print("program closed.")
        break
    else:
        print("Invalid choice")