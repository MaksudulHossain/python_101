class User:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"first name: {self.first_name}")
        print(f"last name: {self.last_name}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}")

user1 = User("Humayun", "Rashid")
user2 = User("Mamunur", "Rashid")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()
