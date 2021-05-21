import PySimpleGUI as sg
import random as rad
from collections import namedtuple
def high_scores():
    score=rad.randint(1,10)
    a=sg.PopupGetText('Name')+':'+str(score)
    f=open('scores/high_score', 'a')
    f.write(a+'\n')
    f.close()
    print(a)
def score_log():
    layout = [[sg.Text(size=(6,0),key='0')], [sg.Text(size=(6,0),key='1')], [sg.Text(size=(6,0),key='2')]]
    window=sg.Window('hi',layout)
    things=[]
    f = open('scores/high_score', 'r')
    contents = f.read()
    if len(contents)>0:
        cool = list(contents.split('\n'))
        f.close()
        cool.pop(len(cool)-1)
        scores = namedtuple('scores', 'name score')
        for i in range(len(cool)):
                name, value=str(cool[i-1]).split(':')
                person=scores(name, int(value))
                things.append(person)
        final=sorted(things, key=lambda x: getattr(x, 'name'), reverse=True)
        tok=1
        while True:
            window.read(20)
            if tok==1:
                for i in range(3):
                    new=final[i-1]
                    print(new)
                    name3, value3=new.name,new.score
                    print(name3)
                    print(value3)
                    window[str(i)].update(str(name3)+': '+str(value3))
                tok=0
high_scores()
score_log()