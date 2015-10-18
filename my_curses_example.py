import curses
import time

# many comments from documentation at: https://docs.python.org/2/howto/curses.html#curses-howto

'''
The following is automated by using curses.wrapper:
    stdscr = curses.initscr() # initialize curses. stdscr is a window object that covers the entire screen
    curses.noecho() # turn of auto echoing of keys
    curses.cbreak() # react to key presses instantly, dont require Enter key
    stdscr.keypad(1) # have curses process special keys

    begin_x = 20; begin_y = 7 # coordinates are always passed in the order y,x, and the top-left corner of a window is coordinate (0,0)
    height = 5; width = 40

    # terminate curses gracefully
    curses.nocbreak(); stdscr.keypad(0); curses.echo()
    curses.endwin()
    stdscr.refresh() # must manually refresh screen
'''


class ScreenApp():

    def __init__(self, stdscreen):
        self.screen = stdscreen
        curses.curs_set(0)

        self.screen.addstr("1.) Say Hello\n")
        self.screen.refresh()
        self.screen.addstr("2.) Say Goodbye\n")
        self.screen.refresh()
        #time.sleep(2)

        # keep running until (q) for quit is pressed
        while True:
            screen_input = stdscreen.getch()
            if screen_input == ord('q'):
                break
            elif screen_input == ord('2'):
                self.screen.addstr("Goodbye!!!!!!!!!")
                self.screen.refresh()
                time.sleep(3)
                break
            else:
                continue

if __name__ == '__main__':
    curses.wrapper(ScreenApp)
    '''curses.wrapper() does the initializations described above, and also initializes colors if color support is
    present. It then runs your provided callable and finally deinitializes appropriately.'''
