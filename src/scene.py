from .widget import BorderSpriteCreator
from .entity import Entity
import sdl2 
import sdl2.ext 

class SceneBase:
    """scene de base juste une bordure"""
    def __init__(self, renderer, factory):
        self.renderer = renderer
        self.factory = factory
        creator = BorderSpriteCreator(self.factory)
        self.spriterenderer = sdl2.ext.TextureSpriteRenderSystem(self.renderer)


        #initalisation des entity et sprites
        border_sprite = creator.create(800, 600, 50, color=(255, 255, 255, 255))
        self.border = Entity(x=50, y=50, sprite=border_sprite, static=True)


    def construire(self):
        self.renderer.clear(sdl2.ext.Color(0, 0, 0))

        self.spriterenderer.render(self.border.sprite)

        self.renderer.present()