"""
A dictionary is simply a key-value paired data type in Python
"""

annettes_facebook_logins = {
    'email': "annette@gmail.com",
    'password': "password123"
}


email = input("Enter your email: ")
password = input("Enter your password: ")


if (email == annettes_facebook_logins['email'] and password == annettes_facebook_logins["password"]):
    print("You successfully logged in to facebook")
else:
    print("Invalid username and password")