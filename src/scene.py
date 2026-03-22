#import des fichiers
from .widget import BorderFactory
from .entity import Entity
from .config import config_window as configW
from .config import config_collision as configC

#import pysdl
import sdl2 
import sdl2.ext 




class SceneBase:
    """scene de base juste une bordure"""
    def __init__(self, renderer, factory):
        configC.ENTITY = []
        self.renderer = renderer
        self.factory = factory
        creator = BorderFactory(self.factory)
        self.spriterenderer = sdl2.ext.TextureSpriteRenderSystem(self.renderer)
        self.table_render = []

        #initalisation des entity et sprites
        MARGIN = 50
        self.borders = creator.create(configW.WINDOW_WIDTH, configW.WINDOW_HEIGHT, MARGIN,thickness=5, color=(255, 255, 255, 255))

        configC.ENTITY.extend(self.borders)
        
        
        


    def construire(self):
        self.renderer.clear(sdl2.ext.Color(0, 0, 0))
        self.table_render = [] 

        for el in configC.ENTITY:
            self.table_render.append(el.sprite)

        self.spriterenderer.render(self.table_render) 





class SceneTEST:
    """scene de TEST"""
    def __init__(self, renderer, factory):
        configC.ENTITY = []

        self.renderer = renderer
        self.factory = factory
        creator = BorderFactory(self.factory)
        self.spriterenderer = sdl2.ext.TextureSpriteRenderSystem(self.renderer)
        self.table_render = []


        #initalisation des entity et sprites
        MARGIN = 50
        self.borders = creator.create(win_w=configW.WINDOW_WIDTH, win_h=configW.WINDOW_HEIGHT, margin=MARGIN, thickness=5)
        configC.ENTITY.extend(self.borders)

        for el in range(10):
            carre =  factory.from_color(sdl2.ext.Color(255, 0, 0), size=(20, 20))
            configC.ENTITY.append(Entity(sprite=carre,x = 200+el*10, y= 200+el*50))

    def construire(self):
        self.renderer.clear(sdl2.ext.Color(0, 0, 0))
        self.table_render = [] 
        for el in configC.ENTITY:
            self.table_render.append(el.sprite)

        self.spriterenderer.render(self.table_render)

