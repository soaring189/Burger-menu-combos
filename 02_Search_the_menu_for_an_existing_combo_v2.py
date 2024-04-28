import easygui
combos = {"Value": {"Beef burger": 5.69, "Fries": 1.00, "Fizzy drink": 1.00},
          "Cheezy": {"Cheeseburger": 6.69, "Fries": 1.00, "Fizzy drink": 1.00},
          "Super": {"Cheeseburger": 6.69, "Large Fries": 2.00,
                    "Smoothie": 2.00}}
choice = ""
while choice != "Exit" and choice is not None:
    choice = easygui.buttonbox("What would you like to do?",
                               choices=["Find combo", "Output all", "Exit"],
                               title="MENU MAKER OPTIONS")
    if choice == "Find combo":
        combo_name = easygui.enterbox("Please enter the combo name you want to find")
        if combo_name is not None:
            for i, j in combos.items():
                if i.upper() == combo_name.upper():
                    search_result = [i]
                    for k in combos[i]:
                        search_result.append(f"{k}: ${'%.2f' % j[k]}")
                    search_result = '\n'.join(search_result)
                    change = easygui.buttonbox(search_result + "\n" + "\n" + "Do you want to make any changes to the current combo?", choices=["Yes", "No"])
                    if change == "Yes":
                        modified_combo = {}
                        modified_name = easygui.enterbox("Please enter the new combo name")
                        change_result = [modified_name]
                        for item in range(0, 3):
                            while True:
                                modified_item = easygui.enterbox(f"Please enter the name of item {item + 1}")
                                if modified_item in modified_combo:
                                    easygui.msgbox("This item is already in the combo")
                                elif modified_item is not None and modified_item != "":
                                    break
                            modified_item_price = easygui.enterbox(f"Please enter the price of item {item + 1}")
                            while type(modified_item_price) != float:
                                try:
                                    modified_item_price = float(modified_item_price)
                                except ValueError:
                                    easygui.msgbox("Please enter a number")
                                    modified_item_price = easygui.enterbox(f"Please enter the price of item {item + 1}")
                            modified_combo[modified_item] = modified_item_price
                            change_result.append(f"{modified_item}: ${'%.2f' % modified_item_price}")
                        change_result = '\n'.join(change_result)
                        confirm = easygui.buttonbox(f"\nChange\n\n{search_result}\n\nTo\n\n{change_result}", title="Confirm changes", choices=["Yes", "No"])
                        if confirm == "Yes":
                            combos.pop(i)
                            combos[modified_name] = modified_combo
                    break
                else:
                    easygui.msgbox("This combo is not on the menu")
                    break
    elif choice == "Output all":
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
