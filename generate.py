import time
import os

out_file = 'test.txt'
if os.path.exists(out_file):
    os.remove(out_file)

def append():
    counter = 0
    while True:
        with open(out_file, 'a') as opened_file:
            opened_file.write(f'{counter}\n')
        counter += 1
        time.sleep(1)


def write():
    counter = 0
    with open(out_file, 'w') as opened_file:
        while True:
            opened_file.write(f'{counter}\n')
            counter += 1
            time.sleep(1)


if __name__ == '__main__':
    #append()
    write()
