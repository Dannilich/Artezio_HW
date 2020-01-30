users_autorization = {"Ivan":"stalinGulag", "Shrek":"42069"}

user_is_logged_in = True
name_is_selected = False
password_is_correcr = False

while(user_is_logged_in):
    if not name_is_selected:
        user = input("Enter your name: ")
        if user in users_autorization: name_is_selected = True
        else: 
            print("Enter correct name !") 
            continue
    else:
        if not password_is_correcr:
            password = input("Enter password: ")
            if password == users_autorization[user]:
                print("Password for user: ", user, " is correct")
                password_is_correcr = True
                continue
            else:
                print("Password for user: ", user, " is incorrect")
                print("Please try again...")
                continue
        else:#Добавленно для расширяемости (мне так интереснее, потому что код кажеться чище)
             user_is_logged_in = False
             break
