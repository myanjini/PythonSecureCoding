import os
import pickle

def deserialize():
    data = ''
    with open('./mydata.pickle', 'rb') as restoredata: 
        data = pickle.load(restoredata)
    return data

if __name__ == '__main__':
    print(deserialize())
