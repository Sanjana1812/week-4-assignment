patients=[]


def add_patient():
    name=input("Enter patient name: ")
    patients.append(name)
    print("Patient Added")


def view_patients():
    print("Patients:",patients)


def search_patient():
    name=input("Enter patient name: ")

    if name in patients:
        print("Patient Found")

    else:
        print("Patient Not Found")


while True:

    print("\n1.Add Patient")
    print("2.View Patients")
    print("3.Search Patient")
    print("4.Exit")

    choice=input("Enter choice: ")

    if choice=="1":
        add_patient()

    elif choice=="2":
        view_patients()

    elif choice=="3":
        search_patient()

    elif choice=="4":
        print("Exited")
        break

    else:
        print("Invalid Choice")
