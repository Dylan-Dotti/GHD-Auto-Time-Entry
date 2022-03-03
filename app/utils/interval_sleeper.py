import time


def sleep(secs: float):
    time.sleep(secs)

def interval_checked_sleep(secs: float, interval: float,
                           continue_callback):
    start_time = time.time()
    while True:
        elapsed = time.time() - start_time
        if (elapsed >= secs):
            return
        if not continue_callback():
            print("Interval-checked sleep breaking after %ss" % elapsed)
            return
        time.sleep(min(interval, secs - elapsed))
