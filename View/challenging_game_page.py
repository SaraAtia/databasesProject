from random import randint
from tkinter import *
from View import start_menu
from Logic import GameLogic as gL


def challenging_game_window(window, Gamer_name):
    for widget in window.winfo_children():
        widget.destroy()
    frame = Frame(window)
    frame.grid(row=1, column=1)

    frame.grid_columnconfigure(0, weight=1)
    frame.grid_rowconfigure(0, weight=1)

    GameInfoDict = gL.start(Gamer_name, 3)


    message1 = Label(frame, text='You will play on 5 artists try to remember all the facts', fg='black',
                     font='Ariel 16 bold')
    message1.grid(row=0, column=0, pady=(5, 5))
    message2 = Label(frame, text='the game will start  in 5 secound', fg='black', font='Ariel 10 bold')
    message2.grid(row=1, column=0, pady=(5, 5))
    frame.after(5000, showArtist, Gamer_name, window, frame, GameInfoDict, 0)


def showArtist(Gamer_name, window, frame, GameInfoDict, artist_number):
    if artist_number < len(GameInfoDict['artist_name']):
        list = frame.grid_slaves()
        for l in list:
            l.destroy()
        message1 = Label(frame, text='you play on: ' + GameInfoDict['artist_name'][artist_number], fg='black', font='Ariel 16 bold')
        message1.grid(row=0, column=0, pady=(5, 5))
        message2 = Label(frame, text='the game will start  in 5 secound', fg='black', font='Ariel 10 bold')
        message2.grid(row=1, column=0, pady=(5, 5))
        frame.after(5000, showAttribute, Gamer_name, window, frame, GameInfoDict, artist_number, 0)
    else:
        frame.after(2000, showQuestion, Gamer_name, window, frame, GameInfoDict, 0, [], "")


def showAttribute(Gamer_name, window, frame, GameInfoDict, artist_number, attribute_number):
    list = frame.grid_slaves()
    for l in list:
        l.destroy()
    frame = Frame(window)
    frame.grid(row=1, column=1)
    for j in range(17):
        for k in range(17):
            message = Label(frame, text="")
            message.grid(row=k, column=j, pady=(5, 5), padx=(5, 5))
    message3 = Label(frame, text=GameInfoDict['properties'][artist_number][attribute_number], fg='black', font='Ariel 16 bold')
    message3.grid(row=randint(0, 16), column=randint(0, 16), pady=(0, 0))
    if attribute_number + 1 < len(GameInfoDict['properties'][artist_number]):
        frame.after(2000, showAttribute, Gamer_name, window, frame, GameInfoDict, artist_number, attribute_number + 1)
    else:
        frame.after(2000, showArtist, Gamer_name, window, frame, GameInfoDict, artist_number + 1)


def showQuestion(Gamer_name, window, frame, GameInfoDict, numberOfQ, answers, get_anwser):
    answers.append(get_anwser)
    if numberOfQ < len(GameInfoDict['questions'].keys()):
        list = frame.grid_slaves()
        for l in list:
            l.destroy()
        frame = Frame(window)
        frame.grid(row=1, column=1)
        list_of_q = []
        for i in GameInfoDict['questions'].keys():
            list_of_q.append(i)
        q = list_of_q[numberOfQ]
        question = Label(frame, text=q, fg='black', font='Ariel 16 bold')
        question.grid(row=0, column=0, pady=(10, 10))

        a1_text = GameInfoDict['questions'][q]['answers'][0]
        a1 = Button(frame, text=a1_text, bg="blue", fg="white", font='Ariel 12 bold',
                    command=lambda: showQuestion(Gamer_name, window, frame, GameInfoDict, numberOfQ + 1,
                                                 answers, a1_text))
        a1.grid(row=1, column=0, pady=(5, 5))

        a2_text = GameInfoDict['questions'][q]['answers'][1]
        a2 = Button(frame, text=a2_text, bg="blue", fg="white", font='Ariel 12 bold',
                    command=lambda: showQuestion(Gamer_name, window, frame, GameInfoDict, numberOfQ + 1,
                                                 answers, a2_text))
        a2.grid(row=2, column=0, pady=(5, 5))

        a3_text = GameInfoDict['questions'][q]['answers'][2]
        a3 = Button(frame, text=a3_text, bg="blue", fg="white", font='Ariel 12 bold',
                    command=lambda: showQuestion(Gamer_name, window, frame, GameInfoDict, numberOfQ + 1,
                                                 answers, a3_text))
        a3.grid(row=3, column=0, pady=(5, 5))

        a4_text = GameInfoDict['questions'][q]['answers'][3]
        a4 = Button(frame, text=a4_text, bg="blue", fg="white", font='Ariel 12 bold',
                    command=lambda: showQuestion(Gamer_name, window, frame, GameInfoDict, numberOfQ + 1,
                                                 answers, a4_text))
        a4.grid(row=4, column=0, pady=(5, 5))
        right_answer = Label(frame, text=GameInfoDict['questions'][q]['true'], fg='black', font='Ariel 8')
        right_answer.grid(row=5, column=0, pady=(10, 10))
    else:
        del answers[0]
        grade = gL.end(Gamer_name, answers, GameInfoDict, 3)
        list = frame.grid_slaves()
        for l in list:
            l.destroy()
        frame = Frame(window)
        frame.grid(row=1, column=1)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(0, weight=1)
        message2 = Label(frame, text='you grade: ' + str(grade), fg='black', font='Ariel 16 bold')
        message2.grid(row=0, column=0, pady=(5, 5))
        bottonEasy = Button(frame, text='Back to menu', bg="green", fg="white", font='Ariel 12 bold',
                            command=lambda: start(window, Gamer_name))
        bottonEasy.grid(row=1, column=0, pady=(5, 5))


def start(window, Gamer_name):
    start_menu.start_menu_window(window, Gamer_name)
