def login(username, password):
    if username == "admin" and password == 1234:
        print("Login Successful")
    else:
        print("Invalid Username or Password")

# Example
login("admin", 1234)
login("user", 1111)