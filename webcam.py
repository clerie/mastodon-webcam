import json
import pygame.camera, pygame.image
from mastodon import Mastodon

with open("conf.json", 'r') as f:
        conf = json.load(f)

mastodon = Mastodon(
    access_token = conf["token"],
    api_base_url = conf["instance"]
)


pygame.camera.init()
print(pygame.camera.list_cameras())
cam = pygame.camera.Camera(pygame.camera.list_cameras()[0], (1280, 720))
cam.start()
img = cam.get_image()

pygame.image.save(img, "shot.jpg")

pygame.camera.quit()

print(mastodon.status_post("#IlmenauHimmelGrau", media_ids=[mastodon.media_post("shot.jpg")]))
