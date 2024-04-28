import easygui
combos = {"Value": {"Beef burger": 5.69, "Fries": 1.00, "Fizzy drink": 1.00},
          "Cheezy": {"Cheeseburger": 6.69, "Fries": 1.00, "Fizzy drink": 1.00},
          "Super": {"Cheeseburger": 6.69, "Large Fries": 2.00, "Smoothie": 2.00}}
choice = ""
while choice != "Exit" and choice is not None:
    choice = easygui.buttonbox("What would you like to do?",choices=["Add combo", "Find combo", "Delete combo", "Output all", "Exit"],title="MENU MAKER OPTIONS")
    if choice == "Add combo":
        fields = ["New combo name:", "Item name 1", "Price 1", "Item name 2", "Price 2", "Item name 3", "Price 3"]
        while True:
            new_combo = easygui.multenterbox('Enter the new combo information:', 'Add combo', fields)
            try:
                new_combo[2] = float(new_combo[2])
                new_combo[4] = float(new_combo[4])
                new_combo[6] = float(new_combo[6])
                break
            except ValueError:
                easygui.msgbox("Please enter a number for the price")
        add_result = f"{new_combo[0]}\n{new_combo[1]}: ${'%.2f' % new_combo[2]}\n{new_combo[3]}: ${'%.2f' % new_combo[4]}\n{new_combo[5]}: ${'%.2f' % new_combo[6]}"
        confirm = easygui.buttonbox(f"Do you want to add\n\n{add_result}\n\nto the menu?", title="Confirm add", choices=["Yes", "No"])
        if confirm == "Yes":
            combos[new_combo[0]] = {new_combo[1]: new_combo[2], new_combo[3]: new_combo[4], new_combo[5]: new_combo[6]}
    elif choice == "Find combo":
        combo_name = easygui.enterbox("Please enter the combo name you want to find")
        if combo_name is not None:
            for i, j in combos.items():
                if i.upper() == combo_name.upper():
                    defaults = [i]
                    search_result = [i]
                    for k in combos[i]:
                        search_result.append(f"{k}: ${'%.2f' % j[k]}")
                        defaults.append(k)
                        defaults.append(j[k])
                    search_result = '\n'.join(search_result)
                    change = easygui.buttonbox(search_result + "\n" + "\n" + "Do you want to make any changes to the current combo?", choices=["Yes", "No"])
                    if change == "Yes":
                        fields = ["New combo name:", "Item name 1", "Price 1", "Item name 2", "Price 2", "Item name 3", "Price 3"]
                        while True:
                            new_combo = easygui.multenterbox('Enter the new combo information:', 'Change combo', fields, defaults)
                            try:
                                new_combo[2] = float(new_combo[2])
                                new_combo[4] = float(new_combo[4])
                                new_combo[6] = float(new_combo[6])
                                break
                            except ValueError:
                                easygui.msgbox("Please enter a number for the price")
                        change_result = f"{new_combo[0]}\n{new_combo[1]}: ${'%.2f' % new_combo[2]}\n{new_combo[3]}: ${'%.2f' % new_combo[4]}\n{new_combo[5]}: ${'%.2f' % new_combo[6]}"
                        confirm = easygui.buttonbox(f"\nChange\n\n{search_result}\n\nTo\n\n{change_result}", title="Confirm changes", choices=["Yes", "No"])
                        if confirm == "Yes":
                            combos.pop(i)
                            combos[new_combo[0]] = {new_combo[1]: new_combo[2], new_combo[3]: new_combo[4], new_combo[5]: new_combo[6]}
                    break
                else:
                    easygui.msgbox("This combo is not on the menu")
                    break
    elif choice == "Delete combo":
        delete = easygui.enterbox("Please enter the combo name you want to delete")
        for i, j in combos.items():
            if i.upper() == delete.upper():
                confirm = easygui.buttonbox(f"Confirm whether to delete {i}", choices=["Yes", "No"])
                if confirm == "Yes":
                    del combos[i]
                    easygui.msgbox(f"{i} has been deleted from the menu")
                break
        else:
            easygui.msgbox("This combo is not on the menu")
    elif choice == "Output all":
        if combos != {}:
            max_name_length = max(len(i) for i in combos.keys())
            max_item_length = max(len(str(j)) for i in combos.values()
                                  for j in i.keys())
            if max_name_length < 5:
                max_name_length = 5
            menu = f"┌{'─' * max_name_length}┬{'─' * max_item_length}┬{'─' * 4}┬{'─' * 7}┐\n"
            menu += f"│{' ' * max_name_length * 2}│ Item{' ' * (max_item_length*2-5)}│ Price  │ Total price  │\n"
            menu += f"├{'─' * max_name_length}┼{'─' * max_item_length}┴{'─' * 4}┼{'─' * 7}┤\n"
            menu += f"│{' ' * int(max_name_length-5)}Combo name{' ' * int(max_name_length-5)}│{' ' * (max_item_length - 1)} Combo items{' ' * (max_item_length - 1)}│{' ' * 14}│\n"
            first_outer_loop = True
            for outer_index, (i, j) in enumerate(combos.items()):
                total_price = 0
                if first_outer_loop:
                    menu += f"├{'─' * max_name_length}┼{'─' * max_item_length}┬{'─' * 4}┼{'─' * 7}┤\n"
                    first_outer_loop = False
                else:
                    menu += f"├{'─' * max_name_length}┼{'─' * max_item_length}┼{'─' * 4}┼{'─' * 7}┤\n"
                menu += f"│ {i + ' ' * (max_name_length * 2 - len(i) - 1)}│"
                for inner_index, (k, l) in enumerate(j.items()):
                    total_price += j[k]
                    if inner_index != len(j) - 1:
                        menu += f" {k + ' ' * (max_item_length * 2 - len(k) - 1)}│{' ' * int((7-len('%.2f' % j[k]))/2)}${'%.2f' % j[k]}{' ' * (int((7-len('%.2f' % j[k]))/2)+ ((7-len('%.2f' % j[k]))%2))}│{' ' * 14}│\n"
                    else:
                        menu += f" {k + ' ' * (max_item_length * 2 - len(k) - 1)}│{' ' * int((7-len('%.2f' % j[k]))/2)}${'%.2f' % j[k]}{' ' * (int((7-len('%.2f' % j[k]))/2)+ ((7-len('%.2f' % j[k]))%2))}│{' ' * int((13-len('%.2f' % total_price))/2)}${'%.2f' % total_price}{' ' * (int((13-len('%.2f' % total_price))/2)+(13 - len('%.2f' % total_price))%2)}│\n"
                    if outer_index == len(combos) - 1 and inner_index == len(j) - 1:
                        menu += f"└{'─' * max_name_length}┴{'─' * max_item_length}┴{'─' * 4}┴{'─' * 7}┘\n"
                    if inner_index != len(j) - 1:
                        menu += f"│{' ' * max_name_length * 2}├{'─' * max_item_length}┼{'─' * 4}┤{' ' * 14}│\n"
                        menu += f"│{' ' * (max_name_length * 2)}│"
            easygui.msgbox(menu)
        else:
            easygui.msgbox("The menu is empty")