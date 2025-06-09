import pygame as pg
def sedakoll():
    pg.mixer.init()
    pg.mixer.music.load("music/C418-Aria-Math-192.mp3") 
    pg.mixer.music.set_volume(0.5)       
    pg.mixer.music.play(-1)
def tavagof():
    pg.mixer.music.stop()
def khordan():
    # pg.mixer.init()
    sound = pg.mixer.Sound('music/eat.mp3')
    sound.set_volume(0.5)          
    sound.play()