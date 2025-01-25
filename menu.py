import pygame
import sys
import csv
import game
import subprocess

# Inicjalizacja Pygame
pygame.init()

# Ustawienia okna
SCREEN_WIDTH, SCREEN_HEIGHT = 700, 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Menu Główne")
winners = pygame.image.load("images/winners.png")
winners = pygame.transform.scale(winners, (700, 700))
snake_start = pygame.image.load("images/start_snake.png")
snake_start = pygame.transform.scale(snake_start, (700, 700))
snake_menu = pygame.image.load("images/menu.png")
snake_menu = pygame.transform.scale(snake_menu, (400, 220))
# Kolory
WHITE = ( 0, 100, 50)
BLACK = (255, 255, 255)
GRAY = (0, 0, 0)

# Czcionka
FONT = pygame.font.Font( "font.ttf", 70)
font_text = pygame.font.Font("font.ttf", 40)

# Funkcja do renderowania tekstu
def render_text(text, font, color, position):
    surface = font.render(text, True, color)
    rect = surface.get_rect(center=position)
    return surface, rect

# Funkcja menu głównego
def main_menu():
    menu_running = True
    clock = pygame.time.Clock()

    # Opcje menu
    menu_options = ["Start Game", "Winners", "Exit"]
    selected_option = 0

    while menu_running:
        screen.blit(snake_start, (0,0))
        screen.blit(snake_menu, (150,400))
        # Obsługa zdarzeń
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(menu_options)
                elif event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(menu_options)
                elif event.key == pygame.K_RETURN:
                    if menu_options[selected_option] == "Start Game":
                        game.main()
                        pygame.quit()
                        sys.exit()
                    elif menu_options[selected_option] == "Winners":
                        winners_menu()
                    elif menu_options[selected_option] == "Exit":
                        pygame.quit()
                        sys.exit()

        # Rysowanie opcji menu
        for i, option in enumerate(menu_options):
            color = BLACK if i == selected_option else GRAY
            text_surface, text_rect = render_text(option, FONT, color, (SCREEN_WIDTH // 2, 445 + i * 63))
            screen.blit(text_surface, text_rect)

        pygame.display.flip()
        clock.tick(30)

# Funkcja głównej gry


# Funkcja menu ustawień
def winners_menu():

    settings_running = True
    clock = pygame.time.Clock()
    while settings_running:
        screen.blit(winners, (0,0))
        def score_data():
                table = []
                with open("rank.csv", "r") as file:
                    reader = csv.reader(file)
                    for row in reader:
                        table.append(row)
                        row[1] = int(row[1])
                        
                return table

        # Odczyt danych z rank.csv
        score_table_database = score_data()
        sorted_scores = sorted(score_table_database, key=lambda x: x[1], reverse=True)

        # Wyświetlanie danych
        score_table_title = FONT.render("Winners: ", True, (255, 255, 0))
        screen.blit(score_table_title, (20, 30))

        y_offset = 150  # Początkowa pozycja
        for i, row in enumerate(sorted_scores[:10], start=1):
            fname, fscore = row[0], row[1]
            win_text = font_text.render(f"{i}. {fname}.......................................{fscore}", True, (0, 0, 0))
            screen.blit(win_text, (20, y_offset))
            y_offset += 50

        # Obsługa zdarzeń
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    settings_running = False

        pygame.display.flip()
        clock.tick(30)

if __name__=="__main__":
     main_menu()

