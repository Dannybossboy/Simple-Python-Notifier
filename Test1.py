from plyer import notification
import time
import sys

time_start = time.time()
seconds = 0
minutes = 0
TimerMin = 20


def Notify():
    notification.notify(title=title,
                        message=message,
                        app_icon=None,
                        timeout=10,
                        toast=False)




title = "Eye Care"
message = "Look at something else for 20 seconds"

while True:
    try:
        sys.stdout.write(f"\r{minutes} Minutes {seconds} Seconds".format(minutes = minutes, seconds = seconds))
        sys.stdout.flush()
        time.sleep(1)
        seconds = int(time.time() - time_start) - minutes * 60
        if seconds >= 60:
            minutes += 1
            seconds=0

        if (minutes == TimerMin):
            Notify()
            TimerMin += 20
        if (minutes == 60):
            minutes = 0


    except KeyboardInterrupt as e:
        break


