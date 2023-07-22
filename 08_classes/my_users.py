import admin


user1 = admin.User('jordi', 'ardura', 'arduriki', 'arduriki@gmail.com')
user2 = admin.User('gerard', 'romero', 'romerito', 'hola@jijantes.com')
user3 = admin.User('adria', 'neila', 'neilasan', 'adria.neila@somvera.cat')

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

user4 = admin.User('dario', 'ardura', 'chanchito', 'darioardura@gmail.com')
user4.describe_user()
user4.greet_user()

user4.increment_login_attempts()
user4.increment_login_attempts()
user4.increment_login_attempts()
print(user4.login_attempts)

user4.reset_login_attempts()
print(user4.login_attempts)

user5 = admin.Admin('keren', 'ardura', 'ardurika', 'kerenardura@gmail.com')
user5.privileges.show_privileges()