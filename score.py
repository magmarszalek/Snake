import csv

def score_data():
    table=[]                                                #tworze listę
    with open("rank.csv", "r") as file:
        reader = csv.reader(file)                           #odczytuje plik linijkami
        headers = next(reader)
        for row in reader:
            table.append(row)
        print(table)
        return table

score_table = []
score_table_database = score_data()

score_table = font_titles.render("Winners: ", True, (0, 0, 255))
screen.blit(score_table, (725, 300))

first = score_table_database[1]
fname, fscore = first[1], first[2]

    
first_win = font_small.render( f"1. {fname}   score: {fscore}", True, (255, 255, 255))
screen.blit(first_win, (725, 350))
    #second_win = font_digits.render(score_table_database[2], True, (255, 255, 255))
    #screen.blit(second, (725, 400))
    #third_win = font_digits.render(score_table_database[3], True, (255, 255, 255))
    #screen.blit(third, (725, 450))
