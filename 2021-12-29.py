import random
from collections import namedtuple

Event = namedtuple('Event','time process action')

def taxi_process(ident,trips,start_time=0):
    time = yield Event(start_time,ident,'leave garage')
    for i in range(trips):
        time = yield Event(time,ident,'pick up passenger')
        time = yield Event(time,ident,'drop off passenger')
    yield Event(time,ident,'going home')

