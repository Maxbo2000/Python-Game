import pygame

from GameObjects.Player import Player


class HealthBar:
    def __init__(self, x: int, y: int, height: int, width: int):
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.font = pygame.font.Font(None, 30)

    def draw(self,screen, player: Player):
        self.width = player.getHealth() * 100 // 100
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(self.x,self.y,self.width,self.height))
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(self.x,self.y,self.width,self.height), 2)
        health_text = self.font.render(f"{player.getHealth()} / 100", True, (255, 255, 255))
        screen.blit(health_text, (self.y + 5, self.x + self.height + 5))
