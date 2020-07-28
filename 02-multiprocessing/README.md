# Multiprocessing

This is not a silver bullet that can be applied to everything and will make everything faster. The idea is to execute lots of things "in parallel" to save time in different places. For example reading and writing from disk or other hardware takes longer time that just calculating things. On the other hand, maybe there are tasks that are independent of each other and which can be done on different cores and can be recombined later.

Additional processes and splitting input and combining output have a cost associated with them, so it can be not worth it if the thing that is being done is really simple.

Regular python has a nice, neat structure, you can probably follow along what is being executed when and all that. Multiprocessing tries to be faster with some tradeoffs. There are many different ways to do it, this is the one I like best.
