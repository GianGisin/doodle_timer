from python_imagesearch.imagesearch import imagesearcharea
import time
import sys
import math
from win32api import GetSystemMetrics

screen_x = GetSystemMetrics(0)
screen_y = GetSystemMetrics(1)

topx = math.floor(screen_x / 3)
topy = math.floor(screen_y / 4)
bottomx = screen_x - math.floor(screen_x / 3)
bottomy = screen_y - math.floor(screen_y / 2)


def await_screen_gone(path):
    is_paused = True
    while is_paused:
        # waiting for pause screen to disappear
        # topx, topy, bottomx, bottomy
        pos = imagesearcharea(path, topx, topy, bottomx, bottomy)
        if pos[0] == -1:
            is_paused = False


def start_timer():
    print("starting timer")
    endtime = 0
    timer = time.time()

    while True:

        pos = imagesearcharea("img\win.png", topx, topy, bottomx, bottomy)

        if pos[0] != -1:
            break

    endtime = time.time() - timer
    print(endtime)
    print("\nPress replay to start the timer again. Ctrl-C to quit.")


def main():
    print("Screen size:", screen_x, screen_y)

    input("press enter when pause screen is visible...")
    pos = imagesearcharea("img\pause.png", topx, topy, bottomx, bottomy)

    if pos[0] != -1:

        print("\nPause screen captured. Unpause to start timer")
        await_screen_gone("img\pause.png")
        # wait for pause screen gone
        start_timer()
        while True:
            await_screen_gone("img\win.png")
            # wait for pause screen gone
            start_timer()

    else:
        print(
            "Screen not recognized - please try again and make sure the images in /img are custom made for your device."
        )


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Quitting Timer\nGoodbye :(")
        sys.exit(0)
