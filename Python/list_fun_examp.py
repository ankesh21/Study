def filter_even_num(num_list):
    num_list1=[]
    for i in num_list:
        if i%2!=0:
            num_list1.append(i)
    return num_list1

print(filter_even_num([1,2,3,4,5,6,7,8,9]))

