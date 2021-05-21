import random as r
import time
from collections import namedtuple
import PySimpleGUI as sg
import keyboard as kb
def leader_board_scores():
    things = []
    f = open('scores/high_score', 'r')
    contents = f.read()
    if len(contents) > 0:
        cool = list(contents.split('\n'))
        f.close()
        cool.pop(len(cool) - 1)
        scores = namedtuple('scores', 'name score')
        for i in range(len(cool)):
            name, value = str(cool[i - 1]).split(':')
            person = scores(name, int(value))
            things.append(person)
        final = sorted(things, key=lambda x: getattr(x, 'score'), reverse=True)
        if len(things)>=3:
            for i in range(3):
                new = final[i]
                print(new)
                name3, value3 = new.name, new.score
                print(name3)
                print(value3)
                window[str(i) + '-'].update(str(name3) + ': ' + str(value3))
        else:
            for i in range(len(final)):
                new = final[i]
                print(new)
                name3, value3 = new.name, new.score
                print(name3)
                print(value3)
                window[str(i)+'-'].update(str(name3) + ': ' + str(value3))

def high_scores(score):
    a=sg.PopupGetText('Name')+':'+str(score)
    f=open('scores/high_score', 'a')
    f.write(a+'\n')
    f.close()


sg.theme('DarkPurple6')
score=0
grid_size=20
snake= []
head = []
colors=['red','blue','orange']
score=0
x,y=5,5
food =(10,10)
cx,cy = 0, 0
segments=3
score_temp = sg.T(str(score),key='-score-',size=(30,2),justification='center', font=('arial', 20),
                  text_color='white')
body = sg.Text('Snake',font=('arial', 20),justification='center',size=(60, 0))

grid = ([sg.Button(key=(row, column), size=(2, 1), button_color=('white','black')) for row in range(grid_size)]
        for column in range(grid_size))

leaderboard=[[sg.Text('Score',justification='center',size=(20,0))],
             [score_temp],
             [sg.Column([sg.Text(' ', key=str(i)+'-', font=('Bold', 15),justification='center',size=(10,2))] for i in range(3))]]

layout = [[body], [sg.Frame('game', grid), sg.Frame('Stats',leaderboard,font=('Bolded',15),border_width=10,size=(300,750),element_justification='center', vertical_alignment='top-center',background_color='DarkBlue')]]

window=sg.Window('hi', layout, finalize=True, size=(900,750))
leader_board_scores()
window[food].update(button_color=('green', 'green'))

while True:
        window.read(20)
        if x>=grid_size or x<0 or y<0 or y>=grid_size:
            high_scores(score)
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
                break
            time.sleep(0.05)
window.close()

