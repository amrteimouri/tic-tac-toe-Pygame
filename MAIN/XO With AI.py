import pygame
pygame.init()
safhe=pygame.display.set_mode((600,600))
run=True
FPS=60
RED=(255,0,0)
pygame.display.set_caption("Negaaheno XO")
fpsClock=pygame.time.Clock()
fpsClock.tick(FPS)
Board=pygame.image.load("board_nad_bc.png")
x_png=pygame.image.load("x.png")
o_png=pygame.image.load("o.png")
safhe.fill((255,255,255))
safhe.blit(Board,(0,0))
blurboard=pygame.image.load("x-o-export.png")
Turn=1
winner=0
run2=True
winnerx=pygame.image.load("WinnerX.png")
winnero=pygame.image.load("WinnerO.png")
tiepng=pygame.image.load("tie.png")
eap=pygame.image.load("Exitandplayagain.png")
pae=pygame.image.load("playandexit.png")
matrix=[[0 for i in range(3)] for j in range(3)]
safhe.blit(blurboard, (0,0))
safhe.blit(pae, (0,0))
pygame.display.update()
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type== pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY=pygame.mouse.get_pos()      

            if 240<=mouseX and mouseX<=365 and 305<=mouseY and mouseY<=365:
                pygame.quit()
            if 200<=mouseX and mouseX<=400 and 215<=mouseY and mouseY<=290:
                run= False 
        if event.type==pygame.QUIT:
            pygame.quit()

safhe.blit(Board,(0,0))
pygame.display.update()

    
def moveX():
    global Turn
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type== pygame.MOUSEBUTTONDOWN:
            
       
            mouseX, mouseY=pygame.mouse.get_pos()
            
            soton_click=int(mouseY//200)
            radif_click=int(mouseX//200)
            if soton_click == 0 and radif_click == 0 and matrix[0][0]==0:
                safhe.blit(x_png, (0,0))
                matrix[0][0]=1
                Turn=(Turn+1)%2
            elif soton_click == 0 and radif_click == 1 and matrix[0][1]==0:
                safhe.blit(x_png, (200,0))
                matrix[0][1]=1
                Turn=(Turn+1)%2
            elif soton_click == 0 and radif_click == 2 and matrix[0][2]==0:
                safhe.blit(x_png, (400,0))
                matrix[0][2]=1
                Turn=(Turn+1)%2
            elif soton_click== 1 and radif_click == 0 and matrix[1][0]==0:
                safhe.blit(x_png, (0,200))
                matrix[1][0]=1
                Turn=(Turn+1)%2
            elif soton_click==1 and radif_click==1 and matrix[1][1]==0:
                safhe.blit(x_png, (200,200))
                matrix[1][1]=1
                Turn=(Turn+1)%2
            elif soton_click==1 and radif_click == 2 and matrix[1][2]==0:
                safhe.blit(x_png, (400,200))
                matrix[1][2]=1
                Turn=(Turn+1)%2
            elif soton_click==2 and radif_click==0 and matrix[2][0]==0:
                safhe.blit(x_png, (0,400))
                matrix[2][0]=1
                Turn=(Turn+1)%2
            elif soton_click==2 and radif_click ==1 and matrix[2][1]==0:
                safhe.blit(x_png, (200,400))
                matrix[2][1]=1
                Turn=(Turn+1)%2
            elif soton_click==2 and radif_click==2 and matrix[2][2]==0:
                safhe.blit(x_png, (400,400))
                matrix[2][2]=1
                Turn=(Turn+1)%2
            else:
                moveX()
        if event.type==pygame.QUIT:
            pygame.quit()


    pygame.display.update()
def moveO():
    global Turn
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit
        if event.type== pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY=pygame.mouse.get_pos()
            soton_click=int(mouseY//200)
            radif_click=int(mouseX//200)
            if soton_click == 0 and radif_click == 0 and matrix[0][0]==0:
                safhe.blit(o_png, (0,0))
                matrix[0][0]=2
                Turn=(Turn+1)%2
            elif soton_click == 0 and radif_click == 1 and matrix[0][1]==0:
                safhe.blit(o_png, (200,0))
                matrix[0][1]=2
                Turn=(Turn+1)%2
            elif soton_click == 0 and radif_click == 2 and matrix[0][2]==0:
                safhe.blit(o_png, (400,0))
                matrix[0][2]=2
                Turn=(Turn+1)%2
            elif soton_click== 1 and radif_click == 0 and matrix[1][0]==0:
                safhe.blit(o_png, (0,200))
                matrix[1][0]=2
                Turn=(Turn+1)%2
            elif soton_click==1 and radif_click==1 and matrix[1][1]==0:
                safhe.blit(o_png, (200,200))
                matrix[1][1]=2
                Turn=(Turn+1)%2
            elif soton_click==1 and radif_click == 2 and matrix[1][2]==0:
                safhe.blit(o_png, (400,200))
                matrix[1][2]=2
                Turn=(Turn+1)%2
            elif soton_click==2 and radif_click==0 and matrix[2][0]==0:
                safhe.blit(o_png, (0,400))
                matrix[2][0]=2
                Turn=(Turn+1)%2
            elif soton_click==2 and radif_click ==1 and matrix[2][1]==0:
                safhe.blit(o_png, (200,400))
                matrix[2][1]=2
                Turn=(Turn+1)%2
            elif soton_click==2 and radif_click==2 and matrix[2][2]==0:
                safhe.blit(o_png, (400,400))
                matrix[2][2]=2
                Turn=(Turn+1)%2
            else:
                moveO()
        if event.type==pygame.QUIT:
            pygame.quit()
    pygame.display.update()



def check():
    if matrix[0][0] == matrix[0][1] and  matrix[0][2] == matrix[0][1] and matrix[0][0]!= 0:
        return matrix[0][0]
    elif matrix[1][0] == matrix[1][1] and  matrix[1][2] == matrix[1][1] and matrix[1][0]!= 0:
        return matrix[1][0]
    elif matrix[2][0] == matrix[2][1] and  matrix[2][2] == matrix[2][1] and matrix[2][0]!= 0:
        return matrix[2][0]
    elif matrix[0][0] == matrix[1][0] and  matrix[2][0] == matrix[1][0] and matrix[0][0]!= 0:
        return matrix[0][0]
    elif matrix[0][1] == matrix[1][1] and  matrix[2][1] == matrix[1][1] and matrix[0][1]!= 0:
        return matrix[0][1]
    elif matrix[0][2] == matrix[1][2] and  matrix[2][2] == matrix[1][2] and matrix[0][2]!= 0:
        return matrix[0][2]
    elif matrix[0][0] == matrix[1][1] and  matrix[2][2] == matrix[1][1] and matrix[0][0]!= 0:
        return matrix[0][0]
    elif matrix[0][2] == matrix[1][1] and  matrix[2][0] == matrix[1][1] and matrix[1][1]!= 0:
        return matrix[1][1]
    else:
        return 0
def xoc():
    cnt=0
    for i in range(3):
        for j in range(3):
            if matrix[i][j]!=0:
                cnt=cnt+1
    return cnt
def tie():
    if check()==0 and xoc()==9:
        return True
    else:
        return False

while run2:
    if Turn == 1:
        moveX()
    else:
        moveO()
    if check()!=0 or tie():
        winner=check()
        safhe.blit(blurboard, (0,0))
        if winner==1:
            safhe.blit(winnerx, (0,0))
            safhe.blit(eap,(0,0))
        elif winner==2:  
            safhe.blit(winnero, (0,0))
            safhe.blit(eap,(0,0))
        else:
            safhe.blit(tiepng,(0,0))
            safhe.blit(eap,(0,0))
        pygame.display.update() 
        run=True
        while run:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    
                if event.type== pygame.MOUSEBUTTONDOWN:
                    mouseX, mouseY=pygame.mouse.get_pos()      

                    if 130<=mouseX and mouseX<=250 and 300<=mouseY and mouseY<=370:
                        pygame.quit()
                        run2=False
                        run=False
                    if 285<=mouseX and mouseX<=485 and 300<=mouseY and mouseY<=370:
                        safhe.blit(Board,(0,0))
                        matrix=[[0 for i in range(3)] for j in range(3)]
                        pygame.display.update()
                        run=False

                if event.type==pygame.QUIT:
                    pygame.quit()


    