#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Reference:
#  http://npyscreen.readthedocs.org/application-structure.html
#  https://code.google.com/p/npyscreen/source/browse/EXAMPLE-Menus.py

import npyscreen, curses

class MenuApp(npyscreen.NPSAppManaged):
    def onStart(self):
        self.registerForm("MAIN", MainForm())

# This application class serves as a wrapper for the initialization of curses
# and also manages the actual forms of the application
class MainForm(npyscreen.FormWithMenus):
    def create(self):
        self.Title = self.add(npyscreen.TitleText, name = "Title Text", value= "Press (Ctrl X) to view the Menus." )
        self.how_exited_handers[npyscreen.wgwidget.EXITED_ESCAPE]  = self.exit_application #

        # The menus are created here.
        self.main_menu = self.new_menu(name="Main Menu", shortcut="^M")
        self.main_menu.addItemsFromList([
            ("Display Text", self.whenDisplayText, None, None, ("some text",)),
            ("Just Beep",   self.whenJustBeep, "e"),
            ("Exit Application", self.exit_application, "^Q"),
        ])

        self.test_menu = self.add_menu(name="Test Menu", shortcut="b",)
        self.test_menu.addItemsFromList([
            ("Just Beep",   self.whenJustBeep),
            ("Just Beep Again", self.whenJustBeep)
        ])

        self.m3 = self.test_menu.addNewSubmenu("A sub menu", "^F")
        self.m3.addItemsFromList([
            ("Just Beep",   self.whenJustBeep),
        ])

        self.exit_menu = self.add_menu(name="Exit Menu", shortcut="^E")
        self.exit_menu.addItemsFromList([
            ("Exit Application", self.exit_application, "^Q")
        ])


    def whenDisplayText(self, argument):
       npyscreen.notify_confirm(argument)

    def whenJustBeep(self):
        curses.beep()

    def exit_application(self):
        curses.beep()
        self.parentApp.setNextForm(None)
        self.editing = False
        self.parentApp.switchFormNow()

if __name__ == '__main__':
    my_menu = MenuApp()
    my_menu.run()