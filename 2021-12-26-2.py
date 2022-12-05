import itertools as it
import threading
import sys
import time

def spinner(msg):
    write,flush = sys.stdout.write,sys.stdout.flush
    for char in it.cycle('|/-\\'):
        status = char +msg
        write(status)
        time.sleep(0.1)
        flush()


