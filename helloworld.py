import pygame
import random
import time


#________Initialize the game________
pygame.init()

'''Review chap 13 for advancement'''
#________GLOBAL CONSTANTS___________
# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
FONT = (250,242,7)


#______SET SCREEN SIZE______
screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])


#__________TEXT____________
pygame.display.set_caption("TNT game")
#Set the font here instead of in while loop because
#the font stay the same, only the text change
#font = pygame.font.SysFont('Calibri', 100, True, False)
# Render the text. "True" means anti-aliased text.
# Black is the color. The variable BLACK was defined
# above as a list of [0, 0, 0]
# Note: This line creates an image of the letters,
# but does not put it on the screen yet.
#text = font.render('You crashed!',True,RED)

#_________CLASSES__________
class Block(pygame.sprite.Sprite):
    """
    This class represents the ball
    It derives from the "Sprite" class in Pygame
    """
    def __init__(self,width,height,image):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.image.load(image).convert()
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
 
    def reset_pos(self):
        """ Reset position to the top of the screen, at a random x location.
        Called by update() or the main program loop if there is a collision.
        """
        self.rect.y = random.randrange(-20, -5)
        self.rect.x = random.randrange(-50, screen_width)
 
    def update(self):
        """ Called each frame. """
 
        # Move block down one pixel
        
        self.rect.y += 6
        self.rect.x += 1
 
        # If block is too far down, reset to top of screen.
        if self.rect.y > 1000:
            self.reset_pos()
        
        screen.blit(self.image,(self.rect.x,self.rect.y))
 
 
class Player(Block):
    """ The player class derives from Block, but overrides the 'update'
    functionality with new a movement function that will move the block
    with the mouse. """
    def update(self):
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        pos = pygame.mouse.get_pos()
 
        # Fetch the x and y out of the list,
        # just like we'd fetch letters out of a string.
        # Set the player object to the mouse location
        self.rect.x = pos[0] - 42
        self.rect.y = pos[1]
        screen.blit(self.image,(self.rect.x,self.rect.y))
        
class Enemy(Block):
    """ The player class derives from Block, but overrides the 'update'
    functionality with new a movement function that will move the block
    with the mouse. """
    def update(self):
        screen.blit(self.image,(self.rect.x,self.rect.y))
        
    
class Laser(Block):
    """ The player class derives from Block, but overrides the 'update'
    functionality with new a movement function that will move the block
    with the mouse. """
    
    def update(self):
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        pos = pygame.mouse.get_pos()
 
        # Fetch the x and y out of the list,
        # just like we'd fetch letters out of a string.
        # Set the player object to the mouse location
        self.rect.x = pos[0] 
        self.rect.y -= 1
        screen.blit(self.image,(self.rect.x,self.rect.y))
        
        


#____________SPRITE_____________
# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
block_list = pygame.sprite.Group()
 
# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()

#List of enemy and laser collision
laser_and_enemy = pygame.sprite.Group()



for i in range(15):
    # This represents a block
    block = Block(10, 10,'fire16.png')
    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(200)
 
    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)
    

    
# Create a Player block
player = Player(80, 40,'player.png')
all_sprites_list.add(player)
#Laser list
laser_list = pygame.sprite.Group()
laser_list1 = [] #This list is to make laser disapear when y < 0

#Create a enemy list:
for i in range(1):
    # This represents a block
    enemy = Enemy(10,10,'enemy.png')
    # Set a random location for the block
    enemy.rect.x = random.randrange(screen_width)
    enemy.rect.y = random.randrange(20)
    laser_and_enemy.add(enemy)
 
    # Add the block to the list of objects
    block_list.add(enemy)
    all_sprites_list.add(enemy)


        
# __________A list of random locations of snow________
snow_list = []
for i in range(1000):
    x = random.randrange(0, 1000)
    y = random.randrange(0, 1000)
    snow_list.append([x,y])
    
#_________________________Image & Music_______________________


#Make mouse cursor disappear
pygame.mouse.set_visible(False)

#Load sound music
sound = pygame.mixer.Sound('laser5.ogg')




 
# Loop until the user clicks the close button.
Intro = False
smallfont = pygame.font.SysFont(None, 30)
done = True
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score = 0

# -------- Main Program Loop -----------

while not Intro:
    
    screen.fill(BLACK)
    font = pygame.font.SysFont('VNI Wed7', 40, True, False)
    text1 = font.render('You are a spaceship traveling through space',True,WHITE)
    text2 = font.render('Unfortunately, you are trespassing on alien territory',True,WHITE)
    text3 = font.render('Now you have to fight the alien',True,WHITE)
    text4 = font.render('Avoid the flares and shoot the alien 50 times',True,WHITE)
    text5 = font.render('use your MOUSE to play the game',True,RED)

    text = font.render('press KEY DOWN to continue',True,FONT)
    
    k = 35
    screen.blit(text1, [200-k,50+k])
    screen.blit(text2, [150-k,100+k])
    screen.blit(text3, [250-k,150+k])
    screen.blit(text4, [150-k,200+k])
    screen.blit(text5, [250-k,250+k])
    
    screen.blit(text, [250-k,300+k])
    
    pygame.display.update()
    clock.tick(15)
    
    for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                Intro = True
                done = False
    
    

                while not done:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            done = True
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                                # Turn the mouse position into a rect with the dimensions
                                # of the laser_image. You can use the event.pos instead
                                # of pygame.mouse.get_pos() and pass it as the `center`
                                # or `topleft` argument.
                                #Create a Laser block
                                laser = Laser(10,10,'fire18.png')
                                laser.rect.x = event.pos[0] 
                                laser.rect.y = event.pos[1]
                                laser_list.add(laser)
                                laser_list1.append(laser)
                                sound.play()
                                laser_and_enemy.add(laser)


                    screen.fill(BLACK)

                    while laser_list1 != []:

                        laser.update()
                        if laser.rect.y < 0:
                            laser_list1.remove(laser)
                    # Set the background
                    #screen.blit(background,[0,0])

                    #Get the mouse position for the player_image
                    '''mouse_position = pygame.mouse.get_pos()
                    x = mouse_position[0]
                    y = mouse_position[1]
                    #Get the above x,y coodinates to become the coordinates of the player_image
                    screen.blit(player_image,[x-50,y-75])'''

                    #_____SPRITE_____

                    enemy.update()

                    # Calls update() method on every sprite in the list
                    all_sprites_list.update()

                    # See if the player block has collided with anything.
                    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, False)

                    # See if the laser block has collided with enemy.
                    laser_hit_enemy = pygame.sprite.spritecollide(enemy, laser_and_enemy, False)



                    if len(blocks_hit_list) >= 1:
                        #Set the font here instead of in while loop because
                        #the font stay the same, only the text change
                        font = pygame.font.SysFont('Calibri', 100, True, False)
                        # Render the text. "True" means anti-aliased text.
                        # Black is the color. The variable BLACK was defined
                        # above as a list of [0, 0, 0]
                        # Note: This line creates an image of the letters,
                        # but does not put it on the screen yet.
                        text = font.render('You crashed!',True,RED)
                        screen.blit(text, [250, 250])
                        done = True
                    elif len(laser_hit_enemy) >= 50:
                        done = True






                    # Draw all the spites
                    all_sprites_list.draw(screen)

                    #____SNOW____
                    #Draw snow based on locations above while loop
                    for i in range(len(snow_list)):
                        pygame.draw.rect(screen, WHITE, [snow_list[i][0],snow_list[i][1],2,5] )
                        #Move snow down
                        snow_list[i][1] += 10
                        #When snow bounce off the screen
                        if snow_list[i][1] > 1000:
                            #Reset x and y locations of snow
                            y = random.randrange(-3,-2)
                            snow_list[i][1] = y
                            x = random.randrange(0,1000)
                            snow_list[i][0] = x





                    pygame.display.flip()
                    clock.tick(30)  # 30 FPS is smoother.


                pygame.quit()
