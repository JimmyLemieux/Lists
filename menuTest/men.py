from cursesmenu import *
from cursesmenu.items import *



index = 0
# menu = CursesMenu("Lists File Selection", "Access your previously created Lists",show_exit_option=True)
# menu_item = MenuItem("The Item")
# menu.append_item(menu_item)
# menu.show()

file = open('testFile.txt','r')
lines = file.readlines()

slection_menu = SelectionMenu(lines,"Previously made files",subtitle="Selection",show_exit_option=True)
slection_menu.show()
slection_menu.join()

print slection_menu.selected_option