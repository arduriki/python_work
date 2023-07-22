car = 'subaru'
print("Is car == 'subaru? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print("\nTherefore, 'audi' is different, right?")
print(car != 'audi')

jordi = 36
keren = 15
print("\nAre Jordi and Keren older than 18? I don't think so...")
print(jordi >= 18 and keren >= 18)

jose = 45
print("\nBut Jordi's brother is older than 18, right?")
print(jordi >= 18 and jose >= 18)

print("\nNo matter how old are Jordi and Keren, one of them can enter into the room.")
print(jordi >= 18 or keren >= 18)

dario = 12
print("\nWhat about if we change Jordi for Dario? Nobody would enter, right?")
print(dario >= 18 or keren >= 18)

users = ['kone', 'adwix', 'bioz']
nickname = 'Arduriki'
print("\nMy nickname is Arduriki, does it exist?")
print(nickname.lower() in users)

print("\nWhat about my friend Bioz?")
print('Bioz'.lower() in users)

if nickname.lower() not in users:
    print(f"{nickname} is no in the user's list.")