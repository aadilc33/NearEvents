from django.http import HttpResponse
from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
def calendarData(request,year=2021,month="March"):
    month_number =list(calendar.month_name).index(month)
    cal = HTMLCalendar().formatmonth(year,month_number)
    now =datetime.now()
    current_year = now.year
    time = now.strftime('%I:%M:%S')
    return render(request,"calendar.html",{"year":year,"month":month,"month_number":month_number,"cal":cal,
                   "current_year":current_year,"time":time})