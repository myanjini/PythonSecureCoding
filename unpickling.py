import os
import pickle

def deserialize():
    with open('./pickle.dat', 'rb') as restoredata: 
        return pickle.load(restoredata)

if __name__ == '__main__':
    print(deserialize())
