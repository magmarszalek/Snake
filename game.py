import pygame
import sys
import random
import csv
import os

pygame.init()

SW, SH = 700, 700

BLOCK_SIZE = 35
font_titles =pygame.font.Font("font.ttf", 35)
font_digits = pygame.font.Font("font.ttf", 70)
font_text = pygame.font.Font("font.ttf", 20)
start_time = 10
score = 0

screen = pygame.display.set_mode((910, 700))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
start_ticks = pygame.time.get_ticks()

# Wczytanie obrazu
snake_image = pygame.image.load("images/snake.png")
snake_image = pygame.transform.scale(snake_image, (BLOCK_SIZE, BLOCK_SIZE))
snake_bok_image = pygame.image.load("images/snake_bok.png")
snake_bok_image = pygame.transform.scale(snake_bok_image, (BLOCK_SIZE, BLOCK_SIZE))
snake_head_image = pygame.image.load("images/snake_head.png")
snake_head_image = pygame.transform.scale(snake_head_image, (BLOCK_SIZE, BLOCK_SIZE))
snake_head_d = pygame.image.load("images/head_d.png")
snake_head_d = pygame.transform.scale(snake_head_d, (BLOCK_SIZE, BLOCK_SIZE))
snake_head_l = pygame.image.load("images/head_l.png")
snake_head_l = pygame.transform.scale(snake_head_l, (BLOCK_SIZE, BLOCK_SIZE))
snake_head_r = pygame.image.load("images/head_r.png")
snake_head_r = pygame.transform.scale(snake_head_r, (BLOCK_SIZE, BLOCK_SIZE))
snake_tail_image = pygame.image.load("images/snake_tail.png")
snake_tail_image = pygame.transform.scale(snake_tail_image, (BLOCK_SIZE, BLOCK_SIZE))
snake_tail_d = pygame.image.load("images/snake_tail_d.png")
snake_tail_d = pygame.transform.scale(snake_tail_d, (BLOCK_SIZE, BLOCK_SIZE))
snake_tail_l = pygame.image.load("images/snake_tail_l.png")
snake_tail_l = pygame.transform.scale(snake_tail_l, (BLOCK_SIZE, BLOCK_SIZE))
snake_tail_r = pygame.image.load("images/snake_tail_r.png")
snake_tail_r = pygame.transform.scale(snake_tail_r, (BLOCK_SIZE, BLOCK_SIZE))
snake_turn_u_r = pygame.image.load("images/snake_turn_u_r.png")
snake_turn_u_r = pygame.transform.scale(snake_turn_u_r, (BLOCK_SIZE, BLOCK_SIZE))
snake_turn_u_l = pygame.image.load("images/snake_turn_u_l.png")
snake_turn_u_l = pygame.transform.scale(snake_turn_u_l, (BLOCK_SIZE, BLOCK_SIZE))
snake_turn_d_r = pygame.image.load("images/snake_turn_d_r.png")
snake_turn_d_r = pygame.transform.scale(snake_turn_d_r, (BLOCK_SIZE, BLOCK_SIZE))
snake_turn_d_l = pygame.image.load("images/snake_turn_d_l.png")
snake_turn_d_l = pygame.transform.scale(snake_turn_d_l, (BLOCK_SIZE, BLOCK_SIZE))
# Wczytanie obrazu dla apple
apple_image = pygame.image.load("images/apple.png")
apple_image = pygame.transform.scale(apple_image, (BLOCK_SIZE, BLOCK_SIZE))
gold_apple_image = pygame.image.load("images/gold_apple.png")
gold_apple_image = pygame.transform.scale(gold_apple_image, (BLOCK_SIZE, BLOCK_SIZE))
# Wczytanie obrazu dla mapy
dirt_image = pygame.image.load("images/board.jpg")
dirt_image = pygame.transform.scale(dirt_image, (700, 700))
#arrows
arrow_u = pygame.image.load("images/u.png")
arrow_u= pygame.transform.scale(arrow_u, (35, 35))
arrow_d = pygame.image.load("images/d.png")
arrow_d= pygame.transform.scale(arrow_d, (35, 35))
arrow_l = pygame.image.load("images/l.png")
arrow_l= pygame.transform.scale(arrow_l, (35, 35))
arrow_r = pygame.image.load("images/r.png")
arrow_r= pygame.transform.scale(arrow_r, (35, 35))

end_image = pygame.image.load("images/end.png")
end_image = pygame.transform.scale(end_image, (700, 700))

class Snake:
     
    def __init__(self):
        self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
        self.xdir = 1 
        self.ydir = 0
        self.head = screen.blit(snake_head_image, (self.x, self.y))
        self.body = [pygame.Rect(self.x - BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
        self.dead = False

    def update(self):
        for square in self.body:
            if self.head.x == square.x and self.head.y == square.y:
                self.dead = True
            if self.head.x not in range (0, SW) or self.head.y not in range (0, SH):
                self.dead = True

        if self.dead:
            name = get_player_name()
            save_score(name, score)
            import menu

        self.body.append(self.head)
        for i in range(len(self.body) - 1):
            self.body[i].x, self.body[i].y = self.body[i+1].x, self.body[i+1].y  # Przesunięcie każdego segmentu ciała w kierunku poprzedniego segmentu
        self.head.x += self.xdir * BLOCK_SIZE # Zmiana pozycji głowy na podstawie kierunku
        self.head.y += self.ydir * BLOCK_SIZE
        self.body.remove(self.head) # Usunięcie ostatniego segmentu ciała

class Apple:
    def __init__(self):
        self.x = random.randrange(0, SW, BLOCK_SIZE)
        self.y = random.randrange(0, SH, BLOCK_SIZE)
        self.rect = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)

    def update(self):
        screen.blit(apple_image, (self.x, self.y))

class GoldApple:
    def __init__(self):
        self.x = random.randrange(0, SW, BLOCK_SIZE)
        self.y = random.randrange(0, SH, BLOCK_SIZE)
        self.rect = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)

    def update(self):
        screen.blit(gold_apple_image, (self.x, self.y))

def drawGrid():
        for x in range(0, SW, BLOCK_SIZE):
             for y in range (0, SH, BLOCK_SIZE):
                rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
                pygame.draw.rect(screen, "black", rect, 1)

def get_player_name():
    input_active = True
    name = ""
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE: 
                    name = name[:-1]
                else:
                    if len(name)<15:
                        name += event.unicode 
        
        
        # Wyświetlanie ekranu z polem do wpisania imienia
        screen.blit(end_image, (0,0))
        prompt_0 = font_digits.render("GAME OVER", True, (255, 0, 0))
        prompt = font_digits.render("Enter your name:", True, (255, 255, 255))
        input_box = font_digits.render(name, True, (255, 0, 0))
        screen.blit(prompt_0, (200, 200))
        screen.blit(prompt, (120, 300))
        screen.blit(input_box, (200, 400))
        prompt_score = font_digits.render(f"Score:  {score}", True, (255, 255, 255))
        screen.blit(prompt_score, (120, 500))
        pygame.display.flip()
    
    return name

def save_score(name, score):
    file_exists = os.path.isfile("rank.csv")
    with open("rank.csv", mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow([0], [1])  # Nagłówki
        writer.writerow([name, score])  # Dodawanie wyniku


def main():
    SW, SH = 700, 700

    BLOCK_SIZE = 35
    font_titles =pygame.font.Font("font.ttf", 35)
    font_digits = pygame.font.Font("font.ttf", 70)
    font_text = pygame.font.Font("font.ttf", 20)
    start_time = 10

    screen = pygame.display.set_mode((910, 700))
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()
    start_ticks = pygame.time.get_ticks()
        
    drawGrid()
    snake = Snake()
    snake.body.append(pygame.Rect(0,0, BLOCK_SIZE, BLOCK_SIZE))
    snake.body.append(pygame.Rect(0,0, BLOCK_SIZE, BLOCK_SIZE))
    gold_apple = None
    apple = Apple()
    APPLE_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(APPLE_EVENT, 12000)

# Główna pętla gry
    while True:    
        seconds_elapsed = (pygame.time.get_ticks() - start_ticks) // 1000 # Oblicz, ile czasu minęło
        remaining_time = start_time - seconds_elapsed

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()     
            elif remaining_time <= 0:
                name = get_player_name()
                save_score(name, score)
                import menu
            elif event.type == APPLE_EVENT:
                if gold_apple is None:
                    gold_apple = GoldApple()
        # Sterowanie
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN and snake.ydir != -1:
                        snake.ydir = 1 # 1 w dół -1 w górę
                        snake.xdir = 0
                    elif event.key == pygame.K_UP and snake.ydir != 1:
                        snake.ydir = -1
                        snake.xdir = 0
                    elif event.key == pygame.K_RIGHT and snake.xdir != -1:
                        snake.ydir = 0
                        snake.xdir = 1 # 1 w prawo -1 w lewo               
                    elif event.key == pygame.K_LEFT and snake.xdir != 1:
                        snake.ydir = 0
                        snake.xdir = -1

        snake.update()
        screen.blit(dirt_image, (0, 0))
        apple.update()
        if gold_apple:
                gold_apple.update()

        # Obraz ciała węża
        if snake.xdir == 0: #głowa
                if snake.ydir == -1 :
                    screen.blit(snake_head_image, (snake.head.x, snake.head.y))
                if snake.ydir == 1 : 
                    screen.blit(snake_head_d, (snake.head.x, snake.head.y))
        else:
                if snake.xdir == -1 :
                    screen.blit(snake_head_l, (snake.head.x, snake.head.y))
                if snake.xdir == 1 : 
                    screen.blit(snake_head_r, (snake.head.x, snake.head.y))    
        for square in snake.body:#ciało
                for i in range(1, len(snake.body)):
                    segment = snake.body[i]
                    prev_segment = snake.body[i-1]
                    beh_segment = snake.body[i-2]
                    # Jeśli segment porusza się w innym kierunku niż poprzedni, zmienia się obrazek
                    if i != 1: #generowanie obrazu ruch pionowy
                        if segment.x == prev_segment.x and segment.y == prev_segment.y + BLOCK_SIZE or segment.x == prev_segment.x and segment.y == prev_segment.y - BLOCK_SIZE:
                            if beh_segment.x == segment.x - BLOCK_SIZE and beh_segment.y == segment.y - BLOCK_SIZE:#generowanie obrazu skrętu
                                screen.blit(snake_image, (segment.x, segment.y))
                                screen.blit(snake_turn_d_l, (segment.x, segment.y -BLOCK_SIZE))
                            elif beh_segment.x == segment.x - BLOCK_SIZE and beh_segment.y == segment.y + BLOCK_SIZE:
                                screen.blit(snake_image, (segment.x, segment.y))
                                screen.blit(snake_turn_u_l, (segment.x, segment.y +BLOCK_SIZE))
                            elif beh_segment.x == segment.x + BLOCK_SIZE and beh_segment.y == segment.y - BLOCK_SIZE:
                                screen.blit(snake_image, (segment.x, segment.y))
                                screen.blit(snake_turn_d_r, (segment.x, segment.y -BLOCK_SIZE))
                            elif beh_segment.x == segment.x + BLOCK_SIZE and beh_segment.y == segment.y + BLOCK_SIZE:
                                screen.blit(snake_image, (segment.x, segment.y))
                                screen.blit(snake_turn_u_r, (segment.x, segment.y +BLOCK_SIZE))
                            else:
                                screen.blit(snake_image, (segment.x, segment.y)) #generowanie obrazu ruch poziomy
                        elif segment.y == prev_segment.y and segment.x == prev_segment.x + BLOCK_SIZE or segment.y == prev_segment.y and segment.x == prev_segment.x - BLOCK_SIZE:
                            if beh_segment.x == segment.x - BLOCK_SIZE and beh_segment.y == segment.y - BLOCK_SIZE:#generowanie obrazu skrętu
                                screen.blit(snake_bok_image, (segment.x, segment.y))
                                screen.blit(snake_turn_u_r, (segment.x-BLOCK_SIZE, segment.y))
                            elif beh_segment.x == segment.x - BLOCK_SIZE and beh_segment.y == segment.y + BLOCK_SIZE:
                                screen.blit(snake_bok_image, (segment.x, segment.y))
                                screen.blit(snake_turn_d_r, (segment.x - BLOCK_SIZE, segment.y))
                            elif beh_segment.x == segment.x + BLOCK_SIZE and beh_segment.y == segment.y - BLOCK_SIZE:
                                screen.blit(snake_bok_image, (segment.x, segment.y))
                                screen.blit(snake_turn_u_l, (segment.x + BLOCK_SIZE, segment.y))
                            elif beh_segment.x == segment.x + BLOCK_SIZE and beh_segment.y == segment.y + BLOCK_SIZE:
                                screen.blit(snake_bok_image, (segment.x, segment.y))
                                screen.blit(snake_turn_d_l, (segment.x + BLOCK_SIZE, segment.y))
                            else:
                                screen.blit(snake_bok_image, (segment.x, segment.y))   

                    if i == 1 :  #segment (ogon)
                        if segment.x == prev_segment.x and segment.y == prev_segment.y - BLOCK_SIZE:  #w górę 
                            screen.blit(snake_tail_image, (segment.x, segment.y)) 
                        elif segment.x == prev_segment.x and segment.y == prev_segment.y + BLOCK_SIZE: #w dół
                            screen.blit(snake_tail_d, (segment.x, segment.y))
                        elif segment.y == prev_segment.y and segment.x == prev_segment.x + BLOCK_SIZE:  # Ruch w prawo
                            screen.blit(snake_tail_r, (segment.x, segment.y))
                        elif segment.y == prev_segment.y and segment.x == prev_segment.x - BLOCK_SIZE:  # Ruch w lewo
                            screen.blit(snake_tail_l, (segment.x, segment.y)) 

        # Obsługa zdarzeń apple
        if snake.head.x == apple.x and snake.head.y == apple.y:
                snake.body.append(pygame.Rect(square.x, square.y, BLOCK_SIZE, BLOCK_SIZE))
                score = score + 50
                apple = Apple()
        if gold_apple:
                if snake.head.x == gold_apple.x and snake.head.y == gold_apple.y:
                    snake.body.append(pygame.Rect(square.x, square.y, BLOCK_SIZE, BLOCK_SIZE))
                    start_time = start_time + 15
                    score = score + 100
                    gold_apple = None
            
        # Wyczyść obszar paska obok planszy
        pygame.draw.rect(screen, (0, 0, 0), (700, 0, 200, SH))  # Prostokąt w obszarze paska

        # Rysowanie statystyk

        if remaining_time >= 1:
                timer_title = font_titles.render("Time:", True, (0, 0, 255))
                screen.blit(timer_title, (710, 12))
                timer_text = font_digits.render(str(remaining_time), True, (255, 255, 255))
                screen.blit(timer_text, (710, 50))
        elif remaining_time < 1:
                timer_text = font_titles.render("Time's up!", True, (255, 0, 0))
                screen.blit(timer_text, (730, 50))
                timer_title = font_titles.render("Time:", True, (0, 0, 255))
                
        score_title = font_titles.render("Score:", True, (0, 0, 255))
        screen.blit(score_title, (710, 132))
        score_text = font_digits.render(str(score), True, (255, 255, 255))
        screen.blit(score_text, (710, 170))
        # How to play
        info_title = font_titles.render("How to play:", True, (0, 0, 255))
        screen.blit(info_title, (710, 250))
        screen.blit(arrow_u, (710, 300))
        info_u = font_text.render("snake go up", True, (255, 255, 255))
        screen.blit(info_u, (750, 300))
        screen.blit(arrow_d, (710, 340))
        info_d = font_text.render("snake go down", True, (255, 255, 255))
        screen.blit(info_d, (750, 340))
        screen.blit(arrow_l, (710, 380))
        info_l = font_text.render("snake go left", True, (255, 255, 255))
        screen.blit(info_l, (750, 380))
        screen.blit(arrow_r, (710, 420))
        info_r = font_text.render("snake go right", True, (255, 255, 255))
        screen.blit(info_r, (750, 420))
        screen.blit(gold_apple_image, (710, 490)) 
        score_text = font_text.render("score + 100", True, (0, 255, 0))
        time_text = font_text.render("time + 15 s", True, (0, 255, 0))
        screen.blit(score_text, (750, 480))  
        screen.blit(time_text, (750, 510)) 
        screen.blit(apple_image, (710, 550)) 
        scorea_text = font_text.render("score + 50", True, (0, 255, 0))
        screen.blit(scorea_text, (750, 560))         
        end_info_text1 = font_text.render("Don't touch the edges !", True, (255, 0, 0))
        end_info_text2 = font_text.render("Don't touch snake's body !", True, (255, 0, 0))
        screen.blit(end_info_text1, (705, 600))
        screen.blit(end_info_text2, (705, 630))

        pygame.display.update() #Odświeża ekran gry, aby zmiany w grafice były widoczne.
        clock.tick(25) #Kontroluje ilość klatek na sekundę. W tym przypadku gra będzie działać z maksymalnie 10 FPS.
        pygame.time.delay(100)

if __name__=="__main__":
     main()

