# Let's consider the username program again and this time add passwords. Test 
# to see how the output changes by changing the values of "user" and "password"

username1 = "Bobby"
password1 = "baloonboy"
username2 = "Sally"
password2 = "simplysecure"
username3 = "Joey"
user = username1
password = "hello"

if user == username1:
    if password == password1:
        print("Welcome, " + username1)
    else:
        print("Wrong password, " + username1)
elif user == username2:
    if password == password2:
        print("Welcome, " + username2)
    else:
        print("Wrong password" + username2)
else:
    print("Intruder alert!")