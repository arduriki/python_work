current_users = ['sirjack', 'kone', 'bioz', 'dawy', 'arduriki']
new_users = ['savitaar', 'SIRJACK', 'occupytheweb', 'Arduriki', 'goalaverage']

for new_user in new_users:
    if new_user.lower() in current_users:
        print("Sorry, enter a new username.")
    else:
        print("The username is available.")