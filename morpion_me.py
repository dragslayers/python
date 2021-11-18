import tkinter as tk

fenetre = tk.Tk()

fenetre.title("Morpion")

taille_case = 100

canvas=tk.Canvas(fenetre,width = 3 * taille_case,height = 3 *taille_case,background="white")
canvas.grid(row=1,column=1)

canvas.create_line(200,0,200,400,fill="black",width=5)
canvas.create_line(100,0,100,400,fill="black",width=5)

canvas.create_line(0,100,300,100,fill="black",width=5)
canvas.create_line(0,200,300,200,fill="black",width=5)

canvas.create_line(0,100,300,100,fill="black",width=5)



def croix(x,y):
    
    

def clic(evenement):
    print(evenement.x,evenement.y)

canvas.bind("<Button-1>",clic)

tk.mainloop()
