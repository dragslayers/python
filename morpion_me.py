import tkinter as tk

fenetre = tk.Tk()

fenetre.title("Morpion")

taille_case = 100

canvas=tk.Canvas(fenetre,width = 3 * taille_case,height = 3 *taille_case,background="white")
canvas.grid(row=1,column=1)

def clic(event):
    print(event.x,event.y)

canvas.bind("Button-1",clic)

tk.mainloop()
