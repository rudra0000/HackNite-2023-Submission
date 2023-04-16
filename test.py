import pygame 
import os
import sys
import random
pygame.mixer.init()
pygame.font.init()
HEALTH_GAIN_SOUND=pygame.mixer.Sound(os.path.join('assets','health_gain_sound.mp3'))
SPACESHIP_CRASH=pygame.mixer.Sound(os.path.join('assets','spaceship_crash.wav'))
ENEMY_DESTROY_SOUND=pygame.mixer.Sound(os.path.join('assets','enemy_destroyed.wav'))
LASER_HIT_SOUND=pygame.mixer.Sound(os.path.join('assets','lase_hit.wav'))
BG_MUSIC=pygame.mixer.Sound(os.path.join('assets','nCapJack.mp3'))
RED=(255,0,0)
GREEN=(0,255,0)
WIDTH,HEIGHT=1000,800
MAX_WINDOW_WIDTH=1400
WIN=pygame.display.set_mode((MAX_WINDOW_WIDTH,HEIGHT))
BASE_YELLOW_SHIP=pygame.image.load(os.path.join('assets','pixel_ship_yellow.png'))
PLAYER_LENGTH=BASE_YELLOW_SHIP.get_height()
PLAYER_WIDTH=BASE_YELLOW_SHIP.get_width()
BASE_LASER=pygame.image.load(os.path.join('assets','pixel_laser_yellow.png'))
YELLOW_LASER_HEIGHT=BASE_LASER.get_height()
YELLOW_LASER_WIDTH=BASE_LASER.get_width()

#IMAGES
#PORTAL=(pygame.image.load(os.path.join('assets','blackhole.png')))
ALIEN = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'alien.png')), (200,200))
PORTAL=pygame.transform.scale(pygame.image.load(os.path.join('assets','blackhole.png')),(20,20))

BASE_GREEN_SHIP=pygame.image.load(os.path.join('assets','pixel_ship_green_small.png'))
BASE_GREEN_LASER=pygame.image.load(os.path.join('assets','pixel_laser_green.png'))

YELLOW_SHIP=pygame.transform.scale(pygame.image.load(os.path.join('assets','rocket.png')),(PLAYER_WIDTH,PLAYER_LENGTH))
BASE_BLUE_LASER=pygame.image.load(os.path.join('assets','pixel_laser_blue.png'))
RED_BASE_LASER=pygame.image.load(os.path.join('assets','pixel_laser_red.png'))
YELLOW_LASER = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'missileOP.png')), (YELLOW_LASER_WIDTH,YELLOW_LASER_HEIGHT))
BG=pygame.transform.scale(pygame.image.load(os.path.join('assets','background-black.png')),(WIDTH,HEIGHT))
WIDE_BG=pygame.transform.scale(pygame.image.load(os.path.join('assets','WIDE_BG.jpeg')),(MAX_WINDOW_WIDTH,HEIGHT))
BULLET_HIT = 10

PLAYER_VEL=10
ENEMY_VEL = 1
LASER_VEL=3
ENEMY_LASER_VEL=1
GREEN_HEALTH=10
PLAYER_HEALTH=150             #player health
RED_HEALTH=20
BLUE_HEALTH=30
BASE_BLUE_SHIP =pygame.image.load(os.path.join('assets','pixel_ship_blue_small.png'))
BLUE_ENEMY_WIDTH=BASE_BLUE_SHIP.get_width()
BLUE_ENEMY_LENGTH=BASE_BLUE_SHIP.get_height()
GREEN_ENEMY_WIDTH=BASE_GREEN_SHIP.get_width()
GREEN_ENEMY_LENGTH=BASE_GREEN_SHIP.get_height()
RED_ENEMY_WIDTH=BLUE_ENEMY_WIDTH
RED_ENEMY_LENGTH=BLUE_ENEMY_LENGTH
BLUE_SHIP=pygame.transform.scale(pygame.image.load(os.path.join('assets','Benemy.png')), (BLUE_ENEMY_WIDTH,BLUE_ENEMY_LENGTH))
RED_SHIP=pygame.transform.scale(pygame.image.load(os.path.join('assets','Renemy.png')),(BLUE_ENEMY_WIDTH,BLUE_ENEMY_LENGTH))
BLUE_LASER_WIDTH=BASE_BLUE_LASER.get_width()
GREEN_LASER_WIDTH=BASE_GREEN_LASER.get_width()
RED_LASER_WIDTH=RED_BASE_LASER.get_width()

GREEN_LASER_HEIGHT=BASE_GREEN_LASER.get_height()
BLUE_LASER_HEIGHT=BASE_BLUE_LASER.get_height()
RED_LASER_HEIGHT=RED_BASE_LASER.get_height()
RED_LASER=pygame.transform.scale(pygame.image.load(os.path.join('assets','Rlaser.png')),(RED_LASER_WIDTH -60,RED_LASER_HEIGHT-60))
GREEN_LASER = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'Glaser.png')), (GREEN_LASER_WIDTH-60,GREEN_LASER_HEIGHT-60))
GREEN_SHIP = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'Genemy.png')), (GREEN_ENEMY_WIDTH+20,GREEN_ENEMY_LENGTH+20))
BLUE_LASER = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'Blaser.png')), (GREEN_LASER_WIDTH-60,GREEN_LASER_HEIGHT-60))
pygame.display.set_caption('Alien Attack')
BLACK=(0,0,0)
FPS=60
class health:
    def __init__(self,x,y):
        self.x_cor=x
        self.y_cor=y
        self.height=50 #to change accordingly
        self.width=50
        self.portal_image=PORTAL
        self.mask = pygame.mask.from_surface(self.portal_image)
    def move(self):
        self.y_cor+=ENEMY_LASER_VEL   
    
class laser:
    COLOR_DICT={
        'green':GREEN_LASER,
        'red':RED_LASER,
        'blue':BLUE_LASER,
        'yellow':YELLOW_LASER
    }
    def __init__(self,x,y,color):
        self.x_cor=x
        self.y_cor=y
        self.color=color
        self.laser_img=self.COLOR_DICT[color]
        self.mask = pygame.mask.from_surface(self.laser_img)
    def draw(self):
        WIN.blit(self.laser_img,(self.x_cor,self.y_cor))
       
    def emove(self):
        self.y_cor+=ENEMY_LASER_VEL
    def pmove(self):
        self.y_cor-=LASER_VEL
    
    def hit(self,object):
        return collide(self,object)



class ship:
    def __init__(self,x_cor,y_cor):
        self.x_cor=x_cor
        self.y_cor=y_cor
        
        self.vel=None
        self.width = None
        self.height = None
        self.ship_image = None
        self.laser_image = None

    def draw(self, window):
        WIN.blit(self.ship_image,(self.x_cor,self.y_cor))

    def get_height(self):
        return self.ship_image.get_height()

    def get_width(self):
        return self.ship_image.get_width()    

class player(ship):
    def __init__(self, x_cor, y_cor):
        super().__init__(x_cor, y_cor)  
        self.ship_image = YELLOW_SHIP
        self.laser_image = YELLOW_LASER  
        self.mask = pygame.mask.from_surface(self.ship_image)
        self.vel=PLAYER_VEL
        self.width=PLAYER_WIDTH
        self.length=PLAYER_LENGTH
        self.life=PLAYER_HEALTH
        self.player_lasers=[]
    def fire(self):
       
            new_laser=laser(self.x_cor+PLAYER_WIDTH/2-YELLOW_LASER_WIDTH/2,self.y_cor-YELLOW_LASER_HEIGHT+PLAYER_LENGTH/2,'yellow')
            self.player_lasers.append(new_laser)
    def checkCollision(self,obj):
        return collide(self,obj)
        

class enemy(ship):
    COLOR_DICT = { 
        'green':(GREEN_SHIP,GREEN_LASER,GREEN_HEALTH,GREEN_ENEMY_WIDTH,GREEN_ENEMY_LENGTH),
        'red':(RED_SHIP,RED_LASER,RED_HEALTH,RED_ENEMY_WIDTH,RED_ENEMY_LENGTH),
        'blue':(BLUE_SHIP,BLUE_LASER,BLUE_HEALTH,BLUE_ENEMY_WIDTH,BLUE_ENEMY_LENGTH)
    }
    SIZE_DICT={
        'green':(GREEN_ENEMY_WIDTH,GREEN_ENEMY_LENGTH,GREEN_LASER_WIDTH,GREEN_LASER_HEIGHT),
        'blue': (BLUE_ENEMY_WIDTH,BLUE_ENEMY_LENGTH,BLUE_LASER_WIDTH,BLUE_LASER_HEIGHT),
        'red': (RED_ENEMY_WIDTH,RED_ENEMY_LENGTH,RED_LASER_WIDTH,RED_LASER_HEIGHT),
    }
    enemy_lasers=[]
    COOLDOWN=120
    cool_down_counter=0
    def __init__(self, x_cor, y_cor,color):
        super().__init__(x_cor, y_cor)
        self.color = color
        self.vel=ENEMY_VEL
        self.ship_image,self.laser_image,self.life,self.width,self.length=self.COLOR_DICT[color]   
        self.mask = pygame.mask.from_surface(self.ship_image)       
        
    def move(self):
        self.y_cor += ENEMY_VEL
    
    def fire(self):
        self.cool_down_counter += 1
        if self.cool_down_counter%150 == 0:
            self.cool_down_counter = 0
            new_laser=laser(self.x_cor+self.SIZE_DICT[self.color][0]/2-self.SIZE_DICT[self.color][2]/2,self.y_cor+self.SIZE_DICT[self.color][3]/2-self.SIZE_DICT[self.color][1],self.color)
            self.enemy_lasers.append(new_laser)



def collide(object1,object2):
    vec_x=(object2.x_cor-object1.x_cor)
    vec_y=(object2.y_cor-object1.y_cor)
    return object1.mask.overlap(object2.mask,(vec_x,vec_y))!=None
def draw(my_ship,enemies,main_font,no_of_kills,level,health_list,lost_font):
    WIN.blit(WIDE_BG,(0,0))
    WIN.blit(BG,(200,0))
    score_level=main_font.render(f'KILLS:{no_of_kills}',1,RED)
    WIN.blit(score_level,(25,10))
    my_ship.draw(WIN)
    if my_ship.life==0:
        lost_label=lost_font.render('You Lost!!',1,RED)
        score_label=lost_font.render(f'Your Kills:{no_of_kills}',1,RED)
        WIN.blit(score_label,(MAX_WINDOW_WIDTH/2-score_label.get_width()/2,HEIGHT/2+50))
        WIN.blit(lost_label,(MAX_WINDOW_WIDTH/2-lost_label.get_width()/2,HEIGHT/2))
    else:
        if len(health_list)!=0:
            WIN.blit(PORTAL,(health_list[0].x_cor,health_list[0].y_cor))
        for enemy in enemies:
            enemy.draw(WIN)
        for lasers in my_ship.player_lasers:
            lasers.draw()
        for enemy in enemies:
            for lasers1 in enemy.enemy_lasers:
                lasers1.draw()
        pygame.draw.rect(WIN,RED,(25,120,150,20))
        pygame.draw.rect(WIN,GREEN,(25,120,my_ship.life,20))
        level_display=main_font.render(f'LEVEL:{level}',1,RED)
        WIN.blit(level_display,(1200+10,HEIGHT-50))
   
    
    pygame.display.update()


def main():
    
    pygame.init()
    run=True
    clock=pygame.time.Clock()
    level = 0
    wave_length = 3
    enemies=[]
    yellow_ship=player(MAX_WINDOW_WIDTH/2-PLAYER_WIDTH/2,HEIGHT-PLAYER_LENGTH)
    main_font=pygame.font.SysFont('comicsans',50)
    health_list=[]
    no_of_kills=0
    lost_font=pygame.font.SysFont('comicsans',70)
    while run:
        clock.tick(FPS)
        #BG_MUSIC.play()
        if  len(enemies)==0:
            level += 1
            wave_length = level*3
            if   len(health_list)==0:
                bonus_health=health(random.randrange(250,WIDTH-40+200),random.randrange(-1000*level//3,-60))
                health_list.append(bonus_health)
                
            else:
                health_list.remove(bonus_health)
                
            for i in range(wave_length):
                Enemy = enemy(random.randrange(250,WIDTH-40+200),random.randrange(-1000*level//3,-60),random.choice(['red','green','blue']))
                enemies.append(Enemy)
        
        
            
            #render one life lost on screen
           
        '''if  yellow_ship.life==0:
            run=False'''

            #render you have lost the game
        
       
        

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    yellow_ship.fire()
                  
          
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and yellow_ship.x_cor - yellow_ship.vel >=200: 
            yellow_ship.x_cor -= yellow_ship.vel
        if keys[pygame.K_d] and yellow_ship.x_cor +yellow_ship.vel +PLAYER_WIDTH <= WIDTH+200: 
            yellow_ship.x_cor += yellow_ship.vel
        if keys[pygame.K_w] and yellow_ship.y_cor - yellow_ship.vel >=0: 
            yellow_ship.y_cor -= yellow_ship.vel
        if keys[pygame.K_s] and yellow_ship.y_cor + PLAYER_LENGTH + yellow_ship.vel<=HEIGHT: 
            yellow_ship.y_cor += yellow_ship.vel            

        #enemy moves
        
        for x in enemies[:]:
             if x.y_cor+ENEMY_VEL+100<=HEIGHT and x.life>0:
                 x.move()
                 x.fire()
               
             else:
                 enemies.remove(x)
                
        for lasers in yellow_ship.player_lasers[:]:
            if lasers.y_cor-LASER_VEL>=0:
                lasers.pmove()
            else:
                yellow_ship.player_lasers.remove(lasers)
        for x in enemies[:]:
            for y in x.enemy_lasers[:]:
                if y.y_cor+ENEMY_LASER_VEL+100<=HEIGHT:
                    y.emove()
                else:
                    x.enemy_lasers.remove(y)

       
        if bonus_health.y_cor+ENEMY_LASER_VEL+50<=HEIGHT:
            bonus_health.move()
        else:
            if len(health_list)!=0:
                health_list.remove(bonus_health)
            

        #checking collisions btw player and enemy lasers  & player and enemy collision
        for x in enemies[:]:
            if yellow_ship.checkCollision(x):
                if yellow_ship.life!=0:
                    yellow_ship.life -= BULLET_HIT
                SPACESHIP_CRASH.play()
                x.life=0
            for y in x.enemy_lasers[:]:
                if yellow_ship.checkCollision(y):
                    x.enemy_lasers.remove(y)
                    if yellow_ship.life!=0:
                         yellow_ship.life -= BULLET_HIT
                    
        #now we are checking the collision of player lasers with enemies
        for x in enemies[:]:
            for i in yellow_ship.player_lasers[:]:
                if collide(x,i):
                    yellow_ship.player_lasers.remove(i)
                    LASER_HIT_SOUND.play()
                    if x.life-BULLET_HIT==0:
                        if yellow_ship.life!=0:
                            no_of_kills+=1
                            ENEMY_DESTROY_SOUND.play()
                    x.life -= BULLET_HIT    
                                
            for y in x.enemy_lasers[:]:
                for j in yellow_ship.player_lasers[:]:
                    if collide(y,j):
                        if y in x.enemy_lasers:
                            x.enemy_lasers.remove(y)
                        yellow_ship.player_lasers.remove(j)
            if  collide(yellow_ship,bonus_health):
                if yellow_ship.life!=0:
                    yellow_ship.life=PLAYER_HEALTH
                    HEALTH_GAIN_SOUND.play()
                if len(health_list)!=0:
                    health_list.remove(bonus_health)
                   
                   

        
      
        print(yellow_ship.life)
        draw(yellow_ship,enemies,main_font,no_of_kills,level,health_list,lost_font)
       
def main_menu():
    run1 = True
    title_font = pygame.font.SysFont("comicsans", 70)
    while run1:
        BG_MUSIC.play()
        WIN.blit(WIDE_BG,(0,0))
        WIN.blit(BG,(200,0))
        title_label = title_font.render("Press enter key...",1,RED)

        WIN.blit(title_label,(MAX_WINDOW_WIDTH/2-title_label.get_width()/2 , HEIGHT/2-100)) 
        WIN.blit(ALIEN, (MAX_WINDOW_WIDTH/2-ALIEN.get_width()/2, HEIGHT/2))
        pygame.display.update() 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run1 = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main()
                    run1 = False

    pygame.quit()   
  
if __name__=='__main__':
    main_menu()
