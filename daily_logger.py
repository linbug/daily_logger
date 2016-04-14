#A simple script to open a daily/weekly log file from the command line

# Order of events:
# -1. Get today's date
# -2. See if this file already exists
# -3. If this file doesn't already exist, make it
# -4. Open the file
# -5. If today is a Sunday, open the week log file too

path = 'path/to/files' # edit this path
text_editor = 'subl ' # edit if required (e.g. 'vim '/'nano '). NB. the trailing space is required

import datetime
import sys
import os.path
import time

def get_date_string():
    date = datetime.date.today()
    datestring=str(date.day)+'_'+str(date.month)+'_'+str(date.year)+'.md'
    weekday = datetime.date.today().weekday()
    return datestring, weekday

def open_dayfile(path, date):
    if not os.path.isfile(path + date):
        os.system('cp ' + path + 'template.md ' + path + date)
    os.system('subl ' + path + date)
    print('opening daily file')
    time.sleep(1)
    print('Have a great day! :)')

def open_weekfile(path,date):
    if not os.path.isfile(path + 'week_plan_starting_' + date):
        os.system('cp ' + path + 'weektemplate.md ' + path + 'week_plan_starting_' + date)
    os.system('subl ' + path + 'week_plan_starting_' + date)
    print('opening weekly file')
    print('Have a fantabulous week! :D')

def open_datefile():
    date, weekday = get_date_string()
    open_dayfile(path,date)
    if weekday == 0:
        open_weekfile(path,date)

if __name__ == '__main__':
    open_datefile()
