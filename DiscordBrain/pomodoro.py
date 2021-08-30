import time

testing = True

if testing:
    workTime = 5
    breakTime = 3
else:
    workTime = 25 * 60
    breakTime = 25 * 60


print("Hi")


def pomodoroCycle(phase):
    print("Phase "+str(phase))
    print("25 Minute Work Period Starts Now")
    # Make a noise to indicate a cycle has begun.
    time.sleep(workTime)
    # Noise to start break time.
    print('Break Time Starting Now!')
    time.sleep(breakTime)


def pomodoroTimer():
    for i in range(1, 5):
        pomodoroCycle(i)


pomodoroTimer()
