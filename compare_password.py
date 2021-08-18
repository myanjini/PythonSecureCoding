import hashlib
import sqlite3
import getpass

def read_password(user):
    db = sqlite3.connect('passwd.db')
    cursor = db.cursor()
    try:
        passwd = cursor.execute("select password from passwds where user = '%(user)s'" % locals()).fetchone()[0]
        return hashlib.sha1(passwd.encode('utf-8')).hexdigest()
    except TypeError:
        pass

def verify_password(user):
    hash_pass = hashlib.sha1(getpass.getpass("Password: ").encode('utf-8')).hexdigest()
    if hash_pass==read_password(user):
        print('Password accepted')
    else:
        print('Wrong password, Try again')
    
if __name__ == "__main__":
    import sys
    verify_password(sys.argv[1])
