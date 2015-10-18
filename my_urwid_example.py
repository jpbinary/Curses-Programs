#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urwid

# urwid Menu Example
# Reference: http://urwid.readthedocs.org/en/latest/tutorial/

MENU_CHOICES = u'Los Angeles,Denver,Dallas,New York'.split(',')

# ------------------------------------------------------------------------------------------------------------------#
# menu() builds a ListBox with a title and a sequence of Button widgets
def menu(title, choices):
    body = [urwid.Text(title), urwid.Divider()]
    for each_menu_item in choices:
        button_label = urwid.Button(each_menu_item)
        #  Each button_label has its 'click' signal attached to menu_item_chosen, with each_menu_item name passed as data.
        urwid.connect_signal(button_label, 'click', menu_item_chosen, each_menu_item)
        body.append(urwid.AttrMap(button_label, None, focus_map='reversed'))

    # class urwid.ListBox(body)
    #  body (ListWalker) – a ListWalker subclass such as SimpleFocusListWalker that contains widgets
    #  to be displayed inside the list box
    return urwid.ListBox(urwid.SimpleFocusListWalker(body))

# ------------------------------------------------------------------------------------------------------------------#
# menu_item_chosen() replaces the menu displayed with text indicating the users’ choice
def menu_item_chosen(button_label, choice):
    response = urwid.Text([u'You chose ', choice, u'\n'])
    go_back_label = urwid.Button(u'Go back')
    urwid.connect_signal(go_back_label, 'click', 'test')
    done_label = urwid.Button(u'Ok')
    urwid.connect_signal(done_label, 'click', exit_program)
    main_padding.original_widget = urwid.Filler(urwid.Pile([response,
                                                            urwid.AttrMap(go_back_label, None, focus_map='reversed'),
                                                            urwid.AttrMap(done_label, None, focus_map='reversed')]))

# ------------------------------------------------------------------------------------------------------------------#
# gracefully exit urwid
def exit_program(button):
    raise urwid.ExitMainLoop()

# ------------------------------------------------------------------------------------------------------------------#
if __name__ == '__main__':
    main_padding = urwid.Padding(menu(u'City Choices Menu Heading', MENU_CHOICES), left=5, right=5)
    # The menu is created and decorated with an Overlay using a SolidFill as the background.
    # The Overlay is given a miniumum width and height but is allowed to expand to 60% of the available space
    # if the user’s terminal window is large enough.
    top_overlay = urwid.Overlay(main_padding, urwid.SolidFill(u'\N{MEDIUM SHADE}'),
                        align='center', width=('relative', 60),
                        valign='middle', height=('relative', 60),
                        min_width=20, min_height=10)

    urwid.MainLoop(top_overlay, palette=[('reversed', 'standout', '')]).run()