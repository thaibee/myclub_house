import calendar
from datetime import datetime
from django.shortcuts import render
from .models import Events,  Venue
from .forms import VenueForm

def all_events(request):
    event_list = Events.objects.all()
    next_month = list(calendar.month_name)[datetime.now().month + 1]
    return render(request, 'events/all_events.html', {
        'event_list': event_list,
        'next_month': next_month,
    })


def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = 'Andrey'
    month = month.title()
    month_n = list(calendar.month_name).index(month)
    cal = calendar.HTMLCalendar().formatmonth(year, month_n)
    current_time = datetime.now().strftime('%I:%M:%p')
    current_year = datetime.now().year
    next_month = list(calendar.month_name)[datetime.now().month + 1]

    return render(request, 'events/home.html', {
        'name': name,
        'year': year,
        'month': month,
        'cal': cal,
        'current_time': current_time,
        'current_year': current_year,
        'next_month': next_month,
    })


def add_venue(request):
    submitted = False
    if request.POST:
        form = VenueForm(request.POST)
        if form.is_valid:
            submitted = True
            form.save()
    else:
        form = VenueForm()
    next_month = list(calendar.month_name)[datetime.now().month + 1]
    return render(request, 'events/add_venue.html', {
        'next_month': next_month,
        'form': form,
        'submitted': submitted
    })


def list_venues(request):
    next_month = list(calendar.month_name)[datetime.now().month + 1]
    list_venues = Venue.objects.all
    return render(request, 'events/list_venues.html', {
        'next_month': next_month,
        'list_venues': list_venues,
    })
