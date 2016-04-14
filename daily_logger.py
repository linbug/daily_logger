#script to open a daily log file from the command line
# one. Get today's date to. See if this file already exists 3. If file doesn't exist make it and Open it, otherwise make file

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
    path = '/Users/Lin/Dropbox/daily_plans_2016/'
    date, weekday = get_date_string()
    open_dayfile(path,date)
    if weekday == 0:
        open_weekfile(path,date)

if __name__ == '__main__':
    open_datefile()
