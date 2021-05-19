import PySimpleGUI as sg
import random as rad
def high_scores():
    score=rad.randint(1,10)
    a=sg.PopupGetText('Name')+': '+str(score)
    f=open('scores/high_score', 'a+')
    f.write('\n'+a)
    f.close()
    print(a)
def score_log():
    f = open('scores/high_score', 'r')
    if f.mode=='r':
        contents=f.read()
        cool=list(contents.split('\n'))
        for i in range(len(cool)):
            name = cool[i]
            print(name)
    f.close()
score_log()