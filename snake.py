import pygame as pg
class mar:
    def __init__(self, safhe, xemar, yemar, pixel, size, tool, ertefa):
        self.safhe = safhe
        self.xemar = xemar
        self.xavval = tool
        self.yavval = ertefa
        self.yemar = yemar
        self.pixel = pixel
        self.rang = (255, 0, 0)
        self.size = size
        self.samt = 'R'
        self.harakatha = [[xemar, yemar]]
        
    def drawsnake(self, bool):
        if(bool):
            self.harakatha.insert(0, [self.xemar, self.yemar])
            for i in self.harakatha:
                pg.draw.rect(self.safhe, self.rang, (i[0] * self.size, i[1] * self.size, self.size, self.size))
        else:          
            self.harakatha.pop()
            self.harakatha.insert(0, [self.xemar, self.yemar])
            
            for i in self.harakatha:
                pg.draw.rect(self.safhe, self.rang, (i[0] * self.size, i[1] * self.size, self.size, self.size))
                
        pg.draw.rect(self.safhe, self.rang, (self.xemar * self.size, self.yemar * self.size, self.size, self.size))
    def harakat(self):
        if(self.samt == 'L'):            
            self.xemar -= 1
    
        elif(self.samt == 'R'):
            self.xemar += 1
           
        elif(self.samt == 'U'):
            self.yemar -= 1  
                      
        elif(self.samt == 'D'):
            self.yemar += 1 
                      
    def jahat(self, jahat1):
        self.samt = jahat1
        
    def mokhtassat(self):
        return self.xemar, self.yemar
    def barresi(self):
        if(self.xemar > self.xavval or self.xemar < 0 or self.yemar > self.yavval or self.yemar < 5):
            return False
        elif self.xemar > 0:
            for i in self.harakatha:
                if(self.harakatha.count(i) >= 2):
                    return False
            return True
        return True