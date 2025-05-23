class User:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"first name: {self.first_name}")
        print(f"last name: {self.last_name}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0
    
user = User("Humayun", "Rashid")
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.reset_login_attempts()
print(user.login_attempts)

