emp_work_hrs = [('ankesh',100),('Nishu',200),('rkesh',400),('rita',10000)]
def check_emp_wrk_hrs(emp_work_hrs):
    max_hrs = 0
    max_hrs_emp = ''
    for emp,hrs in emp_work_hrs:
        if hrs>max_hrs:
            max_hrs = hrs
            max_hrs_emp = emp
    return (max_hrs_emp,max_hrs)
print(check_emp_wrk_hrs(emp_work_hrs))