import pygame
import random
pygame.init()

window=pygame.display.set_mode((1300, 690))
pygame.display.set_caption("BASKETBALL COURT")


pygame.init()

#loading images
surface1=pygame.image.load("./2court.png")
bg=pygame.transform.scale(surface1,(1300,690))
Hoop=pygame.image.load("./hook.png")
Ball=pygame.image.load("./basketball.png")

welcome_screen=pygame.image.load("./basketball-hoop-1.png")
gameover=pygame.image.load("./gameover.png")



bomb=pygame.image.load("./bum.png")


Ball1=pygame.image.load("./BB.png")
Ball5=pygame.image.load("./basketball.png")
Ball2=pygame.image.load("./BB.png")
Ball3=pygame.image.load("./BB.png")
Ball4=pygame.image.load("./basketball.png")

clock=pygame.time.Clock()
font=pygame.font.SysFont("comicsans",55)

#function for text on game screen
def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    window.blit(screen_text,[x,y])


def welcome():
    exit_game=False
    Ball1_x=random.randint(70,1300)
    Ball1_y=random.randint(-20,0)
    Ball2_x = random.randint(1200, 1300)
    Ball2_y = random.randint(-20, 0)
    Ball3_x = random.randint(700, 1300)
    Ball3_y = random.randint(-20, 0)
    Ball4_x = random.randint(200, 300)
    Ball4_y = random.randint(-20, 0)
    Ball5_x = random.randint(100, 500)
    Ball5_y = random.randint(-20, 0)

    while not exit_game:
        #Initializing welcome screen
        window.fill((225,225,225))
        window.blit(welcome_screen,(370,50))
        window.blit(Ball1,(Ball1_x,Ball1_y))
        window.blit(Ball2, (Ball2_x,Ball2_y ))
        window.blit(Ball3, (Ball3_x,Ball3_y))
        window.blit(Ball4, (Ball4_x,Ball4_y))
        window.blit(Ball4, (Ball5_x, Ball5_y))

        text_screen("WELCOME TO BASKETBALL COURT",(139,115,85),210,530)
        text_screen("Press SPACE To Play",(139,115,85),380,580)

        #random movement of balls
        Ball1_y+=5
        Ball1_x-=3
        if Ball1_y>400:
            Ball1_y=400

        Ball2_y += 7
        Ball2_x -= 2
        if Ball2_y>400:
            Ball2_y=400


        Ball3_y += 5
        Ball3_x += 2
        if Ball3_y>400:
            Ball3_y=400

        Ball4_y += 5
        Ball4_x += 3
        if Ball4_y>400:
            Ball4_y=400

        Ball5_y += 5
        Ball5_x += 6
        if Ball5_y>400:
            Ball5_y=400



        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    game_loop()

        pygame.display.update()
        clock.tick(30)


#initializing main game
def game_loop():
    exit_game = True
    Game_over = False

    #game specific variables
    i = 0
    x = random.randint(0, 1300)
    clock = pygame.time.Clock()
    width = 1300
    ball_y = 0
    hoop_y = 600
    score = 0
    Miss = 0
    bomb_x=random.randint(10,1200)
    bomb_y=0
    Ball1_x=random.randint(10,1200)
    Ball1_y=random.randint(-100,0)

    #file for storing highscore
    with open("C:\\Users\\SANA MARIYM\\Desktop\\Basketball court.txt","r") as f:
        hi_score = f.read()


    while exit_game:
        #condition for game over
        if Game_over==True:
            window.fill((225,225,225))
            window.blit(gameover, (0, 0))
            text_screen("PRESS 'ENTER' TO PLAY AGAIN", (225, 225, 0),250,(560))
            with open("C:\\Users\\SANA MARIYM\\Desktop\\Basketball court.txt","w") as f:
                f.write(str(hi_score))


            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or pygame.K_ESCAPE:
                        game_loop()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = False


            mx,my=pygame.mouse.get_pos()

            #storing images in rectangle
            hoop_rect = Hoop.get_rect(center=(mx, hoop_y))
            ball_rect = Ball.get_rect(center=(x, ball_y))
            Ball1_rect = Ball1.get_rect(center=(Ball1_x,Ball1_y))
            bomb_rect = bomb.get_rect(center=(bomb_x, bomb_y))



            #condition for collision of ball and hoop
            if pygame.Rect.colliderect(hoop_rect,  ball_rect):
                ball_y = 0
                x = random.randint(0,1200)
                score +=1
                pygame.mixer.music.load("C:\\Users\\SANA MARIYM\\Music\\whoosh.wav")
                pygame.mixer.music.play()


            #condition for collision of bomb and hoop
            if pygame.Rect.colliderect(hoop_rect,  bomb_rect):
                if score>=15:
                    pygame.mixer.music.load("C:\\Users\\SANA MARIYM\\Music\\mixkit-arcade-game-explosion-2759.wav")
                    pygame.mixer.music.play()
                    Game_over = True

            #moving background
            window.fill((0,0,0))
            window.blit(bg,(i,0))
            window.blit(bg,(width+i,0))
            if i==-width:
                window.blit(bg,(width+i,0))
                i=0
            i-=1

            ball_y+=5
            bomb_y+=3
            Ball1_y+=5


            window.blit(Ball, ball_rect)
            window.blit(Hoop, hoop_rect)

            #condition for ball miss
            if ball_y>500:
                ball_y= random.randint(-200,0)
                x = random.randint(0, 1200)
                Miss+=1


            text_screen("MISSED:" + str(Miss), (0, 0, 0), 1000, 100)
            #condition for gameover
            if Miss==3:
                Game_over=True



            text_screen("SCORE:" + str(score), (0, 0, 0), 1000, 50)
            #condition for bomb blit
            if score>15:
                window.blit(bomb,bomb_rect)
                if bomb_y>600:
                    bomb_x = random.randint(10, 1200)
                    bomb_y = random.randint(-1000,-100)


            if score>20:
                ball_y+=3

             #condition for second ball
            if score>50:
                window.blit(Ball1,(Ball1_x,Ball1_y))
                if Ball1_y > 600:
                        Ball1_y = random.randint(-200, -100)
                        Ball1_x = random.randint(0, 1200)
                        Miss += 1

                #collision of 2nd ball and hoop
                if pygame.Rect.colliderect(hoop_rect, Ball1_rect):
                    score+=1
                    Ball1_y = random.randint(-200, -100)
                    Ball1_x = random.randint(0, 1200)
                    pygame.mixer.music.load("C:\\Users\\SANA MARIYM\\Music\\whoosh.wav")
                    pygame.mixer.music.play()


            if score>60:
                ball_y+=3

            if score>int(hi_score):
                hi_score=score
            text_screen("HIGHSCORE:" + str(hi_score), (0, 0, 0), 10, 100)

        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    quit()
welcome()
