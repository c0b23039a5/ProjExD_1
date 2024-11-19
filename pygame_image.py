import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    koukaton_img = pg.image.load("fig/3.png")
    koukaton_img = pg.transform.flip(koukaton_img,True,False)
    bg_img_flip = pg.transform.flip(bg_img,True,False)
    tmr = 0
    kk_rct= koukaton_img.get_rect()
    kk_rct.center = 300,200
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed()
        screen.blit(bg_img, [-(tmr%3200), 0])
        screen.blit(bg_img_flip, [-(tmr%3200)+1600, 0])
        screen.blit(bg_img, [-(tmr%3200)+3200, 0])
        screen.blit(bg_img_flip, [-(tmr%3200)+4800, 0])
        move_cache=[0,0]
        if key_lst[pg.K_UP]:
            move_cache[1]-=1
        if key_lst[pg.K_DOWN]:
            move_cache[1]+=1
        if key_lst[pg.K_LEFT]:
            move_cache[0]-=1
        if key_lst[pg.K_RIGHT]:
            move_cache[0]+=2
        move_cache[0]-=1
        kk_rct.move_ip(move_cache)
        screen.blit(koukaton_img,kk_rct.center)
        pg.display.update()
        tmr += 1
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
