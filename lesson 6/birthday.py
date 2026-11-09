import pygame
import time

pygame.init()
WIDTH = 600
HEIGHT = 600
screen=pygame.display.set_mode([WIDTH,HEIGHT])

image1=pygame.image.load("image1.jpg")
image1=pygame.transform.scale(image1,(WIDTH,HEIGHT))

image2=pygame.image.load("image2.jpg")
image2=pygame.transform.scale(image2,(WIDTH,HEIGHT))

image3=pygame.image.load("image3.jpg")
image3=pygame.transform.scale(image3,(WIDTH,HEIGHT))
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if  event.type == pygame.QUIT:
            pygame.quit()
    screen.fill("white")
    screen.blit(image1,(0,0))
    font=pygame.font.SysFont("Times New Roman",50)
    text1=font.render("Happy",True,(0,0,0))
    text2=font.render("Birthday!",True,(0,0,0))

    screen.blit(text1,(210,180))
    screen.blit(text2,(160,264))

    pygame.display.update()
    time.sleep(3)

    screen.blit(image2,(0,0))
    font=pygame.font.SysFont("Times New Roman",50)
    text3=font.render("A gift with",True,(0,0,0))
    text4=font.render("Noting!, but confetti.",True,(0,0,0))
    
    screen.blit(text3,(210,180))
    screen.blit(text4,(160,264))
    
    pygame.display.update()
    time.sleep(3)

    screen.blit(image3,(0,0))
    font=pygame.font.SysFont("Times New Roman",50)
    text5=font.render("Happy Birthday!",True,(0,0,0))
    text6=font.render("You're officily THREE",True,(0,0,0))
    
    screen.blit(text5,(210,180))
    screen.blit(text6,(130,264))
    
    pygame.display.update()
    time.sleep(3)