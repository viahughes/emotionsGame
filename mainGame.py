import pygame

pygame.init()

#800 pixels wide, 480 pixels tall
gameDisplay = pygame.display.set_mode((800,480)) #use tuple (()) or list([])
pygame.display.set_caption('Emotions Game')


#**************** MAIN GAMEPLAY *********************************************

#MAIN TITLE SCREEN ANIMATION + CLICKABLE PLAY BUTTON

#MAKI EXPLAINS HOW TO PLAY (AUDIO + VISUAL ON SCREEN)
# (We need to write dialogue for what maki will say for each part of the game
#  then do a text-to-speech recording or something)

#SCREEN SAYS TO WATCH CLOSELY, ONCE SCREEN IS TOUCHED TRIGGER A VIDEO TO PLAY

#WHEN VIDEO IS DONE, SHOW CLICKABLE EMOTION OPTIONS

#WHEN EMOTION IS CHOSEN, STORE DATA (CORRECT OR NOT ETC), SHOW SOMETHING FUN
#OR EDUCATIONAL ON SCREEN (prof emailed about making the game about learning
# and not just testing so we need to squeeze in learning between testing

#***************************************************************************



#***************   SETTINGS  ************************************************


# (refer to flowchart on google drive for a rough plan for settings)
import pygame

pygame.init()

white = (255,255,255)
red = (255,0,0)

display_width = 800
display_height = 480


gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Emotions Game')

font = pygame.font.SysFont(None, 25)


def message_to_screen (msg, color):
  screen_text = font.render(msg, True, color)
  gameDisplay.blit(screen_text, [display_width/2, display_height/2])
  
def settingsLoop():
    gameDisplay.fill(white)
    message_to_screen("Select C to go to clients or R to return to game", red);
    pygame.display.update()
    
    for event in pygame.event.get():
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                settingsLoop() 
            if event.key == pygame.K_c:
                settingsLoop()
                
    gameDisplay.fill(white)     
    pygame.display.update()


settingsLoop()
            
            
            
  



#****************************************************************************




