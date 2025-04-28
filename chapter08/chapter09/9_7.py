class User:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"first name: {self.first_name}")
        print(f"last name: {self.last_name}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}")

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = ["can add post", "can delete post", "can ban user"]
    
    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)

admin = Admin('Jacob', 'Oram')
admin.show_privileges()