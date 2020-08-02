
#concerning the unix philosophy of small programs that do one thing well

#this is what I ended up doing
#the disadvantage: d is basically a global. It's not a "real" global though, it's not actually globally accessible. 

#Good functional programming practice can still be applied

#there is only one "entry" and one "exit"
#everything can be logged and the isolated parts can be played
#back individually for testing
#it's very easy to read the code, because everything happens sequentially this way
#it's even easy to divide work for multiprocessing when the need arises
#for example 

def example_div(d):
    keys=list(d.keys())
    lkeys=len(keys)
    l1,l2=keys[:lkeys/2],keys[keys/2:]

#it could be more sophisticated, taking load into account,
#but I feel it's a good model to go by.

def f1(d):
    #for example this could be gui
    my_data=d.pop("data")
    print(my_data)
    return d

def f2(d):
    #this could be data processing
    my_data=[1,2,3]
    d={"data":my_data}
    return d

def main():
    d={}
    while True:
        d=f1(d)
        d=f2(d)
        if "quit" in d:
            break

if __name__=="__main__":
    main()
