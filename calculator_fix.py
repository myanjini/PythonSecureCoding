import sys
import os

def run_code(string):
    try:
        result = eval(string, {'__builtins__': {}})
        print("{} = {}".format(string, result))
    except Exception as e:
        print(repr(e))

if __name__ == "__main__":
     run_code(sys.argv[1])
