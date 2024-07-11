import pgzrun
from pgzhelper import *

WIDTH = 1000
HEIGHT = 700

zombie_run_img = ['zombie/run/tile002',
                  'zombie/run/tile003',
                  'zombie/run/tile004',
                  'zombie/run/tile005']

player_idle1_img = ['player/idle1/tile000',
                  'player/idle1/tile001',
                  'player/idle1/tile002',
                  'player/idle1/tile003']

player_die1_img = ['player/die1/tile000',
                   'player/die1/tile001',
                   'player/die1/tile002',
                   'player/die1/tile003',
                   'player/die1/tile004',
                   'player/die1/tile005',
                   'player/die1/tile006',]


zombie = Actor(zombie_run_img[0])
zombie.images = zombie_run_img
zombie.scale = (5)
zombie.fps = 10
zombie.right = WIDTH+100
zombie.bottom = HEIGHT

player = Actor(player_idle1_img[0])
player.images = player_idle1_img
player.fps = 20 
player.scale = 5
player.bottom = HEIGHT + 350

question = 'hello world'
response = ' '



def update():
    global response
    zombie.animate()
    player.animate()
    if not(player.image in player_die1_img):
        zombie.x -=1
    if player.image == player_die1_img[-1]:
        player.images = player_idle1_img
        player.fps=20
    if zombie.left <= 0:
        zombie.right = WIDTH + 100 
        response = ''
    if zombie.collide_pixel(player):
        zombie.right = WIDTH + 100
        response = ''
        player.images = player_die1_img
        player.fps = 5

    

def on_key_down(key):
    if key in range(97, 122+1):
        print(chr(key))
        response += chr(key)
    elif key == keys.SPACE:
        response += ' '
    elif key == keys.BACKSPACE:
        response = response [0:-1]



def draw():
    screen.clear()
    screen.draw.text(question, {50, 100}, fontsize=120)
    screen.draw.text(response,(50,100),fontsize=120,color='orange')
    zombie.draw()
    player.draw()

pgzrun.go()