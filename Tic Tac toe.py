#modules for this game
import pygame
from pygame.locals import *
pygame.init()

#screen initialization
screenwidth=300
screenheight=300
screen=pygame.display.set_mode((screenwidth,screenheight))
pygame.display.set_caption("Tic Tac Toe")

#declarind some global variables which is to be used in whole program
linewidth=5
markers=[]
clicked=False
pos=[]
players=1
win=0
over=False
again_rect=Rect(screenwidth//2-80,screenheight//2,160,50)
font=pygame.font.SysFont(None,40)

green=(0,255,0)
red=(255,0,0)
blue=(0,0,255)

#creating a 2d list for markers
for x in range(3):
    rows=[0]*3
    markers.append(rows)

#function for grid lines
def draw_lines():
    bg=(255,255,200)
    grid=(50,50,50)
    screen.fill(bg)
    for x in range(1,3):
        pygame.draw.line(screen,grid,(0,x*100),(screenwidth,x*100),linewidth)
        pygame.draw.line(screen,grid,(x*100,0),(x*100,screenheight),linewidth)

#function for creating x and o
def draw_markers():
    x_pos=0
    for x in markers:
        y_pos=0
        for y in x:
            if y==1 :
                pygame.draw.line(screen,green,(x_pos*100+15,y_pos*100+15),(x_pos*100+85,y_pos*100+85),linewidth)
                pygame.draw.line(screen,green,(x_pos*100+15,y_pos*100+85),(x_pos*100+85,y_pos*100+15),linewidth)
            if y==-1:
                pygame.draw.circle(screen,red,(x_pos*100+50,y_pos*100+50),38,linewidth)
            y_pos+=1
        x_pos+=1

#function for checking winner
def check_winner():
    global win
    global over
    y_pos=0
    for x in markers:
        if sum(x)==3:
            win=1
            over=True
        if sum(x)==-3:
            win=2
            over=True
        if markers[0][y_pos]+markers[1][y_pos]+markers[2][y_pos]==3:
            win=1
            over=True
        if markers[0][y_pos]+markers[1][y_pos]+markers[2][y_pos]==-3:
            win=2
            over=True
    if markers[0][0]+markers[1][1]+markers[2][2]==3:
        win=1
        over=True
    if markers[0][0]+markers[1][1]+markers[2][2]==-3:
         win=1
         over=True
    if markers[2][0]+markers[1][1]+markers[0][2]==3:
        win=1
        over=True
    if markers[2][0]+markers[1][1]+markers[0][2]==-3:
        win=2
        over=True
    count=0;
    for x in markers:
        for y in x:
            if y==0:
                break;
            else:
                count+=1
    if count==9:
        over=True
            

def draw_winner(win):
    if win==0:
        draw_text="  Match Draw"
        draw_img=font.render(draw_text,True,blue)
        pygame.draw.rect(screen,green,(screenwidth//2-100,screenheight//2-60,200,50))
        screen.blit(draw_img,(screenwidth//2-100,screenheight//2-50))
    else:
        win_text="Player "+str(win)+" wins !"
        win_img=font.render(win_text,True,blue)
        pygame.draw.rect(screen,green,(screenwidth//2-100,screenheight//2-60,200,50))
        screen.blit(win_img,(screenwidth//2-100,screenheight//2-50))

    again_text="Play Again?"
    again_img=font.render(again_text,True,blue)
    pygame.draw.rect(screen,green,again_rect)
    screen.blit(again_img,(screenwidth//2-80,screenheight//2+10))
    

                

#main loops for windows
run=True
while run:

    draw_lines()
    draw_markers()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if over==False:
            if event.type==pygame.MOUSEBUTTONDOWN and clicked==False:
                clicked=True
            if event.type==pygame.MOUSEBUTTONUP and clicked==True:
                clicked=False
                pos=pygame.mouse.get_pos()
                cell_x=pos[0]
                cell_y=pos[1]
                if markers[cell_x//100][cell_y//100]==0:
                    markers[cell_x//100][cell_y//100]=players
                    players*=-1
                    check_winner()
    if over==True:
        draw_winner(win)
        if event.type==pygame.MOUSEBUTTONDOWN and clicked==False:
                clicked=True
        if event.type==pygame.MOUSEBUTTONUP and clicked==True:
            clicked=False
            pos=pygame.mouse.get_pos()
            if again_rect.collidepoint(pos):
                markers=[]
                clicked=False
                pos=[]
                players=1
                win=0
                over=False
                for x in range(3):
                    rows=[0]*3
                    markers.append(rows)

                

        
    pygame.display.update()

pygame.quit()
        
