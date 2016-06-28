from tkinter import *
from tkinter.messagebox import *

win = Tk()
win.geometry("500x400+450+150")
win.title('Menu Jeu du Pendu')
win['bg'] = 'sky blue'

def callback():
    if askyesno('Jeu du Pendu', 'Voulez-vous jouez au Pendu?'):
        showinfo('Jeu du Pendu', 'Commencer la partie')
    else:
        askquestion('Jeu du Pendu', 'Etes-vous sûr?')
        showinfo('Jeu du Pendu', 'Retour au Menu')
        

    
text= Label(win,text='Jeu du Pendu',fg='royal blue',width=200).pack()         #on place le label au centre



button1=Button(win,text='Jouer au Pendu', command=callback).pack()
button2=Button(win,text='Quitter le Jeu', command=win.destroy).pack(side=RIGHT) #on crée un bouton qui permettra de quitter le jeu

button1.place(x=200,y=500)                                                      #on choisit l'emplacement des boutons
button2.place(x=200,y=0)
text.place(x=50,y=30)

win.mainloop()
