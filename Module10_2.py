import threading
import time



class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name} на нас напали')
        enemy = 100       #враги. дла кажгого потока их 100
        day = 0           #счетчик дней сражения
        while enemy >0:
            enemy =  enemy - self.power    #кол-во врагов уменьшается на силу
            day += 1                       #дни плюсуем
            time.sleep(1)                  #задержка в 1 сек
            print(f'{self.name} сражается {day} день, осталось {enemy} воинов.')
        print(f'{self.name} одержал победу спустя {day} дней(дня)!')



first_knight = Knight('Sir Lancelot', 10)  #создаем поток
second_knight = Knight("Sir Galahad", 20)

first_knight.start()                 #запускаем поток
second_knight.start()

first_knight.join()                 #стоп основной поток, чтобы строка про все битвы вышла в конце
second_knight.join()

print(f'Все битвы закончились')