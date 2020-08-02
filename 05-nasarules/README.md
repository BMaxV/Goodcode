# Goodcode



The original 10 Rules

x    Avoid complex flow constructs, such as goto and recursion
x    All loops must have fixed bounds (this prevents runaway code)
-    Avoid heap memory allocation
x    Restrict functions to a single printed page
x    Use a minimum of two runtime assertions per function
x    Restrict the scope of data to the smallest possible
(x)  Check the return value of all nonvoid functions, or cast to void to indicate the return value is useless
x    Use the preprocessor sparingly
(x)  Limit pointer use to a single dereference, and do not use function pointers
x    Compile with all possible warnings active; all warnings should then be addressed before the release of the software

several things that are good advice. let me resort this.

x    Avoid complex flow constructs. Period. 
x    All loops must have fixed bounds. But only if it's safety critical.
x    Restrict functions to a single printed page
x    Restrict the scope of data to the smallest possible
x    Minimize assumptions that must be true for the code to run successfully(Use a minimum of two runtime assertions per function.)
x    Use the preprocessor sparingly

As in, if you need to double check with tools or metaprogram the code too much, you're not writing the code cleanly in the first place and you should do that.

x    Compile with all possible warnings active; all warnings should then be addressed before the release of the software

There are no warnings in python. Sooo... hm. Run all tests?

(x)  Check the return value of all nonvoid functions, or cast to void to indicate the return value is useless

hm check against what? "make sure everything you do is within normal parameters"?

(x)  Limit pointer use to a single dereference, and do not use function pointers.

This is actually good advice. I found that when things get more complicated and I ended up recreating a memory in form of a dictionary, and it's absolutely a good idea to have one place to pop things from the dict.

And functions are never renamed or passed by value, they're only used directly. In fact, the cases where this needs to be done are areas like multiprocessing that are notoriously tricky.

(-    Avoid heap memory allocation.

 There is no heap memory allocation in pyhton)

