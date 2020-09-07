from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break
def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")
if __name__ =='__main__':
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 1200 #20min
    eyessecs = 1800  # 30min
    exsecs = 2700  # 45min
    while True:
        if time() - init_water > watersecs:
            print("Water drinking time. Enter 'drank' to stop the alaram\n =>")
            musiconloop("Small-rock-water-splash.mp3", "drank")
            init_water = time()
            log_now("Drank water at")
        if time() - init_eyes > eyessecs:
            print("Eye exercise time. Enter 'done' to stop the alaram\n =>")
            musiconloop("eye.mp3", "done")
            init_eyes = time()
            log_now("Done eye exercise at")
        if time() - init_exercise > exsecs:
            print("Exercise time. Enter 'done ex' to stop the alaram\n =>")
            musiconloop("breathe.mp3", "done ex")
            init_exercise = time()
            log_now("Done exercise at")

