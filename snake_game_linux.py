def main():
    def leader_board_scores():
        from collections import namedtuple
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
                things.append(scores(name, int(value)))
            final = sorted(things, key=lambda x: getattr(x, 'score'), reverse=True)
            if len(things) >= 3:
                for i in range(3):
                    name3, value3 = final[i]
                    window[str(i) + '-'].update(f'{name3}: {value3}')
            else:
                for i in range(len(final)):
                    name3, value3 = final[i]
                    window[str(i) + '-'].update(f'{name3}: {value3}')

    def high_scores(score):
        import PySimpleGUI as sg
        a = sg.PopupGetText('Name') + ':' + str(score)
        f = open('scores/high_score', 'a')
        f.write(str(a)+'\n')
        f.close()
    import PySimpleGUI as sg
    import random as r
    import time
    sg.theme('DarkPurple6')
    grid_size = 20
    snake = []
    head = []
    colors = ['red', 'blue', 'orange']
    score = 0
    x, y = 5, 5
    food = (10, 10)
    cx, cy = 0, 0
    segments = 3
    score_temp = sg.T(str(score), key='-score-', size=(30, 2), justification='center', font=('arial', 20),
                      text_color='white')
    body = sg.Text('Snake', font=('arial', 20), justification='center', size=(60, 0))

    grid = ([sg.Button(key=(row, column), size=(2, 1), button_color=('white', 'black')) for row in range(grid_size)]
            for column in range(grid_size))
    top3 = ([sg.Text(' ', key=f'{i}-', font=('Bold', 15), justification='center', size=(10, 2))] for i in range(3))

    controlpanel=[[sg.B('⇧',size=(2,0) ,font=('arial',20),key='up')],
                  [sg.B('⇦',size=(2,0), font=('arial',20), key='left'),sg.B('⇨',size=(2,0), font=('arial',20), key='right')],
                  [sg.B('⇩',size=(2,0), font=('arial',20), key='down')]
                  ]

    leaderboard = [[sg.Text('Score', justification='center', size=(20, 0))],
                   [score_temp],
                   [sg.Column(top3)],
                   [sg.Frame('hi',controlpanel,element_justification='center')]
                   ]

    layout = [[body], [sg.Frame('game', grid),
                       sg.Frame('Stats', leaderboard, font=('Bolded', 15), border_width=10, size=(300, 750),
                                element_justification='center', vertical_alignment='top-center',
                                background_color='DarkBlue')]]

    window = sg.Window('hi', layout, finalize=True, size=(900, 750))
    leader_board_scores()
    window[food].update(button_color=('green', 'green'))
    while True:
        event, value = window.read(20)
        if x >= grid_size or x < 0 or y < 0 or y >= grid_size:
            high_scores(score)
            break
        else:
            if event == 'up' and event != 'down':
                cx = 0
                cy = -1
            if event == 'down' and event != 'up':
                cx = 0
                cy = 1
            if event == 'left' and event != 'right':
                cx = -1
                cy = 0
            if event == 'right' and event != 'left':
                cx = 1
                cy = 0
            oldx, oldy = x, y
            x, y = x + cx, y + cy
            if x != oldx or y != oldy:
                snake.insert(0, (oldx, oldy))
                head = snake[0]
                if len(snake) > segments:
                    window[snake[-1]].update(button_color=('white', 'black'))
                    snake.pop(len(snake)-1)
                window[snake[0]].update(button_color=('blue', colors[r.randint(0, 2)]))
            if head == food:
                while food in snake:
                    food = (r.randint(0, grid_size - 1), r.randint(0, grid_size - 1))
                else:
                    segments = segments + 1
                    window[food].update(button_color=('green', 'green'))
                    score = score + 1
                    window['-score-'].update('score:  ' + str(score))
            if head in snake[1:-1]:  # death
                break
            time.sleep(0.025)
    window.close()


if __name__ in "__main__":
    main()
