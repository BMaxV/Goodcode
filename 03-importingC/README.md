compile the .so object you need:

gcc -shared -o mysharedobject.so -fPIC myexample.c

source https://stackoverflow.com/questions/14884126/build-so-file-from-c-file-using-gcc-command-line

then call python, it should work.

python3 main.py
