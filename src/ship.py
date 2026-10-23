import pygame
from pygame.surface import Surface

from src.settings import Settings


class Ship:
    """Gerencia a nave espacial."""

    def __init__(
        self,
        alien_invasion_screen: Surface,
        alien_invasion_settings: Settings,
    ) -> None:
        """Inicializa a nave e define sua posição inicial."""
        self.screen = alien_invasion_screen
        self.settings = alien_invasion_settings
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_right = False
        self.moving_left = False

        self.x = float(self.rect.x)

    def blitme(self) -> None:
        """Desenha a nave em sua posição atual."""
        self.screen.blit(self.image, self.rect)

    def update(self) -> None:
        """Atualiza a posição da nave conforme os comandos de movimento."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x
