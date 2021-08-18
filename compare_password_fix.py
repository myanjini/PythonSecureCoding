import sqlite3
import getpass
from passlib.hash import bcrypt

def read_passwords():
    db = sqlite3.connect('passwd.db')
    cursor = db.cursor()
    hashes = {}    
    for user,passwd in cursor.execute("select user,password from passwds"):
        hashes[user] = bcrypt.encrypt(passwd, rounds=8)
    return hashes

def verify_password(user):
    passwds = read_passwords()
    cipher = passwds.get(user)
    if bcrypt.verify(getpass.getpass("Password: "), cipher):
        print('Password accepted')      
    else:
        print('Wrong password, Try again')

if __name__ == "__main__":
    import sys
    verify_password(sys.argv[1])
