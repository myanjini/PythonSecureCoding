import os
import json
import datetime

class ExploitEncoder(json.JSONEncoder):
    def default(self, obj):
        if any(isinstance(obj, x) for x in (datetime.datetime, datetime.date)):
            return str(obj)
        return (os.system, ('ls -al /',))

def serialize():
    data = json.dumps([range(10), datetime.datetime.now()], cls=ExploitEncoder)
    with open('./mydata.json', 'w') as f: 
        f.write(data)

if __name__ == '__main__':
    serialize()
    

