import asyncio
import itertools as it
import sys
from datetime import datetime

async def spinner(msg):
    write = sys.stdout.write
    flush = sys.stdout.flush
    for char in it.cycle('|/-\\'):
        status = char+msg
        write(status)
        flush()
        write('\x08'*len(status))
        await asyncio.sleep(0.1)

async def slow_func():
    await asyncio.sleep(3)
    return str(datetime.today()) 

async def supervisor(loop):
    spin = loop.create_task(spinner('song is genius'))
    print(spin)
    result = await slow_func()
    print(result)

def main():
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(supervisor(loop))
    loop.close()

if __name__=='__main__':
    main()



    

