import os
import pickle
from contextlib import contextmanager

@contextmanager
def system_jail():
    os.chroot('safe_root/')
    yield
    os.chroot('/')

def deserialize():
    with system_jail():
        with open('./mydata.pickle', 'rb') as restoredata: 
            return pickle.load(restoredata)

if __name__ == '__main__':
    print(deserialize())
