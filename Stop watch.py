import time

print("Press Enter to start the stopwatch.")
input()
print("Stopwatch started.")
start_time = time.time()

last_time = start_time
lap_num = 1

try:
    while True:
        input()
        current_time = time.time()
        lap_time = round(current_time - last_time, 2)
        total_time = round(current_time - start_time, 2)
        print(f"Lap #{lap_num}: {total_time} ({lap_time})")
        lap_num += 1
        last_time = current_time
except KeyboardInterrupt:
    print("Stopwatch stopped.")
