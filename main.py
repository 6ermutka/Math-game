from tkinter import *
from tkinter import ttk
from random import randint

valueid = 0
score = 0
vsego = 0

text = ["хороший результат!", "молодец", "неплохо!", "тебе нужно больше тренироваться!", "постарайся получше!", "попробуй еще раз", "пример", "примеров", "примера"]



def mainbody():
    global btn2, btn1, btn3, label,header1, header2
    try:
        btn3.destroy()
        label.destroy()
        label1.destroy()
        label2.destroy()
    except:
        print()
    header2 = Label(text=str(name1)+",", font=('Comic Sans MS', 20, 'bold'))
    header1 = Label(text="выбери тип игры!", font=('Comic Sans MS', 20, 'bold'))
    header1.place(anchor='nw', x = 10, y=90)
    header2.place(anchor="nw", y = 50, x =10)
    btn1 = Button(text="Сложи и вычти", command=option1, font='Times 40')
    btn1.place(x=10, y=150, width=380, height=100)
    btn2 = Button(text="Таблица умножения", command=option2, font='Times 30')
    btn2.place(x=10, y=250, width=380, height=100)

def option1():
    global spinbox1, cont, header1, header2
    header1.destroy()
    header2.destroy()
    header1 = Label(text='Привет, ' + str(name1) + ",",font=('Comic Sans MS', 24, 'bold'))
    header1.place(anchor='nw')
    header2 = Label(text='сколько примеров хочешь решить?',font=('Comic Sans MS', 16, 'bold'))
    header2.place(rely=0.1)
    btn1.destroy()
    btn2.destroy()

    spinbox1 = ttk.Spinbox(from_=1.0, to=1000000, textvariable=1)
    spinbox1.place(x=10, y=150, width=380, height=70)

    cont = Button(root, text="Продолжить", font=('Comic Sans MS', 20, 'bold'), command=getprimerov1)
    cont.place(rely=0.7)


def option2():
    global spinbox1, cont, header1, header2
    header1.destroy()
    header2.destroy()
    header1 = Label(text='Привет, ' + str(name1) + ",",font=('Comic Sans MS', 24, 'bold'))
    header1.place(anchor='nw')
    header2 = Label(text='сколько примеров хочешь решить?',font=('Comic Sans MS', 16, 'bold'))
    header2.place(rely=0.1)
    btn1.destroy()
    btn2.destroy()

    spinbox1 = ttk.Spinbox(from_=1.0, to=1000000, textvariable=1)
    spinbox1.place(x=10, y=150, width=380, height=70)

    cont = Button(root, text="Продолжить", font=('Comic Sans MS', 20, 'bold'), command=getprimerov2)
    cont.place(rely=0.7)

def getprimerov1():
    global primerov
    primerov = int(spinbox1.get())
    print(primerov)
    game1()

def getprimerov2():
    global primerov
    primerov = int(spinbox1.get())
    print(primerov)
    game2()


def znach():
    global x1, x2, x3, znak
    znak = randint(1, 2)
    x1 = randint(10, 100)
    x2 = randint(10, 100)
    x3 = randint(1, 3)
    if znak == 2:
        while x1 < x2:
            x1 = randint(1, 100)
            x2 = randint(1, 100)



def game2():
    global otvet1, otvet2, otvet3, primer, primerov1, textik, Trueotvet, Falseotvet1, Falseotvet2, x1, x2, x3
    x1 = randint(2, 9)
    x2 = randint(2, 9)
    x3 = randint(1, 3)
    spinbox1.destroy()
    cont.destroy()
    btn1.destroy()
    btn2.destroy()
    header1.destroy()
    header2.destroy()
    primer = Label(text=str(x1) + ' * ' + str(x2) + ' = ?' ,font=('Comic Sans MS', 64, 'bold'))
    primer.place(rely=0)
    Trueotvet = x1 * x2
    Falseotvet1 = x1 * x2 + x3
    Falseotvet2 = x1 * x2 - x3


    if x3 == 3:
        otvet1 = Button(text=str(Trueotvet), font='Times 55', command=win2)
        otvet2 = Button(text=str(Falseotvet1), font='Times 55', command=lose2)
        otvet3 = Button(text=str(Falseotvet2), font='Times 55', command=lose2)

    if x3 == 2:
        otvet1 = Button(text=str(Falseotvet1), font='Times 55', command=lose2)
        otvet2 = Button(text=str(Trueotvet), font='Times 55', command=win2)
        otvet3 = Button(text=str(Falseotvet2), font='Times 55', command=lose2)

    if x3 == 1:
        otvet1 = Button(text=str(Falseotvet2), font='Times 55', command=lose2)
        otvet2 = Button(text=str(Falseotvet1), font='Times 55', command=lose2)
        otvet3 = Button(text=str(Trueotvet), font='Times 55', command=win2)

    otvet1.place(x=10, y=190, width=380, height=70)
    otvet2.place(x=10, y=270, width=380, height=70)
    otvet3.place(x=10, y=350, width=380, height=70)

    if primerov == 1:
        textik = text[6]
        primerov1 = Label(text="Осталось " + str(primerov) + " " + str(textik), font=('Comic Sans MS', 20, 'bold'))
        primerov1.place(x=10, y=100, width=380, height=70)
    if primerov > 1 and primerov <= 4:
        textik = text[8]
        primerov1 = Label(text="Осталось " + str(primerov) + " " + str(textik), font=('Comic Sans MS', 20, 'bold'))
        primerov1.place(x=10, y=100, width=380, height=70)
    if primerov > 4:
        textik = text[7]
        primerov1 = Label(text="Осталось " + str(primerov) + " " + str(textik), font=('Comic Sans MS', 20, 'bold'))
        primerov1.place(x=10, y=100, width=380, height=70)







def game1():
    znach()
    global otvet1, otvet2, otvet3, primer, primerov1, Trueotvet
    spinbox1.destroy()
    cont.destroy()
    btn1.destroy()
    btn2.destroy()
    header1.destroy()
    header2.destroy()

    if znak == 1:
        primer = Label(text=str(x1) + ' + ' + str(x2) + ' = ?', font=('Comic Sans MS', 64, 'bold'))
        Trueotvet = x1 + x2
        Falseotvet1 = x1 + x2 + x3
        Falseotvet2 = x1 + x2 - x3
    if znak == 2:
        primer = Label(text=str(x1) + ' - ' + str(x2) + ' = ?', font=('Comic Sans MS', 64, 'bold'))
        Falseotvet1 = x1 - x2 + x3
        Falseotvet2 = x1 - x2 - x3
        Trueotvet = x1 - x2
    primer.place(rely=0)

    if x3 == 3:
        otvet1 = Button(text=str(Trueotvet), font='Times 55', command=win1)
        otvet2 = Button(text=str(Falseotvet1), font='Times 55', command=lose1)
        otvet3 = Button(text=str(Falseotvet2), font='Times 55', command=lose1)

    if x3 == 2:
        otvet1 = Button(text=str(Falseotvet1), font='Times 55', command=lose1)
        otvet2 = Button(text=str(Trueotvet), font='Times 55', command=win1)
        otvet3 = Button(text=str(Falseotvet2), font='Times 55', command=lose1)

    if x3 == 1:
        otvet1 = Button(text=str(Falseotvet2), font='Times 55', command=lose1)
        otvet2 = Button(text=str(Falseotvet1), font='Times 55', command=lose1)
        otvet3 = Button(text=str(Trueotvet), font='Times 55', command=win1)

    otvet1.place(x=10, y=190, width=380, height=70)
    otvet2.place(x=10, y=270, width=380, height=70)
    otvet3.place(x=10, y=350, width=380, height=70)

    if primerov == 1:
        textik = text[6]
        primerov1 = Label(text="Осталось " + str(primerov) + " " + str(textik), font=('Comic Sans MS', 20, 'bold'))
        primerov1.place(x=10, y=100, width=380, height=70)
    if primerov > 1 and primerov <= 4:
        textik = text[8]
        primerov1 = Label(text="Осталось " + str(primerov) + " " + str(textik), font=('Comic Sans MS', 20, 'bold'))
        primerov1.place(x=10, y=100, width=380, height=70)
    if primerov > 4:
        textik = text[7]
        primerov1 = Label(text="Осталось " + str(primerov) + " " + str(textik), font=('Comic Sans MS', 20, 'bold'))
        primerov1.place(x=10, y=100, width=380, height=70)


def lose1():
    global vsego, primerov, primerov1
    primerov = primerov - 1
    vsego += 1
    otvet1.destroy()
    primerov1.destroy()
    otvet2.destroy()
    primer.destroy()
    otvet3.destroy()
    if primerov == 0:
        result()
    else:
        game1()



def lose2():
    global vsego, primerov, primerov1
    vsego += 1
    primerov -= 1
    otvet1.destroy()
    otvet2.destroy()
    primer.destroy()
    primerov1.destroy()
    otvet3.destroy()
    if primerov == 0:
        result()
    else:
        game2()




def win1():
    global score, vsego, primerov, primerov1
    primerov -= 1
    score += 1
    vsego += 1
    otvet1.destroy()
    otvet2.destroy()
    primerov1.destroy()
    primer.destroy()
    otvet3.destroy()
    if primerov == 0:
        result()
    else:
        game1()



def win2():
    global score, primerov, vsego, primerov1
    score += 1
    primerov -= 1
    vsego += 1
    primerov1.destroy()
    otvet1.destroy()
    otvet2.destroy()
    primer.destroy()
    otvet3.destroy()
    if primerov == 0:
        result()
    else:
        game2()


def result():
    global btn3, score, xx, vsego, label, label1, primerov, label2, primerov1, textik
    otvet2.destroy()
    primer.destroy()
    primerov1.destroy()
    otvet3.destroy()
    xxx = score * 100 / vsego
    if xxx > 87:
        ocenka = "5"
        g1 = randint(0, 1)
        textik = text[g1]
    if xxx > 66 and xxx < 86:
        ocenka = "4"
        textik = text[2]
    if xxx > 42 and xxx < 65:
        ocenka = "3"
        g1 = randint(3, 4)
        textik = text[g1]
    if xxx< 41:
        ocenka = "2"
        textik = text[5]

    label = Label(text=str(name1) +", "+ str(textik), font=('Comic Sans MS', 20, 'bold'))
    label.place(rely=0.1)
    label1 = Label(text="Твой результат: " + str(score) + " из " + str(vsego), font=('Comic Sans MS', 20, 'bold'))
    label1.place(rely=0.2)
    label2 = Label(text="Твоя оценка: "+ str(ocenka),font=('Comic Sans MS', 20, 'bold') )
    label2.place(rely=0.3)
    btn3 = Button(text="Главное меню", command=mainbody, font='Times 30')
    btn3.place(x=10, y=350, width=380, height=100)
    score = 0
    xx = 10
    vsego = 0



def clear():
    global name1
    name1 = name.get()
    header.destroy()
    header1.destroy()
    name.destroy()
    cont.destroy()
    mainbody()

root = Tk()
root.title("Математическая игра")
root.geometry("400x500")
root.resizable(width=False, height=False)

root.image = PhotoImage(file="logo.png")
bg_logo = Label(root, image=root.image)
bg_logo.pack()

header = Label(text="Привет! Это математическая\nигра проверит твои умения\nв устном счете!", font=('Comic Sans MS', 20, 'bold'))
header.place(rely=0)

header1 = Label(text="Представься, пожалуйста!", font=('Comic Sans MS', 20, 'bold'))
header1.place(rely=0.3)

name = ttk.Entry(textvariable='Введи тут свое имя')
name.place(rely=0.5)

cont = Button(root, text="Продолжить", font=('Comic Sans MS', 20, 'bold'), command=clear)
cont.place(rely=0.7)



root.mainloop()
