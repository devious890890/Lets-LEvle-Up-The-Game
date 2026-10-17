import pygame
import random

SCREENHEIGHT, SCREENWIDTH = 500, 400
MOVEMENT_SPEED = 5
Font_size = 72

pygame.init()

background_image = pygame.transform.scale(pygame.image.load("bg.png"),  (SCREENHEIGHT, SCREENWIDTH))

font = pygame.font.SysFont("Times New Roman", Font_size)

class sprite(pygame.sprite.sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.fill = self.image.fill("dodgerblue")
        pygame.draw.rect(self.image, color, pygame.Rect(0,0, height, width) )
        self.rect = self.image.get_rect()

    def move(self, x_change, y_change):
        self.rect.x = max(min(self.rect.x + x_change, SCREENWIDTH - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + y_change, SCREENHEIGHT- self.rect.height), 0)

screen = pygame.dislay.set_mode((SCREENWIDTH,SCREENHEIGHT))
pygame.display.set_caption("Sprite Collision")
all_sprite = pygame.sprite.Group()


spr1 = sprite(pygame.Color("Black"), 20,30)
spr1.rect.x, spr1.rect.y = random.randit(0, SCREENWIDTH - spr1.rect.width,0, SCREENHEIGHT - spr1.rect.height)
