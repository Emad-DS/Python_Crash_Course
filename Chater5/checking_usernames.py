current_users = ['Admin','adam','Sami','emad','rana']
new_users = ['adam','sami','kermit','john']
current_user_lower_case = []

for user in current_users:
    current_user_lower_case.append(user.lower())
print(current_user_lower_case)
print(current_users)

for user in new_users:
    if user.lower() in current_user_lower_case:
        print(f"{user} in use")
    else:
        print(f"{user} username accepted")