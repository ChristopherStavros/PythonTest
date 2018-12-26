import pygame, os, webbrowser, time, sys, random, pyttsx3

############
#VARIABLES
############

#Text to  speech engine
engine = pyttsx3.init()
#Colors
red = (255,0,0)
white = (255, 255, 255)
bright_red = (255,0,0)
bright_green = (0,255,0)
#Media
song = 'C:\\_Repositories\\PythonTest\\Projects\\PythonStudy1\\Erazer2.mp3'
image = 'C:\\_Repositories\\PythonTest\\Projects\\PythonStudy1\\FullSizeRender.jpg'

###########
#Functions
###########

def setBackGround():
    bg = pygame.image.load(image)
    screen.blit(bg, (0, 0))

def setWhite():
    screen.fill(white)
    pygame.display.flip()

def setRed():
    screen.fill(red)
    pygame.display.flip()

def setRandom():
    color = (random.randint(0,255),random.randint(0,255), random.randint(0,255))
    screen.fill(color)
    pygame.display.flip()

def talk(words):
    engine.say(words)
    engine.runAndWait() 

def drawRect(color):
    mouse_position = pygame.mouse.get_pos()
    setBackGround()
    pygame.draw.rect(screen, color, (mouse_position[0],mouse_position[1],50,50))
    pygame.display.flip()

###############
#Main program
###############

#Load screen
screen = pygame.display.set_mode ( (800, 600) )
bg = pygame.image.load(image)
screen.blit(bg, (0, 0))

#Setup screen and load song
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)
pygame.mixer.music.load(song)

#########
#EVENTS
#########

while True:
    for event in pygame.event.get():
        #MOUSE MOTION
        if event.type == pygame.MOUSEMOTION:
            drawRect(bright_green)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawRect(bright_red)
        #QUIT
        elif event.type == pygame.QUIT:
            sys.exit()
        #Keystrokes
        elif event.type == pygame.KEYDOWN:
            #ESCAPE
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            #PLAY
            elif event.key == pygame.K_p:
                if not pygame.mixer.music.get_busy():
                    talk('Calibrating...the nozzle.')
                    pygame.mixer.music.play()
                    setRandom()
            #STOP
            elif event.key == pygame.K_t:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.stop()
                    setWhite()
            #PAUSE
            elif event.key == pygame.K_s:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    setRandom()
            #UNPAUSE
            elif event.key == pygame.K_r:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.unpause()
                    setRandom()

'''
NOTES

os.system('start C:\\_Repositories\\PythonTest\\Projects\\PythonStudy1\\a.wav')
webbrowser.open('C:\\_Repositories\\PythonTest\\Projects\\PythonStudy1\\a.wav') 

http://www.petercollingridge.co.uk/tutorials/pygame-physics-simulation/creating-pygame-window/
https://stackoverflow.com/questions/41189928/pygame-how-to-change-background-color
'''