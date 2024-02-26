#5-8
usernames = ['admin','adam','sami','emad','rana']
for user in usernames:
    if user.lower() == 'admin':
        print('Hello admin')
    else:
        print(f"hello {user}")

#5-9
usernames = []
if not usernames:
    print('we need users')
else:
    for user in usernames:
        if user.lower() == 'admin':
            print('Hello admin')
        else:
            print(f"hello {user}")
