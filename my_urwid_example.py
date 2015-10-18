#!/usr/bin/env python
import urwid


# Menu Example

choices = u'Los Angeles, Denver, Dallas, New York'.split(',')

def menu(title, choices):
    body = [urwid.Text(title), urwid.Divider()]
    for each_menu_item in choices:
        button = urwid.Button(each_menu_item)
        urwid.connect_signal(button, 'click', menu_item_chosen, each_menu_item)
        body.append(urwid.AttrMap(button, None, focus_map='reversed'))
    return urwid.ListBox(urwid.SimpleFocusListWalker(body))

def menu_item_chosen(button, choice):
    response = urwid.Text([u'You chose ', choice, u'\n'])
    done = urwid.Button(u'Ok')
    urwid.connect_signal(done, 'click', exit_program)
    main.original_widget = urwid.Filler(urwid.Pile([response,
                                                    urwid.AttrMap(done, None, focus_map='reversed')]))

def exit_program(button):
    raise urwid.ExitMainLoop()

main = urwid.Padding(menu(u'City Choices Menu Heading', choices), left=2, right=2)
top = urwid.Overlay(main, urwid.SolidFill(u'\N{MEDIUM SHADE}'),
                    align='center', width=('relative', 60),
                    valign='middle', height=('relative', 60),
                    min_width=20, min_height=9)

urwid.MainLoop(top, palette=[('reversed', 'standout', '')]).run()