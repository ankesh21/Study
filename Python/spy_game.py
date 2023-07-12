def spy_game(spy_list):
    spy_cd=[0,0,7]
    rslt = 0
    index_no=0
    for i in spy_list:
        for j in spy_cd:
            if i == j:
                if spy_cd ==spy_list[index_no:index_no+3]:
                    rslt=1
                    break
            else:
                pass
        index_no+=1
    return rslt

print(spy_game([1,2,3,0,0,0,7,6]))

