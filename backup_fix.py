import subprocess

def backup():
    filename = raw_input('Please provide the path for the file to backup: ')
    command = [ "cp", filename, "/home/nanjini/backup/" ]
    subprocess.call(command, shell=False)

if __name__ == "__main__":
    backup()
