current_users = ['rome','juliet','python','romeo','alfa']
new_users = ['alfa','beta']

for new_user in new_users:
    if new_user in current_users:
        print('The username has been taken.')
