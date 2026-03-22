import sdl2
import sdl2.ext

class BorderSpriteCreator:
    def __init__(self, factory):
        self.factory = factory

    def create(self, width, height, margin, color=(255, 255, 255, 255)):
        rect_w = width - (margin * 2)
        rect_h = height - (margin * 2)

        surface = sdl2.SDL_CreateRGBSurface(0, rect_w, rect_h, 32, 0, 0, 0, 0)
        
        sdl_color = sdl2.ext.Color(*color)
       
        sdl2.ext.line(surface, sdl_color, (0, 0, rect_w - 1, 0))              
        sdl2.ext.line(surface, sdl_color, (0, rect_h - 1, rect_w - 1, rect_h - 1))
        sdl2.ext.line(surface, sdl_color, (0, 0, 0, rect_h - 1))            
        sdl2.ext.line(surface, sdl_color, (rect_w - 1, 0, rect_w - 1, rect_h - 1)) 

        sprite = self.factory.from_surface(surface)
        
        sdl2.SDL_FreeSurface(surface)
        
        return sprite