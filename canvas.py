from pickletools import read_stringnl_noescape

from pico2d import *

player = load_image("run_animation.png")
grass = load_image("grass.png")
frame = 0

running = True

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

for x in range(0,800,5):
    clear_canvas()
    grass.draw(400,30)
    player.clip_draw(frame * 100, 100, 100, 100, x, 90)
    update_canvas()

    handle_events()
    if not running:
        break

    frame = (frame + 1) % 0
    delay(0.05)

close_canvas()
