import tkinter as tk
from random import randint
root = tk.Tk()
root.title("My Program")
canvas = tk.Canvas(root, width=1366, height=748, bg="red")
canvas.pack(padx=10, pady=10)
a=0
canvas.create_text(700,350,text="New Year",
                    font=("Comic Sans MS",60),fill="blue")
while 1:
        #домик
    canvas.create_polygon(450, 300+a, 150, 300+a, 300, 100+a,
                   fill= '#%02x%02x%02x' % (randint(0, 255),randint(0, 255),randint(0, 255)))
    canvas.create_polygon(500, 450+a, 100, 450+a, 300, 250+a,
                   fill= '#%02x%02x%02x' % (randint(0, 255),randint(0, 255),randint(0, 255)))             
    canvas.create_polygon(550, 600+a, 50, 600+a, 300, 400+a,
                   fill= '#%02x%02x%02x' % (randint(0, 255),randint(0, 255),randint(0, 255)))
    #елка     
    canvas.create_polygon(450+800, 300, 150+800, 300, 300+800, 100,
                   fill= "green")
    canvas.create_polygon(500+800, 450, 100+800, 450, 300+800, 250,
                   fill= "green")             
    canvas.create_polygon(550+800, 600, 50+800, 600, 300+800, 400,
                   fill= "green")
    k=randint(1,5)
    x=randint(0,1366)
    y=randint(0,748)
    canvas.create_oval(x-k,y-k,x+k,y+k,
                       fill="white",outline="white")
    a=a+3
    root.update()
root.mainloop()

