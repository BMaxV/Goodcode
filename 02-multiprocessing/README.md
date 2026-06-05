# Multiprocessing

This is not a silver bullet that can be applied to everything and will make everything faster. The idea is to execute lots of things "in parallel" to save time in different places. For example reading and writing from disk or other hardware takes longer time that just calculating things. On the other hand, maybe there are tasks that are independent of each other and which can be done on different cores and can be recombined later.

Additional processes and splitting input and combining output have a cost associated with them, so it can be not worth it if the thing that is being done is really simple.

Regular python has a nice, neat structure, you can probably follow along what is being executed when and all that. Multiprocessing tries to be faster with some tradeoffs. There are many different ways to do it, this is the one I like best.

# why.

It's somewhat of a way out and as a technique it changes the way you can think about code just like loops or recursion do.

Assuming you're coming from a sequential mindset, the order you do things in, and the availability of data or results is obvious. Even if that's a main function inside a permanently running main loop.

```
while:
  A = calculate_A()
  B = calculate_B()
  update_visuals(A,B)
```

Even more basic, "normal" programs can be thought of starting, doing a thing, returning the result and shutting down. So games already have this more complex idea of "I'm continuously running and something may or may not happen in this loop". But the update and rendering process work the same way again.

So inside your main loop, the steps being taken are basically linear. And they are implicitly linear in exactly the order you specified. If any step takes more time, your entire program will halt and wait for it to finish before moving on.

Particularly for games, that's kinda bad, it's a problem that motivates solving it. We are on a schedule, we prefer to be done within 1/framerate . That's nearly guaranteed or easier for FPS or games with few elements, but less so for more complex games. Maybe you have an "internal time" for your game that does things "on daybreak" and that result in somewhat isolated peaks in "needed calculations". 

Multiprocessing is the way to keep your game running, while doing the complicated thing in the background and integrating the result when you have it.

If you think about it, a computer running is already lots of different processes running "at the same time". In the past, that had to be solved by giving a share of processing time on the CPU to each process. Stopping and resuming as you went. With Moore's law slowing down, CPUs went parallel. [...]

Doing things in parallel gives you a new set of constraints. Sharing data between processes is kinda "meh" and "hard-ish" and doesn't really serve the point of why you're doing it in the first place (big isolated problem). So a very good way of doing it, is preparing all the data, handing it over and just checking whether the task is done and then eventually collecting the result.

This means, you can't use "private" or "global" variables the same way as previously. It's inconvenient. Accessing a private or global variable that may or may not have changed is no longer just "bad practice", it is actually hard.

That forces you to write very functional code, that really does only take the data you start the process with and has a definite end point and return type.

And it's a neat reminder, if you have a bunch of functions that do unrelated things, the condition for the main function to finish is that those things are done, but not necessarily in the order you wrote them in. 

It's more about thinking of it as a chance to reduce complexity to you as the programmer. You want to avoid baking implications into the order you write your functions in, you want stuff to depend on data and state. It's longer do(A) then do(B) then do(C) then do(D)  instead it's do(stuff) and tell when you're done. 

Also, yes, "being done in time" comes into focus a bit. There are lots of techniques to deal with loading times, sometimes stuff is assumed to be quick enough and then it stutters when you run into problems after all. Or it looks bad for n frames until the higher detail model or texture gets loaded
