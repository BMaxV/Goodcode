
#so this is what I ended up doing to reign in complexity
#the disadvantage: d is basically a global. It's not a "real" global though, it's not actually globally accessible. 
#Good functional programming practice can still be applied

def f1(d):
    a=1
    return d

def f2(d):
    a=1
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
