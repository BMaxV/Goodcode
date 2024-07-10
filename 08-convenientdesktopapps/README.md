writing easy to use, convenient desktop apps is really difficult.

# guis

There are too many GUI frameworks to count, all radically different. This doesn't even relate to the language. The only unified framework we have that is really cross platform and adopted and supported is html. That's why "bundling everything in electron" (which essentially packages a browser and runs the software as a website) is popular and makes sense.

Obviously that's not ideal.

So for now, there is no harm in just picking any. It's chaos anyway.

# tray Icons / interactive background stuff.

pystray works for me.

# notifications

Yes. They work. py notify or something.

# autostart

"place something in ~/.config/autostart"

This can't be done on install, has to be done on "first run" which is a bit of a pain for python programs, since a "user" would still have to navigate and use pip or something.

# python packaging

I don't even know man.

Use setup.py and setuptools.

# "real" packaging

See the other file.

.deb this seems like an OK guide, have not tested it though:



original source:
https://www.sindastra.de/p/1684/how-to-make-a-basic-debian-and-ubuntu-package-deb-the-easy-way



# registering as a thing/file in the "start menu"

???



