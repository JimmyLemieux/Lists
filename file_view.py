import argparse
import math
import os
import sys
import curses
import curses.textpad
from datetime import date
import getpass
from file_nav import fileNavigation




#This is the second page that will need to be put into another file
class ascii_art_view:
    def __init__(self,mode):
        self.mode = mode
        # file = open(mode,'r')
        # lines = []
        # #Each line will be a string that will be stored in the array
        # for line in file.readlines:
        #     lines.append(line)
            

    def open_art(self):
        file = open(self. mode,'r')
        lines = []
        #Each line will be a string that will be stored in the array
        for line in file.readlines():
            lines.append(line)
        return lines



class file_viewer:
    def __init__(self):
        self.file_list = fileNavigation().get_files()
        pass

    def make_title(self,stdscr,width,height):
        title_view = curses.newwin(10,width,0 ,0)
        title_view.border(0)
        title_view.refresh()
        row = 2
        for line in ascii_art_view("title.ascii").open_art():
            title_view.addstr(row,width/2 - 25,str(line),curses.A_BLINK)
            row+=1

        title_view.refresh()

    def main(self,stdscr):
        try:
            height, width = stdscr.getmaxyx()
            self.make_title(stdscr,width, height)    #This will make the ascii art
    
            curses.init_pair(4,curses.COLOR_BLACK, curses.COLOR_CYAN)
            field = curses.newwin(30,50,height/2-10,width/2 - 30)
            field.border(0)
            field.bkgd(curses.color_pair(4))
            field.refresh()
            row = 1
            for name in self.file_list:
                field.addstr(row,20,name.upper())
                row += 2
            field.refresh()
        finally:
            curses.endwin()
            print "We out "
