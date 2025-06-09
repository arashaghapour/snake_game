import random as rd
import pygame as pg
class ghaza:
    def __init__(self, safhe, tool, ertefa, size):
        self.safhe = safhe
        self.tool = tool
        self.ertefa = ertefa
        self.size = size
        self.rang = (231, 76, 60)
        self.xeghaza = 0
        self.yeghaza = 0

  
        self.font = pg.font.SysFont("Noto Color Emoji", size=int(self.size * 0.6))
    def toolidtasadofi(self):
        self.xeghaza = rd.randint(0, self.tool - 1)
        self.yeghaza = rd.randint(5, self.ertefa - 5)
        self.xeghaza = 15
        self.yeghaza = rd.randint(self.ertefa // 2 - 10, self.ertefa // 2 + 10)
    
        return self.xeghaza, self.yeghaza
    def keshidanghaza(self):
        pg.draw.rect(self.safhe, self.rang, (self.xeghaza * self.size, self.yeghaza * self.size, self.size, self.size))