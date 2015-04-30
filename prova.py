from __future__ import print_function
import sys
import time
import random

import pyglet

window = pyglet.window.Window( resizable=True)
fp=open("testo.txt",'r')

lista=fp.read().decode("utf8").split("\n")
def rainbow():
	return pyglet.image.load("rainbow-stalin.gif")

rainbow().height=window.height
rainbow().width=window.width
rainbow().anchor_y=window.height//2
rainbow().anchor_x=window.width//2


#lista=['ciao','come','Ar byte macht fried']
window.labels = [
            pyglet.text.Label('window', x=10, y=100, anchor_y='bottom',
                              color=(0, 0, 0, 255))
				]

def documento():
    	concept=random.choice(lista)
    	document=pyglet.text.decode_attributed(concept)
	document.set_style(0,len(concept), dict(font_name='Impact', font_size=window.height/10))
	document.set_style(0,len(concept),{"color":(255,255,255,255),
							})
	document.set_paragraph_style(0,10,{"align":"center","wrap":True})
	return pyglet.text.layout.TextLayout(document,width=window.width,height=window.height-100,
										multiline=True)



def label():
    #document=pyglet.text.document.FormattedDocument()
       return  pyglet.text.Label(random.choice(lista),
                          font_name='Courier',
                          font_size=16,
                          color=(10,10,100,255),
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

@window.event
def on_draw():
	window.clear()
	documento().anchor_y='bottom'
	if (random.choice([False,True])==True) :
		documento().draw()
	else:
		rainbow().blit(x=(window.width-rainbow().width)/2,y=0)

@window.event
def on_key_press(symbol, modifiers):
    on_draw()
    print(symbol)
    if symbol in (ord('q'), ord('Q')):
        sys.exit(0)
    return True

@window.event
def on_resize(widht,height):
	print "bella!"
	on_draw()
	#rainbow().height=window.height
	#rainbow().width=window.width

def callback(dt):
    return on_draw()

pyglet.clock.schedule_interval(callback,3)

pyglet.app.run()
