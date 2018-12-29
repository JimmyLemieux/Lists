import argparse
import math
import os
import sys
import curses
import curses.textpad
from datetime import date
import getpass
from file_nav import fileNavigation

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
        args = self.parser.parse_args()
        return args