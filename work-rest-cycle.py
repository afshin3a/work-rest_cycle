import time
import winsound
# Set work and break time in minutes
work_time = 30
break_time = 10

# Number of repetitions
iterations = 4

for _ in range(iterations):
    # Start working
    frequency = 500  # تنظیم فرکانس صدا
    duration = 500  # تنظیم مدت زمان پخش صدا (به میلی‌ثانیه)
    winsound.Beep(frequency, duration)
    print(f"Starting work for {work_time} minutes")
    start_time = time.time()
    while time.time() - start_time < work_time * 60:
        remaining_time = work_time * 60 - (time.time() - start_time)
        print(f"{int(remaining_time // 60)} minutes and {int(remaining_time % 60)} seconds left of work")
        time.sleep(1)

    # Beep sound
    print("\a")

    # Start break
    frequency = 2500  # تنظیم فرکانس صدا
    duration = 2000  # تنظیم مدت زمان پخش صدا (به میلی‌ثانیه)
    winsound.Beep(frequency, duration)
    # Start working
    print(f"Starting break for {break_time} minutes")
    start_time = time.time()
    while time.time() - start_time < break_time * 60:
        remaining_time = break_time * 60 - (time.time() - start_time)
        print(f"{int(remaining_time // 60)} minutes and {int(remaining_time % 60)} seconds left of break")
        time.sleep(1)

    # Beep sound
    print("\a")

print("Program ended.")
