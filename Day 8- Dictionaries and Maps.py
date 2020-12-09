# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
name_numbers = [input().split() for i in range(n)]
phone_book = {k:v for k,v in name_numbers}

while True:
    try:
        
        name = input()
        if name in phone_book:
            print('{}={}'.format(name,phone_book[name]))
        else:
            print('Not found')
    except:
        break



