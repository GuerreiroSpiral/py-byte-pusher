import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, DISPLAY_HEIGHT
from pygame import gfxdraw
from pygame import freetype

# Graphics: 256*256 pixels, 1 byte per pixel, 216 fixed colors


class ByteScreen:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Python Byte Pusher")
        self._screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self._screen_surface = pygame.display.get_surface()
        self._color_palette = [pygame.Color(0, 0, 0)] * 256
        self.font = freetype.Font("../font/8BITWONDER.TTF", 10)
        self._fill_palette()
    
    def blit_text(self, text, pos):
        # Clears the debug area
        self._screen_surface.fill((0, 0, 0), (0, DISPLAY_HEIGHT-1, SCREEN_WIDTH, SCREEN_HEIGHT))
        # Render the text
        self.font.render_to(self._screen_surface, pos, text, (255, 255, 255))
        # Update only the text area
        pygame.display.update()

    def _fill_palette(self):
        index = 0
        """
        The 216 colors are organized into a 6*6*6 color cube (a.k.a the "websafe" palette). Each of the red, green and blue components 
        can have an intensity value from 0 to 5. The formula to calculate a pixel's color value is: Red*36 + Green*6 + Blue. 
        If the actual display device has 8-bit (00h-FFh) color components, we have to multiply each intensity value by 33h 
        when blitting to the screen: 
		"""
        for red in range(0, 256, 0x33):
            for green in range(0, 256, 0x33):
                for blue in range(0, 256, 0x33):
                    self._color_palette[index] = pygame.Color(red, green, blue)

                    index += 1

    def render_frame(self, frame_data):
        for y in range(DISPLAY_HEIGHT):
            for x in range(SCREEN_WIDTH):
                gfxdraw.pixel(self._screen_surface, x, y,
                              self._color_palette[frame_data[(y * 256) + x]])
                pygame.display.update()
