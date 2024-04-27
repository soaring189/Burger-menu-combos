combos = {"Value": {"Beef burger": 5.69, "Fries": 1.00, "Fizzy drink": 1.00},
          "Cheezy": {"Cheeseburger": 6.69, "Fries": 1.00, "Fizzy drink": 1.00},
          "Super": {"Cheeseburger": 6.69, "Large Fries": 2.00,
                    "Smoothie": 2.00}}
for i, j in combos.items():
    print(i)
    for k in j:
        print(f"{k}: ${'%.2f' % j[k]}")
    print()
