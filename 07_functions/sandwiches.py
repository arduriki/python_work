def make_sandwich(*items):
    print("Items in the sandwich:")
    for item in items:
        print(f"- {item}")


make_sandwich('bread', 'tomatoe', 'cheese')
print()
make_sandwich('bread', 'ham')
print()
make_sandwich('bread')