import json

def deserialize():
    with open('./mydata.json', 'r') as f: 
        return json.load(f)

if __name__ == '__main__':
    print(deserialize())
    

