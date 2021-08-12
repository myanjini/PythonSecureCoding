import subprocess
import shlex

def backup():
    filename = raw_input('Please provide the path for the file to backup: ')
    command = 'cp {source} /home/nanjini/backup/'.format(source=filename)
    subprocess.call(shlex.split(command), shell=False)

if __name__ == "__main__":
    backup()
