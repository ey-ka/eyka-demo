loose = ("Неудача")
win = ("ПОБЕДА!!!")
жизни = 3
drew = 0
computers_lives = 3
print("У тебя и у компьютера по 3 жизни")
print("Поехали!")
while True:
    rps = input ("Камень, Ножницы, Бумага?")
    rps = rps.title()
    import random
    computer = ("Камень","Ножницы","Бумага")
    computer = random.choice(computer)

    if rps == "Камень" and computer == "Бумага":
        print("Компьютер выбрал",computer)
        print(loose)
        жизни -=1
    if rps == "Камень" and computer == "Ножницы":
        print("Компьютер выбрал",computer)
        print(win)
        computers_lives -= 1
        
    if rps == "Ножницы" and computer == "Бумага":
        print("Компьютер выбрал",computer)
        print(win)
        computers_lives -=1
    if rps == "Ножницы" and computer == "Камень":
        print("Компьютер выбрал",computer)
        print(loose)
        жизни -= 1
        
    if rps == "Бумага" and computer == "Камень":
        print("Компьютер выбрал",computer)
        print(win)
        computers_lives -=1
    if rps == "Бумага" and computer == "Ножницы":
        print("Компьютер выбрал",computer)
        print(loose)
        жизни -= 1

    if rps == "Камень" and computer == "Камень":
       print("Компьютер выбрал",computer)
       print("Ничья")
       drew +=1
    
    if rps == "Ножницы" and computer == "Ножницы":
       print("Компьютер выбрал",computer)
       print("Ничья")
       drew +=1   
    
    if rps == "Бумага" and computer == "Бумага":
       print("Компьютер выбрал",computer)
       print("Ничья")
       drew +=1
    if жизни == 0 or rps == "test":
        print("Спасибо за игру!")
        print("У Вас закончились жизни")
        stop = input("Нажмите Enter для выхода")
        exit()
    if computers_lives == 0:
        print("Это полная победа!!!")
        stop = input("Нажмите Enter для выхода")
        exit()
    if rps == "exit":
        break

    

    

    

