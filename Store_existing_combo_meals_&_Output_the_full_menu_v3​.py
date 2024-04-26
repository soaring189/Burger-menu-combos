import easygui
combos = {"Value": {"Beef burger": 5.69, "Fries": 1.00, "Fizzy drink": 1.00},
          "Cheezy": {"Cheeseburger": 6.69, "Fries": 1.00, "Fizzy drink": 1.00},
          "Super": {"Cheeseburger": 6.69, "Large Fries": 2.00,
                    "Smoothie": 2.00}}
choice = ""
while choice != "Exit" and choice is not None:
    choice = easygui.buttonbox("What would you like to do?",
                               choices=["Output all", "Exit"],
                               title="MENU MAKER OPTIONS")
    if choice == "Output all":
        max_name_length = max(len(i) for i in combos.keys())
        max_item_length = max(len(str(j)) for i in combos.values()
                              for j in i.keys())
        if max_name_length < 5:
            max_name_length = 5
        menu = f"┌{'─' * max_name_length}┬{'─' * max_item_length}┬{'─' * 4}┐\n"
        menu += f"│{' ' * max_name_length * 2}│ Item{' ' * (max_item_length*2-5)}│ Price  │\n"
        menu += f"├{'─' * max_name_length}┼{'─' * max_item_length}┴{'─' * 4}┤\n"
        menu += f"│{' ' * int(max_name_length-5)}Combo name{' ' * int(max_name_length-5)}│{' ' * (max_item_length - 1)} Combo items{' ' * (max_item_length - 1)}│\n"
        first_outer_loop = True
        for outer_index, (i, j) in enumerate(combos.items()):
            if first_outer_loop:
                menu += f"├{'─' * max_name_length}┼{'─' * max_item_length}┬{'─' * 4}┤\n"
                first_outer_loop = False
            else:
                menu += f"├{'─' * max_name_length}┼{'─' * max_item_length}┼{'─' * 4}┤\n"
            menu += f"│ {i + ' ' * (max_name_length * 2 - len(i) - 1)}│"
            for inner_index, (k, l) in enumerate(j.items()):
                menu += f" {k + ' ' * (max_item_length * 2 - len(k) - 1)}│ ${'%.2f' % j[k]}  │\n"
                if outer_index == len(combos) - 1 and inner_index == len(j) - 1:
                    menu += f"└{'─' * max_name_length}┴{'─' * max_item_length}┴{'─' * 4}┘\n"
                if inner_index != len(j) - 1:
                    menu += f"│{' ' * max_name_length * 2}├{'─' * max_item_length}┼{'─' * 4}│\n"
                    menu += f"│{' ' * (max_name_length * 2)}│"
        easygui.msgbox(menu)
