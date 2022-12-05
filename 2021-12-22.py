import asyncio
import itertools as it
import sys

async def spinner(msg):
    '''
    旋转 0.1s 显示 清除
    '''
    write = sys.stdout.write
    flush = sys.stdout.flush
    for char in it.cycle('|/-\\'):
        status = char+msg 
        write(status)
        flush()
        write('\x08'*len(status))
        try:
            await asyncio.sleep(0.1)
        except asyncio.CancelledError:
            break



async def slow_func():
    await asyncio.sleep(3)
    return 44


async def supervisor(loop):
    spin = loop.create_task(spinner('song is genius'))
    print(spin)
    result = await slow_func()

def main():
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(supervisor(loop))
    loop.close()
if __name__=='__main__':
    main()
