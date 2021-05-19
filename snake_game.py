import random as r
import time

import PySimpleGUI as sg
import keyboard as kb
import time as t
sg.theme('DarkPurple6')
grid_size=20
snake= []
head = []
colors=['red','blue','orange']
score=0
x,y=5,5
food =(10,10)
cx,cy = 0, 0
segments=3
score_temp = sg.T('score:'+'\n'+str(score),key='-score-',size=(0,50),justification='top_center', font=('arial', 20),
                  text_color='white')
body = sg.Text('Snake',font=('arial', 20),justification='center',size=(60, 0))

grid = ([sg.Button(key=(row, column), size=(2, 1), button_color=('white','black')) for row in range(grid_size)]
        for column in range(grid_size))
leaderboard=[sg.Text()]
layout = [[body], [sg.Frame('game', grid), score_temp]]
window=sg.Window('hi', layout, finalize=True, size=(800,800))

window[food].update(button_color=('green', 'green'))
def high_scores():
    a=sg.PopupGetText('Name')+': '+str(score)
    f=open('scores/high_score', 'a+')
    f.write('\n'+str(a))
    f.close()
def score_log():
    f = open('scores/high_score', 'r')
    if f.mode=='r':
        contents=f.read()
        for i in range(len(contents)):
            print(contents[i])
    f.close()
while True:
        window.read(20)
        if x>=grid_size or x<0 or y<0 or y>=grid_size:
            high_scores()
            #sg.popup('game over',font=('Bold',20))
            break
        else:
            if kb.is_pressed('d') and cx!=-1:
                cx = 1
                cy = 0
            if kb.is_pressed('a') and cx!=1:
                cx = -1
                cy = 0
            if kb.is_pressed('w') and cy!=1:
                cx = 0
                cy = -1
            if kb.is_pressed('s') and cy!=-1:
                cx = 0
                cy = 1
            oldx=x
            oldy=y
            x = x+cx
            y = y+cy
            if x!=oldx or y!=oldy:
                print(snake)
                snake.insert(0, (oldx, oldy))
                head=snake[0]
                if len(snake)>segments:
                    window[snake[-1]].update(button_color=('white', 'black'))
                    snake.__delitem__(-1)
                window[snake[0]].update(button_color=('blue', colors[r.randint(0,2)]))
            if head==food:
                while food in snake:
                    food = (r.randint(0, grid_size - 1), r.randint(0, grid_size - 1))
                if food not in snake:
                    segments = segments + 1
                    window[food].update(button_color=('green', 'green'))
                    score=score+1
                    window['-score-'].update('score:  '+str(score))
            if head in snake[1:-1]: #death
                high_scores()
                break
            time.sleep(0.05)
window.close()





