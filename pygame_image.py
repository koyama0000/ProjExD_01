import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex01/fig/3.png")
    kk_img0 = pg.transform.flip(kk_img, True, False)
    kk_img1 = pg.transform.rotozoom(kk_img0, 10, 1.0)
    lst = [kk_img0, kk_img1]

    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        tmr += 1
        x = tmr%1600
        
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img, [1600-x, 0])
        screen.blit(lst[tmr%2], [300, 200])

        pg.display.update()
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()