# -*- coding: utf-8 -*-
# -*- coding: iso-8859-1 -*-
"""
Dominik Peter Bayer
Matrikelnummer: 11771277

TU Wien 
Grundlagen des Programmierens für MB, WIMB und VT 


#"""
import tkinter as tk
from tkinter import *
import os
import random
import sys
from tkinter import WORD


class fenster:
    def __init__(self):
        self.root = Tk()
        self.root.iconbitmap(os.getcwd() + '\Images\Icon\icon.ico')
        self.root.title('Dominicolo')
        self.root.geometry("800x500") 
        self.root.resizable(0, 0)
        self.root.configure(bg = '#1b586b')


        self.frame_1 = Frame(self.root, bg = '#1b586b')
        self.frame_2 = Frame(self.root, bg = '#1b586b')
        self.frame_3 = Frame(self.root, bg = '#1b586b')
        self.frame_4 = Frame(self.root, bg = '#1b586b')
        self.frame_5 = Frame(self.root, bg = '#1b586b')
        self.frame_6 = Frame(self.root, bg = '#1b586b')
        
        self.game = Frame(self.root, bg = '#1b586b')
        self.down = Frame(self.root, bg = '#1b586b')
        self.end_screen = Frame(self.root, bg = '#1b586b')
        self.end_screen_2 = Frame(self.root, bg = '#1b586b')
        self.settings_10 = Frame(self.root, bg = '#1b586b')
        self.close_frame = Frame(self.root)


        self.root.bind('<Return>', lambda event: self.decide())

              #AENDEREN!!! SO DASS NICHT BEI JEDEN LEER ES PASSIERT 
        
# =============================================================================
# IMAGES:
# =============================================================================
        
        self.img = PhotoImage(file = os.getcwd() + '\Images\Buttons\start.gif')
        self.logo = PhotoImage(file = os.getcwd() + '\Images\BAnner\TItlelogo.gif')
        self.settings = PhotoImage(file = os.getcwd() + '\Images\Buttons\settings.gif')
        self.info = PhotoImage(file = os.getcwd() + '\Images\Buttons\info.gif')
        self.instruct = PhotoImage(file = os.getcwd() + '\Images\Buttons\instruction.gif')
        self.exit = PhotoImage(file = os.getcwd() + '\Images\Buttons\exit.gif')
        self.repeat_img = PhotoImage(file = os.getcwd() + '\Images\BUttons\REpeat.gif')
        self.end_img = PhotoImage(file = os.getcwd() + '\Images\Banner\end.gif')
        self.ini = PhotoImage(file = os.getcwd() + '\Images\BAnner\ANleitung.gif')
        self.about_img = PhotoImage(file = os.getcwd() + '\Images\BAnner\ABout.gif')
        self.back_img = PhotoImage(file = os.getcwd() + '\Images\BUttons\Back.gif')
        self.settings_img = PhotoImage(file = os.getcwd() + '\Images\BAnner\EInstellungen.gif')
        self.set_img = PhotoImage(file = os.getcwd() + '\Images\BUttons\set.gif')
        self.close_img = PhotoImage(file = os.getcwd() + '\Images\BUttons\close.gif')
        
# =============================================================================
# OTHER:
# =============================================================================
        self.Player_List = []
        self.Task_round = []
        self.Tasks_full = []
        self.Number_r = 15
        self.Number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.color = ['#f6bf4e', '#b3af38', '#ff3e3e', '#1b586b', '#008aff', '#b31dc0', '#00c437', '#1a592c', '#451a59']
        self.filename = os.getcwd() + '\Tasks\Tasks.csv'
        self.task_new = ''
        
        self.Read_Tasks()
        
        self.Anleitung_1 = """
        1. Trage die Spielernamen ein. Es kann max. 6 Spieler geben. 
        
        2. Drücke auf 'GET DRUNK' um das Spiel zu starten. 
        
        3. Durch das drücken der Leertaste kommt die nächste Aufgabe.
        """
        
        
        self.Anleitung_2 = """
        Solltest du selber Fragen hinzufuegen wollen, dann musst du einfach nur
        in den Installationspfad gehen. Dort befindet sich ein Ordner 'Tasks'. 
        In diesem Ordner findest du eine CSV Datei, welche du mix Excel oder 
        jeden anderen Textdateinprogramm äffnen kannst. 
        Füge die neue Aufgabe als neue Spalte hinzu. Beachte dabei, dass wenn
        der Name eines Spielers vorkommen soll, dass du diesen durch ein '%s' 
        ersetzt. Wenn eine zufällige Anzahl an Schlücken eingesetzt werden soll,
        dann schreibe bitte ein '%i' hin. 
        
        Speicher diese Datei dann im selben Ordner wieder ab und schon kannst 
        du mit deinen eigenen Regeln spielen!
        """
        
        
        self.ueber = """
        Created by Nobody
        
        Button and Icon Licences: Flaticon Basic License 
        Button and Icon Creator: www.flaticon.com
        
        Fonts: Space Comic, Halvetica
        
        I do not take any credit for this program except creating the python code.
        Design and Idea is copied from the famous college drinking app Picolo made by Marmelapp. 
        
        Original Idea by Marmelapp (App: Picolo)
        
        
        Python 2.7.15 64-bit | Qt 5.6.2 | PyQt5 5.6 | Windows 10 
        """
        
        
# =============================================================================
# LABELS:
# =============================================================================
       
        self.label = tk.Label(master = self.root, image = self.logo, bg = '#1b586b')      
        self.task = tk.Label(master = self.game, text = '',  font = 'Halvetica 18 bold', fg = 'white', justify = 'center', wraplength = 700)
        self.end = tk.Label(master = self.root, text = 'Fertig!', font = 'Halvetica 40', fg = 'white', bg = '#1b586b')
        self.error = tk.Label(master = self.root, text = 'Bitte geben Sie min. 2 Spielernamen ein!', font = 'Halvetica 10 bold', fg = 'red', bg = '#1b586b')
        self.end = tk.Label(master = self.root, image = self.end_img, bg = '#1b586b' )
                              
        self.repeat_text = tk.Label(master = self.end_screen_2, text = 'Nochmal', font = 'Helvetica 12 bold', fg = 'white', bg = '#1b586b')
        self.home_text = tk.Label(master = self.end_screen_2, text = 'Startseite', font = 'Helvetica 12 bold', fg = 'white',  bg = '#1b586b')        

        self.about_1 = tk.Label(master = self.root, image = self.about_img, bg = '#1b586b')

        self.ins = tk.Label(master = self.root, image = self.ini, bg = '#1b586b' )
        self.anl_1 = tk.Label(master = self.root, text = self.Anleitung_1, bg = '#1b586b', justify = 'left', font = 'Halvetica 12 bold', fg = 'white')
        self.anl_2 = tk.Label(master = self.root, text = self.Anleitung_2, bg = '#1b586b', font = 'Halvetica 10', fg = 'white')
        self.aboutt = tk.Label(master = self.root, text = self.ueber, bg = '#1b586b', font = 'Halvetica 12', fg = 'white')
          
        self.settings_img_img = tk.Label(master = self.root, image = self.settings_img, bg = '#1b586b')                       
        self.settings_text = tk.Label(master = self.root, text = 'In Arbeit!', font = 'Halvetica 20 bold', fg = 'white', bg = '#1b586b')                      
        self.runde = tk.Label(master = self.settings_10, text = 'Runden Anzahl:', font = 'Halvetica 10 bold', fg = 'white', bg = '#1b586b')
                                     
                                      
        self.player__1 = tk.Label(master = self.frame_1, text = 'Spieler 1', bg = '#1b586b', fg = 'white', font = 'Helvetica 14 bold', justify = 'left')
        self.player__2 = tk.Label(master = self.frame_2, text = 'Spieler 2', bg = '#1b586b', fg = 'white', font = 'Helvetica 14 bold', justify = 'left')
        self.player__3 = tk.Label(master = self.frame_3, text = 'Spieler 3', bg = '#1b586b', fg = 'white', font = 'Helvetica 14 bold', justify = 'left')
        self.player__4 = tk.Label(master = self.frame_4, text = 'Spieler 4', bg = '#1b586b', fg = 'white', font = 'Helvetica 14 bold', justify = 'left')
        self.player__5 = tk.Label(master = self.frame_5, text = 'Spieler 5', bg = '#1b586b', fg = 'white', font = 'Helvetica 14 bold', justify = 'left')
        self.player__6 = tk.Label(master = self.frame_6, text = 'Spieler 6', bg = '#1b586b', fg = 'white', font = 'Helvetica 14 bold', justify = 'left')
        
        
# =============================================================================
# BUTTONS:
# =============================================================================


        self.instructions = tk.Button(master = self.down, image = self.instruct, command = self.instructions_page, borderwidth = 0, background = '#1b586b', relief = 'flat')
        self.set = tk.Button(master = self.down, image = self.settings, command = self.settings_app, borderwidth = 0, background = '#1b586b')
        self.about = tk.Button(master = self.down, image = self.info, command = self.about_app,  borderwidth = 0, background = '#1b586b')
        self.start = tk.Button(master = self.root, image = self.img, command = self.decide, borderwidth = 0, background = '#1b586b', relief = 'flat')
        self.next = tk.Button(master = self.root, text = 'weiter', command = self.nextt)
        self.home = tk.Button(master = self.end_screen, image = self.exit, command = self.home, borderwidth = 0, background = '#1b586b')
        self.repeat = tk.Button(master = self.end_screen, image = self.repeat_img, command = self.repeat, borderwidth = 0, background = '#1b586b')
        self.back_about_app = tk.Button(master = self.root, image = self.back_img, command = self.back_about, borderwidth = 0, background = '#1b586b')
        self.back_inst_app = tk.Button(master = self.root, image = self.back_img, command = self.back_inst, borderwidth = 0, background = '#1b586b')
        self.back_set_app = tk.Button(master = self.root, image = self.back_img, command = self.back_set, borderwidth = 0, background = '#1b586b')
  
        self.set_round_app = tk.Button(master = self.settings_10, image = self.set_img, command = self.set_number, borderwidth = 0, background = '#1b586b')
    
        self.close = tk.Button(master = self.close_frame, image = self.close_img, command = self.close_app, borderwidth = 0 ,background = '#1b586b')

# =============================================================================
# ENTRYS:
# =============================================================================
        self.player_1 = tk.Entry(master = self.frame_1, bg = '#1b586b', fg = 'white', font = 'Helvetica 14')
        self.player_2 = tk.Entry(master = self.frame_2, bg = '#1b586b', fg = 'white', font = 'Helvetica 14')
        self.player_3 = tk.Entry(master = self.frame_3, bg = '#1b586b', fg = 'white', font = 'Helvetica 14')
        self.player_4 = tk.Entry(master = self.frame_4, bg = '#1b586b', fg = 'white', font = 'Helvetica 14')
        self.player_5 = tk.Entry(master = self.frame_5, bg = '#1b586b', fg = 'white', font = 'Helvetica 14')
        self.player_6 = tk.Entry(master = self.frame_6, bg = '#1b586b', fg = 'white', font = 'Helvetica 14')
        
        self.Round_Number = tk.Entry(master = self.settings_10, bg = '#1b586b', fg = 'white', font = 'Helvetica 14')


        self.label.pack(side = 'top')
        self.frame_1.pack()
        self.frame_2.pack()
        self.frame_3.pack()
        self.frame_4.pack()
        self.frame_5.pack()
        self.frame_6.pack()
        

        self.player__1.pack(side = LEFT, padx=10, pady=5)
        self.player_1.pack(side = RIGHT, padx=10, pady=5)
        self.player__2.pack(side = LEFT, padx=10, pady=5)
        self.player_2.pack(side = RIGHT, padx=10, pady=5)
        self.player__3.pack(side = LEFT, padx=10, pady=5)
        self.player_3.pack(side = RIGHT, padx=10, pady=5)
        self.player__4.pack(side = LEFT, padx=10, pady=5)
        self.player_4.pack(side = RIGHT, padx=10, pady=5)
        self.player__5.pack(side = LEFT, padx=10, pady=5)
        self.player_5.pack(side = RIGHT, padx=10, pady=5)
        self.player__6.pack(side = LEFT, padx=10, pady=5)
        self.player_6.pack(side = RIGHT, padx=10, pady=5)
        self.start.pack(padx=10, pady=20)
        self.down.pack()
        self.set.pack(side = LEFT, padx = 10, pady = 10)
        self.instructions.pack(side = LEFT, padx = 10)
        self.about.pack(side = LEFT, padx = 10)







        
        
        self.root.mainloop()
        
        


        
# =============================================================================
# Players:
# =============================================================================

    def close_app(self):
        

        self.player_1.delete(first = 0, last = 50)
        self.player_2.delete(first = 0, last = 50)
        self.player_3.delete(first = 0, last = 50)
        self.player_4.delete(first = 0, last = 50)
        self.player_5.delete(first = 0, last = 50)
        self.player_6.delete(first = 0, last = 50)
        self.close_frame.pack_forget()
        self.game.pack_forget()
        self.task.pack_forget()
        self.close.pack_forget()
        self.root.config(bg = '#1b586b')
        
        del self.Player_List[:]
        
        self.label.pack(side = 'top')
        self.frame_1.pack()
        self.frame_2.pack()
        self.frame_3.pack()
        self.frame_4.pack()
        self.frame_5.pack()
        self.frame_6.pack()
        

        self.player__1.pack(side = LEFT, padx=10, pady=5)
        self.player_1.pack(side = RIGHT, padx=10, pady=5)
        self.player__2.pack(side = LEFT, padx=10, pady=5)
        self.player_2.pack(side = RIGHT, padx=10, pady=5)
        self.player__3.pack(side = LEFT, padx=10, pady=5)
        self.player_3.pack(side = RIGHT, padx=10, pady=5)
        self.player__4.pack(side = LEFT, padx=10, pady=5)
        self.player_4.pack(side = RIGHT, padx=10, pady=5)
        self.player__5.pack(side = LEFT, padx=10, pady=5)
        self.player_5.pack(side = RIGHT, padx=10, pady=5)
        self.player__6.pack(side = LEFT, padx=10, pady=5)
        self.player_6.pack(side = RIGHT, padx=10, pady=5)
        self.start.pack(padx=10, pady=20)
        self.down.pack()
        self.set.pack(side = LEFT, padx = 10, pady = 10)
        self.instructions.pack(side = LEFT, padx = 10)
        self.about.pack(side = LEFT, padx = 10)

    def set_number(self):
        self.Number_r = self.Round_Number.get()
        print self.Number_r


    def back_set(self):
        
        self.settings_img_img.pack_forget()
        self.runde.pack_forget()
        self.settings_10.pack_forget()
        
        
        
        self.back_set_app.pack_forget()

        self.Round_Number.pack_forget()
        self.set_round_app.pack_forget()
        self.back_set_app.pack_forget()
        
        
        
        
        
        self.label.pack(side = 'top')
        self.frame_1.pack()
        self.frame_2.pack()
        self.frame_3.pack()
        self.frame_4.pack()
        self.frame_5.pack()
        self.frame_6.pack()
        

        self.player__1.pack(side = LEFT, padx=10, pady=5)
        self.player_1.pack(side = RIGHT, padx=10, pady=5)
        self.player__2.pack(side = LEFT, padx=10, pady=5)
        self.player_2.pack(side = RIGHT, padx=10, pady=5)
        self.player__3.pack(side = LEFT, padx=10, pady=5)
        self.player_3.pack(side = RIGHT, padx=10, pady=5)
        self.player__4.pack(side = LEFT, padx=10, pady=5)
        self.player_4.pack(side = RIGHT, padx=10, pady=5)
        self.player__5.pack(side = LEFT, padx=10, pady=5)
        self.player_5.pack(side = RIGHT, padx=10, pady=5)
        self.player__6.pack(side = LEFT, padx=10, pady=5)
        self.player_6.pack(side = RIGHT, padx=10, pady=5)
        self.start.pack(padx=10, pady=20)
        self.down.pack()
        self.set.pack(side = LEFT, padx = 10, pady = 10)
        self.instructions.pack(side = LEFT, padx = 10)
        self.about.pack(side = LEFT, padx = 10)
        
    def back_inst(self):
        self.ins.pack_forget()
        self.anl_1.pack_forget()
        self.anl_2.pack_forget()
        self.back_inst_app.pack_forget()
        
        self.label.pack(side = 'top')
        self.frame_1.pack()
        self.frame_2.pack()
        self.frame_3.pack()
        self.frame_4.pack()
        self.frame_5.pack()
        self.frame_6.pack()
        

        self.player__1.pack(side = LEFT, padx=10, pady=5)
        self.player_1.pack(side = RIGHT, padx=10, pady=5)
        self.player__2.pack(side = LEFT, padx=10, pady=5)
        self.player_2.pack(side = RIGHT, padx=10, pady=5)
        self.player__3.pack(side = LEFT, padx=10, pady=5)
        self.player_3.pack(side = RIGHT, padx=10, pady=5)
        self.player__4.pack(side = LEFT, padx=10, pady=5)
        self.player_4.pack(side = RIGHT, padx=10, pady=5)
        self.player__5.pack(side = LEFT, padx=10, pady=5)
        self.player_5.pack(side = RIGHT, padx=10, pady=5)
        self.player__6.pack(side = LEFT, padx=10, pady=5)
        self.player_6.pack(side = RIGHT, padx=10, pady=5)
        self.start.pack(padx=10, pady=20)
        self.down.pack()
        self.set.pack(side = LEFT, padx = 10, pady = 10)
        self.instructions.pack(side = LEFT, padx = 10)
        self.about.pack(side = LEFT, padx = 10)

    def back_about(self):
        self.about_1.pack_forget()
        self.aboutt.pack_forget()
        self.back_about_app.pack_forget()
        
        self.label.pack(side = 'top')
        self.frame_1.pack()
        self.frame_2.pack()
        self.frame_3.pack()
        self.frame_4.pack()
        self.frame_5.pack()
        self.frame_6.pack()
        

        self.player__1.pack(side = LEFT, padx=10, pady=5)
        self.player_1.pack(side = RIGHT, padx=10, pady=5)
        self.player__2.pack(side = LEFT, padx=10, pady=5)
        self.player_2.pack(side = RIGHT, padx=10, pady=5)
        self.player__3.pack(side = LEFT, padx=10, pady=5)
        self.player_3.pack(side = RIGHT, padx=10, pady=5)
        self.player__4.pack(side = LEFT, padx=10, pady=5)
        self.player_4.pack(side = RIGHT, padx=10, pady=5)
        self.player__5.pack(side = LEFT, padx=10, pady=5)
        self.player_5.pack(side = RIGHT, padx=10, pady=5)
        self.player__6.pack(side = LEFT, padx=10, pady=5)
        self.player_6.pack(side = RIGHT, padx=10, pady=5)
        self.start.pack(padx=10, pady=20)
        self.down.pack()
        self.set.pack(side = LEFT, padx = 10, pady = 10)
        self.instructions.pack(side = LEFT, padx = 10)
        self.about.pack(side = LEFT, padx = 10)


    def settings_app(self):
        
        self.frame_1.pack_forget()
        self.frame_2.pack_forget()
        self.frame_3.pack_forget()
        self.frame_4.pack_forget()
        self.frame_5.pack_forget()
        self.frame_6.pack_forget()
        self.label.pack_forget()
        self.start.pack_forget()
        self.down.pack_forget()
        self.set.pack_forget()
        self.instructions.pack_forget()
        self.about.pack_forget()
        self.player__1.pack_forget()
        self.player_1.pack_forget()
        self.player__2.pack_forget()
        self.player_2.pack_forget()
        self.player__3.pack_forget()
        self.player_3.pack_forget()
        self.player__4.pack_forget()
        self.player_4.pack_forget()
        self.player__5.pack_forget()
        self.player_5.pack_forget()
        self.player__6.pack_forget()
        self.player_6.pack_forget()
        self.error.pack_forget()
        
        self.settings_img_img.pack(side = TOP)
#        self.settings_text.pack(pady = 80)
        self.settings_10.pack(pady = 120)
        self.runde.pack(side = LEFT, padx = 10)
        self.Round_Number.pack(side = LEFT, padx = 10)
        self.set_round_app.pack(side = LEFT, padx = 10)
        self.back_set_app.pack(side = BOTTOM, pady = 20)


    def about_app(self):
        self.frame_1.pack_forget()
        self.frame_2.pack_forget()
        self.frame_3.pack_forget()
        self.frame_4.pack_forget()
        self.frame_5.pack_forget()
        self.frame_6.pack_forget()
        self.label.pack_forget()
        self.start.pack_forget()
        self.down.pack_forget()
        self.set.pack_forget()
        self.instructions.pack_forget()
        self.about.pack_forget()
        self.player__1.pack_forget()
        self.player_1.pack_forget()
        self.player__2.pack_forget()
        self.player_2.pack_forget()
        self.player__3.pack_forget()
        self.player_3.pack_forget()
        self.player__4.pack_forget()
        self.player_4.pack_forget()
        self.player__5.pack_forget()
        self.player_5.pack_forget()
        self.player__6.pack_forget()
        self.player_6.pack_forget()
        self.error.pack_forget()


        self.about_1.pack()
        self.aboutt.pack(side = TOP)
        self.back_about_app.pack(side = 'bottom', pady = 20)


    def instructions_page(self):
        self.frame_1.pack_forget()
        self.frame_2.pack_forget()
        self.frame_3.pack_forget()
        self.frame_4.pack_forget()
        self.frame_5.pack_forget()
        self.frame_6.pack_forget()
        self.label.pack_forget()
        self.start.pack_forget()
        self.down.pack_forget()
        self.set.pack_forget()
        self.instructions.pack_forget()
        self.about.pack_forget()
        self.player__1.pack_forget()
        self.player_1.pack_forget()
        self.player__2.pack_forget()
        self.player_2.pack_forget()
        self.player__3.pack_forget()
        self.player_3.pack_forget()
        self.player__4.pack_forget()
        self.player_4.pack_forget()
        self.player__5.pack_forget()
        self.player_5.pack_forget()
        self.player__6.pack_forget()
        self.player_6.pack_forget()
        self.error.pack_forget()
        
        self.ins.pack()
        self.anl_1.pack()
        self.anl_2.pack()
        self.back_inst_app.pack(side = 'bottom', pady = 10)

    def repeat(self):
        print self.Player_List
        self.end.pack_forget()
        self.end_screen.pack_forget()
        self.repeat.pack_forget()
        self.home.pack_forget()
        self.end_screen_2.pack_forget()
        self.repeat_text.pack_forget()
        self.home_text.pack_forget()
        color = random.choice(self.color)
        self.root.bind('<space>', lambda event: self.nextt())
        self.Creat_Round_tasks()
        self.close_frame.pack(side = BOTTOM)
        self.close.pack(pady = 20)
        self.close_frame.config(bg = color)
        self.close.config(background = color)
        self.root.configure(bg = color)
        self.game.pack()
        self.game.config(bg = color)
        self.task.pack(pady = 150)
        
        self.pick_task()
            
        self.task.config(text = self.task_new, bg = color)
            
            
    def home(self):
        self.Number_r = 0
        self.end.pack_forget()
        self.end_screen.pack_forget()
        self.repeat.pack_forget()
        self.end_screen_2.pack_forget()
        self.home.pack_forget()
        self.repeat_text.pack_forget()
        self.home_text.pack_forget()
        self.player_1.delete(first = 0, last = 50)
        self.player_2.delete(first = 0, last = 50)
        self.player_3.delete(first = 0, last = 50)
        self.player_4.delete(first = 0, last = 50)
        self.player_5.delete(first = 0, last = 50)
        self.player_6.delete(first = 0, last = 50)
        
        self.root.bind('<Return>', lambda event: self.decide())
        del self.Player_List[:]
        
        self.label.pack(side = 'top')
        self.frame_1.pack()
        self.frame_2.pack()
        self.frame_3.pack()
        self.frame_4.pack()
        self.frame_5.pack()
        self.frame_6.pack()
        

        self.player__1.pack(side = LEFT, padx=10, pady=5)
        self.player_1.pack(side = RIGHT, padx=10, pady=5)
        self.player__2.pack(side = LEFT, padx=10, pady=5)
        self.player_2.pack(side = RIGHT, padx=10, pady=5)
        self.player__3.pack(side = LEFT, padx=10, pady=5)
        self.player_3.pack(side = RIGHT, padx=10, pady=5)
        self.player__4.pack(side = LEFT, padx=10, pady=5)
        self.player_4.pack(side = RIGHT, padx=10, pady=5)
        self.player__5.pack(side = LEFT, padx=10, pady=5)
        self.player_5.pack(side = RIGHT, padx=10, pady=5)
        self.player__6.pack(side = LEFT, padx=10, pady=5)
        self.player_6.pack(side = RIGHT, padx=10, pady=5)
        self.start.pack(padx=10, pady=20)
        self.down.pack()
        self.set.pack(side = LEFT, padx = 10, pady = 10)
        self.instructions.pack(side = LEFT, padx = 10)
        self.about.pack(side = LEFT, padx = 10)


    def decide(self):
        print self.Number_r
        self.button_player()
        if len(self.Player_List) > 1 :
            self.frame_1.pack_forget()
            self.frame_2.pack_forget()
            self.frame_3.pack_forget()
            self.frame_4.pack_forget()
            self.frame_5.pack_forget()
            self.frame_6.pack_forget()
            self.label.pack_forget()
            self.start.pack_forget()
            self.down.pack_forget()
            self.set.pack_forget()
            self.instructions.pack_forget()
            self.about.pack_forget()
            self.player__1.pack_forget()
            self.player_1.pack_forget()
            self.player__2.pack_forget()
            self.player_2.pack_forget()
            self.player__3.pack_forget()
            self.player_3.pack_forget()
            self.player__4.pack_forget()
            self.player_4.pack_forget()
            self.player__5.pack_forget()
            self.player_5.pack_forget()
            self.player__6.pack_forget()
            self.player_6.pack_forget()
            self.error.pack_forget()
            self.root.unbind('<Return>')
            self.root.bind('<space>', lambda event: self.nextt())
        
            color = random.choice(self.color)
            
            
            self.close_frame.pack(side = BOTTOM)
            self.close.pack(pady = 20)
            self.close_frame.config(bg = color)
            self.close.config(background = color)
            self.Creat_Round_tasks()
            self.root.configure(bg = color)
            self.game.pack()
            self.game.config(bg = color)
            self.task.pack(pady = 130)
            self.pick_task()
            
            
            self.task.config(text = self.task_new, bg = color)
        
        
        
        
        else:
            del self.Player_List[:]
            self.error.pack()



    def button_player(self):
        Player_1 = self.player_1.get()
        if len(Player_1) > 0:
            self.Player_List.append(Player_1)
       
        Player_2 = self.player_2.get()
        if len(Player_2) > 0:
            self.Player_List.append(Player_2)
       
        Player_3 = self.player_3.get()
        if len(Player_3) > 0:
            self.Player_List.append(Player_3)
       
        Player_4 = self.player_4.get()
        if len(Player_4) > 0:
            self.Player_List.append(Player_4)
       
        Player_5 = self.player_5.get()
        if len(Player_5) > 0:
            self.Player_List.append(Player_5)
        
        Player_6 = self.player_6.get()
        if len(Player_6) > 0:
            self.Player_List.append(Player_6)
        
        
        
        print self.Player_List


# =============================================================================
# MAIN GAME:
# =============================================================================

#    def get(self):
        

    def nextt(self):
        self.pick_task()
        color = random.choice(self.color)
        self.root.configure(bg = color)
        self.game.pack()
        self.game.config(bg = color)
        self.close_frame.config(bg = color)
        self.close.config(background = color)
        self.task.config(text = self.task_new, bg = color)
        
    def Read_Tasks(self):
        try:
            file = open(self.filename, 'r')
        except IOError:
            print 'The file does not exist! \nPlease make sure, that the Task.csv is in the correct directory or check for the spelling!'
            sys.exit()
        else:
            for task in file:
                self.Tasks_full.append(task)
           
    def Creat_Round_tasks(self):
        a = self.Number_r
        random.shuffle(self.Tasks_full)
        for Task in self.Tasks_full:
            Taskss = random.choice(self.Tasks_full)
            self.Task_round.append(Task)
            if len(self.Task_round) == a:
                break
            else:
                continue
        random.shuffle(self.Task_round)
        print len(self.Task_round)
        
    def pick_task(self):
        
        if len(self.Task_round) == 0:
            self.root.unbind('<space>')
            self.next.pack_forget()
            self.task.pack_forget()
            self.game.pack_forget()
            self.close_frame.pack_forget()
            self.close.pack_forget()
            self.root.config(bg = '#1b586b')
            self.end.pack(pady = 140)
            self.end_screen.pack()
            self.end_screen_2.pack()
            self.repeat_text.pack(side = 'left', padx = 19)
            self.home_text.pack(side = 'left', padx = 16)
            self.repeat.pack(side = 'left', padx = 40)
            self.home.pack(side = 'left', padx = 40)
        
        Task = random.choice(self.Task_round)
        self.Task_round.remove(Task)
                
        Player_1 = random.choice(self.Player_List)
        Player_2 = random.choice(self.Player_List)
        if Player_1 == Player_2:
            Player_2 = random.choice(self.Player_List)
        
        Task = str(Task)
        print Task
        
        if Task.count('%s') > 1:
            if '%i' in Task:
                self.task_new = Task % (Player_1, Player_2, random.choice(self.Number))
            else:
                self.task_new = Task % (Player_1, Player_2)
        else:
            if Task.count('%s') == 1:
                if '%i' in Task:
                    self.task_new = Task % (Player_1, random.choice(self.Number))
                else:
                    self.task_new = Task % (Player_1)
            else:
                if '%i' in Task:
                    self.task_new = Task % (random.choice(self.Number))
                else:
                    self.task_new = Task 
                    
#        print self.Number_r


        
if __name__ == '__main__':


    anwendung = fenster()
    
