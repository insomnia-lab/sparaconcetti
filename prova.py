from __future__ import print_function
import os
import sys
import time
import random

import pyglet


### CONF
imgdir = 'imgs'
img_random_prob = 2
next_timeout = 3
textdir='txt'
###

last_manual_click = 0
window = pyglet.window.Window(fullscreen=True)

def read_textfile(fname):
    with open(fname) as fp:
        return filter(lambda s: s,
                    map(lambda s: s.strip(), fp.read().decode("utf8").split("\n"))
                    )

#testi_fnames = [os.path.join(textdir, fname) for fname in os.listdir(textdir)]
#testi =[read_textfile(fname) for fname in testi_fnames]
listabene=read_textfile("testimisti.txt")
listamale=read_textfile("short.txt")
def get_img(fname):
    if fname not in get_img.cache:
        get_img.cache[fname] = pyglet.image.load(fname)
    return get_img.cache[fname]
get_img.cache = {}
img_fnames = [os.path.join(imgdir, fname) for fname in os.listdir(imgdir)]
def get_random_img():
    return get_img(random.choice(img_fnames))
for fname in img_fnames:
    get_img(fname)


window.labels = [
            pyglet.text.Label('window', x=10, y=100, anchor_y='bottom',
                              color=(0, 0, 0, 255))
                ]

def documento():
    concept=random.choice(random.choice([listabene,listamale]))
    document=pyglet.text.decode_attributed(concept)
    document.set_style(0,len(concept), dict(font_name='Impact', font_size=window.height/10))
    document.set_style(0,len(concept),{"color":(255,255,255,255)})
#    document.set_style(0,len(concept),{"background_color":(100,255,255,255)})
    document.set_paragraph_style(0,10,{"align":"center","wrap":True})
    laiaut=pyglet.text.layout
    return laiaut.TextLayout(document,width=window.width,height=window.height-100,multiline=True)


def label():
    #document=pyglet.text.document.FormattedDocument()
       return  pyglet.text.Label(random.choice(listabene),
                          font_name='Courier',
                          font_size=16,
                          color=(10,10,100,255),
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

# @window.event
def on_draw():
    pyglet.gl.glClearColor(random.random()/2,
                           random.random()/2,
                           random.random()/2,
                           100)
    window.clear()
    documento().anchor_y='bottom'
    if random.randint(0, img_random_prob) > 0:
        documento().draw()
    else:
        img = get_random_img()
        sprite = pyglet.sprite.Sprite(img)
        #sprite.x = (window.width - img.width)/2
        #sprite.y = (window.height - img.height)/2
        sprite.scale = min(float(window.width) / img.width,
                           float(window.height) / img.height)
        sprite.x = (window.width - img.width*sprite.scale)/2
        sprite.y = (window.height - img.height*sprite.scale)/2

        # img.blit(x=(window.width - img.width)/2,
        #          y=(window.height - img.height)/2)
        sprite.draw()

pyglet.gl.glClearColor(1,0.5,0.5,1)
@window.event
def on_key_press(symbol, modifiers):
    global last_manual_click
    on_draw()
    last_manual_click = time.time()
    if symbol in map(ord,('q', 'Q')):
        sys.exit(0)
    return True

@window.event
def on_resize(widht,height):
    on_draw()
    #rainbow().height=window.height
    #rainbow().width=window.width

def callback(dt):
    global last_manual_click
    now = time.time()
    print('DIFF', now, last_manual_click, now - last_manual_click)
    if (now - last_manual_click) > next_timeout:
        on_draw()
    else:
        print('no, skip')

pyglet.clock.schedule_interval(callback, next_timeout)

pyglet.app.run()
