from threading import Timer
import time


def timeloop():

    print(
        f"--- LOOP: {time.ctime()} ---"
    )

    Timer(
        5,
        timeloop
    ).start()


timeloop()