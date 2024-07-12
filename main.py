import pgzrun
from pgzhelper import *
import random

WIDTH = 1000
HEIGHT = 700

zombie_run_img = ['zombie/run/tile002',
                  'zombie/run/tile003',
                  'zombie/run/tile004',
                  'zombie/run/tile005']

zombie_die_img = ['zombie/die/tile014',
    'zombie/die/tile015',
    'zombie/die/tile016',
    'zombie/die/tile017',
    'zombie/die/tile018',
    'zombie/die/tile019',
    'zombie/die/tile020',
    'zombie/die/tile021',
    'zombie/die/tile022',
    'zombie/die/tile023',
    'zombie/die/tile024']

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

player_attack2_img = ['player/attack2/tile000',
                      'player/attack2/tile001',
                      'player/attack2/tile002',
                      'player/attack2/tile003']


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

fireball_img = ['fireball/fb001',
                'fireball/fb002',
                'fireball/fb003',
                'fireball/fb004',
                'fireball/fb005']

fireball = Actor(fireball_img[0])
fireball.images = fireball_img
fireball.scale = 4
fireball.fps = 10
fireball.active = False
fireball.y = player.y



word_list = ['James','Mary','Michael','Patricia','Robert','Jennifer','John','Linda','David','Elizabeth','William','Barbara','Richard','Susan','Joseph','Jessica','Thomas','Karen','Christopher','Sarah','Charles','Lisa','Daniel','Nancy','Matthew','Sandra','Anthony','Betty','Mark','Ashley','Donald','Emily','Steven','Kimberly','Andrew','Margaret','Paul','Donna','Joshua','Michelle','Kenneth','Carol','Kevin','Amanda','Brian','Melissa','Timothy','Deborah','Ronald','Stephanie','George','Rebecca','Jason','Sharon','Edward','Laura','Jeffrey','Cynthia','Ryan','Dorothy','Jacob','Amy','Nicholas','Kathleen','Gary','Angela','Eric','Shirley','Jonathan','Emma','Stephen','Brenda','Larry','Pamela','Justin','Nicole','Scott','Anna','Brandon','Samantha','Benjamin','Katherine','Samuel','Christine','Gregory','Debra','Alexander','Rachel','Patrick','Carolyn','Frank','Janet','Raymond','Maria','Jack','Olivia','Dennis','Heather','Jerry','Helen','Tyler','Catherine','Aaron','Diane','Jose','Julie','Adam','Victoria','Nathan','Joyce','Henry','Lauren','Zachary','Kelly','Douglas','Christina','Peter','Ruth','Kyle','Joan','Noah','Virginia','Ethan','Judith','Jeremy','Evelyn','Christian','Hannah','Walter','Andrea','Keith','Megan','Austin','Cheryl','Roger','Jacqueline','Terry','Madison','Sean','Teresa','Gerald','Abigail','Carl','Sophia','Dylan','Martha','Harold','Sara','Jordan','Gloria','Jesse','Janice','Bryan','Kathryn','Lawrence','Ann','Arthur','Isabella','Gabriel','Judy','Bruce','Charlotte','Logan','Julia','Billy','Grace','Joe','Amber','Alan','Alice','Juan','Jean','Elijah','Denise','Willie','Frances','Albert','Danielle','Wayne','Marilyn','Randy','Natalie','Mason','Beverly','Vincent','Diana','Liam','Brittany','Roy','Theresa','Bobby','Kayla','Caleb','Alexis','Bradley','Doris','Russell','Lori','Lucas','Tiffany']



question = random.choice(word_list)
question = question.lower()
response = ''



def update():
    global response
    zombie.animate()
    player.animate()
    fireball.animate()
    if not(player.image in player_die1_img) and not(zombie.image in zombie_die_img):
        zombie.x -=1
    if player.image == player_die1_img[-1]:
        player.images = player_idle1_img
        player.fps=20
    if player.image == player_attack2_img[-1]:
        player.images = player_idle1_img
        player.fps=20
    if  zombie.image == zombie_die_img[-1]:
        zombie.images = zombie_run_img
        zombie.right = WIDTH 
    if zombie.left <= 0:
        zombie.right = WIDTH + 100 
        response = ''
    if zombie.collide_pixel(player) and not(player.image in player_attack2_img):
        zombie.right = WIDTH + 100
        response = ''
        player.images = player_die1_img
        player.fps = 5
    if fireball.active:
        fireball.move_forward(5)
        if fireball.collide_pixel(zombie):
            fireball.active = False
            zombie.images = zombie_die_img

    

def on_key_down(key):
    global response, question
    if key in range(97, 123):
        print(chr(key))
        response += chr(key)
    elif key == keys.SPACE:
        # response +- ' '
        if response == question:
            print('correct')
            response = ''
            question = random.choice(word_list).lower()
            player.images = player_attack2_img
            fireball.pos = player.pos
            fireball.active = True
    elif key == keys.BACKSPACE:
        response = response [0:-1]
    



def draw():
    screen.clear()
    screen.draw.text(question, {50, 100}, fontsize=120)
    screen.draw.text(response,(50,100),fontsize=120,color='orange')
    zombie.draw()
    player.draw()
    if fireball.active:
        fireball.draw()

pgzrun.go()