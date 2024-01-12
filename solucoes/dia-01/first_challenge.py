user_input = input('Type a number: ')
int_user_input = int(user_input)

if int_user_input % 2 == 0:
    print(f'{int_user_input} is a pair number')
else:
    print(f'{int_user_input} is a odd number')
