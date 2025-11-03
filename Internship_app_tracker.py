# Mini project E-30 : Internship Application Tracker
#Aveek Kumar
#Enrollment No - 2502140127

appli = []

def add():
    company = input("Company: ")
    role = input("Role: ")
    status = input("Status (applied/offer/rejected): ").lower()
    deadline = input("Deadline (YYYY-MM-DD): ")
    new_app = {
        "company": company,
        "role": role,
        "status": status,
        "deadline": deadline
    }
    appli.append(new_app)
    print("✅ Application added!\n")
def show():
    if len(appli) == 0:
        print("No applications yet.\n")
    else:
        print("-----All Applications-----")
        for app in appli:
            print(app["company"], "|", app["role"], "|", app["status"], "|", app["deadline"])
        print()
def count():
    counts = {}
    for app in appli:
        status = app["status"]
        if status in counts:
            counts[status] = counts[status] + 1
        else:
            counts[status] = 1
    print(" Count by status:", counts , "\n")
def due():
    applied_apps = []
    for app in appli:
        if app["status"] == "applied":
            applied_apps.append(app)
    if len(applied_apps) == 0:
        print("No 'applied' applications.\n")
        return
    early = min(applied_apps, key=lambda x: x["deadline"])
    print("Next due:", early["deadline"], "@", early["company"], "\n")

#Main output display
while True:
    print("=+=+=+= Welcome to Internship Tracker =+=+=+=")
    print("1. Add  2. Show  3. Count  4. Next Due  5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add()
    elif choice == "2":
        show()
    elif choice == "3":
        count()
    elif choice == "4":
        due()
    elif choice == "5":
        print("You have exited from the program . Thank you :)  ")
        break
    else:
        print("! Invalid choice !")
