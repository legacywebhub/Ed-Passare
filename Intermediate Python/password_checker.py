database = [
    {'username': "Mr. paulson", 'password': "12345"},
    {'username': "dumebi", 'password': "dumebi123"},
    {'username': "zoe", 'password': "zoe123"},
    {'username': "alexander", 'password': "###123"},
    {'username': "bryant", 'password': "bryant"},
    {'username': "emeka", 'password': "password"}
]

login_attempts = 0
maximum_attempts = 3  # Maximum allowed attempts

while login_attempts < maximum_attempts:

    try:
        username = input('Enter your username: ')
        password = input('Enter your password: ')
        found = False # This flag checks if the user is found in the database

        for record in database:
            if (username == record['username'] and password == record['password']):
                print(f'Congratulations {username}, you have successfully logged in!')
                found = True
                break # break out of the for loop
        
        if found == True:
            break # break out of the while loop
        else:
            print('Incorrect username or password. Please try again.')
            login_attempts += 1  # Increment the login attempt counter
    except:
        print('Oops.. an error occured. Please try again later')

if login_attempts == maximum_attempts:
    print('You have reached the maximum number of login attempts.')