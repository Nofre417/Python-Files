# username = input('Your name: ' )
# if username == 'David':
#     print('David its me')
# elif username == 'Eva':
#     print('Eva nice girl')
# else:
#     print('Hi ', username)

def sum_finder(n):
    sum = 0
    for i in range(1,n + 1):
        sum += i
    print(sum)

sum_finder(5)