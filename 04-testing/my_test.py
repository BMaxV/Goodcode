from my_main_file import my_main_f
from my_main_file import my_main_f_fake
from my_main_file import my_main_f_type_check

import random

def test_my_main_1():
    #this is the base line, it verifies that the function
    assert my_main_f(1,1) == 1+1

    assert my_main_f_type_check(1,1) == 1+1

def test_my_type_check():
    r=False
    try:
        my_main_f_type_check(1.2,2)
    except TypeError:
        r=True
    assert r

def test_my_fake():
    #this doesn't actually do the computation, but the test still passes!
    assert my_main_f_fake(1,1) == 1+1
    
    #see? not the !=
    assert my_main_f_fake(2,3) != 2+3 
    
    #so it might be important that the test 
    #tests for a wide of inputs. Like in the joke in the readme,
    #that can cover lots of values, or you can do it in a general way
    #if you can create fake data
    
    #it's unlikely that this will pass
    assert my_main_f_fake != random.random()+random.random()

def test_my_main_2():
    assert True

def test_my_timeouts():
    
    #put in proper termination for the pool object
    return
    #the good people at NASA have stipulated in their good code
    #guidelines that loops must finish in a certain amount of time
    #and or iterations.
    import multiprocessing
    
    with multiprocessing.Pool(2) as P:
        #don't do this...
        assert False
        #this is set up to fail
        task=P.apply_async(my_timeout_1,(1,2))
        task2=P.apply_async(my_timeout_2,(1,2,True))
        
        #this doesn't matter
        my_time=10
        time.sleep(my_time)
        
        try:
            #actually how DO you (force) quit async tasks?
            assert task.rdy()
        except AssertionError:
            task.hurr()
        try:
            #actually how DO you (force) quit async tasks?
            assert task2.rdy()
        except AssertionError:
            task.hurr()
        
        #terminate the pool and all it's tasks we created.
    
    a=1
