import curses

# Get Window
screen = curses.initscr()
# Turn off Echo
curses.noecho()
# Instant Response
curses.cbreak()
# Use Special Keys
screen.keypad(True)

try:
    while True:
        char = screen.getch()
        # if 'q' is pressed
        if char == ord('q'):
            break
        # If  UP Key is pressed
        elif char == curses.KEY_UP:
            print("UP Key")
        # If  Down Key is pressed
        elif char == curses.KEY_DOWN:
            print("DOWN Key")
        # If  LeftKey is pressed
        elif char == curses.KEY_LEFT:
            print("LEFT Key")
        # If  Right Key is pressed
        elif char == curses.KEY_RIGHT:
            print("RIGHT Key")
        # If ENTER is pressed
        elif char == 10:
            print("STOP")
finally:
    # When 'q' is pressed and program ends
    curses.nocbreak();
    screen.keypad(0);
    curses.echo()
    curses.endwin()