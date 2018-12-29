import argparse
import math
import os
import sys
import curses
import curses.textpad
from datetime import date
import getpass

from argument_parse import argParsing
from file_view import file_viewer



class create_file:
    def __init__(self,fileName,):
        self.file_content = ""
        self.fileName = fileName
        pass


    def saveState(self,filename,contents):
        print "The users file is " + filename
        print "the contents of the file will be " + contents
        file = open(filename,'w+')
        file.writelines(contents)
        file.close()


    def main(self,stdscr):

        try:

            curses.start_color()
            curses.init_pair(5,curses.COLOR_WHITE, curses.COLOR_BLUE)
            curses.init_pair(3,curses.COLOR_BLUE,curses.COLOR_YELLOW)
            curses.init_pair(6,curses.COLOR_CYAN,curses.COLOR_BLACK)


            curses.mousemask(1)

            height, width = stdscr.getmaxyx()
            field = curses.newwin(50,100,0,width/2 - 50)
            field.border(0)
            field.addstr(1,15,"Enter Text In here",curses.A_REVERSE)
            field.refresh()

            #Add the help and view options field
            options = curses.newwin(20,100,50,width/2 - 50)
            options.border(0)
            options.bkgd(curses.color_pair(3))
            options.addstr(0,35,"OPTIONS ARE TO BE INCLUDED",curses.A_BLINK)
            options.addstr(2,2, "Control H = Backspace. Delete option will be in later version")
            options.addstr(3,2, "Arrows = line navigation")
            options.addstr(4,2, "Control K = Delete a whole line")
            options.addstr(5,2, "Control G = Save and Exit the file")
            options.addstr(10,2, "Current version: 1.0.0 >Developed by James",curses.A_BOLD)
            options.addstr(12,2, "Alot of the key features are not working yet", curses.A_BOLD)
            options.refresh()

            current_win = curses.newwin(20,52,0,0)
            current_win.border(0)
            current_win.bkgd(curses.color_pair(6))
            current_win.addstr(0,18,self.fileName.upper(),curses.A_REVERSE)
            current_win.addstr(2,2,"Current date is: " + str(date.today()))
            current_win.addstr(4,2, "Current Admin User: " + str(getpass.getuser()),curses.A_PROTECT)
            current_win.addstr(6,2, "You are currently in Edit Mode:::")
            current_win.refresh()

            #<!---- Text Field Beginning ---->

            tbWin = curses.newwin(48,98,1,width/2 - 49)
            tbWin.bkgd(curses.color_pair(5))
            tb = curses.textpad.Textbox(tbWin,insert_mode=True)        
            tb.edit()
            tbWin.refresh()
            tbWin.getch()
            self.file_content = tb.gather()
        finally:    #This is the end of the ui, This is where we begin to save the contents
            curses.endwin()
            self.saveState(self.fileName,self.file_content)
            print "File has been created!"



sys.setrecursionlimit(100000)
parser = argparse.ArgumentParser(description="This is the parser")
parsingObj = argParsing(parser)

args = parsingObj.get_args() 
if(args.view):
    curses.wrapper(file_viewer().main)

#This is the creation of a file
#When the user has a certain flag enabled, this will be called
 
#There is a bug here when trying to load the new screen with custom -n/--new flag
#This bug has been fixed
if(args.new):
    try:
        file = open(str(args.new), 'r+')
        print "This file already exists, to edit enter edit mode. See --help"
    except:
        curses.wrapper(create_file(args.new).main)
