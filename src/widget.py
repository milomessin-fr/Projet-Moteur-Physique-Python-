import sdl2
import sdl2.ext

#import de fichiers
from .entity import Entity


class BorderFactory:
    def __init__(self, factory):
        self.factory = factory

    def create(self, win_w, win_h, margin, thickness, color=(255, 255, 0, 255), static=True):
        """
        Crée 4 murs statiques à une distance 'margin' des bords de la fenêtre.
        """
        print("odsuhgidsughidjsghqsihghidshw")

        # 1. Calcul des dimensions du cadre intérieur
        # La largeur du rectangle formé par les murs
        inner_w = win_w - (2 * margin)
        inner_h = win_h - (2 * margin)

        # 2. Créer les surfaces (surfaces pleines pour les collisions)
        # On crée une surface horizontale et une verticale
        surf_h = sdl2.SDL_CreateRGBSurface(0, inner_w, thickness, 32, 0, 0, 0, 0)
        surf_v = sdl2.SDL_CreateRGBSurface(0, thickness, inner_h, 32, 0, 0, 0, 0)
        
        sdl_color = sdl2.ext.Color(*color)
        sdl2.ext.fill(surf_h, sdl_color)
        sdl2.ext.fill(surf_v, sdl_color)

        # Transformation en sprites (textures)
        s_top = self.factory.from_surface(surf_h)
        s_bottom = self.factory.from_surface(surf_h)
        s_left = self.factory.from_surface(surf_v)
        s_right = self.factory.from_surface(surf_v)

        # 3. Positionnement des 4 entités
        # x_start et y_start correspondent à ta marge
        x_start = margin
        y_start = margin

        return [
            # HAUT : commence à la marge, s'étale sur inner_w
            Entity(x_start, y_start, s_top, static),
            
            # BAS : décalé de la hauteur intérieure moins l'épaisseur du mur
            Entity(x_start, y_start + inner_h - thickness, s_bottom, static),
            
            # GAUCHE : commence à la marge, s'étale sur inner_h
            Entity(x_start, y_start, s_left,static),
            
            # DROITE : décalé de la largeur intérieure moins l'épaisseur du mur
            Entity(x_start + inner_w - thickness, y_start, s_right, static)
        ]