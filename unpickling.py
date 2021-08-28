import os
import pickle

def deserialize():
    data = ''
    with open('./pickle.dat', 'rb') as restoredata: 
        data = pickle.load(restoredata)
    return data

if __name__ == '__main__':
    print(deserialize())
