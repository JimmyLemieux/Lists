import argparse
import math
import os
import sys
import curses
import curses.textpad
from datetime import date
import getpass


class fileNavigation:
    def __init__(self):
        self.files = os.listdir('.') #This returns all of the files in the directory
        

    
    def delete_files(self, files):
        for name in files:
            #Find the file in the dir and then delete it
            pass

    def find_txt_files(self):
        txt_files = []
        for name in self.files:
            if '.txt' in name:
                txt_files.append(name)
        return txt_files


    def get_files(self):
        return self.files

    
    def edit_file(self, files_name):
        #Should open a file and be able to edit it
        pass
    