from tkinter import *

def red_f(event):
    l['text'] = 'Красный'
    l.configure(bg = 'red')
def orange_f(event):
    l['text'] = 'Оранжевый '
    l.configure(bg = 'orange')
def yellow_f(event):
    l['text'] = 'Желтый'
    l.configure(bg = 'yellow')
def green_f(event):
    l['text'] = 'Зеленый'
    l.configure(bg = 'green')
def skyblue_f(event):
    l['text'] = 'Голубой'
    l.configure(bg = 'skyblue')
def blue_f(event):
    l['text'] = 'Синий'
    l.configure(bg = 'blue')
def purple_f(event):
    l['text'] = 'Фиолетовый'
    l.configure(bg = 'purple')


root = Tk()

l = Label(root, bg = 'white', width = 15, height = 2)
l.pack()

button1 = Button(root, bg = 'red', width = 15, height = 2)
button2 = Button(root, bg = 'orange', width = 15, height = 2)
button3 = Button(root, bg = 'yellow', width = 15, height = 2)
button4 = Button(root, bg = 'green',width = 15, height = 2) 
button5 = Button(root, bg = 'skyblue',width = 15, height = 2) 
button6 = Button(root, bg = 'blue',width = 15, height = 2) 
button7 = Button(root, bg = 'purple',width = 15, height = 2) 

button1.bind('<Button-1>', red_f)
button1.pack()
button2.bind('<Button-1>', orange_f)
button2.pack()
button3.bind('<Button-1>', yellow_f)
button3.pack()
button4.bind('<Button-1>', green_f)
button4.pack()
button5.bind('<Button-1>', skyblue_f)
button5.pack()
button6.bind('<Button-1>', blue_f)
button6.pack()
button7.bind('<Button-1>', purple_f)
button7.pack()



root.mainloop()