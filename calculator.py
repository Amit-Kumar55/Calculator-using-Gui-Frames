from tkinter import *
root = Tk()

root.geometry("644x1000")
def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = "error"
        scvalue.set(value)
        screen.update()


        pass 
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()




scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar= scvalue, font= "lucida 40 bold")
screen.pack(fill = X , ipadx = 8, pady = 10, padx = 10)
f = Frame(root, bg = "grey")
b = Button(f, text = "9", padx = 28, pady = 18, font = "lucida 35 bold")
b.bind("<Button -1>", click)
b.pack(side = LEFT, padx = 18, pady = 5)

b = Button(f, text = "8", padx = 28, pady =18, font = "lucida 35 bold")
b.bind("<Button -1>", click)
b.pack(side = LEFT, padx = 18, pady = 5 )

b = Button(f, text = "7", padx = 28, pady = 18, font = "lucida 35 bold")
b.bind("<Button -1>", click)
b.pack(side = LEFT,  padx = 18, pady = 5)


f.pack()

f = Frame(root, bg = "grey")
b = Button(f, text = "6", padx = 28, pady = 18, font = "lucida 35 bold")
b.bind("<Button -1>", click)
b.pack(side = LEFT, padx = 18, pady = 5)

b = Button(f, text = "5", padx = 28, pady = 18, font = "lucida 35 bold")
b.bind("<Button -1>", click)
b.pack(side = LEFT, padx = 18, pady = 5)
b = Button(f, text = "4", padx = 28, pady = 18, font = "lucida 35 bold")
b.bind("<Button -1>", click)
b.pack(side = LEFT,  padx = 18, pady = 5)


f.pack()

f = Frame(root, bg = "grey")
b = Button(f, text = "3", padx = 28, pady = 18, font = "lucida 35 bold")
b.bind("<Button -1>", click)
b.pack(side = LEFT, padx = 18, pady = 5)

b = Button(f, text = "2", padx = 28, pady = 18, font = "lucida 35 bold")
b.bind("<Button -1>", click)
b.pack(side = LEFT, padx = 18, pady = 5 )

b = Button(f, text = "1", padx = 28, pady = 18, font = "lucida 35 bold")
b.bind("<Button -1>", click)
b.pack(side = LEFT,  padx = 18, pady = 5)


f.pack()

f = Frame(root, bg = "grey")
b = Button(f, text = "/", padx = 28, pady = 18, font = "lucida 35 bold")
b.bind("<Button -1>", click)
b.pack(side = LEFT, padx = 18, pady = 5)

b = Button(f, text = "=", padx = 28, pady = 18, font = "lucida 35 bold")
b.bind("<Button -1>", click)
b.pack(side = LEFT, padx = 18, pady = 5)

b = Button(f, text = "C", padx = 28, pady = 18, font = "lucida 35 bold")
b.bind("<Button -1>", click)
b.pack(side = LEFT,  padx = 18, pady = 5)
f.pack()



f = Frame(root, bg = "grey")
b = Button(f, text = "0", padx = 27, pady = 18, font = "lucida 35 bold")
b.bind("<Button -1>", click)
b.pack(side = LEFT, padx = 30, pady = 5)

b = Button(f, text = "-", padx = 27, pady = 18, font = "lucida 35 bold")
b.bind("<Button -1>", click)
b.pack(side = LEFT, padx = 18, pady = 5 )

b = Button(f, text = "+", padx = 27, pady = 18, font = "lucida 35 bold")
b.bind("<Button -1>", click)
b.pack(side = LEFT, padx = 18, pady = 5 )


b = Button(f, text = "*", padx = 27, pady = 18, font = "lucida 35 bold")
b.bind("<Button -1>", click)
b.pack(side = LEFT,  padx = 18, pady = 5)


f.pack()


root.mainloop()












