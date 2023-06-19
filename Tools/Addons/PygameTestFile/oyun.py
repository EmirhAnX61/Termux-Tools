import pygame
pygame.init()

from pygame import mixer
mixer.music.load('Musics/sansfight.mp3')
mixer.music.play(1)

print("Oyun açıldı")


win = pygame.display.set_mode((1000,700))
pygame.display.set_caption("CUBE SANS FIGHT V.1.0")


xd = 200
yd = 500
height5 = 25
width5 = 50
xa = 400
ya = 100
xc = 500
yc = 110
width4 = 40
height4 = 40
xb = 410
yb = 110
x = 500
y = 500
width2 = 150
height2 = 150
width3 = 40
height3 = 40
width = 50
height = 50
vel = 20

run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a]:
        x -= vel

    if keys[pygame.K_d]:
        x += vel

    if keys[pygame.K_w]:
        y -= vel

    if keys[pygame.K_s]:
        y += vel
    
    if keys[pygame.K_ESCAPE]:
        pygame.quit()


        
    win.fill((0,0,0))
    obje = pygame.draw.rect(win, (255,0,0), (x, y, width, height))
    pygame.draw.rect(win, (255,255,255), (xa, ya, width2, height2))
    pygame.draw.rect(win, (0,0,0), (xb, yb, width3, height3))
    pygame.draw.rect(win, (0,0,0), (xc, yc, width4, height4))
    kemik = pygame.draw.rect(win, (255,255,255), (xd, yd, width5, height5))    
    pygame.display.update() 
    

pygame.quit()
print("Oyun kapandı")