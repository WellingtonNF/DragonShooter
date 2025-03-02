import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/menubg.png')  # load img
        self.rect = self.surf.get_rect(left=0, top=0)  # define um retangulo invisivel no ponto 0 da janela

    def run(self):
        pygame.mixer.music.load('./asset/Menu.wav')  # load music menu
        pygame.mixer.music.play(-1)  # tocar a musica carregada, o -1 significa colocar ela em loop, tocar infinito

        while True:
            self.window.blit(source=self.surf, dest=self.rect)  # primeiro desenha o fundo / o source é a origem, o dest é o destino da imagem
            self.menu_text(50, 'Dragon', COLOR_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, 'Shooter', COLOR_ORANGE, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 30 * i))

            pygame.display.flip()  # atualiza a imagem na surface, ou seja, ele vai pegar a imagem do destino e colocar no retangulo

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # End pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()  # isso é uma imagem agora
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)  # desenhar a imagem porém com texto
