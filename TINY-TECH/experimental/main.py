import json
import os
from login_ui import LoginUI

class LoginSystem:
    def __init__(self):
        self.db_file = "user_accounts.json"
        self.initialize_database()
        self.ui = LoginUI(self)  # Pass self as reference to access methods
        
    def initialize_database(self):
        if not os.path.exists(self.db_file):
            initial_data = {
                "users": [
                    {
                        "email": "test@example.com",
                        "username": "test_user",
                        "password": "Test123",
                        "first_name": "Test",
                        "last_name": "User"
                    }
                ]
            }
            with open(self.db_file, 'w') as f:
                json.dump(initial_data, f, indent=4)

    def login(self, username, password):
        with open(self.db_file, 'r') as f:
            data = json.load(f)
            
        for user in data['users']:
            if user['username'] == username and user['password'] == password:
                return True, f"Welcome, {user['first_name']}!"
                
        return False, "Invalid username or password."

    def signup(self, user_data):
        with open(self.db_file, 'r') as f:
            data = json.load(f)
            
        if any(user['username'] == user_data['username'] for user in data['users']):
            return False, "Username already exists!"

        data['users'].append(user_data)
        
        with open(self.db_file, 'w') as f:
            json.dump(data, f, indent=4)

        return True, "Account created successfully!"

    def run(self):
        self.ui.run()

if __name__ == "__main__":
    app = LoginSystem()
    app.run()