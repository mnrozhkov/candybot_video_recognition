import speech_recognizer as sr

cityDB = 'cityDB'
cities = []
named_cities = []
last_letter = ''

MESSAGES = ['city does not exists', 'bad first letter', 'city already named',
            'ok']

def load_cities():
    global cityDB
    global cities
    
    with open(cityDB, 'r') as fcityDB:
        for city in fcityDB:
            cities.append(city.strip())


def det_last_letter(city):
    ll = city[len(city) - 1]
    if ll == 'ь' or ll == 'ы':
        return city[len(city) - 2]
    else:
        return ll


def name_city(city):
    global cities
    global named_cities
    global last_letter
    global MESSAGES
    
    if city in cities:
        if last_letter == '' or city[0] == last_letter:        
            if not city in named_cities:
                named_cities.append(city)
                last_letter = det_last_letter(city)
                return MESSAGES[3]
            else:
                return MESSAGES[2]
        else:
            return MESSAGES[1]
    else:
        return MESSAGES[0]


def computer_move():
    global cities
    global MESSAGES
    
    print('Ходит компьютер...')
    for city in cities:
        msg = name_city(city)
        if msg == MESSAGES[3]:
            print(city)
            human_move()
            return
    print('Человек выиграл')
            

def city_starts_letter_exists():
    global cities
    global named_cities
    global last_letter
    
    for city in cities:
        if (not city in named_cities) and (city[0] == last_letter or last_letter == ''):
            return True
    return False


def human_move():
    global MESSAGES
    
    if not city_starts_letter_exists():
        print('Не осталось городов, начинающихся на букву ', last_letter)
        print('Компьютер выиграл')
        return
    print('Назовите город на букву ', last_letter, ': ')
    city = sr.listen()
    city = city.lower().strip()
    if city != 'стоп':
        msg = name_city(city)
        if msg == MESSAGES[0]:
            print(city)
            print('Город неизвестен')
            human_move()
        elif msg == MESSAGES[1]:
            print(city)
            print('Первая буква неверна')
            human_move()
        elif msg == MESSAGES[2]:
            print(city)
            print('Город уже был назван')
            human_move()
        else:
            print(city)
            computer_move()
    else:
        print('Компьютер выиграл')

        
def choose_1st_player():
    print('Выберете первого игрока (компьютер - компьютер, я - человек): ')
    fst_player = sr.listen()
    if fst_player == 'компьютер':
        computer_move()
    elif fst_player == 'я':
        human_move()
    else:
        choose_1st_player()

def start():
    load_cities()
    choose_1st_player()

def main():
    if sr.init('ru-ru','cityDict', 'ru.lm.bin'):
        sr.min_rms = 500
        start()

if __name__ == '__main__':
    main()
