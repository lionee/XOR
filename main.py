import numpy
from termcolor import colored
import pygame
from pygame.locals import *

sx=512
sy=512

colors = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
attrs = ['on_grey', 'on_red', 'on_green', 'on_yellow', 'on_blue', 'on_magenta', 'on_cyan', 'on_white']


def draw_txt():
    arr = numpy.zeros((256, 256))
    rows = arr.shape[0]
    cols = arr.shape[1]

    while True:
        for x in range(0, rows):
            for y in range(0, cols):
            #print(colored('Xor', colors[round((x^y)/4)], attrs[round((x^y)/8)]), end='')
                print(colored(chr(65+round((x^y)/8)), colors[int(round((x^y)/37))], attrs[int(round((x^y)/64))]), end='')
                arr[x][y] = int(round((x^y)/32))
            print("")

def draw_graphics():
    pygame.init()
    screen = pygame.display.set_mode((sx, sy))
    arr = numpy.zeros((sx, sy))
    rows = arr.shape[0]
    cols = arr.shape[1]

    for x in range(0, rows):
        for y in range(0, cols):

            arr[x][y] = int(round(x ^ y))
    surface = pygame.surfarray.make_surface(arr)


    screen.blit(pygame.transform.scale2x(surface), (0, 0))
    pygame.display.flip()
    input("Press Enter to continue...")
    pygame.quit()


def main():
    print("Menu:")
    print("1 - txt mode")
    print("2 - gfx mode")
    answer = input()
    if answer=="1":
        draw_txt()
    if answer=="2":
        draw_graphics()

if __name__ == "__main__":
    main()