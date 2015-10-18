import curses

stdscr = curses.initscr() # initialize curses. stdscr is a window object that covers the entire screen
curses.noecho() # turn of auto echoing of keys
curses.cbreak() # react to key presses instantly, dont require Enter key
stdscr.keypad(1) # have curses process special keys

begin_x = 20; begin_y = 7
height = 5; width = 40
win = curses.newwin(height, width, begin_y, begin_x)

# terminate curses gracefully
curses.nocbreak(); stdscr.keypad(0); curses.echo()
curses.endwin()

