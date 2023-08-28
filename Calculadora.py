import tkinter

expr = ""


def limpiar():
    global expr
    expr = ""
    eq.set(expr)
    return


def apretar(num):
    global expr
    expr = expr + str(num)
    eq.set(expr)
    return


def calc():
    global expr

    tot = str(eval(expr))
    eq.set(tot)

    expr = tot
    return


def agregar_botones(gui):
    # Fila 1
    boton_limpiar = tkinter.Button(gui, text="AC", fg='purple', bg='gray',
                                   command=lambda: limpiar(), height=2, width=4)
    boton_limpiar.grid(row=4, column=0)
    boton_div = tkinter.Button(gui, text="/ ", fg="white", bg="violet",
                               command=lambda: apretar("/"), height=2, width=4)
    boton_div.grid(row=4, column=3)

    # Fila 2
    bot7 = tkinter.Button(gui, text='7', fg='purple', bg="gray",
                          command=lambda: apretar(7), height=2, width=4)
    bot7.grid(row=5, column=0)
    bot8 = tkinter.Button(gui, text='8', fg='purple', bg='gray',
                          command=lambda: apretar(8), height=2, width=4)
    bot8.grid(row=5, column=1)
    bot9 = tkinter.Button(gui, text='9', fg='purple', bg='gray',
                          command=lambda: apretar(9), height=2, width=4)
    bot9.grid(row=5, column=2)
    bot_mult = tkinter.Button(gui, text='X', fg='purple', bg='gray',
                              command=lambda: apretar("*"), height=2, width=4)
    bot_mult.grid(row=5, column=3)

    # Fila 3
    bot4 = tkinter.Button(gui, text='4', fg='purple', bg='gray',
                          command=lambda: apretar(6), height=2, width=4)
    bot4.grid(row=6, column=0)
    bot5 = tkinter.Button(gui, text='5', fg='purple', bg='gray',
                          command=lambda: apretar(5), height=2, width=4)
    bot5.grid(row=6, column=1)
    bot6 = tkinter.Button(gui, text='5', fg='purple', bg='gray',
                          command=lambda: apretar(5), height=2, width=4)
    bot6.grid(row=6, column=2)
    bot_men = tkinter.Button(gui, text=' - ', fg='purple', bg='gray',
                             command=lambda: apretar(6), height=2, width=4)
    bot_men.grid(row=6, column=3)

    # Fila 4
    bot1 = tkinter.Button(gui, text='1', fg='purple', bg='gray',
                          command=lambda: apretar(1), height=2, width=4)
    bot1.grid(row=7, column=0)
    bot2 = tkinter.Button(gui, text='2', fg='purple', bg='gray',
                          command=lambda: apretar(2), height=2, width=4)
    bot2.grid(row=7, column=1)
    bot3 = tkinter.Button(gui, text='3', fg='purple', bg='gray',
                          command=lambda: apretar(3), height=2, width=4)
    bot3.grid(row=7, column=2)
    bot_mas = tkinter.Button(gui, text=' + ', fg='white', bg='violet',
                             command=lambda: apretar("+"), height=2, width=4)
    bot_mas.grid(row=7, column=3)

    # Fila 5
    bot0 = tkinter.Button(gui, text='0', fg='purple', bg='gray',
                          command=lambda: apretar(0), height=2, width=8)
    bot0.grid(row=8, column=0, columnspan=2)
    bot_punto = tkinter.Button(gui, text='. ', fg='White', bg='violet',
                               command=lambda: apretar("."), height=2, width=4)
    bot_punto.grid(row=8, column=2)
    bot_mas = tkinter.Button(gui, text=' = ', fg='purple', bg='gray',
                             command=lambda: calc(), height=2, width=4)
    bot_mas.grid(row=8, column=3)


if __name__ == "__main__":
    gui = tkinter.Tk()
    gui.configure(background="light gray")
    gui.title("Calculadora")
    gui.geometry("180x260")

    eq = tkinter.StringVar()

    campo_exp = tkinter.Entry(gui, textvariable=eq)
    campo_exp.grid(columnspan=3)

    agregar_botones(gui)
    gui.mainloop()
