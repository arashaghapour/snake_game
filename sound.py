import pygame as pg
def sedakoll():
    pg.mixer.init()
    pg.mixer.music.load("music/C418-Aria-Math-192.mp3")  # مسیر فایل موزیک
    pg.mixer.music.set_volume(0.5)         # میزان صدا بین 0.0 تا 1.0
    pg.mixer.music.play(-1)
def tavagof():
    pg.mixer.music.stop()