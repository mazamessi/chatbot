import tkinter as tk
root = tk.Tk()
score=0
root.title("My Program")
canvas = tk.Canvas(root, width=600, height=400, bg="red")
canvas.pack(padx=10, pady=10)
import random as r
list_color=['красный','синий','зелёный','желтый','белый','розовый','чёрный']
color_en=['red','blue','green','yellow','white','pink','black']
while 1:
    canvas.delete("all")
    rand=r.randint(0,len(color_en)-1)
    canvas.create_text(300, 200, text=list_color[r.randint(0,len(list_color)-1)], font=('Comic Sans MS', 30), fill=color_en[rand])
    root.update()
    b=input("Введите цвет текста ")
    if b==list_color[rand]:
        score=score+1
    print(score)
root.mainloop()
