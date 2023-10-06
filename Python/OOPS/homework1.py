""" try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print('the list values are not number')

print('----------------------------------')

try:
    x=5
    y=0
    z=x/y
except ZeroDivisionError:
    print(str(x)+" can't be devided by "+str(y))
finally:
    print('All done')
 """

def ask():
    while True:
        try:
            num=int(input('Input an Integer : '))
        except:
            print('An error occured! Please try again')
            continue
        else:
            print('Thank you , your number square is '+str(num**2))
            break

ask()
