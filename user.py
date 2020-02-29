import sqlite3
import random
import pyttsx3
conn=sqlite3.connect('test.db')
c=conn.cursor()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
def chat():
    print("Start talking with the bot (type quit to stop)!")
    while True:
        l=list()
        inp=input("You: ")
        if inp.lower()=="quit":
            print('bot: ok exiting program')
            engine.say('ok exiting program')
            engine.runAndWait()
            break
        inp=(inp,)
        d=c.execute("SELECT * FROM CHAT WHERE question=?",inp)
        for r in d:
            if r[2]:
                l.append(r[2])
        count=len(l)
        if count!=0:
            rl=random.randrange(0,count,1)
            print(rl)
            engine.say(l[rl])
            print("bot: ",l[rl])
            engine.runAndWait()
        else:
            s="sorry, Answer not found :-("
            engine.say(s)
            print("bot:",s)
            engine.runAndWait()
chat()
