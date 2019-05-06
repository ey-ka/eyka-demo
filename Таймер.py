import time

print('Нажми ENTER чтобы начать, нажмиCtrl+C чтобы остановить')

while True:
    try:
        input()

        начало = time.time()
        print('Поехали!')

    except KeyboardInterrupt:
        print('Хватит!')
        конец = time.time()
        print('Всего времени:', round(конец - начало,2),'секунд')
        break
input()
