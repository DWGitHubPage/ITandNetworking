#!/usr/bin/env python3
# Python 3.9.5
# Script to know on what dates Patch Tuesday for Windows will be this year.

import argparse
import calendar
import datetime

now = datetime.datetime.now().year

parser = argparse.ArgumentParser(description='Get patch Tuesday for a given year. Current year by default.')
parser.add_argument('year', nargs='?', help='The year, example 2019', default=now, type=int)
args = parser.parse_args()

for month in range (1,13):
    cal = calendar.monthcalendar(args.year, month)
    # Second Tuesday will be in the second or third week of the month.
    week2 = cal[1]
    week3 = cal[2]

    # Check if Tuesday is between 8 and 14. If so, second tuesday is in week two. If not, then week three.
    if week2[calendar.TUESDAY] >=8 <=14:
        patchday = week2[calendar.TUESDAY]
    else:
        patchday = week3[calendar.TUESDAY]
    print(calendar.month_name[month], patchday, args.year)
