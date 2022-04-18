# Goodcode
trying to write Good Code about nothing

I have an interest in doing things "neatly". I wouldn't call it an obsession but seeing different solutions, there is some preferences for "good" solutions and "bad" solutions. There is some good subjectivity in there, but there are some general rules too.

So the goal of this repo would be an executable that "ticks" all the boxes and a form actually containing bullet points and boxes to check. I want to put in some "minimum effort" stuff I have picked up over the years.

In particular, there are some ideals that are frequently ignored? It's probably a spectrum between "getting something done" and getting it done Right and most of the time stuff ends up on the "it works" side more than the "this makes sense to do" side.

So. What should programs be like?

 * They should do X.
 * They should do it reliably.
 * That should be verifiable. This can vary a bit. Sometimes it's good enough to just run it again and checking that it worked this time. The most common purpose of tests is probably to keep output consistent and independent of internal changes. Sometimes it's helpful to define tests as a target. Verifiable builds are also something that comes to mind, although the efforts are focused on *really* compiled languages.
 * Parts of programs should be easy to replace or fix. For that it is necessary that the part is easy to understand. This has some variable space(?) around it. Things that are small are easy to understand. Things that are consistently formatted are easier to understand. Things that don't do "weird stuff" are easier to understand. The "magic number 5" is a good guide. There is the "Zen of Python". There is a NASA code writing guide that has 10 somewhat transferable rules.
 
 * All of that should cover the UNIX philosophy of doing small things and doing them well.
Beyond this point, things get even more vague.
 * There is the step of optimzing things to make stuff fast or more fault tolerant. This might increase complexity and dependencies, so they are definitely no longer as easy to understand. Or at least sometimes. If it's done "right", maybe the added complexity can be treated like any other step in the pyramid of complexity.
 * This ties into interoperability. There is the ideal that these small programs should pass simple types, like strings. Again, because they are easy to understand, you can write your own parsers if necessary. The more you can rely on built-in types, the less effort you have to go through to make different libraries work together. When custom types are useful, it pays off to have serialization functions and functions that can recreate the object from text. Also, usually projects are written in some agreed upon language. Which is a bit sad, because if someone has already invented the wheel I want to use in a different language, it's often not possible to just use that. I shouldn't have to care which language you prefer, it's all the same to the computer anyway. I just want it to work.
 * There is "functional programming" that tries to be "side effect free". Meaning that programs should only work with data that it is given access to explicitly and nothing else.
 * There is also stuff in the meta space. Making sure things are portable and that they fit "nicely" into some framework, as a package, or to make sure it's easy to install. Having a good readme that actually fits into any of the various "description" fields that will inevitably surround the program if it is available for download anywhere.

Here are some naming conventions https://namingconvention.org/python/
Here is autopep8, because you don't need to know how I write code when I write it, you just need to be able to read the final result. https://pypi.org/project/autopep8/


here are some cool CSS tricks that might be handy in the future

https://markodenic.com/css-tips/
