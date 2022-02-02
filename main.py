import pygame
import sys
import random
from time import sleep

# BLACK=(0,0,0)
padWidth=480
padHeight=640

rockImage=['rock01.png','rock02.png','rock03.png','rock04.png','rock05.png',\
           'rock06.png','rock07.png','rock08.png','rock09.png','rock10.png',\
           'rock11.png','rock12.png','rock13.png','rock14.png','rock15.png',\
           'rock16.png','rock17.png','rock18.png','rock19.png','rock20.png',\
           'rock21.png','rock22.png','rock23.png','rock24.png','rock25.png',\
           'rock26.png','rock27.png','rock28.png','rock29.png','rock30.png']






def drawObject(obj,x,y):
    global gamePad
    gamePad.blit(obj,(x,y))
    

def initGame():
    global gamePad, clock, background, fighter, missile, explosion
    pygame.init()
    gamePad=pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption('상환이 게임') # 게임이름
    background=pygame.image.load('background.png') #배경 그림
    fighter=pygame.image.load('fighter.png')# 전투기 그림
    missile=pygame.image.load('missile.png')
    explosion=pygame.image.load('explosion.png') #전투기 미사일 운석에 맞은경우
    clock= pygame.time.Clock()

def runGame():
    global gamePad, clock, background, fighter, missile, explosion
    isShot = False
    shotCount = 0
    rockPassed = 0
    
   
    
    
    
    
    
    # 전투기 크기
    fighterSize=fighter.get_rect().size
    fighterWidth=fighterSize[0]
    fighterHeight=fighterSize[1]
    
    #전투기 초기 위치
    x=padWidth * 0.45
    y=padHeight * 0.9
    fighterX = 0
    
    #무기좌표 리스트
    missileXY = []
    
    # 운석 랜덤생성
    rock=pygame.image.load(random.choice(rockImage))
    rockSize = rock.get_rect().size #운석 크기
    rockWidth= rockSize[0]
    rockHeight = rockSize[1]
    
    # 운석 초기 위치 설정
    rockX = random.randrange(0, padWidth - rockWidth) 
    rockY = 0
    rockSpeed = 2   
    
    onGame=False
    while not onGame:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()
                
            if event.type in[pygame.KEYDOWN]:
                if event.key==pygame.K_LEFT:
                    fighterX -=5
                elif event.key == pygame.K_RIGHT:
                    fighterX += 5    
                
                elif event.key == pygame.K_SPACE:
                    missileX = x + fighterWidth/2
                    missileY = y - fighterHeight
                    missileXY.append([missileX,missileY])    
                    
                    
            if event.type in[pygame.KEYUP]:
                if event.key == pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    fighterX=0
        
        
        drawObject(background,0,0) #배경그림 그리기
        x += fighterX
        if x < 0:
           x = 0
        elif x > padWidth-fighterWidth:
             x = padWidth-fighterWidth
        
        drawObject(fighter,x,y)
        
        if len(missileXY) != 0:
            for i, bxy in enumerate(missileXY):
                bxy[1] -= 10
                missileXY[i][1]=bxy[1]
                if bxy[1] <= 0:
                    try:
                        missileXY.remove(bxy)
                    except:
                        pass
        
        if len(missileXY) != 0:
            for bx, by in missileXY:
                drawObject(missile, bx, by)         
        
        
        rockY += rockSpeed # 운석 아래로 움직임
        
        #운석이 지구로 떨어진 경우
        if rockY > padHeight:
            # 새로운 운석(랜덤)
           rock = pygame.image.load(random.choice(rockImage))
           rockSize = rock.get_rect().size
           rockWidth = rockSize[0]
           rockHight = rockSize[1]
           rockX = random.randrange(0, padWidth - rockWidth)
           rocky = 0
                       
        drawObject(rock, rockX,rockY)# 운석 그리기
        # gamePad.fill(BLACK)

        pygame.display.update() # 게임화면을 다시 그림
        
        clock.tick(60)
    pygame.quit()
    
initGame()
runGame()    
                