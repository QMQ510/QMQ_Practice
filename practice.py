for x in range(1, 100):
    if x % 2 == 0:
        print(f"{x}")
number = len([x for x in range(1, 100) if x % 2 == 0])
print(f"We have {number} even numbers")
