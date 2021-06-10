from django.shortcuts import render
import calendar
from datetime import datetime, timedelta
from .models import Events
from dateutil.relativedelta import relativedelta


def all_events(request):
    event_list = Events.objects.all()
    return render(request, 'events/all_events.html', {
        'event_list': event_list,
    })


def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = 'Andrey'
    month = month.title()
    month_n = list(calendar.month_name).index(month)
    cal = calendar.HTMLCalendar().formatmonth(year, month_n)
    current_time = datetime.now().strftime('%I:%M:%p')
    current_year = datetime.now().year
    next_month = list(calendar.month_name)[datetime.now().month+1]

    return render(request, 'events/home.html', {
        'name': name,
        'year': year,
        'month': month,
        'cal': cal,
        'current_time': current_time,
        'current_year': current_year,
        'next_month': next_month,
    })
