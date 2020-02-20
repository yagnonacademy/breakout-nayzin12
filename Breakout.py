##############################################
#                                            #
#               Breakout Game                #
#               by: Brendan                  #
#                                            #
#                                            #
##############################################

import sys
 
import pygame
from pygame.locals import *


BLACK=(0,0,0)
WHITE=(250,250,250)
RED=(250,0,0)
GREEN=(0,250,0)
BLUE=(0,0,250)

def draw_block(screen,x,y):
    pygame.draw.rect(screen,BLUE,(70+x,50+y,125,20))
        
def main():



        
    pygame.init()

    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    myfont2 = pygame.font.SysFont('Comic Sans MS', 50)
    fps = 60
    fpsClock = pygame.time.Clock()
     
    width, height = 800, 700
    screen = pygame.display.set_mode((width, height))


    xspeed=10
    yspeed=10
    ball_position=[400,250]
    pos_list=[[0,0],[170,0],[340,0],[510,0],[0,50],[170,50],[340,50],[510,50],[0,100],[170,100],[340,100],[510,100],[0,150],[170,150],[340,150],[510,150]]
    score=0
    life=3

    #Sound Track
    pygame.mixer.music.load("background_music.mp3")
    pygame.mixer.music.play()

    destroy_sound=pygame.mixer.Sound("explode.ogg")

     
    # Game loop.
    done=False
    while not done:
      screen.fill(BLACK)
      
      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
      
      # Update.
      ball_position[1]+=yspeed
      ball_position[0]+=xspeed

      if ball_position[0] >= 770 or ball_position[0] <= 30:
          xspeed=-xspeed

      if ball_position[1] >= 675 or ball_position[1] <= 30:
          yspeed=-yspeed


      #mouse control
      pos=pygame.mouse.get_pos()
      mouse_x=pos[0]
      mouse_y= pos[1]

      if mouse_x >= 645:
          mouse_x=645

      if mouse_x <= 30:
          mouse_x=30

      pygame.mouse.set_visible(False)


      #Game Over
      if ball_position[1] >= 675:
          life -= 1
          ball_position=[400,300]
          yspeed=-yspeed
          
      if life == 0:    
          done=True
          pygame.mouse.set_visible(True)
          game_over = myfont2.render('GAME OVER', False, RED)
          screen.blit(game_over,(300,300))

      if score == 16:    
          done=True
          pygame.mouse.set_visible(True)
          game_over = myfont2.render('CONGRATULATIONS!', False, WHITE)
          screen.blit(game_over,(225,300))


      #paddle collision
      paddle_x1=mouse_x
      paddle_x2=mouse_x+125
      paddle_y=570
      if paddle_x1 < ball_position[0] < paddle_x2 and  ball_position[1]==paddle_y:
          yspeed=-yspeed
          xspeed+= int(2*yspeed*(ball_position[0]-(mouse_x+62))/125)

      
          
      # Draw.

      #Borders
      pygame.draw.circle(screen,RED,ball_position,10)
      pygame.draw.rect(screen,BLUE,(0,0,800,30))
      pygame.draw.rect(screen,BLUE,(0,0,30,700))
      pygame.draw.rect(screen,BLUE,(770,0,30,700))
      pygame.draw.rect(screen,BLUE,(0,620,800,90))
      

      #block position
     
      for i in range(len(pos_list)):

          #ball collision
          if 70+pos_list[i][0] < ball_position[0] < 70+pos_list[i][0]+125 and ball_position[1] == pos_list[i][1]+70:
              yspeed=-yspeed
              destroy_sound.play()
              del pos_list[i]
              score += 1
              break

      score_font = myfont.render('Score: '+ str(score), False, WHITE)
              
      for i in range(len(pos_list)):
          draw_block(screen,pos_list[i][0],pos_list[i][1])   


      #paddle
      pygame.draw.rect(screen,WHITE,(mouse_x,570,125,10))

      #text
      screen.blit(score_font,(650,650))

      life_font = myfont.render('Lives Remaining: '+ str(life), False, WHITE)
      screen.blit(life_font,(30,650))

      
      
      
      
      pygame.display.set_caption('Breakout (Created by: Brendan)')
      pygame.display.flip()
      fpsClock.tick(fps)

    
    while True:
      screen.fill(BLACK)
      
      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
         
main()  
