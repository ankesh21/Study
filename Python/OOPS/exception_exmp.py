def test_exception():
    while True:
        try:
            user_num=int(input('Please provide a number'))
        except:
            print('Opps ..its not a number')
            continue
        else:
            print(str(user_num)+' is a valid number')
            break
        finally:
            print('end of the test')
            print('-----------------------------')

test_exception()