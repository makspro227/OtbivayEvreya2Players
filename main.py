import spritePro
import pygame
from time import sleep


pygame.init()
FPS = 60
WIDTH , HEIGHT = 800, 600
pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('sounds/fon.ogg')
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)
pygame.mixer.Sound('sounds/hit.ogg')



screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Отбивай Еврея X')

bg = pygame.transform.scale(pygame.image.load('sprites/bg.jpg'),(WIDTH, HEIGHT))

clock = pygame.time.Clock()
pygame.font.init()
 
font = pygame.font.Font(None, 110)
font_2 = pygame.font.Font(None,87)
lose_screen = font.render('Ты Его Выбил!', True, (0, 255, 0))
skip_screen = font.render('Пропустил!!!', True, (255, 0, 0))
win_screen = font.render('Тотально Отбил!!!', True, (0, 0, 255))
win_screen_2 = font_2.render('Тотально Пропустил!!!', True, (255, 0, 255))


p1 = spritePro.GameSprite('sprites/platforma.png',(150,50),(50,250),4)
p1.rotate_to(-90)

p2 = spritePro.GameSprite('sprites/platforma.png',(150,50),(750,250),4)
p2.rotate_to(90)

ball = spritePro.GameSprite('sprites/Igor_ball.png',(50,50),(400,300),3)

ball_speed_x = 3
ball_speed_y = 3


lose_frames_1 = 0
lose_frames_2 = 0
total_frames = 0
score_1 = 0
score_2 = 0
clock = pygame.time.Clock()
run = True
game_over = False
winner = None




while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.blit(bg,(0,0))
    score_1_text = font.render(str(score_1), True, (255, 255, 0))
    screen.blit(score_1_text,(100,100))
    score_2_text = font.render(str(score_2), True, (150, 255, 150))
    screen.blit(score_2_text,(600,100))
    if not game_over:
        p1.update(screen)
        p1.handle_keyboard_input(up_key=pygame.K_w, down_key=pygame.K_s, left_key= None, right_key= None)
        
        p2.update(screen)
        p2.handle_keyboard_input(up_key=pygame.K_UP, down_key=pygame.K_DOWN, left_key= None, right_key= None)
        ball.update(screen)
        ball.move(ball_speed_x, ball_speed_y)
        p1.limit_movement(screen.get_rect())
        p2.limit_movement(screen.get_rect())
        

        if ball.rect.top < 0 or ball.rect.bottom > HEIGHT:
            ball_speed_y += 1
            ball_speed_y *= -1

            
            
        if ball.collide_with(p1) or ball.collide_with(p2):
            ball_speed_x += 1
            ball_speed_x *= -1
            pygame.mixer.Sound.play(pygame.mixer.Sound('sounds/hit.ogg'))
            
            
            
        if ball.rect.right > WIDTH:
            lose_frames_1 = 30
            score_1 += 1
            ball.position.x , ball.position.y = (400,300)
            ball_speed_x *= -1
        if lose_frames_1 > 0 and total_frames == 0:
            screen.blit(lose_screen,(100,200))
            lose_frames_1 -= 1
        if ball.rect.right < 0:
            lose_frames_2 = 30
            score_2 += 1
            ball.position.x , ball.position.y = (400,300)
            ball_speed_x *= -1
        if lose_frames_2 > 0 and total_frames == 0:
            lose_frames_2 -= 1
            screen.blit(skip_screen,(100,200))

        if score_1 == 3:
            winner = "Игрок 1"
            game_over = True
            
        if score_2 == 3:
            winner = "Игрок 2"
            game_over = True
        
    if game_over:
        if winner == 'Игрок 1':
            screen.blit(win_screen,(100,200))
            pygame.mixer.music.stop()

        if winner == 'Игрок 2':
            screen.blit(win_screen_2,(50,200))
            pygame.mixer.music.stop()
        



        
        

        

    pygame.display.update()
    clock.tick(FPS)


