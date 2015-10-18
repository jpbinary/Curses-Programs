import curses

stdscr = curses.initscr() # initialize curses
curses.noecho() # turn of auto echoing of keys
curses.cbreak() # react to key presses instantly, dont require Enter key
stdscr.keypad(1)

begin_x = 20; begin_y = 7
height = 5; width = 40
win = curses.newwin(height, width, begin_y, begin_x)

# terminate curses
curses.nocbreak(); stdscr.keypad(0); curses.echo()
curses.endwin()

