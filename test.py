import PySimpleGUI as sg
import random as rad
import re
import numpy as np
def high_scores():
    score=rad.randint(1,10)
    a=sg.PopupGetText('Name')+': '+str(score)
    f=open('scores/high_score', 'a+')
    f.write('\n'+a)
    f.close()
    print(a)
def score_log():
    layout = [[sg.Text('',key='-0-')], [sg.Text('',key='-1-')], [sg.Text('',key='-2-')]]
    window=sg.Window('hi',layout)
    score_value=[]
    f = open('scores/high_score', 'r')
    if f.mode=='r':
        contents=f.read()
        cool=list(contents.split('\n'))
        print(cool)
        for i in range(len(cool)+1):
            name,value= str(cool[i]).split(': ')
            person = str(value+": "+name)
            score_value.append(person)
        score_value.sort()
        score_value.reverse()
        a=score_value
        if len(score_value)>=3:
            print(a[0:3])
        print(a)
        while True:
            window.read(20)
            window['-'+str(1)+'-'].update(a[1].split(':'))

    f.close()
high_scores()
score_log()