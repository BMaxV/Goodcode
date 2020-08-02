
def my_main_f(a,b):
    return a+b

def my_main_f_fake(a,b):
    return 2
    
def my_main_f_type_check(a,b):
    if type(a)!=int:
        raise TypeError
    return a+b

def my_timeout_1(a,b):
    #this function will never finish.
    while True:
        a=b
    return a+b
    
def my_timeout_2(a,b,my_condition):
    #this function CAN never finish, depending on my_condition
    while my_condition:
        a=b
    return a+b
