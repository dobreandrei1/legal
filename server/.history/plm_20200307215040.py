import os

if os.fork():
    print('hello')
else:
    print('world')