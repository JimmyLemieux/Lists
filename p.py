import argparse
import math
import os
import sys
import curses
import curses.textpad
from datetime import date
import getpass

class argParsing:
    def __init__(self,parser):
        self.parser = parser
        parser.add_argument('-f',action="store_true",help="These are the files")
        parser.add_argument('-n','--new',type=str,nargs='?',const="new_file.txt",help="Will make a new note with specified title")
        parser.add_argument('-v','--view',action="store_true",help="View all of the lists you have made")
        parser.add_argument('-md','--make_d',nargs="?",const="New-List-Group",help="Creates a new list-group with a defualt name of 'New-List-Group'")
        parser.add_argument('-vf','--view-file',type=str,help="Takes in a string as an argument and will open a file for this string")
        parser.add_argument('-d','--delete',nargs="*",type=str,help='Takes an argument of a string, representing a file name')
        parser.add_argument('-e','-edit',type=str,help="Takes in a file name and begins in edit mode")
    
    def get_args(self):
        args = parser.parse_args()
        return args


class fileNavigation:
    def __init__(self):
        self.files = os.listdir('.')

    
    def delete_files(self, files):
        for name in files:
            #Find the file in the dir and then delete it
            pass

    def get_files(self):
        return self.files

    
    def edit_file(self, files_name):
        #Should open a file and be able to edit it
        pass
    

class create_file:
    def __init__(self,fileName):
        self.file_content = ""
        self.fileName = fileName
        pass


    def saveState(self,filename,contents):
        print "The users file is " + filename
        print "the contents of the file will be " + contents



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
            self.file_content = tb.gather()
        finally:    #This is the end of the ui, This is where we begin to save the contents
            curses.endwin()
            self.saveState(self.fileName,self.file_content)



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
            field.getch()
        finally:
            curses.endwin()
            print "We out "






sys.setrecursionlimit(100000)
parser = argparse.ArgumentParser(description="This is the parser")
parsingObj = argParsing(parser)

args = parsingObj.get_args() 
if(args.view):
    curses.wrapper(file_viewer().main)

#This is the creation of a file
#When the user has a certain flag enabled, this will be called

# if(args.new):
#     curses.wrapper(create_file(args.new).main)


