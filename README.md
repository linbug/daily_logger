# daily_logger

For those that want to keep track of their daily work goals in markdown format, this is a simple script that opens a daily/weekly markdown file from the command line, saved under the appropriate day's date.

## Usage

- change the `path` variable to the file path where you want your log files to live
- change the `text_editor` variable to the command for your fave text editor
- create template.md and weektemplate.md files in this directory as daily and weekly log templates, respectively
- open your .bash_profile and make a new alias: `alias log='python path/to/daily_logger.py`
- now when you type the command `log` your logfile will open, and will save as '*day*\_*month*_*year*.md'
- the weekly log will open if today is Sunday. You can change the day it opens by changing `weekday == 0` to some other value (0-6)

## Requirements
Python 2/3
