from os import walk
from pygame.image import load
def import_folder(path):

    image_surfaces = list()
    for _, __, img_files in walk(path):
        for img in img_files:
            full_image_path = path + '/' + img
            surface = load(full_image_path).convert_alpha()
            image_surfaces.append(surface)
    return image_surfaces
