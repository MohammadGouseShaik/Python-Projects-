import time

def countdown(hours, minutes, seconds):
    total_seconds = (hours * 3600) + (minutes * 60) + seconds
    while total_seconds:
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        time_format = "Time remaining: {:02}:{:02}:{:02}".format(int(hours), int(minutes), int(seconds))
        print(time_format, end="\r")
        total_seconds -= 1
        time.sleep(1)
    print("Time's up!")

countdown(0, 0, 5)
