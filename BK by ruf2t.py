import random

#fight
def fight_a (player_a,health_a) :
    global health_b
    kick_a = int(input('Введите 1(бить рукой) или 2(бить ногой)'))
    if kick_a == 1:
        str_a = random.randint(1, 10)
        health_b = health_b - str_a
        print (player_a,'наносит рукой',str_a)
        print('У', player_b, 'осталоь', health_b)
    elif kick_a == 2:
        agl = random.randint(0, 1)
        if agl == 1:
            print (player_b,'увернулся')
        else:
            str_a = random.randint(5, 15)
            health_b = health_b - str_a
            print(player_a,'наносит ногой', str_a)
        print('У', player_b, 'осталоь', health_b)

def fight_b (player_b,health_b) :
    global health_a

    kick_b = int(input('Введите 1(бить рукой) или 2(бить ногой)'))
    if kick_b == 1:
        str_b = random.randint(1, 10)
        health_a = health_a - str_b
        print (player_b,'наносит рукой',str_b)
        print('У', player_a, 'осталоь', health_a)
    elif kick_b == 2:
        str_b = random.randint(5, 15)
        health_a = health_a - str_b
        print(player_b,'наносит ногой', str_b)
        print('У', player_a, 'осталоь', health_a)


player_a = 'Коля'
health_a = 50

player_b = 'Дима'
health_b = 50


while True:
    if health_a < 1:
        print ('Поздравляем',player_b )
        break
    print (player_a, 'Твой ход')
    fight_a(player_a, health_a)
    if health_b <1:
        print ('Поздравляем', player_a)
        break
    print(player_b, 'Твой ход')
    fight_b(player_b, health_b)
