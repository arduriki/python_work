sandwich_orders = ['tuna', 'pastrami', 'chicken', 'beef', 'veggie', 'turkey']
finished_sandwiches = []

print("The deli has no pastrami, so there won't be any pastramy sandwiches.\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    making_sandwich = sandwich_orders.pop()
    print(f"I made your {making_sandwich} sandwich.")
    finished_sandwiches.append(making_sandwich)

print("\nThese are the sandwiches that I've done:")
for sandwich in finished_sandwiches:
    print(sandwich)

