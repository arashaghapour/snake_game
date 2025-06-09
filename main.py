import pygame as pg
import sqlite3
import sys
import snake
import food
import sound
import score
pg.font.init()
tool, ertefa = 1500, 1000

toolindex = tool // 20
ertefaindex = ertefa // 20
pixel = 20
safhe = pg.display.set_mode((tool, ertefa))
pg.display.set_caption('snake game')
rangesafhe = (0, 0, 0)
sizemar = 20
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

font = pg.font.Font("font/LiberationSans-Bold.ttf", 80)
clock = pg.time.Clock()

dokmerestatrt = pg.Rect(tool // 2 - 130, ertefa // 2 + 40, 300, 80)
dokmeh_asan = pg.Rect(tool // 2 - 150, 250, 300, 80)
dokmeh_motavaset = pg.Rect(tool // 2 - 150, 400, 300, 80)
dokmeh_sakht = pg.Rect(tool // 2 - 150, 550, 300, 80)
def bazi_ra_start_kon():
    s = snake.mar(safhe, 45, 20, pixel, sizemar, toolindex, ertefaindex)
    f = food.ghaza(safhe, toolindex, ertefaindex, sizemar)
    xeghaza, yeghaza = f.toolidtasadofi()
    return s, f, xeghaza, yeghaza

s, f, xeghaza, yeghaza = bazi_ra_start_kon()
# score.emtiaz(0)
edame = True
sound.sedakoll()
emtiaz = 0
kilic_ebteda = False
sakhti = 0
while edame:
    if(kilic_ebteda):
        bool = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                edame = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    s.jahat('L')
                elif event.key == pg.K_RIGHT:
                    s.jahat('R')
                elif event.key == pg.K_UP:
                    s.jahat('U')
                elif event.key == pg.K_DOWN:
                    s.jahat('D')

        if not s.barresi():
            # safhe.fill((0, 0, 0))
            text = font.render("Game Over", True, (255, 0, 0))
            rect = text.get_rect(center=(tool // 2, ertefa // 2))
            safhe.blit(text, rect)
            pg.draw.rect(safhe, (0, 100, 255), dokmerestatrt)
            label = font.render("Restart", True, (255, 255, 255))
            label_rect = label.get_rect(center=dokmerestatrt.center)
            cursor.execute('''
                        INSERT INTO scores (scores)
                        VALUES (?)
                    ''', (emtiaz, ))
            cursor.execute('SELECT * FROM scores')
            rows = cursor.fetchall()
            label1 = font.render(f'best score is: {max(rows)}', True, (255, 255, 255))
            safhe.blit(label1, (450, 300))
            conn.commit()
            conn.close()
            safhe.blit(label, label_rect)
            pg.display.flip()


            restart_clicked = False
            while not restart_clicked:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()
                        sys.exit()
                    elif event.type == pg.MOUSEBUTTONDOWN:
                        if dokmerestatrt.collidepoint(event.pos):
                            s, f, xeghaza, yeghaza = bazi_ra_start_kon()
                            restart_clicked = True
                            kilic_ebteda = False
                            score.emtiaz(0)
                clock.tick(10)
            continue 

        s.harakat()
        if s.mokhtassat() == (xeghaza, yeghaza):
            xeghaza, yeghaza = f.toolidtasadofi()
            bool = True
            emtiaz = score.emtiaz()

        safhe.fill(rangesafhe)
        s.drawsnake(bool)
        f.keshidanghaza()
        pg.draw.rect(safhe, (0, 0, 128), (0, 0, tool, 100))
        matne_emtiaz = font.render(f"Score: {emtiaz}", True, (255, 255, 255))
        safhe.blit(matne_emtiaz, (10, 5))
        pg.display.flip()
        clock.tick(sakhti)
    else:
        safhe.fill((0, 0, 0))
        matn = font.render("Select Difficulty", True, (255, 255, 255))
        safhe.blit(matn, (tool // 2 - matn.get_width() // 2, 100))

        pg.draw.rect(safhe, (0, 200, 0), dokmeh_asan)
        pg.draw.rect(safhe, (255, 165, 0), dokmeh_motavaset)
        pg.draw.rect(safhe, (200, 0, 0), dokmeh_sakht)

        label_asan = font.render("Easy", True, (0, 0, 0))
        label_motavaset = font.render("Medium", True, (0, 0, 0))
        label_sakht = font.render("Hard", True, (0, 0, 0))

        safhe.blit(label_asan, label_asan.get_rect(center=dokmeh_asan.center))
        safhe.blit(label_motavaset, label_motavaset.get_rect(center=dokmeh_motavaset.center))
        safhe.blit(label_sakht, label_sakht.get_rect(center=dokmeh_sakht.center))

        pg.display.flip()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                kilic_ebteda = True
                if dokmeh_asan.collidepoint(event.pos):
                    sakhti = 10
                elif dokmeh_motavaset.collidepoint(event.pos):
                    sakhti = 15
                elif dokmeh_sakht.collidepoint(event.pos):
                   sakhti = 20
sound.tavagof()
pg.quit()
sys.exit()
