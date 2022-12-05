from collections import namedtuple
Event = namedtuple('event','idx starttime behavour')

def gen_taxi(idx,trips,starttime):
    time = yield Event(idx,starttime,'leave garge') 
    for i in trips:
        time = yield Event(idx,time,'get sb')

        time = yield Event(idx,time,'leave sb')
    yield Event(idx,starttime,'return garge')

