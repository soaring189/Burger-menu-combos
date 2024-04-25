import easygui
combos = {"Value": {"Beef burger": 5.69, "Fries": 1.00, "Fizzy drink": 1.00},
          "Cheezy": {"Cheeseburger": 6.69, "Fries": 1.00, "Fizzy drink": 1.00},
          "Super": {"Cheeseburger": 6.69, "Large Fries": 2.00,
                    "Smoothie": 2.00}}
choice = ""
while choice != "Exit":
    choice = easygui.buttonbox("What would you like to do?",
                               choices=["Output all", "Exit"],
                               title="MENU MAKER OPTIONS")
    if choice == "Output all":
        menu = ""
        for i, j in combos.items():
            menu += i + "\n"
            for k in j:
                menu += f"{k}: ${'%.2f' % j[k]}" + "\n"
            menu += "\n"
        easygui.msgbox(menu)
